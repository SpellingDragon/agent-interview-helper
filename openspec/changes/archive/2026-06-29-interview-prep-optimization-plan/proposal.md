# 技术准备方案与题库优化计划

## Why

当前正在准备 Agent 平台 / AI Infra 方向面试，候选人具备复杂运行时、策略系统、规则引擎、DSL/SDK 与 Agent 实践的交叉背景。项目已经用两份 Markdown 驱动准备：

- `.personal/plan.md`：14 天执行清单。
- `.personal/question.md`：94 道高频问答题。

两份文档结构清晰，也已经被 `interview_assistant.py` 稳定解析。但内容上还有提升空间：

- `question.md` 中概念题、对比题较多，场景设计题、失败模式题、与候选人身份深度结合的前沿题偏少。
- 部分题目的回答要点偏浅，缺乏项目锚定和可深挖的追问点。
- `plan.md` 对“每日怎么练、产出什么、复习哪些题”还可以更具体。
- 大量分领域学习资料（`ai_infra_learning/docs`）尚未被整理进这两份文档的引用和训练闭环中。

因此，本轮优化的目标非常聚焦：**在不修改任何代码、不新增文档的前提下，只对 `.personal/plan.md` 和 `.personal/question.md` 做深度内容优化**。方法论和参考资料都嵌入到这两份文档的现有结构里。

## What Changes

- 在 `.personal/plan.md` 中：
  - 在总原则里明确四层题模型和“回答四要素”方法论。
  - 在每日任务中明确“分层口述练习”、参考资料和具体题目 qid。
  - 在每日输出中明确必须产出的 artifact（图/稿/伪代码/checklist）。
  - 在晚间复盘中加入“今日最卡 3 题”和“明日弱链”。
  - 在面试前最终检查表中覆盖 L1-L4 四层能力。
- 在 `.personal/question.md` 中：
  - 在使用说明里写入题目质量标准（四要素、追问点、常见误区、项目锚定）。
  - 逐分类优化现有题目：重写回答要点、补全一句话版、补充 L3 场景追问和 L4 身份/前沿追问、补充常见误区。
  - 为每道核心题嵌入项目锚点（`长程 Agent 框架`、数据流水线 Agent、策略平台 / 规则引擎 / MCP Tool）。
  - 拆分复合标题，新增缺口题和跨域设计题，尤其是 目标团队 技术栈结合题。
  - 在每个分类末尾或相关题目中注明参考资料范围。
- 不修改 `interview_assistant.py`，不新增 CLI 参数，不新增任何辅助 Markdown 文件。

## Capabilities

### New Capabilities

- `plan-content-optimization`: 在保持现有 `plan.md` 结构的前提下，把方法论、每日任务、输出物、弱链复习和参考资料嵌入到现有 section 中。
- `question-content-optimization`: 在保持现有 `question.md` 结构的前提下，逐分类提升题目深度、追问点、失败模式、项目锚定和参考范围，并补充缺口题。

### Modified Capabilities

- 无现有 spec 需要修改。

## Impact

- 仅影响 `.personal/plan.md` 和 `.personal/question.md` 两份文件的内容。
- 不修改 `interview_assistant.py`、不新增 CLI 参数、不新增解析规则。
- 不影响已归档的 `agent/`、`ai-infra/`、`llm/`、`mygo/` 题库。
