# 技术准备方案与题库优化计划 — 具体修改任务清单

完成本清单后，`.personal/plan.md` 和 `.personal/question.md` 应达到可直接驱动高强度面试训练的水平。所有修改严格遵循现有 Markdown 结构，不改动 `interview_assistant.py`。

## 1. 准备与基线

- [x] 1.1 备份 `.personal/plan.md` → `.personal/plan.md.bak`。
- [x] 1.2 备份 `.personal/question.md` → `.personal/question.md.bak`。
- [x] 1.3 通读当前两份文档，标记明显偏浅、缺追问点、缺项目锚定的题目。
- [x] 1.4 基于 `.personal/.interview_assistant_state.json` 找出平均分 ≤2 的题目，作为首批优化对象（首批：Q5 `长程 Agent 框架` 核心探索点，自评分 1/5）。
- [x] 1.5 确认 `ai_infra_learning/docs` 十个领域的 README 和关键文件路径可用。

## 2. plan.md 内容优化

### 2.1 方法论与模板嵌入

- [x] 2.1.1 在 `1. 总原则` 中加入四层题模型（L1-L4）和“回答四要素”方法论。
- [x] 2.1.2 在 `2. 执行模板` 的 Step 2 中加入“分层口述练习”要求（30s / 2min / 追问版）。
- [x] 2.1.3 在 `2. 执行模板` 的 Step 3 中加入“输出物检查”要求。
- [x] 2.1.4 在 `17. 每晚 15 分钟复盘模板` 中加入“今日最卡 3 题（注明 qid）”和“明日弱链”。

### 2.2 逐 Day 任务增强

对 Day 1-14，每个 Day 执行以下三项修改：

- [x] 2.2.1 优化 Day 1 `今日任务`：引用具体 qid（Q1-Q4）和 `ai_infra_learning/docs/interview/`、`ai_infra_learning/docs/agent/` 参考范围。
- [x] 2.2.2 优化 Day 1 `今日输出`：明确当天必须产出的 artifact（90 秒自我介绍稿、岗位匹配稿）。
- [x] 2.2.3 优化 Day 1 `晚间复盘`：加入“今日最卡 3 题”和“明日必须补的 3 件事”。

- [x] 2.2.4 优化 Day 2 `今日任务`：引用 qid Q5-Q7，参考 `ai_infra_learning/docs/agent/01-agent-frameworks-and-mcp.md`。
- [x] 2.2.5 优化 Day 2 `今日输出`：明确产出 `长程 Agent 框架` 架构图和 5 分钟讲稿。
- [x] 2.2.6 优化 Day 2 `晚间复盘`：记录 `长程 Agent 框架` 相关最卡题目和弱链。

- [x] 2.2.7 优化 Day 3 `今日任务`：引用 qid Q8-Q9，参考 `ai_infra_learning/docs/agent/01-agent-frameworks-and-mcp.md`、数据流水线项目资料。
- [x] 2.2.8 优化 Day 3 `今日输出`：明确产出数据流水线 Agent 链路图和 5 分钟讲稿。
- [x] 2.2.9 优化 Day 3 `晚间复盘`：记录数据流水线 Agent 相关最卡题目和弱链。

- [x] 2.2.10 优化 Day 4 `今日任务`：引用 qid Q10-Q12，参考 `ai_infra_learning/docs/recsys-infra/`、规则引擎项目资料。
- [x] 2.2.11 优化 Day 4 `今日输出`：明确产出规则引擎与 Agent Runtime 对照表和 5 分钟讲稿。
- [x] 2.2.12 优化 Day 4 `晚间复盘`：记录规则引擎相关最卡题目和弱链。

- [x] 2.2.13 优化 Day 5 `今日任务`：引用 qid Q13-Q23，参考 `ai_infra_learning/docs/agent/04-agent-evaluation-and-harness.md`。
- [x] 2.2.14 优化 Day 5 `今日输出`：明确产出 Agent Runtime 总论笔记和 5 个核心抽象定义。
- [x] 2.2.15 优化 Day 5 `晚间复盘`：记录 Agent/Agent Runtime 核心题最卡点。

- [x] 2.2.16 优化 Day 6 `今日任务`：引用 qid Q16-Q27，参考 `ai_infra_learning/docs/agent/01-agent-frameworks-and-mcp.md`。
- [x] 2.2.17 优化 Day 6 `今日输出`：明确产出 Tool Use 流程图和 Skill/Tool/Workflow/Subagent 对照表。
- [x] 2.2.18 优化 Day 6 `晚间复盘`：记录 Tool/MCP 相关最卡题目和弱链。

- [x] 2.2.19 优化 Day 7 `今日任务`：引用 qid Q28-Q36，参考 `ai_infra_learning/docs/transformer/02-attention-variants.md`、`ai_infra_learning/docs/transformer/07-long-context.md`。
- [x] 2.2.20 优化 Day 7 `今日输出`：明确产出 Memory 分层图和 Context Engineering 口述稿。
- [x] 2.2.21 优化 Day 7 `晚间复盘`：记录 Memory/Context 相关最卡题目和弱链。

- [x] 2.2.22 优化 Day 8 `今日任务`：引用 qid Q37-Q42，参考 `ai_infra_learning/docs/agent/04-agent-evaluation-and-harness.md`。
- [x] 2.2.23 优化 Day 8 `今日输出`：明确产出 Trace 字段清单和 Eval 指标草案。
- [x] 2.2.24 优化 Day 8 `晚间复盘`：记录 Trace/Eval/Replay 相关最卡题目和弱链。

- [x] 2.2.25 优化 Day 9 `今日任务`：引用 qid Q43-Q52，参考 `ai_infra_learning/docs/transformer/`、`ai_infra_learning/docs/ai-infra-basics/01-gpu-memory-analysis.md`。
- [x] 2.2.26 优化 Day 9 `今日输出`：明确产出 LLM/推理基础笔记和 KV Cache 1 分钟解释稿。
- [x] 2.2.27 优化 Day 9 `晚间复盘`：记录 LLM/推理基础最卡题目和弱链。

- [x] 2.2.28 优化 Day 10 `今日任务`：引用 qid Q53-Q66，参考 `ai_infra_learning/docs/cs-foundations/` 系统设计相关文件。
- [x] 2.2.29 优化 Day 10 `今日输出`：明确产出 Agent Tool 服务系统设计草图和缓存/幂等问答卡。
- [x] 2.2.30 优化 Day 10 `晚间复盘`：记录系统设计与后端基础最卡题目和弱链。

- [x] 2.2.31 优化 Day 11 `今日任务`：引用 qid Q73-Q80，参考 `ai_infra_learning/docs/cs-foundations/os-basics-for-ai-infra.md`、`computer-networks-for-ai-infra.md`。
- [x] 2.2.32 优化 Day 11 `今日输出`：明确产出基础题速记表和 40 题快答卡。
- [x] 2.2.33 优化 Day 11 `晚间复盘`：记录 OS/网络/SQL/前端最卡题目和弱链。

- [x] 2.2.34 优化 Day 12 `今日任务`：引用 qid Q67-Q72，参考 `ai_infra_learning/docs/cs-foundations/cpp-basics-for-ai-infra.md`。
- [x] 2.2.35 优化 Day 12 `今日输出`：明确产出 Go/C++/STL 快答卡。
- [x] 2.2.36 优化 Day 12 `晚间复盘`：记录语言基础最卡题目和弱链。

- [x] 2.2.37 优化 Day 13 `今日任务`：引用 qid Q88-Q92，参考 `ai_infra_learning/docs/cs-foundations/algorithms-for-ai-infra.md`。
- [x] 2.2.38 优化 Day 13 `今日输出`：明确产出 40 分钟笔试结果和错题复盘记录。
- [x] 2.2.39 优化 Day 13 `晚间复盘`：记录算法/coding 最卡题目和弱链。

- [x] 2.2.40 优化 Day 14 `今日任务`：引用 qid Q1-Q94 中弱链题，参考相关分类资料。
- [x] 2.2.41 优化 Day 14 `今日输出`：明确产出模拟面录音/逐题记录和最终卡点清单。
- [x] 2.2.42 优化 Day 14 `晚间复盘`：记录全链路模拟面暴露的顶层弱链。

### 2.3 最终检查表

- [x] 2.3.1 更新 `18. 面试前最后检查表`，按 L1-L4 四层能力组织检查项。
- [x] 2.3.2 确保所有 Day 标题和 section 名称符合现有解析规则（无新增 section）。

## 3. question.md 内容优化

### 3.1 使用说明

- [x] 3.1.1 在 `1. 使用说明` 中写入题目质量标准：四要素、追问点、常见误区、项目锚定。
- [x] 3.1.2 在使用说明中明确“一句话版”用于 30 秒快答，并给出示例。
- [x] 3.1.3 在使用说明中说明 L3/L4 追问的训练方法。

### 3.2 岗位匹配与动机（Q1-Q4）

- [x] 3.2.1 重写 Q1-Q4 的 `回答要点`，按四要素组织。
- [x] 3.2.2 为 Q1-Q4 补充 L3 场景追问和 L4 身份/前沿追问。
- [x] 3.2.3 为 Q1-Q4 补充 `常见误区`。
- [x] 3.2.4 在 Q1-Q4 中自然嵌入 `长程 Agent 框架`、数据流水线 Agent、策略平台 / 规则引擎等项目锚点。
- [x] 3.2.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/interview/`、`ai_infra_learning/docs/agent/README.md`。

### 3.3 项目与经历（Q5-Q12）

- [x] 3.3.1 重写 Q5-Q12 的 `回答要点`，突出“为什么做、核心抽象、失败案例、演进方向”。
- [x] 3.3.2 为 Q5-Q12 补充 L3 追问（如 EventKey 延迟抖动定位、数据流水线链路瓶颈）。
- [x] 3.3.3 为 Q5-Q12 补充 L4 追问（如把 MLA/Mooncake 思想应用到项目）。
- [x] 3.3.4 为 Q5-Q12 补充 `常见误区`。
- [x] 3.3.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/agent/01-agent-frameworks-and-mcp.md`、`ai_infra_learning/docs/agent/04-agent-evaluation-and-harness.md`。

### 3.4 Agent / Agent Runtime 核心（Q13-Q23）

- [x] 3.4.1 重写 Q13-Q23 的 `回答要点`，确保每个答案包含四要素。
- [x] 3.4.2 为 Q13-Q23 补充 L3 场景追问（Tool 失败、上下文污染、规划失败诊断）。
- [x] 3.4.3 为 Q13-Q23 补充 L4 身份/前沿追问（与 `长程 Agent 框架` 设计对照、与 Agent 平台 / AI Infra 定位对照）。
- [x] 3.4.4 为 Q13-Q23 补充 `常见误区`。
- [x] 3.4.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/agent/01-agent-frameworks-and-mcp.md`、`ai_infra_learning/docs/agent/04-agent-evaluation-and-harness.md`、`ai_infra_learning/docs/agent/06-open-source-agent-ecosystem-and-long-horizon-training.md`。

### 3.5 MCP / Tool 平台（Q24-Q27）

- [x] 3.5.1 重写 Q24-Q27 的 `回答要点`，按四要素组织。
- [x] 3.5.2 为 Q24-Q27 补充 L3 追问（权限隔离、缓存策略、失败重试设计）。
- [x] 3.5.3 为 Q24-Q27 补充 L4 追问（把 MCP Tool 与策略平台内容解析 Tool 的经历结合）。
- [x] 3.5.4 为 Q24-Q27 补充 `常见误区`。
- [x] 3.5.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/agent/01-agent-frameworks-and-mcp.md`。

### 3.6 Memory / Context Engineering（Q28-Q36）

- [x] 3.6.1 重写 Q28-Q36 的 `回答要点`，强化 Memory 与 RAG/历史/上下文的边界。
- [x] 3.6.2 为 Q28-Q36 补充 L3 追问（长上下文 OOM、Memory 清理策略、按阶段注入）。
- [x] 3.6.3 为 Q28-Q36 补充 L4 追问（把 MLA/Engram 的 KV 压缩思想应用到 `长程 Agent 框架` Memory）。
- [x] 3.6.4 为 Q28-Q36 补充 `常见误区`。
- [x] 3.6.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/transformer/02-attention-variants.md`、`ai_infra_learning/docs/transformer/07-long-context.md`、`ai_infra_learning/docs/transformer/10-mla-deep-dive.md`。

### 3.7 Trace / Eval / Replay（Q37-Q42）

- [x] 3.7.1 重写 Q37-Q42 的 `回答要点`，按四要素组织。
- [x] 3.7.2 为 Q37-Q42 补充 L3 追问（失败归因路径、没有标准答案时怎么做 Eval）。
- [x] 3.7.3 为 Q37-Q42 补充 L4 追问（数据流水线 Agent 的失败归因案例、与 `长程 Agent 框架` Trace 设计对照）。
- [x] 3.7.4 为 Q37-Q42 补充 `常见误区`。
- [x] 3.7.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/agent/04-agent-evaluation-and-harness.md`。

### 3.8 LLM 与推理基础（Q43-Q52）

- [x] 3.8.1 重写 Q43-Q52 的 `回答要点`，确保从直觉到工程影响完整。
- [x] 3.8.2 为 Q43-Q52 补充 L3 追问（显存估算、batch/延迟/吞吐权衡、Agent 多轮成本爆炸）。
- [x] 3.8.3 为 Q43-Q52 补充 L4 追问（长程 Agent 中的 KV Cache 管理、与 vLLM 调度结合）。
- [x] 3.8.4 为 Q43-Q52 补充 `常见误区`。
- [x] 3.8.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/transformer/`、`ai_infra_learning/docs/ai-infra-basics/01-gpu-memory-analysis.md`、`ai_infra_learning/docs/pytorch/04-rope-rmsnorm-swiglu-mla.md`。

### 3.9 Multi-Agent / Planning（Q53-Q56）

- [x] 3.9.1 重写 Q53-Q56 的 `回答要点`，按四要素组织。
- [x] 3.9.2 为 Q53-Q56 补充 L3 追问（什么情况下 Multi-Agent 反而更差、规划失败恢复）。
- [x] 3.9.3 为 Q53-Q56 补充 L4 追问（数据流水线 Agent 中哪些步骤该工程约束、哪些该模型规划）。
- [x] 3.9.4 为 Q53-Q56 补充 `常见误区`。
- [x] 3.9.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/agent/06-open-source-agent-ecosystem-and-long-horizon-training.md`。

### 3.10 规则引擎 / DAG Runtime / DSL（Q57-Q60）

- [x] 3.10.1 重写 Q57-Q60 的 `回答要点`，按四要素组织。
- [x] 3.10.2 为 Q57-Q60 补充 L3 追问（配置热更新回滚、DSL 失控防御、DAG Runtime 失败恢复）。
- [x] 3.10.3 为 Q57-Q60 补充 L4 追问（把规则引擎经验映射到 Agent Runtime 的 Prompt/Policy 配置化系统）。
- [x] 3.10.4 为 Q57-Q60 补充 `常见误区`。
- [x] 3.10.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/recsys-infra/01-recsys-infra-overview.md`（DSL/算子编排部分）。

### 3.11 后端与系统设计（Q61-Q66）

- [x] 3.11.1 重写 Q61-Q66 的 `回答要点`，按四要素组织。
- [x] 3.11.2 为 Q61-Q66 补充 L3 追问（Agent 高频调用 Tool 的限流熔断设计、幂等实现细节）。
- [x] 3.11.3 为 Q61-Q66 补充 L4 追问（把后端经验与 Agent 运行时稳定性结合）。
- [x] 3.11.4 为 Q61-Q66 补充 `常见误区`。
- [x] 3.11.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/cs-foundations/os-basics-for-ai-infra.md`、`computer-networks-for-ai-infra.md`。

### 3.12 Go / C++ / 语言基础（Q67-Q72）

- [x] 3.12.1 重写 Q67-Q72 的 `回答要点`，按四要素组织。
- [x] 3.12.2 为 Q67-Q72 补充 L3 追问（goroutine 调度对 Agent 并发的影响、C++ 容器在推理服务中的使用陷阱）。
- [x] 3.12.3 为 Q67-Q72 补充 L4 追问（`长程 Agent 框架` 选择 Go 的 trade-off、与 C++ 推理服务交互的边界）。
- [x] 3.12.4 为 Q67-Q72 补充 `常见误区`。
- [x] 3.12.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/cs-foundations/cpp-basics-for-ai-infra.md`、`cpp-concurrency-and-memory-model.md`。

### 3.13 操作系统 / 网络 / SQL / 前端（Q73-Q80）

- [x] 3.13.1 重写 Q73-Q80 的 `回答要点`，按四要素组织。
- [x] 3.13.2 为 Q73-Q80 补充 L3 追问（高并发下的 TCP 行为、SQL 慢查询分析、跨域安全实践）。
- [x] 3.13.3 为 Q73-Q80 补充 L4 追问（这些基础问题如何影响 Agent 服务稳定性）。
- [x] 3.13.4 为 Q73-Q80 补充 `常见误区`。
- [x] 3.13.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/cs-foundations/os-basics-for-ai-infra.md`、`computer-networks-for-ai-infra.md`。

### 3.14 GPU / 推理工程（Q81-Q83）

- [x] 3.14.1 重写 Q81-Q83 的 `回答要点`，按四要素组织。
- [x] 3.14.2 为 Q81-Q83 补充 L3 追问（显存瓶颈定位、batch 与延迟权衡）。
- [x] 3.14.3 为 Q81-Q83 补充 L4 追问（Agent 多轮 loop 中的推理成本优化、与 vLLM 调度结合）。
- [x] 3.14.4 为 Q81-Q83 补充 `常见误区`。
- [x] 3.14.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/ai-infra-basics/01-gpu-memory-analysis.md`、`ai_infra_learning/docs/vllm/02-vllm-block-attention-deep-dive.md`。

### 3.15 AI Coding 与开发者体验（Q84-Q87）

- [x] 3.15.1 重写 Q84-Q87 的 `回答要点`，按四要素组织。
- [x] 3.15.2 为 Q84-Q87 补充 L3 追问（AI 生成代码的 review 流程、关键路径如何保留人工把控）。
- [x] 3.15.3 为 Q84-Q87 补充 L4 追问（AI Coding 实践如何反哺 Agent/Agent Runtime 设计）。
- [x] 3.15.4 为 Q84-Q87 补充 `常见误区`。
- [x] 3.15.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/interview/custom-preset-questions.md`。

### 3.16 算法与 coding（Q88-Q92）

- [x] 3.16.1 重写 Q88-Q92 的 `回答要点`，按四要素组织。
- [x] 3.16.2 为 Q88-Q92 补充 L3 追问（复杂度分析常见漏点、大输入规模下的边界处理）。
- [x] 3.16.3 为 Q88-Q92 补充 L4 追问（这些算法能力在 Agent 运行时或推理优化中的实际应用场景）。
- [x] 3.16.4 为 Q88-Q92 补充 `常见误区`。
- [x] 3.16.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/cs-foundations/algorithms-for-ai-infra.md`、`ai_infra_learning/docs/interview/quant-cpp-coding-problems.md`。

### 3.17 反问面试官（Q93-Q94）

- [x] 3.17.1 重写 Q93-Q94 的 `回答要点`，按四要素组织。
- [x] 3.17.2 为 Q93-Q94 补充 L3 追问（如何根据面试官回答判断团队技术深度）。
- [x] 3.17.3 为 Q93-Q94 补充 L4 追问（针对 Agent Runtime 团队提出能体现技术判断的问题）。
- [x] 3.17.4 为 Q93-Q94 补充 `常见误区`。
- [x] 3.17.5 在该分类末尾添加 `#### 本分类参考范围`：`ai_infra_learning/docs/interview/README.md`。

### 3.18 每日抽查清单

- [x] 3.18.1 更新抽查标准：每题抽查是否达到 30s 结论、2min 结构、项目例子、trade-off、失败模式。
- [x] 3.18.2 在抽查清单后补充“资料范围总览”，指向 `ai_infra_learning/docs` 各目录。

### 3.19 新增与跨域题目补充

- [x] 3.19.1 在 `Agent / Agent Runtime 核心` 分类中新增 3-5 道 L4 题，结合 目标团队 MLA/GRPO/DualPipe/Mooncake 与项目锚点。
- [x] 3.19.2 在 `LLM 与推理基础` / `GPU / 推理工程` 中补充 3-5 道 vLLM 调度、Prefix Caching、PD 分离相关题。
- [x] 3.19.3 在 `规则引擎 / DAG Runtime / DSL` 中补充 2-3 道与推荐系统 Infra DSL/算子编排相关题，参考 `ai_infra_learning/docs/recsys-infra/`。
- [x] 3.19.4 如需系统覆盖 recsys，可在 question.md 末尾新增 `## 19. 推荐系统与 Infra` 分类，包含 5-8 道题。（已通过在规则引擎分类中新增 Q66、Q67 系统覆盖 recsys，未新增独立分类以保持文档聚焦。）
- [x] 3.19.5 统一全题库编号，确保新增/拆分题目后 qid 连续；同步更新 `plan.md` 中引用的 qid。

### 3.20 coding 算法题扩充（用户追加）

- [x] 3.20.1 在 `16. 算法与 coding` 分类中新增 4 道 coding 算法题，覆盖双指针/滑动窗口、前缀和/差分、链表、递归改迭代模式。
- [x] 3.20.2 为新题按四要素组织 `回答要点`，补充 L3 追问（边界处理、性能优化）和 L4 追问（与 Agent/Infra 场景的关联）。
- [x] 3.20.3 为新题补充 `常见误区`。
- [x] 3.20.4 统一全题库编号，同步更新 `plan.md` Day 13 的 qid 范围。
- [x] 3.20.5 运行 `python3 interview_assistant.py --topic coding --count 5` 验证新题解析与分类显示正常。

## 4. 验证与闭环

- [x] 4.1 运行 `python3 interview_assistant.py --overview` 确认 `plan.md` 解析正常。
- [x] 4.2 运行 `python3 interview_assistant.py --topic Memory --count 3` 确认 `question.md` section 显示正常。
- [x] 4.3 对优化后的分类逐个运行 `python3 interview_assistant.py --topic <关键词> --count 5`，验证无格式错误。
- [x] 4.4 运行一次 `python3 interview_assistant.py --mock --count 8`，记录新题分数。
- [x] 4.5 根据 mock 结果微调 `plan.md` 的 Day 任务和 `question.md` 的追问点。
- [x] 4.6 删除备份文件 `.personal/plan.md.bak` 和 `.personal/question.md.bak`（确认无误后）。
