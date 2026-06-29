## Context

`interview_assistant.py` 是一个零依赖的 Python CLI 工具，通过 argparse 提供 `--overview`、`--day`、`--search`、`--topic`、`--mock` 等命令。当前所有输出都是 `print()` 直接输出中文文本，包含表格、分隔线和交互式菜单。

项目的 `.qoder/skills/` 目录已有 openspec 相关 skill，但没有面试助手自己的 skill。

## Goals / Non-Goals

**Goals:**
- 所有命令支持 `--json` 输出，返回结构化 JSON 供 Agent 解析
- 创建 Qoder Skill，让 AI 可通过 `/interview` 调用核心功能
- 保持零依赖、向后兼容
- 默认行为（人类模式）完全不变

**Non-Goals:**
- 不引入第三方依赖
- 不改为 click/typer 等框架
- 不创建 REST API 或 MCP server
- 不修改 question/plan 文件格式

## Decisions

### 1. JSON 输出架构

新增一个 `OutputFormatter` 抽象，封装两种输出模式：

```
class OutputFormatter:
    def overview(plans, state) -> None     # 人类: 表格 / JSON: 结构化
    def day_detail(plan, state) -> None    # 人类: 带 section / JSON: 嵌套对象
    def search_results(results) -> None    # 人类: 列表 / JSON: 数组
    def practice_session(questions) -> None # 人类: 交互 / JSON: 题目数组
```

`--json` 参数控制 formatter 走哪条路径。`--quiet` 抑制 "进入练习模式" 等提示文字。

**理由**：最小侵入性改动，不改变现有逻辑流，只在输出层分支。

### 2. JSON Schema 设计

每个命令的输出对应一个 JSON 结构：

**overview**:
```json
{
  "total_days": 14,
  "days": [
    {"day": 1, "title": "统一岗位叙事", "completed": false}
  ],
  "progress": {"completed": 0, "total": 14}
}
```

**search**:
```json
{
  "keyword": "MoE",
  "count": 5,
  "questions": [
    {"qid": 15, "title": "...", "category": "Transformer 架构"}
  ]
}
```

**day detail**:
```json
{
  "day": 7,
  "title": "CUDA / GPU 编程",
  "sections": {
    "今日目标": ["..."],
    "今日任务": ["..."],
    "验收标准": ["..."]
  }
}
```

**mock/practice**:
```json
{
  "mode": "mock",
  "count": 5,
  "questions": [
    {"qid": 35, "title": "...", "category": "RL 后训练", "answer_points": ["..."]}
  ]
}
```

### 3. Skill 设计

创建 `.qoder/skills/interview/SKILL.md`，定义一个 `interview` 斜杠命令：

- 输入：用户请求（如 "overview agent"、"search MoE in llm"、"mock 5 questions from ai-infra"）
- 行为：Skill 指导 Agent 构造对应的 CLI 命令，执行并解析 JSON 输出
- 输出：Agent 将结果以自然语言呈现给用户

Skill 本质上是一个 prompt 模板，教 Agent 如何调用 CLI。

### 4. 参数设计

```
python3 interview_assistant.py --data-dir ./agent --overview --json
python3 interview_assistant.py --data-dir ./llm --search "MoE" --json
python3 interview_assistant.py --data-dir ./ai-infra --mock --count 5 --json
python3 interview_assistant.py --data-dir ./mygo --day 3 --json
```

新增参数：
- `--json`：输出 JSON 格式（全局可用）
- `--quiet`：抑制交互提示和非必要输出（与 `--json` 搭配使用）

## Risks / Trade-offs

- **[兼容性]** 所有现有命令默认行为不变 → 通过 `--json` opt-in
- **[Skill 维护]** Skill 需要跟随 CLI 更新 → Skill 描述保持高层抽象，不硬编码参数细节
- **[JSON 稳定性]** JSON schema 可能随功能演进变化 → 在 README 中标注 JSON schema 版本
- **[交互模式]** `--mock` 和 `--topic` 在人类模式下有交互式打分，JSON 模式下跳过交互 → `--quiet` 或 `--json` 时自动非交互
