# plan-content-optimization

## ADDED Requirements

### Requirement: Preserve existing plan structure

All changes to `.personal/plan.md` SHALL keep the existing structure:
- Days as `## N. Day X：标题`.
- Sections inside each Day as `### 今日目标`, `### 今日任务`, `### 今日输出`, `### 验收标准`, `### 晚间复盘`.
- Top-level sections such as `1. 总原则`, `2. 执行模板`, `17. 每晚 15 分钟复盘模板`, `18. 面试前最后检查表`.

No new required sections, YAML frontmatter, or metadata blocks SHALL be introduced.

#### Scenario: Opening plan.md after optimization
- **WHEN** the candidate opens `.personal/plan.md`
- **THEN** the parser SHALL continue to recognize every Day and every standard section without modification to `interview_assistant.py`.

### Requirement: Methodology embedded in 总原则

The `1. 总原则` section SHALL explicitly describe:
- The four-layer question model (L1 concept, L2 integration, L3 scenario, L4 identity/frontier).
- The four-element answer standard: definition/mechanism → importance → engineering practice → trade-off/boundary/failure mode.
- The requirement that every L2-L4 answer must be anchored to one of the candidate's projects.

#### Scenario: Reading the principles
- **WHEN** the candidate reads `1. 总原则`
- **THEN** they SHALL understand how to classify a question and how to structure an answer before reading any specific Day.

### Requirement: Daily tasks reference concrete questions and materials

For each Day, the `### 今日任务` section SHALL include:
- The specific qids or classification names to practice (e.g., "练习 Q5-Q7" or "复习 Memory 分类 Q28-Q36").
- The reference files or sections from `ai_infra_learning/docs` to read that day.
- A note about layered oral practice (30s / 2min / deep follow-up).

#### Scenario: Day 2 task list
- **WHEN** the candidate reads Day 2 "项目深讲一，`长程 Agent 框架`"
- **THEN** the `今日任务` SHALL list qids such as Q5, Q6, Q7 and reference files such as `ai_infra_learning/docs/agent/01-agent-frameworks-and-mcp.md`.

### Requirement: Daily output specifies concrete artifacts

For each Day, the `### 今日输出` section SHALL list at least one concrete artifact the candidate must produce, such as a diagram, a one-page spoken script, pseudo-code, or a checklist.

#### Scenario: Day 3 output list
- **WHEN** the candidate reads Day 3 "数据流水线 Agent"
- **THEN** the `今日输出` SHALL include items such as "数据流水线 Agent 链路图" and "5 分钟讲稿".

### Requirement: Evening review captures weak links

For each Day, the `### 晚间复盘` section SHALL prompt the candidate to record:
- The top 3 questions that were hardest today.
- The weakest project detail.
- The 3 things to address tomorrow.

#### Scenario: Day 7 evening review
- **WHEN** the candidate finishes Day 7 "Memory / Context Engineering"
- **THEN** the `晚间复盘` SHALL guide them to write "今日最卡 3 题" and "明天必须补的 3 件事", referencing specific qids where possible.

### Requirement: Final checklist covers four layers

The final pre-interview checklist SHALL verify that the candidate can answer questions from all four layers: concept, integration, scenario, identity/frontier.

#### Scenario: Pre-interview review
- **WHEN** the candidate reads the final checklist
- **THEN** it SHALL contain items such as "能否 30 秒说出 KV Cache 作用" (L1), "能否 90 秒讲清自己为什么适合 Agent Runtime" (L2), "能否 5 分钟讲清 `长程 Agent 框架` 并回应一个追问" (L3), and "能否把 MLA 的 KV 压缩思想联系到 `长程 Agent 框架` 的 Memory 设计" (L4).

### Requirement: No code or file changes outside plan.md

All plan-content-optimization work SHALL be confined to `.personal/plan.md`. No changes to `interview_assistant.py`, no new files, and no changes to `.personal/question.md` structure are allowed under this capability.

#### Scenario: Verifying scope
- **WHEN** the optimization is complete
- **THEN** the only modified file related to the plan SHALL be `.personal/plan.md`.
