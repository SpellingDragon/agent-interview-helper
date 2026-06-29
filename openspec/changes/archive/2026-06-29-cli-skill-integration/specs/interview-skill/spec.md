## ADDED Requirements

### Requirement: Skill 文件存在
项目 SHALL 包含 `.qoder/skills/interview/SKILL.md`，定义 `interview` 斜杠命令。

#### Scenario: Skill 文件可被发现
- **WHEN** Qoder 扫描 `.qoder/skills/` 目录
- **THEN** 发现 `interview` skill，包含 name、description、兼容性和使用指引

### Requirement: Skill 覆盖核心命令
Skill SHALL 指引 Agent 如何调用以下 CLI 命令：overview、day detail、search、topic practice、mock interview。每个命令 SHALL 使用 `--json` 输出。

#### Scenario: Agent 调用 overview
- **WHEN** 用户请求"查看 agent 题库的进度概览"
- **THEN** Agent 构造命令 `python3 interview_assistant.py --data-dir ./agent --overview --json` 并解析 JSON 结果

#### Scenario: Agent 调用 search
- **WHEN** 用户请求"在 llm 题库中搜索 Transformer 相关题目"
- **THEN** Agent 构造命令 `python3 interview_assistant.py --data-dir ./llm --search "Transformer" --json` 并解析 JSON 结果

#### Scenario: Agent 调用 mock
- **WHEN** 用户请求"从 ai-infra 题库随机抽 5 题模拟面试"
- **THEN** Agent 构造命令 `python3 interview_assistant.py --data-dir ./ai-infra --mock --count 5 --json` 并将题目以自然语言呈现给用户

### Requirement: Skill 描述可用题库
Skill SHALL 列出项目中可用的题库目录（agent、ai-infra、llm、mygo）及其定位，帮助 Agent 选择正确的 `--data-dir`。

#### Scenario: Agent 选择正确题库
- **WHEN** 用户请求"帮我练习 CUDA 相关的面试题"
- **THEN** Agent 识别 CUDA 属于 ai-infra 方向，使用 `--data-dir ./ai-infra`
