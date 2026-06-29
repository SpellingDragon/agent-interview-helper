## ADDED Requirements

### Requirement: LLM 题库文件结构
`llm/` 目录 SHALL 包含 `plan.md` 和 `question.md` 两个文件，格式与现有 `agent/` 一致，可被 `interview_assistant.py --data-dir llm` 正常加载。

#### Scenario: 脚本加载验证
- **WHEN** 执行 `python3 interview_assistant.py --data-dir ./llm --overview`
- **THEN** 输出 14 天执行清单概览，且 question 文件被正确解析

### Requirement: LLM 题库覆盖范围
`llm/question.md` SHALL 覆盖以下核心分类：Transformer 架构深度（Attention 变体、MoE、位置编码、长上下文）、RL 后训练（SFT/DPO/PPO/GRPO）、Scaling Law 与推理模型、PyTorch 实现（GPT/LoRA/量化）、KV Cache 与显存理论。

#### Scenario: 分类完整性
- **WHEN** 检查 question.md 的分类标题
- **THEN** 至少包含 8 个一级分类，总题数不少于 80 题

### Requirement: LLM 项目叙事
`llm/question.md` SHALL 包含项目叙事类题目，参考知识库 `docs/interview/` 和 `docs/pytorch/` 中的真实项目素材，脱敏后使用。

#### Scenario: 项目题存在
- **WHEN** 检查 question.md 中"项目与经历"分类
- **THEN** 至少包含 5 道项目叙事题，每题有回答要点

### Requirement: LLM 执行清单
`llm/plan.md` SHALL 定义 14 天执行清单，每天包含主题、任务类型、时间分配和验收标准。MUST NOT 内联具体题目内容或答案。

#### Scenario: Plan 行为约束
- **WHEN** 检查 plan.md 的每日任务
- **THEN** 每天包含明确的验收标准，且不引用具体题号

### Requirement: LLM 题库脱敏
`llm/` 中的所有文件 MUST NOT 包含公司名称、内部产品名或项目代号。

#### Scenario: 敏感词扫描
- **WHEN** 对 llm/ 目录执行敏感词检查
- **THEN** 无 DeepSeek、Harness、tagent、元宝等残留
