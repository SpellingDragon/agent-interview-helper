## Why

当前 `agent-interview-helper` 只维护一套 Agent 平台工程师题库（`agent/plan.md` + `agent/question.md`）。用户的面试准备实际覆盖三个方向：Agent 平台、AI Infra（训练/推理系统）、LLM 理论（Transformer/RL 后训练）。一套题库无法充分覆盖，且不同方向的项目叙事、知识深度和面试表达差异显著。需要拆分为三套独立题库并行维护，并充分利用 `ai_infra_learning` 知识库中的 130+ 篇笔记作为内容来源。

## What Changes

- 新增 `llm/plan.md` + `llm/question.md`：LLM 理论与后训练方向题库
- 新增 `ai-infra/plan.md` + `ai-infra/question.md`：AI Infra 系统工程方向题库
- 优化 `agent/plan.md` + `agent/question.md`：补充 Transformer 深度、Agent Benchmark、Agentic 推理优化等缺失内容
- 三套题库的项目叙事统一参考 `ai_infra_learning/docs/` 知识库中的真实项目素材
- 每套 plan 只记录行为约束（每天做什么、验收标准），不内联具体题目内容
- question 文件作为独立题库，由 plan 通过主题索引引用

## Capabilities

### New Capabilities
- `llm-bank`: LLM 理论与后训练题库（Transformer 架构、RL 后训练、Scaling Law、推理优化理论）
- `ai-infra-bank`: AI Infra 系统工程题库（推理引擎、分布式训练、CUDA/GPU、C++ 性能工程、系统设计）
- `agent-bank-upgrade`: 优化现有 Agent 题库（补 Transformer 深度、Agent Benchmark、Agentic 推理）

### Modified Capabilities

（无已有 spec 需要修改）

## Impact

- **文件结构**：新增 `llm/`、`ai-infra/` 两个数据目录，与现有 `agent/` 并列
- **脚本兼容**：`interview_assistant.py --data-dir` 已支持任意目录，无需改动
- **知识库依赖**：三套题库的内容生成和校验均参考 `../ai_infra_learning/docs/`
- **.gitignore**：无需改动（新目录均非隐藏目录）
