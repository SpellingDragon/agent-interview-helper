# Agent 工程师 14 天每日执行清单

> 适用对象：当前会话中的候选人背景
> 目标：把面试准备从“知道要学什么”变成“每天具体做什么”
> 使用方式：
> 1. 每天按清单执行
> 2. 每天结束做 15 分钟复盘
> 3. 未完成项顺延，但不要打乱主线优先级

---

## 1. 总原则

这 14 天的准备按四条主线推进：

- `主线一`：把项目讲扎实，尤其是 `长程 Agent 框架`、数据流水线 Agent、策略平台 / 规则引擎
- `主线二`：把 Agent / Agent Runtime / Memory / MCP / Trace / Eval 补成系统认知
- `主线三`：把 OS / 网络 / SQL / Go / C++ / 算法这些宽口径基础补齐
- `主线四`：形成稳定的面试表达，包括自我介绍、项目叙事、问答节奏和 coding 手感

每天建议时间分配：

- `90 分钟`：项目与岗位叙事
- `90 分钟`：Agent / LLM / Agent Runtime 理论
- `60 分钟`：基础知识快问快答
- `60 分钟`：算法 / coding
- `15 分钟`：复盘

如果工作日时间紧，最低保底也要做三件事：

- 口述 1 次项目
- 刷 1 组基础题
- 写 1 道 coding

### 面试题四层模型与回答四要素

为了让每道题都能答出深度，我们把面试题按四层递进准备：

- `L1 概念层`：是什么、为什么。用于 30 秒快答。
- `L2 整合层`：对比、边界、trade-off。用于 2 分钟结构化回答。
- `L3 场景层`：设计、诊断、优化。用于回答“如果它错了/慢了/贵了怎么办”。
- `L4 身份/前沿层`：把问题焊接到自己的项目，或连接到 目标团队 技术栈（MLA、GRPO、DualPipe、Mooncake、Engram）。

每道核心题的回答按四要素组织：

1. `定义/机制`：先讲清楚它是什么。
2. `为什么重要`：说明它在真实系统中的作用。
3. `工程做法`：常见实现或你的实践经验。
4. `权衡/边界/失败模式`：什么时候会崩、怎么做取舍。

L2-L4 题必须落到自己的项目：`长程 Agent 框架`、数据流水线 Agent、策略平台 / 规则引擎 / MCP Tool。

---

## 2. 执行模板

每天统一按下面四步做：

### Step 1. 输入

- 阅读当日主题材料
- 对照前一天复盘结果
- 明确今天的产出物

### Step 2. 输出

- 至少口述 2 次，其中至少 1 次按“30 秒结论 → 2 分钟结构 → 追问版”分层练习
- 至少写 1 页笔记
- 至少完成 1 次限时题目练习
- 至少产出 1 个可交付 artifact（图 / 讲稿 / 伪代码 / checklist）

### Step 3. 验收

- 是否能脱稿回答
- 是否能给出工程 trade-off
- 是否能举自己项目里的例子
- 是否能说出一个失败模式
- 当天的 artifact 是否完整

### Step 4. 复盘

- 今天最卡的 3 道题是什么（注明 qid）
- 哪些回答还是“概念对，表达乱”
- 哪些题会做，但速度还不够
- 明天的 3 个弱链是什么

---

## 3. Day 1：统一岗位叙事

### 今日目标

- 把“为什么是我、为什么是 Agent Runtime、为什么是 目标团队”讲顺
- 形成 90 秒自我介绍
- 形成 3 个项目的主叙事框架

### 今日任务

1. 写一版 90 秒自我介绍
2. 写一版 3 分钟岗位匹配表达
3. 为以下项目各写 1 页讲稿
   - `长程 Agent 框架`
   - 数据流水线 Agent
   - 策略平台 / 规则引擎 / 在线 Agent 内容解析 Tool
4. 每个项目列 10 个可能追问
5. 分层口述练习：Q1-Q4（岗位匹配与动机）
6. 参考资料：`ai_infra_learning/docs/interview/`、`ai_infra_learning/docs/agent/README.md`

### 今日输出

- `90 秒自我介绍稿`
- `为什么是 Agent Runtime` 口述稿
- `3 个项目的讲稿初版`
- Q1-Q4 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 能在 90 秒内清楚说出自己的定位
- 不使用空泛表达，如“我对 AI 很有热情”
- 能把过去经历自然过渡到 Agent Runtime，而不是像转行

### 晚间复盘

- 今天是否能不看稿完整讲一遍
- 哪个项目最虚，需要补细节
- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 4. Day 2：项目深讲一，`长程 Agent 框架`

### 今日目标

- 把 `长程 Agent 框架` 讲成“有抽象、有取舍、有演进路线”的项目

### 今日任务

1. 画出 `长程 Agent 框架` 的简版架构图
2. 梳理以下问题的回答
   - 为什么做这个项目
   - 和通用 Agent 框架相比，核心探索点是什么
   - 为什么 Memory 是核心抽象
   - 为什么 Agent 之间传 `EventKey`
   - Skill / Tool / Agent / Model 边界是什么
3. 写出 3 个失败案例或尚未解决的问题
4. 写出 3 个下一步演进方向
5. 分层口述练习：Q5-Q7（项目与经历）
6. 参考资料：`ai_infra_learning/docs/agent/01-agent-frameworks-and-mcp.md`

### 今日输出

- `长程 Agent 框架 架构图`
- `长程 Agent 框架 5 分钟讲稿`
- `长程 Agent 框架 追问题答案`
- Q5-Q7 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 能清晰讲出系统边界和执行路径
- 能说出不是“造轮子”，而是在探索什么问题
- 能讲 trade-off，而不是只讲亮点

### 加练

- 用 1 分钟回答“为什么 Agent 之间不直接传大段上下文”

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 5. Day 3：项目深讲二，数据流水线 Agent

### 今日目标

- 把数据流水线 Agent 讲成一个完整闭环的工程系统，而不是一个 Demo

### 今日任务

1. 梳理链路
   - 直播事件监听
   - 互动清洗与抽样
   - 热点时间段识别
   - 多模态理解
   - 切片方案生成
   - 视频处理
   - 投稿与归档
2. 分析哪些步骤由工程确定，哪些步骤交给 Agent
3. 梳理 Tool 化设计和参数校验方式
4. 补 3 个可追问的工程难点
5. 分层口述练习：Q8-Q9（项目与经历）
6. 参考资料：`ai_infra_learning/docs/agent/01-agent-frameworks-and-mcp.md`、数据流水线 Agent 项目资料

### 今日输出

- `数据流水线 Agent 链路图`
- `数据流水线 Agent 5 分钟讲稿`
- `数据流水线 Agent 工程难点清单`
- Q8-Q9 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 能说清楚它为什么是 Agent，而不是纯 workflow
- 能说清楚 Tool 和 Memory key 的价值
- 能回答“20 分钟链路里瓶颈在哪”

### 晚间抽查

- 用 2 分钟回答“哪些步骤必须靠 Tool，哪些可以交给模型”

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 6. Day 4：项目深讲三，策略平台 / 规则引擎

### 今日目标

- 把规则引擎项目翻译成 Agent Runtime 语言

### 今日任务

1. 梳理系统核心链路
   - 实验组获取
   - 策略决策
   - 执行上报
   - 配置热发布
   - 灰度和回滚
2. 梳理 DSL / AST / UDF / SDK 本地预解析的设计取舍
3. 写出这个项目和 Agent Runtime 的相似点与不同点
4. 准备缓存、校验、配置安全、审批、回滚相关追问
5. 分层口述练习：Q10-Q12（项目与经历）
6. 参考资料：`ai_infra_learning/docs/recsys-infra/01-recsys-infra-overview.md`、规则引擎项目资料

### 今日输出

- `规则引擎与 Agent Runtime 对照表`
- `策略平台项目 5 分钟讲稿`
- `可视化配置与热更新答题卡`
- Q10-Q12 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 能回答“为什么这个项目与 Agent Runtime 相关”
- 能说出配置化系统和模型行为策略平台的共性
- 能回答“为什么把策略从代码发布改成配置热变更”

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 7. Day 5：Agent / Agent Runtime 总论

### 今日目标

- 建立岗位语言下的统一知识框架

### 今日任务

1. 逐题口述以下主题
   - 什么是 Agent Runtime
   - Agent Runtime 和 Agent Framework 的区别
   - Agent Runtime 和 Workflow Engine 的关系
   - Prompt Engineering、Context Engineering、Agent Runtime Engineering 的区别
2. 为每个概念补 1 个工程例子
3. 写出 5 个你认同的 Agent Runtime 核心抽象
4. 分层口述练习：Q13-Q26（Agent / Agent Runtime 核心）
5. 参考资料：`ai_infra_learning/docs/agent/04-agent-evaluation-and-harness.md`

### 今日输出

- `Agent Runtime 总论笔记`
- `5 个核心抽象与定义`
- `高频问答口述录音或草稿`
- Q13-Q26 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 能用自己的话定义 Agent Runtime
- 能区分“Agent 产品”和“Agent Agent Runtime”
- 能把答案落回自己做过的系统

### 晚间抽查

- 用 2 分钟回答“Prompt、Context、Agent Runtime 三者分工是什么”

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 8. Day 6：Tool Use / MCP / Skill / Subagent

### 今日目标

- 把工具调用系统讲到“既懂协议也懂工程”

### 今日任务

1. 写出 Tool Use 的完整流程
2. 总结 8 个常见失败模式
3. 梳理 MCP 的价值、边界与接入成本
4. 区分 Tool / Skill / Workflow / Subagent
5. 准备“为什么很多 Multi-Agent 系统效果不好”的回答
6. 分层口述练习：Q16-Q30（Agent / Agent Runtime 核心 + MCP / Tool 平台）
7. 参考资料：`ai_infra_learning/docs/agent/01-agent-frameworks-and-mcp.md`

### 今日输出

- `Tool Use 全流程图`
- `MCP 工程价值清单`
- `Skill / Tool / Workflow / Subagent 对照表`
- Q16-Q30 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 能解释 Tool schema 为什么重要
- 能说明 MCP 的工程意义，而不只是“统一协议”
- 能说清什么时候应该做 Multi-Agent

### coding 保底

- 1 道字符串或 JSON 解析题

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 9. Day 7：Memory / Context Engineering

### 今日目标

- 把这部分练成自己的核心竞争力

### 今日任务

1. 梳理以下问题
   - Memory 和聊天历史的区别
   - Memory 和 RAG 的区别
   - 为什么不能直接把所有历史塞给模型
   - 什么是按任务阶段注入上下文
2. 画出你认同的 Memory 分层图
3. 写出一套 Memory 写入和读取策略
4. 结合 `长程 Agent 框架` 和数据流水线 Agent 准备两个案例
5. 分层口述练习：Q31-Q39（Memory / Context Engineering）
6. 参考资料：`ai_infra_learning/docs/transformer/02-attention-variants.md`、`ai_infra_learning/docs/transformer/07-long-context.md`、`ai_infra_learning/docs/transformer/10-mla-deep-dive.md`

### 今日输出

- `Memory 分层图`
- `写入策略 / 读取策略说明`
- `Context Engineering 口述稿`
- Q31-Q39 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 能回答“Memory 的核心不是存，而是正确取用”
- 能清楚说明 `EventKey` 的价值
- 能讲出长期记忆的失败模式和清理策略

### 晚间抽查

- 用 2 分钟回答“为什么长上下文不是越长越好”

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 10. Day 8：Trace / Eval / Replay / 反馈闭环

### 今日目标

- 把可观测性从日志上升到 Agent Runtime 核心能力

### 今日任务

1. 写出一次 Agent 执行链路中 Trace 至少要记录哪些信息
2. 梳理 Replay 的用途
3. 设计一套基础 Eval 指标
4. 结合数据流水线 Agent 或 `长程 Agent 框架` 举例说明失败归因方法
5. 写出“真实任务反馈如何进入产品和模型迭代闭环”
6. 分层口述练习：Q40-Q45（Trace / Eval / Replay）
7. 参考资料：`ai_infra_learning/docs/agent/04-agent-evaluation-and-harness.md`

### 今日输出

- `Trace 字段清单`
- `Eval 指标草案`
- `失败归因路径图`
- Q40-Q45 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 能回答“Trace 和日志有什么区别”
- 能回答“没有标准答案的 Agent 任务怎么评估”
- 能说清是模型问题、工具问题还是上下文问题

### coding 保底

- 1 道哈希统计题

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 11. Day 9：LLM / 推理基础

### 今日目标

- 补齐模型基础宽度，避免被判断成只会做壳层工程

### 今日任务

1. 梳理以下概念
   - Transformer 基本组成
   - Attention 的直觉
   - KV Cache
   - Prefill / Decode
   - 显存占用来源
   - batch / 吞吐 / 延迟权衡
2. 写出“为什么 Context Engineering 会直接影响推理成本”
3. 准备 GPU、显存和 KV Cache 相关快答题
4. 分层口述练习：Q46-Q57（LLM 与推理基础）
5. 参考资料：`ai_infra_learning/docs/transformer/`、`ai_infra_learning/docs/ai-infra-basics/01-gpu-memory-analysis.md`、`ai_infra_learning/docs/pytorch/04-rope-rmsnorm-swiglu-mla.md`

### 今日输出

- `LLM / 推理基础笔记`
- `KV Cache 1 分钟解释稿`
- `显存与上下文成本说明`
- Q46-Q57 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 能回答“KV Cache 的作用和代价是什么”
- 能回答“为什么长上下文昂贵”
- 能说出在线 Agent 场景中为何推理成本容易爆炸

### 晚间抽查

- 口述 10 个和推理成本相关的关键词

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 12. Day 10：系统设计与后端基础

### 今日目标

- 守住工程基本盘，补齐高并发、缓存、一致性和故障处理表达

### 今日任务

1. 快速复习
   - 缓存穿透、击穿、雪崩
   - 消息队列语义
   - 幂等、重试、退避
   - 限流、降级、熔断
   - 最终一致性
2. 用“Agent Tool 服务”做一个系统设计小题
3. 准备“如何保护高频解析服务”的回答
4. 分层口述练习：Q58-Q73（Multi-Agent / Planning、规则引擎 / DAG Runtime / DSL、后端与系统设计）
5. 参考资料：`ai_infra_learning/docs/cs-foundations/os-basics-for-ai-infra.md`、`ai_infra_learning/docs/cs-foundations/computer-networks-for-ai-infra.md`

### 今日输出

- `高并发与故障处理速记`
- `Agent Tool 服务系统设计草图`
- `缓存与幂等问答卡`
- Q58-Q73 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 能回答“为什么重试有时很危险”
- 能回答“幂等如何保证”
- 能回答“如何保护被 Agent 高频调用的 Tool 服务”

### coding 保底

- 1 道队列 / BFS 题

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 13. Day 11：操作系统 / 网络 / SQL / 前端

### 今日目标

- 补齐最容易被忽视、但最容易丢分的基础题

### 今日任务

1. 操作系统
   - 进程、线程、协程
   - 死锁四条件
   - 共享内存
2. 网络
   - TCP 三次握手四次挥手
   - HTTP1.1 / HTTP2
   - 跨域和 CORS
3. SQL
   - 执行顺序
   - join
   - 索引基础
4. 前端
   - CSS 优先级
   - 同源策略
   - 浏览器请求流程基础
5. 分层口述练习：Q80-Q87（操作系统 / 网络 / SQL / 前端）
6. 参考资料：`ai_infra_learning/docs/cs-foundations/os-basics-for-ai-infra.md`、`ai_infra_learning/docs/cs-foundations/computer-networks-for-ai-infra.md`

### 今日输出

- `基础题速记表`
- `OS / 网络 / SQL / 前端 40 题快答卡`
- Q80-Q87 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 能 30 秒回答“SQL 执行顺序是什么”
- 能 30 秒回答“死锁四条件是什么”
- 能 30 秒回答“为什么会跨域”
- 能 30 秒回答“HTTP2 改进了什么”

### 今晚必须做

- 自测 20 题快问快答，不允许看答案

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 14. Day 12：Go / C++ / STL / 语言底层

### 今日目标

- 防止语言细节题失分

### 今日任务

1. Go
   - goroutine 和线程关系
   - `context.Context`
   - channel
   - 逃逸分析
2. C++
   - 虚函数和动态绑定
   - vtable 直觉
   - `vector` 扩容和迭代器失效
   - `map` / `unordered_map`
3. 准备 20 个语言基础快答题
4. 分层口述练习：Q74-Q79（Go / C++ / 语言基础）
5. 参考资料：`ai_infra_learning/docs/cs-foundations/cpp-basics-for-ai-infra.md`、`ai_infra_learning/docs/cs-foundations/cpp-concurrency-and-memory-model.md`

### 今日输出

- `Go 语言基础问答卡`
- `C++ / STL 快答卡`
- Q74-Q79 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 能回答“虚函数调用在什么时候确定”
- 能回答“goroutine 和线程是什么关系”
- 能回答“vector 扩容为什么会让迭代器失效”

### coding 保底

- 1 道字符串或容器模拟题

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 15. Day 13：算法与 40 分钟笔试模拟

### 今日目标

- 对齐反馈中的笔试节奏

### 今日任务

1. 限时 40 分钟完成 3 题模拟
   - 字符串处理
   - digit mask / 概率统计
   - BFS 变种
2. 做完后复盘
   - 是否先想清复杂度
   - 边界条件是否覆盖
   - 是否有大输入规模下的性能问题
3. 再补刷 1 题自己最弱的类型
4. 分层口述练习：Q96-Q104（算法与 coding）
5. 参考资料：`ai_infra_learning/docs/cs-foundations/algorithms-for-ai-infra.md`、`ai_infra_learning/docs/interview/quant-cpp-coding-problems.md`

### 今日输出

- `40 分钟笔试结果`
- `错题复盘记录`
- `算法薄弱点清单`
- Q96-Q104 的 30 秒版 / 2 分钟版 / 追问版

### 验收标准

- 至少稳定写出 2 题
- 第 3 题即使没写完，也要有正确思路和合理数据结构
- 代码不能明显乱，变量命名和边界处理要稳

### 今晚复盘重点

- 速度不够，是思路慢还是实现慢
- 字符串题和 BFS 题哪类更不稳

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 明天必须补的 3 件事：____、____、____

---

## 16. Day 14：全链路模拟面

### 今日目标

- 把知识从“看过”变成“会答”

### 今日任务

1. 做 1 次 60 分钟模拟面
   - 5 分钟自我介绍
   - 15 分钟 `长程 Agent 框架`
   - 10 分钟数据流水线 Agent
   - 10 分钟策略平台 / 规则引擎
   - 10 分钟 Agent / LLM / Memory / MCP
   - 10 分钟基础快问快答
2. 做 1 次 20 分钟快答模拟
3. 整理最后的错题和卡点
4. 重点复习 `.interview_assistant_state.json` 中评分 ≤2 的题目（根据 state 文件中的实际弱链动态调整），以及新增 L4 题（Q24、Q25、Q26、Q56、Q57、Q66、Q67、Q91）。
5. 参考资料：本轮优化后的 `agent/question.md` 全部分类，特别注意高级分类（Transformer 架构深度 Q107-Q116、Agent 评估与 Benchmark Q117-Q121、Agentic 推理优化 Q122-Q124）

### 今日输出

- `模拟面录音或逐题记录`
- `最终卡点清单`
- `面试前一天最终检查表`

### 验收标准

- 自我介绍自然，不背稿感太强
- 项目讲述结构稳定
- 基础题不明显失速
- 遇到不会的问题能给出边界清晰、诚实且有判断的回答

### 晚间复盘

- 今日最卡 3 题（qid）：____、____、____
- 考前最后 3 个弱链：____、____、____

---

## 17. 每晚 15 分钟复盘模板

每天结束后直接填这 5 项：

### 今日完成

- 今天完成了什么

### 今日最卡 3 题（注明 qid）

- 题 1（qid：____）
- 题 2（qid：____）
- 题 3（qid：____）

### 今日最虚 1 个项目点

- 哪个项目细节一追问就不稳

### 明天必须补的 3 件事

- 任务 1
- 任务 2
- 任务 3

### 一句话结论

- 今天距离“能拿下 Agent Runtime 面试”还差什么

---

## 18. 面试前最后检查表

面试前一天，逐项过一遍：

### L1 概念层

- [ ] 能否 30 秒说出 KV Cache、Attention、Transformer 的基本概念
- [ ] 能否 30 秒回答 SQL 执行顺序、死锁四条件、HTTP2 改进、跨域原因

### L2 整合层

- [ ] 能否 90 秒讲清自己为什么适合 Agent Runtime
- [ ] 能否清晰对比 Prompt / Context / Memory / RAG / 长上下文
- [ ] 能否说明 Tool / Skill / Workflow / Subagent / Multi-Agent 的边界

### L3 场景层

- [ ] 能否 5 分钟讲清 `长程 Agent 框架` 并回应一个具体追问
- [ ] 能否 5 分钟讲清数据流水线 Agent 并指出链路瓶颈
- [ ] 能否 5 分钟讲清策略平台 / 规则引擎和 Agent Runtime 的关系
- [ ] 能否回答“如何保护被 Agent 高频调用的 Tool 服务”并给出具体策略
- [ ] 能否诊断一次 Agent 执行失败是模型问题、工具问题还是上下文问题

### L4 身份/前沿层

- [ ] 能否把 MLA / GRPO / DualPipe / Mooncake / Engram 中的至少一个概念联系到自己的项目
- [ ] 能否回答“如果给 `长程 Agent 框架` 引入 MLA 的 KV 压缩思想，你会怎么设计 Memory”
- [ ] 能否针对 Agent Runtime 团队提出 3 个体现技术判断的反问

### 项目与表达

- [ ] 能否 90 秒自我介绍不背稿
- [ ] 能否在限时下稳住 2 到 3 道 coding

如果以上任何一项还答不顺，就不要继续扩展新知识，优先回头补最薄弱项。
