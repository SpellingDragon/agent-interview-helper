## Why

当前 `interview_assistant.py` 的 CLI 输出面向人类阅读（表格、中文提示、交互菜单），缺少机器可读的结构化输出。AI Agent 想调用这个工具（如查询题目、推荐练习、搜索）只能解析文本，效率低且不稳定。同时，项目没有 Qoder Skill，AI 无法通过斜杠命令直接调用面试助手功能。项目零依赖的特性让它非常适合做成轻量 CLI + Skill 的组合。

## What Changes

- 新增 `--json` 全局参数，让所有输出命令支持 JSON 结构化输出
- 新增 `--quiet` 参数，抑制交互式提示和非必要输出
- 重构 CLI 输出层，分离"人类展示"和"机器输出"两条路径
- 创建 Qoder Skill `interview`，支持 Agent 通过 `/interview` 斜杠命令调用面试助手
- Skill 覆盖核心功能：概览、搜索、推荐练习、随机模拟

## Capabilities

### New Capabilities
- `json-output`: 所有 CLI 命令支持 `--json` 结构化输出，Agent 可直接解析
- `interview-skill`: Qoder Skill，让 AI Agent 通过斜杠命令调用面试助手

### Modified Capabilities
（无已有 spec 需要修改）

## Impact

- **代码**：`interview_assistant.py` 的输出层重构，新增 JSON formatter
- **文件**：`.qoder/skills/interview/SKILL.md` 新增
- **兼容性**：完全向后兼容，默认行为不变，`--json` 为可选参数
- **依赖**：仍然零依赖（`json` 是标准库）
