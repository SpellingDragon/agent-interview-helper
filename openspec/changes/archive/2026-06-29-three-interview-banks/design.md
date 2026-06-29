## Context

项目 `agent-interview-helper` 是一个零依赖 Python 面试助手，通过 `--data-dir` 加载指定目录下的 `plan.md`（14 天执行清单）和 `question.md`（高频问答题库）。当前只有一套 `agent/` 数据。

用户的知识库 `ai_infra_learning/docs/` 包含 130+ 篇笔记，覆盖 Transformer、vLLM、CUDA、Megatron、RL 后训练、CS 基础等方向，是三套题库的主要素材来源。

## Goals / Non-Goals

**Goals:**
- 建立三套独立题库（agent / ai-infra / llm），每套包含 plan + question
- 三套并行生成，互不依赖
- 项目叙事参考知识库中的真实项目素材，脱敏后使用
- plan 只记录行为约束（每天做什么、时间分配、验收标准），不内联具体题目
- question 作为独立题库，题目数量和深度匹配知识库覆盖范围

**Non-Goals:**
- 不修改 `interview_assistant.py` 脚本（已支持 `--data-dir`）
- 不建立跨题库的共享基础模块（各自独立维护）
- 不创建新的文件格式或解析逻辑
- 不在 plan 中嵌入题目答案或详细知识点

## Decisions

### 1. 三套题库的边界划分

| 题库 | 定位 | 核心覆盖 |
|------|------|----------|
| agent | Agent 平台工程师 | Runtime / Tool / MCP / Memory / Eval / Multi-Agent |
| ai-infra | AI Infra 系统工程师 | 推理引擎 / 分布式训练 / CUDA / 系统设计 / C++ 性能 |
| llm | LLM 理论与后训练 | Transformer 架构 / RL 后训练 / Scaling Law / 推理理论 |

**理由**：agent 和 llm 有重叠（如 Attention、KV Cache），但深度和视角不同——agent 侧重"怎么用"，llm 侧重"为什么这样设计"。ai-infra 侧重系统工程实现。三者正交性足够，值得独立维护。

### 2. 知识库引用策略

生成题目时，优先从知识库中提取：
- `ai_infra_learning/docs/interview/` 中的面试真题和回答模板
- 各模块 README 中的"面试定位"和"核心问题"
- 具体笔记中的技术细节和 trade-off 分析

不直接复制知识库原文，而是转化为面试问答格式。

### 3. Plan 与 Question 的解耦

- **plan.md**：只定义每天的主题、任务类型、时间分配、验收标准
- **question.md**：独立的题库文件，按分类编号
- plan 通过主题名称关联 question 中的分类，不引用具体题号

**理由**：题目可能增删，plan 不应与题号耦合。

### 4. 项目叙事来源

| 题库 | 项目叙事来源 |
|------|-------------|
| agent | 现有 agent/ 中的脱敏项目（长程 Agent 框架、数据流水线 Agent、策略平台） |
| ai-infra | `docs/interview/ai-infra-self-engine-interview.md`（自研推理引擎）、`docs/notes/` 中的优化实践 |
| llm | `docs/interview/` 中的 RL 训练实践、`docs/pytorch/07-dpo-ppo-grpo.md` 等 |

### 5. 并行生成策略

三套题库独立生成，每套按以下顺序：
1. 从知识库提取该方向的核心知识点和面试题
2. 生成 question.md（题库）
3. 生成 plan.md（14 天执行清单，引用 question 分类）
4. 验证脚本可正常加载

## Risks / Trade-offs

- **[冗余]** CS 基础题在三套中有重叠 → 各自保留必要子集，不强求去重
- **[知识库时效]** 知识库内容可能未覆盖最新面试题 → 生成后人工审查补充
- **[题目质量]** 纯从知识库提取可能导致题目偏理论 → 加入项目实践类和 trade-off 类题目平衡
- **[脱敏]** 知识库中的项目可能包含敏感信息 → 统一脱敏后再写入题库
