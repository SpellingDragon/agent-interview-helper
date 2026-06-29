## ADDED Requirements

### Requirement: JSON 输出参数
脚本 SHALL 支持 `--json` 全局参数。当指定时，所有命令的输出 SHALL 为合法的 JSON 格式。

#### Scenario: overview 命令 JSON 输出
- **WHEN** 执行 `python3 interview_assistant.py --data-dir ./agent --overview --json`
- **THEN** stdout 输出合法 JSON，包含 `total_days`、`days` 数组（每项含 `day`、`title`、`completed`）、`progress` 对象

#### Scenario: day 详情 JSON 输出
- **WHEN** 执行 `python3 interview_assistant.py --data-dir ./agent --day 7 --json`
- **THEN** stdout 输出合法 JSON，包含 `day`、`title`、`sections` 对象

#### Scenario: search 命令 JSON 输出
- **WHEN** 执行 `python3 interview_assistant.py --data-dir ./llm --search "MoE" --json`
- **THEN** stdout 输出合法 JSON，包含 `keyword`、`count`、`questions` 数组

#### Scenario: mock/practice JSON 输出
- **WHEN** 执行 `python3 interview_assistant.py --data-dir ./ai-infra --mock --count 3 --json`
- **THEN** stdout 输出合法 JSON，包含 `mode`、`count`、`questions` 数组（每项含 `qid`、`title`、`category`、`answer_points`）

### Requirement: JSON 模式非交互
当指定 `--json` 时，脚本 SHALL 不进入交互式菜单，不输出 "进入练习模式" 等提示，不等待用户输入打分或卡点。

#### Scenario: mock 命令不等待输入
- **WHEN** 执行 `python3 interview_assistant.py --data-dir ./agent --mock --count 2 --json`
- **THEN** 命令立即返回 JSON 输出，不等待 stdin 输入

### Requirement: 向后兼容
不指定 `--json` 时，所有命令的行为 SHALL 与修改前完全一致。

#### Scenario: 默认输出不变
- **WHEN** 执行 `python3 interview_assistant.py --data-dir ./agent --overview`
- **THEN** 输出与修改前的表格格式完全一致

### Requirement: progress 命令 JSON 输出
`--progress --json` SHALL 输出进度信息的 JSON 格式。

#### Scenario: progress JSON
- **WHEN** 执行 `python3 interview_assistant.py --data-dir ./agent --progress --json`
- **THEN** stdout 输出合法 JSON，包含 `completed_days`、`total_days`、`completion_rate`
