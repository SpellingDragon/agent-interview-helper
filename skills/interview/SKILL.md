---
name: interview
description: Interview preparation assistant. Query study plans, search questions, get practice recommendations, and run mock interviews across multiple question banks.
license: MIT
compatibility: Requires Python 3.6+. No external dependencies.
metadata:
  author: agent-interview-helper
  version: "1.0"
  source: https://github.com/SpellingDragon/agent-interview-helper
  skill_url: https://raw.githubusercontent.com/SpellingDragon/agent-interview-helper/main/skills/interview/SKILL.md
---

Interview preparation assistant — query study plans, search questions, get practice recommendations, and run mock interviews.

## Setup

Clone the repository to access the script and question banks:

```bash
git clone https://github.com/SpellingDragon/agent-interview-helper.git
cd agent-interview-helper
```

The script is `interview_assistant.py` at the project root. No dependencies to install.

## Available Question Banks

| Bank | Directory | Focus |
|------|-----------|-------|
| Agent Platform Engineer | `agent/` | Agent Runtime / Tool / MCP / Memory / Eval (110 questions) |
| AI Infra Engineer | `ai-infra/` | Inference engines / Distributed training / CUDA / System design (105 questions) |
| LLM Theory & Post-training | `llm/` | Transformer / RL post-training / Scaling Law (82 questions) |
| MyGO!!!!! Fan Training | `mygo/` | Members / Music / Live / Trivia (30 questions) |

## CLI Commands

All commands support `--json` for structured output. **Always use `--json` when calling from an agent context.**

### Overview — view study plan progress

```bash
python3 interview_assistant.py --data-dir ./<bank> --overview --json
```

Output: `{"total_days": N, "days": [...], "progress": {"completed": N, "total": N}}`

### Day Detail — view a specific day's tasks

```bash
python3 interview_assistant.py --data-dir ./<bank> --day <N> --json
```

Output: `{"day": N, "title": "...", "sections": {"今日目标": [...], "今日任务": [...], ...}}`

### Search — find questions by keyword

```bash
python3 interview_assistant.py --data-dir ./<bank> --search "<keyword>" --json
```

Output: `{"keyword": "...", "count": N, "questions": [{"qid": N, "title": "...", "category": "..."}]}`

### Practice — get day-recommended questions

```bash
python3 interview_assistant.py --data-dir ./<bank> --practice-day <N> --count <N> --json
```

Output: `{"mode": "practice", "day": N, "count": N, "questions": [{"qid": N, "title": "...", "category": "...", "answer_points": [...]}]}`

### Topic Practice — questions by topic keyword

```bash
python3 interview_assistant.py --data-dir ./<bank> --topic "<keyword>" --count <N> --json
```

Output: `{"mode": "topic", "keyword": "...", "count": N, "questions": [...]}`

### Mock Interview — random question selection

```bash
python3 interview_assistant.py --data-dir ./<bank> --mock --count <N> --json
```

Output: `{"mode": "mock", "count": N, "questions": [{"qid": N, "title": "...", "category": "...", "answer_points": [...]}]}`

### Progress — view completion status

```bash
python3 interview_assistant.py --data-dir ./<bank> --progress --json
```

Output: `{"completed_days": [...], "total_days": N, "completion_rate": 0.0, "recommended_day": N, "practice_sessions": N}`

## How to Choose a Bank

Based on the user's request, select the appropriate `--data-dir`:

- **Agent**: MCP, Tool, Memory, Runtime, Context Engineering, Multi-Agent → `agent/`
- **AI Infra**: CUDA, GPU, vLLM, SGLang, Megatron, distributed training, system design, C++ → `ai-infra/`
- **LLM**: Transformer, attention, MoE, RL, PPO, DPO, GRPO, Scaling Law, PyTorch → `llm/`
- **MyGO!!!!!**: BanG Dream, anime, music, trivia → `mygo/`

If unsure, search across all banks by running `--search` for each.

## Example Interactions

**User**: "Help me practice Transformer questions"
**Agent**: `python3 interview_assistant.py --data-dir ./llm --topic "Transformer" --count 5 --json`

**User**: "Show me the AI Infra study plan"
**Agent**: `python3 interview_assistant.py --data-dir ./ai-infra --overview --json`

**User**: "Run a 5-question mock interview on agent topics"
**Agent**: `python3 interview_assistant.py --data-dir ./agent --mock --count 5 --json`

**User**: "Search for KV Cache questions"
**Agent**: Run `--search "KV Cache" --json` for each bank, aggregate results.

## Important Notes

- Always use `--json` for agent calls — returns valid JSON on stdout, no interactive prompts
- Without `--json`, the tool enters interactive mode and waits for user input
- In `--json` mode, practice/mock commands return questions **with answer points** immediately
- Exit code 0 = success, 1 = error (error details in JSON `error` field)
- The tool reads from `plan.md` and `question.md` in the specified `--data-dir`
