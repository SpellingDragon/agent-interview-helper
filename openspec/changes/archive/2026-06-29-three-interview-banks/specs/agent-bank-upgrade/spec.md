## ADDED Requirements

### Requirement: Agent 题库 Transformer 补充
`agent/question.md` SHALL 新增 Transformer 架构深度题目，覆盖 MHA→GQA→MLA 演进、RoPE 位置编码、MoE 路由策略、FlashAttention/PagedAttention。新增题目 SHALL 融入现有分类体系，不破坏已有编号。

#### Scenario: Transformer 题数增加
- **WHEN** 检查 agent/question.md 中与 Transformer 相关的题目
- **THEN** 至少新增 10 题，覆盖注意力变体、位置编码、MoE、加速

### Requirement: Agent 题库 Benchmark 补充
`agent/question.md` SHALL 新增 Agent 评估与 Benchmark 题目，覆盖 SWE-bench、GAIA、WebArena 等具体 benchmark 的评估流程，以及 Harness 体系设计。

#### Scenario: Benchmark 题数增加
- **WHEN** 检查 agent/question.md 中与 Agent 评估相关的题目
- **THEN** 至少新增 5 题

### Requirement: Agent 题库 Agentic 推理补充
`agent/question.md` SHALL 新增 Agentic 推理优化题目，覆盖 Agent 场景的 prefill/decode 比特性、Prefix Caching 复用 system prompt、DualPath 等。

#### Scenario: 推理优化题数增加
- **WHEN** 检查 agent/question.md 中与 Agentic 推理相关的题目
- **THEN** 至少新增 3 题

### Requirement: Agent Plan 同步更新
`agent/plan.md` SHALL 在相关 Day 中增加新增题目的练习安排，保持 plan 与 question 的主题对齐。MUST NOT 内联具体题目内容。

#### Scenario: Plan-Question 对齐
- **WHEN** 检查 plan.md 中 Transformer、Benchmark、推理优化相关 Day
- **THEN** 每天任务包含对这些新增主题的练习安排

### Requirement: Agent 题库编号连续
新增题目后，`agent/question.md` 的题号 SHALL 保持从 Q1 开始连续编号，无跳号无重复。

#### Scenario: 编号验证
- **WHEN** 解析 agent/question.md 的所有题号
- **THEN** 题号从 1 到 N 连续递增，无间隔
