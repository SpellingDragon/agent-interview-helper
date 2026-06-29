## ADDED Requirements

### Requirement: AI Infra 题库文件结构
`ai-infra/` 目录 SHALL 包含 `plan.md` 和 `question.md` 两个文件，格式与现有 `agent/` 一致，可被 `interview_assistant.py --data-dir ai-infra` 正常加载。

#### Scenario: 脚本加载验证
- **WHEN** 执行 `python3 interview_assistant.py --data-dir ./ai-infra --overview`
- **THEN** 输出 14 天执行清单概览，且 question 文件被正确解析

### Requirement: AI Infra 题库覆盖范围
`ai-infra/question.md` SHALL 覆盖以下核心分类：推理引擎（vLLM/SGLang 源码级）、分布式训练（Megatron TP/PP/EP/DP）、CUDA/GPU 编程（架构/Kernel/Triton）、C++ 性能工程（并发/内存模型/Modern C++）、KV Cache 与显存工程、系统设计（训练平台/推理服务）、OS/体系结构/Linux 编程、集合通信与网络。

#### Scenario: 分类完整性
- **WHEN** 检查 question.md 的分类标题
- **THEN** 至少包含 10 个一级分类，总题数不少于 100 题

### Requirement: AI Infra 项目叙事
`ai-infra/question.md` SHALL 包含项目叙事类题目，参考知识库 `docs/interview/ai-infra-self-engine-interview.md`（自研推理引擎）和 `docs/notes/` 中的优化实践，脱敏后使用。

#### Scenario: 项目题存在
- **WHEN** 检查 question.md 中"项目与经历"分类
- **THEN** 至少包含 5 道项目叙事题，每题有回答要点，覆盖自研推理引擎和性能优化实践

### Requirement: AI Infra 执行清单
`ai-infra/plan.md` SHALL 定义 14 天执行清单，每天包含主题、任务类型、时间分配和验收标准。MUST NOT 内联具体题目内容或答案。

#### Scenario: Plan 行为约束
- **WHEN** 检查 plan.md 的每日任务
- **THEN** 每天包含明确的验收标准，且不引用具体题号

### Requirement: AI Infra 题库脱敏
`ai-infra/` 中的所有文件 MUST NOT 包含公司名称、内部产品名或项目代号。

#### Scenario: 敏感词扫描
- **WHEN** 对 ai-infra/ 目录执行敏感词检查
- **THEN** 无敏感词残留
