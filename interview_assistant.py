#!/usr/bin/env python3
"""面试助手。

零依赖命令行工具，默认读取数据目录下的两份 Markdown：
- plan.md
- question.md

可通过 --data-dir 指定数据目录，文件名固定不变。

功能：
- 查看执行计划概览和某一天详情
- 按天推荐练习题
- 按主题抽问
- 随机模拟面试
- 搜索问题
- 记录进度、练习结果和每日复盘
- 默认把练习、自评分、卡点和复盘追加到当天 Markdown 日志
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List, Optional


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = BASE_DIR

PLAN_FILENAME = "plan.md"
QUESTION_FILENAME = "question.md"
STATE_FILENAME = ".interview_assistant_state.json"


_STOP_WORDS = frozenset({
    "的", "一", "和", "与", "是", "在", "把", "对", "从", "为", "了",
    "也", "不", "要", "能", "会", "可", "做", "用", "有", "被", "让",
    "而", "但", "又", "或", "及", "等", "这个", "那个",
})


def _is_hint(text: str) -> bool:
    """判断一段文字是否适合作为主题关键词。"""
    cleaned = text.strip().strip("`'\"")
    if not cleaned or len(cleaned) < 2:
        return False
    if cleaned in _STOP_WORDS:
        return False
    return True


def extract_day_topic_hints(plan: DayPlan) -> List[str]:
    """从 Day 标题和内容中自动提取主题关键词。"""
    hints: List[str] = []
    seen: set = set()

    def _add(text: str) -> None:
        cleaned = text.strip().strip("`'\"")
        if _is_hint(cleaned) and cleaned not in seen:
            hints.append(cleaned)
            seen.add(cleaned)

    # 从标题提取：按 / 和 ， 拆分，取有意义的片段
    for segment in re.split(r"[/，,]", plan.title):
        segment = segment.strip().strip("`'\"")
        if _is_hint(segment):
            _add(segment)

    # 从 section 内容提取：仅从“今日目标”“今日任务”中提取反引号内的技术术语
    backtick_re = re.compile(r"`([^`]+)`")
    target_sections = {"今日目标", "今日任务"}
    for section_name, lines in plan.sections.items():
        if section_name not in target_sections:
            continue
        for line in lines:
            for match in backtick_re.finditer(line):
                term = match.group(1).strip()
                if _is_hint(term):
                    _add(term)

    return hints


@dataclass
class DayPlan:
    day: int
    title: str
    sections: Dict[str, List[str]] = field(default_factory=dict)


@dataclass
class Question:
    qid: int
    title: str
    category: str
    sections: Dict[str, List[str]] = field(default_factory=dict)

    def keywords_text(self) -> str:
        parts = [self.title, self.category]
        for section_name, lines in self.sections.items():
            parts.append(section_name)
            parts.extend(lines)
        return "\n".join(parts)


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"找不到文件：{path}")
    return path.read_text(encoding="utf-8")


def parse_day_plans(text: str) -> Dict[int, DayPlan]:
    lines = text.splitlines()
    day_pattern = re.compile(r"^##\s+\d+\.\s+Day\s+(\d+)[：:]\s*(.+)$")
    section_pattern = re.compile(r"^###\s+(.+)$")

    plans: Dict[int, DayPlan] = {}
    current: Optional[DayPlan] = None
    current_section: Optional[str] = None

    for raw_line in lines:
        line = raw_line.rstrip()
        day_match = day_pattern.match(line)
        if day_match:
            current = DayPlan(day=int(day_match.group(1)), title=day_match.group(2).strip())
            plans[current.day] = current
            current_section = None
            continue

        if current is None:
            continue

        section_match = section_pattern.match(line)
        if section_match:
            current_section = section_match.group(1).strip()
            current.sections.setdefault(current_section, [])
            continue

        if line.startswith("## "):
            current = None
            current_section = None
            continue

        if current_section is not None:
            current.sections[current_section].append(line)

    return plans


def parse_questions(text: str) -> List[Question]:
    lines = text.splitlines()
    category_pattern = re.compile(r"^##\s+\d+\.\s+(.+)$")
    question_pattern = re.compile(r"^###\s+Q(\d+)\.\s+(.+)$")
    section_pattern = re.compile(r"^####\s+(.+)$")

    questions: List[Question] = []
    current_category: Optional[str] = None
    current_question: Optional[Question] = None
    current_section: Optional[str] = None

    for raw_line in lines:
        line = raw_line.rstrip()

        category_match = category_pattern.match(line)
        if category_match:
            current_category = category_match.group(1).strip()
            current_question = None
            current_section = None
            continue

        question_match = question_pattern.match(line)
        if question_match:
            if current_category is None:
                current_category = "未分类"
            current_question = Question(
                qid=int(question_match.group(1)),
                title=question_match.group(2).strip(),
                category=current_category,
            )
            questions.append(current_question)
            current_section = None
            continue

        section_match = section_pattern.match(line)
        if section_match and current_question is not None:
            current_section = section_match.group(1).strip()
            current_question.sections.setdefault(current_section, [])
            continue

        if current_question is not None and current_section is not None:
            current_question.sections[current_section].append(line)

    return questions


def load_state(data_dir: Path) -> dict:
    state_file = data_dir / STATE_FILENAME
    if not state_file.exists():
        return {
            "completed_days": [],
            "day_notes": {},
            "practice_history": [],
        }
    try:
        return json.loads(state_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {
            "completed_days": [],
            "day_notes": {},
            "practice_history": [],
        }


def save_state(state: dict, data_dir: Path) -> None:
    state_file = data_dir / STATE_FILENAME
    state_file.write_text(
        json.dumps(state, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def clean_lines(lines: List[str]) -> List[str]:
    cleaned: List[str] = []
    for line in lines:
        stripped = line.rstrip()
        if not stripped and (not cleaned or not cleaned[-1]):
            continue
        cleaned.append(stripped)
    while cleaned and not cleaned[-1]:
        cleaned.pop()
    return cleaned


def print_block(title: str, lines: List[str]) -> None:
    lines = clean_lines(lines)
    if not lines:
        return
    print(f"\n[{title}]")
    for line in lines:
        print(line if line else "")


def print_day_overview(plans: Dict[int, DayPlan], state: dict, *, json_mode: bool = False) -> None:
    completed = set(state.get("completed_days", []))
    if json_mode:
        data = {
            "total_days": len(plans),
            "days": [
                {"day": d, "title": plans[d].title, "completed": d in completed}
                for d in sorted(plans)
            ],
            "progress": {"completed": len(completed), "total": len(plans)},
        }
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return
    total_days = len(plans)
    print(f"\n{total_days} 天执行清单概览")
    print("-" * 48)
    for day in sorted(plans):
        status = "已完成" if day in completed else "未完成"
        print(f"Day {day:>2} | {plans[day].title} | {status}")


def print_day_detail(plan: DayPlan, state: Optional[dict] = None, *, json_mode: bool = False) -> None:
    if json_mode:
        sections = {k: clean_lines(v) for k, v in plan.sections.items()}
        data = {"day": plan.day, "title": plan.title, "sections": sections}
        if state:
            note = state.get("day_notes", {}).get(str(plan.day))
            if note:
                data["note"] = note
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return
    print(f"\nDay {plan.day}: {plan.title}")
    print("=" * 60)
    for section_name, lines in plan.sections.items():
        print_block(section_name, lines)
    if state:
        note = state.get("day_notes", {}).get(str(plan.day))
        if note:
            print("\n[已记录复盘]")
            print(note)


def print_question(question: Question, show_answer: bool = True) -> None:
    print(f"\nQ{question.qid}. {question.title}")
    print(f"分类：{question.category}")
    if show_answer:
        for section_name, lines in question.sections.items():
            print_block(section_name, lines)


def find_questions_by_keyword(questions: List[Question], keyword: str) -> List[Question]:
    keyword_lower = keyword.lower()
    results = []
    for question in questions:
        if keyword_lower in question.keywords_text().lower():
            results.append(question)
    return results


def find_questions_by_topics(questions: List[Question], topic_hints: List[str]) -> List[Question]:
    results = []
    for question in questions:
        haystack = question.keywords_text().lower()
        if any(topic.lower() in haystack for topic in topic_hints):
            results.append(question)
    return results


def get_recommended_day(plans: Dict[int, DayPlan], state: dict) -> int:
    completed = set(state.get("completed_days", []))
    for day in sorted(plans):
        if day not in completed:
            return day
    return min(plans) if plans else 1


def choose_questions_for_day(plan: DayPlan, questions: List[Question], count: int) -> List[Question]:
    hints = extract_day_topic_hints(plan)
    matched = find_questions_by_topics(questions, hints) if hints else questions[:]
    if not matched:
        matched = questions[:]
    random.shuffle(matched)
    return matched[: min(count, len(matched))]


def summarize_practice_session(items: List[dict]) -> None:
    if not items:
        print("\n本次没有记录评分。")
        return
    avg = sum(item["score"] for item in items) / len(items)
    weak = [item for item in items if item["score"] <= 2]
    print("\n练习总结")
    print("-" * 48)
    print(f"题目数：{len(items)}")
    print(f"平均自评分：{avg:.2f} / 5")
    if weak:
        print("建议优先复习以下薄弱题：")
        for item in weak:
            print(f"- Q{item['qid']} {item['title']}（评分 {item['score']}）")


def input_with_default(prompt: str, default: str = "") -> str:
    try:
        text = input(prompt).strip()
    except EOFError:
        print()
        return default
    return text if text else default


def safe_int(text: str, default: int) -> int:
    try:
        return int(text)
    except ValueError:
        return default


def record_note_for_day(state: dict, day: int, data_dir: Path) -> None:
    print("\n请输入今天的复盘内容。直接回车可跳过。")
    note = input_with_default("复盘> ", "")
    if note:
        state.setdefault("day_notes", {})[str(day)] = note
        save_state(state, data_dir)
        log_path = append_daily_log(
            f"Day {day} 复盘",
            [
                f"- 对应 Day：Day {day}",
                f"- 内容：{note}",
            ],
            data_dir,
        )
        print("已保存复盘。")
        print(f"已追加到：{log_path}")


def mark_day_completed(state: dict, day: int, data_dir: Path) -> None:
    completed = set(state.setdefault("completed_days", []))
    if day not in completed:
        completed.add(day)
        state["completed_days"] = sorted(completed)
        save_state(state, data_dir)
        log_path = append_daily_log(
            f"Day {day} 完成",
            [
                f"- 对应 Day：Day {day}",
                "- 状态：已标记完成",
            ],
            data_dir,
        )
        print(f"已标记 Day {day} 完成。")
        print(f"已追加到：{log_path}")
    else:
        print(f"Day {day} 已经是完成状态。")


def practice_questions(
    questions: List[Question],
    state: dict,
    mode: str,
    data_dir: Path,
    day: Optional[int] = None,
    allow_notes: bool = False,
) -> None:
    if not questions:
        print("没有找到可练习的问题。")
        return

    results = []
    print("\n进入练习模式。")
    print("每道题先自己回答，按回车后再看要点。")

    for index, question in enumerate(questions, start=1):
        print("\n" + "=" * 60)
        print(f"第 {index}/{len(questions)} 题")
        print(f"Q{question.qid}. {question.title}")
        print(f"分类：{question.category}")
        input_with_default("按回车查看回答要点...", "")
        print_question(question, show_answer=True)

        score_text = input_with_default("给自己打分（1-5，默认 3）> ", "3")
        try:
            score = max(1, min(5, int(score_text)))
        except ValueError:
            score = 3

        reflection = input_with_default("一句话记录卡点（可留空）> ", "")
        results.append(
            {
                "qid": question.qid,
                "title": question.title,
                "category": question.category,
                "score": score,
                "reflection": reflection,
            }
        )

    state.setdefault("practice_history", []).append(
        {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "mode": mode,
            "day": day,
            "count": len(results),
            "results": results,
        }
    )
    save_state(state, data_dir)
    log_lines = [
        f"- 模式：{mode}",
        f"- 题目数：{len(results)}",
    ]
    if day is not None:
        log_lines.append(f"- 对应 Day：Day {day}")
    avg_score = (sum(item["score"] for item in results) / len(results)) if results else 0.0
    log_lines.append(f"- 平均自评分：{avg_score:.2f} / 5")
    log_lines.append("")
    log_lines.append("### 题目记录")
    log_lines.append("")
    for item in results:
        log_lines.append(
            f"- Q{item['qid']} {item['title']} | 分类：{item['category']} | 自评分：{item['score']}/5"
        )
        if item.get("reflection"):
            log_lines.append(f"  - 卡点：{item['reflection']}")
    log_path = append_daily_log("练习记录", log_lines, data_dir)
    summarize_practice_session(results)
    print(f"已追加到：{log_path}")

    if allow_notes and day is not None:
        if input_with_default("\n是否记录今天复盘？(y/N) > ", "n").lower() == "y":
            record_note_for_day(state, day, data_dir)
        if input_with_default("是否将今天标记为完成？(y/N) > ", "n").lower() == "y":
            mark_day_completed(state, day, data_dir)


def _question_to_dict(question: Question, include_answer: bool = True) -> dict:
    d = {"qid": question.qid, "title": question.title, "category": question.category}
    if include_answer:
        d["answer_points"] = clean_lines(question.sections.get("回答要点", []))
        oneliner = clean_lines(question.sections.get("一句话版", []))
        if oneliner:
            d["oneliner"] = oneliner
    return d


def print_progress(state: dict, plans: Dict[int, DayPlan], *, json_mode: bool = False) -> None:
    completed = set(state.get("completed_days", []))
    if json_mode:
        history = state.get("practice_history", [])
        data = {
            "completed_days": sorted(completed),
            "total_days": len(plans),
            "completion_rate": round(len(completed) / len(plans), 2) if plans else 0,
            "recommended_day": get_recommended_day(plans, state),
            "practice_sessions": len(history),
        }
        if history:
            data["last_practice"] = history[-1]["timestamp"]
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return
    print("\n当前进度")
    print("-" * 48)
    print(f"已完成天数：{len(completed)} / {len(plans)}")
    print(f"推荐下一天：Day {get_recommended_day(plans, state)}")
    if completed:
        print("已完成：", ", ".join(f"Day {day}" for day in sorted(completed)))
    history = state.get("practice_history", [])
    print(f"练习记录数：{len(history)}")
    if history:
        last = history[-1]
        print(f"最近一次练习：{last['timestamp']} | 模式：{last['mode']} | 题数：{last['count']}")


def get_day_title(plans: Dict[int, DayPlan], day: Optional[int]) -> str:
    if day is None or day not in plans:
        return "未指定"
    return plans[day].title


def get_today_log_path(data_dir: Path) -> Path:
    return data_dir / f"交互记录_{date.today().strftime('%Y%m%d')}.md"


def append_daily_log(title: str, lines: List[str], data_dir: Path) -> Path:
    log_path = get_today_log_path(data_dir)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not log_path.exists():
        header = [
            f"# 交互记录 - {date.today().isoformat()}",
            "",
            "> 由 `interview_assistant.py` 自动追加记录",
            "",
        ]
        log_path.write_text("\n".join(header), encoding="utf-8")

    entry: List[str] = [
        "",
        f"## {title}",
        "",
        f"- 时间：{timestamp}",
    ]
    entry.extend(lines)
    entry.append("")
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write("\n".join(entry))
    return log_path


class HelpFormatter(
    argparse.RawTextHelpFormatter,
    argparse.ArgumentDefaultsHelpFormatter,
):
    pass


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="interview_assistant.py",
        description=(
            "面试助手\n"
            "\n"
            "读取数据目录下的执行计划和高频问答题库，支持查看计划、搜索题目、"
            "按天练习、按主题抽问、随机模拟面试，以及记录练习结果和复盘。"
        ),
        epilog=(
            "使用说明：\n"
            "  1. 不带任何参数运行时，会进入交互式菜单。\n"
            "  2. 使用命令行参数时，会直接执行对应动作并输出结果。\n"
            "  3. 练习记录、自评分和复盘会自动追加到当天日志 Markdown。\n"
            "  4. 可通过 --data-dir 指定数据目录，目录内需包含 plan.md 和 question.md。\n"
            "\n"
            "常用示例：\n"
            "  python3 interview_assistant.py\n"
            "  python3 interview_assistant.py --overview\n"
            "  python3 interview_assistant.py --day 7\n"
            "  python3 interview_assistant.py --search Memory\n"
            "  python3 interview_assistant.py --practice-day 5 --count 3\n"
            "  python3 interview_assistant.py --topic MCP --count 5\n"
            "  python3 interview_assistant.py --mock --count 8\n"
            "  python3 interview_assistant.py --data-dir ./my_data\n"
        ),
        formatter_class=HelpFormatter,
    )
    parser.add_argument("--overview", action="store_true", help="查看执行计划概览")
    parser.add_argument("--day", type=int, help="查看某一天详情，例如 --day 7")
    parser.add_argument("--search", type=str, help="按关键词搜索题目")
    parser.add_argument("--progress", action="store_true", help="查看当前进度")
    parser.add_argument("--practice-day", type=int, help="按天练习推荐题")
    parser.add_argument("--topic", type=str, help="按主题关键词练习")
    parser.add_argument("--mock", action="store_true", help="随机模拟面试")
    parser.add_argument("--count", type=int, default=5, help="练习题数，默认 5")
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=DEFAULT_DATA_DIR,
        help=f"数据目录，包含 plan.md 和 question.md，默认 {DEFAULT_DATA_DIR.name}",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="以 JSON 格式输出，适合 Agent 和脚本调用",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="抑制交互提示和非必要输出",
    )
    return parser


def interactive_menu(plans: Dict[int, DayPlan], questions: List[Question], state: dict, data_dir: Path) -> None:
    while True:
        recommended_day = get_recommended_day(plans, state)
        print("\n面试助手")
        print("=" * 60)
        print(f"推荐今天练习：Day {recommended_day} - {plans[recommended_day].title}")
        print(f"1. 查看 {len(plans)} 天计划概览")
        print("2. 查看某一天详情")
        print("3. 开始今天的推荐练习")
        print("4. 按主题抽问")
        print("5. 随机模拟面试")
        print("6. 搜索题目")
        print("7. 查看当前进度")
        print("8. 记录某一天复盘")
        print("9. 标记某一天完成")
        print("0. 退出")

        choice = input_with_default("\n请选择 > ", "0")
        if choice == "1":
            print_day_overview(plans, state)
        elif choice == "2":
            day = safe_int(input_with_default("输入 Day 编号 > ", str(recommended_day)), recommended_day)
            plan = plans.get(day)
            if not plan:
                print("没有这个 Day。")
            else:
                print_day_detail(plan, state)
        elif choice == "3":
            plan = plans[recommended_day]
            print_day_detail(plan, state)
            selected = choose_questions_for_day(plan, questions, 5)
            practice_questions(selected, state, mode="daily", data_dir=data_dir, day=recommended_day, allow_notes=True)
        elif choice == "4":
            keyword = input_with_default("输入主题关键词，例如 Memory / MCP / SQL > ", "")
            if not keyword:
                print("关键词不能为空。")
                continue
            matched = find_questions_by_keyword(questions, keyword)
            if not matched:
                print("没有找到匹配的问题。")
                continue
            random.shuffle(matched)
            practice_questions(matched[:5], state, mode=f"topic:{keyword}", data_dir=data_dir)
        elif choice == "5":
            selected = questions[:]
            random.shuffle(selected)
            practice_questions(selected[:5], state, mode="mock", data_dir=data_dir)
        elif choice == "6":
            keyword = input_with_default("输入搜索关键词 > ", "")
            matched = find_questions_by_keyword(questions, keyword)
            if not matched:
                print("没有找到匹配的问题。")
                continue
            print(f"\n共找到 {len(matched)} 题：")
            for question in matched[:20]:
                print(f"- Q{question.qid} | {question.category} | {question.title}")
        elif choice == "7":
            print_progress(state, plans)
        elif choice == "8":
            day = safe_int(input_with_default("输入 Day 编号 > ", str(recommended_day)), recommended_day)
            record_note_for_day(state, day, data_dir)
        elif choice == "9":
            day = safe_int(input_with_default("输入 Day 编号 > ", str(recommended_day)), recommended_day)
            mark_day_completed(state, day, data_dir)
        elif choice == "0":
            print("已退出。")
            return
        else:
            print("无效选项，请重新输入。")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    data_dir: Path = args.data_dir.resolve()
    plan_file = data_dir / PLAN_FILENAME
    question_file = data_dir / QUESTION_FILENAME

    try:
        plans = parse_day_plans(read_text(plan_file))
        questions = parse_questions(read_text(question_file))
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    state = load_state(data_dir)

    if args.overview:
        print_day_overview(plans, state, json_mode=args.json_output)
        return 0

    if args.day is not None:
        plan = plans.get(args.day)
        if not plan:
            if args.json_output:
                print(json.dumps({"error": f"找不到 Day {args.day}"}, ensure_ascii=False))
            else:
                print(f"找不到 Day {args.day}")
            return 1
        print_day_detail(plan, state, json_mode=args.json_output)
        return 0

    if args.search:
        matched = find_questions_by_keyword(questions, args.search)
        if args.json_output:
            data = {
                "keyword": args.search,
                "count": len(matched),
                "questions": [_question_to_dict(q, include_answer=False) for q in matched[:50]],
            }
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            print(f"关键词：{args.search}")
            print(f"共找到 {len(matched)} 题")
            for question in matched[:50]:
                print(f"- Q{question.qid} | {question.category} | {question.title}")
        return 0

    if args.progress:
        print_progress(state, plans, json_mode=args.json_output)
        return 0

    if args.practice_day is not None:
        if args.practice_day not in plans:
            if args.json_output:
                print(json.dumps({"error": f"找不到 Day {args.practice_day}"}, ensure_ascii=False))
            else:
                print(f"找不到 Day {args.practice_day}")
            return 1
        plan = plans[args.practice_day]
        selected = choose_questions_for_day(plan, questions, args.count)
        if args.json_output:
            data = {
                "mode": "practice",
                "day": args.practice_day,
                "count": len(selected),
                "questions": [_question_to_dict(q) for q in selected],
            }
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            practice_questions(selected, state, mode="daily", data_dir=data_dir, day=args.practice_day, allow_notes=True)
        return 0

    if args.topic:
        matched = find_questions_by_keyword(questions, args.topic)
        if not matched:
            if args.json_output:
                print(json.dumps({"keyword": args.topic, "count": 0, "questions": []}, ensure_ascii=False))
            else:
                print("没有找到匹配的问题。")
            return 1
        random.shuffle(matched)
        selected = matched[: args.count]
        if args.json_output:
            data = {
                "mode": "topic",
                "keyword": args.topic,
                "count": len(selected),
                "questions": [_question_to_dict(q) for q in selected],
            }
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            practice_questions(selected, state, mode=f"topic:{args.topic}", data_dir=data_dir)
        return 0

    if args.mock:
        selected = questions[:]
        random.shuffle(selected)
        selected = selected[: args.count]
        if args.json_output:
            data = {
                "mode": "mock",
                "count": len(selected),
                "questions": [_question_to_dict(q) for q in selected],
            }
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            practice_questions(selected, state, mode="mock", data_dir=data_dir)
        return 0

    if args.json_output:
        print(json.dumps({"error": "JSON 模式不支持交互式菜单，请使用具体命令参数"}, ensure_ascii=False))
        return 1

    interactive_menu(plans, questions, state, data_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
