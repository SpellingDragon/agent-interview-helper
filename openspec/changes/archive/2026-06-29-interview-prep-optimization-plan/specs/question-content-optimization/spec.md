# question-content-optimization

## ADDED Requirements

### Requirement: Preserve existing question structure

All changes to `.personal/question.md` SHALL keep the existing structure:
- Categories as `## N. 分类名`.
- Questions as `### QN. 题目`.
- Content sections as `#### 回答要点`, `#### 一句话版`, `#### 追问点`, `#### 常见误区`.

No new metadata sections, YAML frontmatter, or parser-specific formatting SHALL be introduced.

#### Scenario: Opening question.md after optimization
- **WHEN** the candidate opens `.personal/question.md`
- **THEN** the parser SHALL continue to recognize every category, question, and standard section without modification to `interview_assistant.py`.

### Requirement: Quality standard embedded in 使用说明

The `1. 使用说明` section SHALL explicitly state the quality standard for every core question:
- `回答要点` organized as four elements: definition/mechanism → importance → engineering practice → trade-off/boundary/failure mode.
- `一句话版` as a 30-second standalone conclusion.
- `追问点` containing at least one L3 scenario follow-up and one L4 identity/frontier follow-up.
- `常见误区` naming at least one shallow or wrong answer.
- Project anchors embedded naturally in `回答要点` or `追问点`.

#### Scenario: Reading the usage instructions
- **WHEN** the candidate reads `1. 使用说明`
- **THEN** they SHALL know exactly what a "complete" question entry looks like.

### Requirement: Four-element answer points

For every L2-L4 question, the `#### 回答要点` section SHALL be organized into the four elements in order. Each element may be one or more bullet points.

#### Scenario: Reviewing a Memory question
- **WHEN** the candidate reads Q28 "Prompt、Context、Memory 的区别是什么？"
- **THEN** the `回答要点` SHALL clearly cover definitions, why the distinction matters, typical engineering practice, and at least one trade-off or boundary.

### Requirement: Layered follow-up points

For every L2-L4 question, the `#### 追问点` section SHALL include:
- At least one L3 scenario follow-up (design / diagnosis / optimization under realistic constraints).
- At least one L4 identity/frontier follow-up (connecting the concept to the candidate's project or to 目标团队/frontier context).

#### Scenario: Tool-service protection question
- **WHEN** the candidate reviews Q62 "如何保护一个被 Agent 高频调用的 Tool 服务？"
- **THEN** the `追问点` SHALL contain an L3 follow-up such as "若该 Tool 下游 P99 延迟从 20ms 涨到 200ms，你的熔断策略怎么调？" and an L4 follow-up such as "在 `长程 Agent 框架` 中，如果某个 Skill 频繁触发同一个 Tool，你会如何把这种保护做成 runtime 策略？"

### Requirement: Project anchors embedded in content

Every L2-L4 question SHALL naturally reference at least one of the candidate's projects in either `回答要点` or `追问点`. Allowed anchors are `长程 Agent 框架`, 数据流水线 Agent, and 策略平台 / 在线 Agent 内容解析 Tool.

#### Scenario: Agent communication question
- **WHEN** the candidate answers Q6 "为什么 Agent 间不直接传上下文，而是传 `EventKey`？"
- **THEN** the answer SHALL reference the memory-key design from `长程 Agent 框架` and explain a concrete cost or debugging benefit observed in that project.

### Requirement: Common pitfalls section

Every L2-L4 question SHALL include a `#### 常见误区` section that names at least one mistake or shallow answer an interviewer would push back on.

#### Scenario: KV Cache question
- **WHEN** the candidate studies Q45 "KV Cache 的作用是什么？"
- **THEN** the `常见误区` SHALL point out that "KV Cache 只是加速，不占显存" is wrong and explain the memory cost.

### Requirement: Single-focused question titles

Each question title SHALL express exactly one core problem. Compound questions SHALL be split into multiple entries with consecutive numbering, and `plan.md` references SHALL be updated accordingly.

#### Scenario: Splitting a compound title
- **WHEN** a draft reads "KV Cache 是什么，和 PagedAttention 有什么关系，长上下文为什么昂贵"
- **THEN** it SHALL become three questions, each with its own `Q`, title, and four content sections.

### Requirement: Reference scope per category

At the end of each category, a `#### 本分类参考范围` section SHALL list 2-5 concrete reference files from `ai_infra_learning/docs/` that support the questions in that category.

#### Scenario: Agent category reference
- **WHEN** the candidate finishes reading the Agent category
- **THEN** they SHALL see a reference list such as `ai_infra_learning/docs/agent/01-agent-frameworks-and-mcp.md` and `ai_infra_learning/docs/agent/04-agent-evaluation-and-harness.md`.

### Requirement: Gap and cross-domain questions

The question bank SHALL be extended with high-quality questions that cover:
- Uncovered topics from the target domain reference materials.
- Cross-domain design problems (e.g., Agent + vLLM + RL Rollout).
- 目标团队-specific or frontier context tied to the candidate's projects.

New questions SHALL follow the same four-section structure and SHALL be inserted into the most appropriate existing category.

#### Scenario: Adding a 目标团队-anchored question
- **WHEN** a new question is added under the Agent/Agent Runtime category
- **THEN** it SHALL connect a 目标团队 technology such as MLA, GRPO, DualPipe, or Mooncake to one of the candidate's projects and include a quantitative or design dimension.

### Requirement: No code or file changes outside question.md

All question-content-optimization work SHALL be confined to `.personal/question.md`. No changes to `interview_assistant.py`, no new files, and no changes to `.personal/plan.md` structure are allowed under this capability.

#### Scenario: Verifying scope
- **WHEN** the optimization is complete
- **THEN** the only modified file related to the question bank SHALL be `.personal/question.md`.
