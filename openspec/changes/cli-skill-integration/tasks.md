## 1. CLI JSON 输出层

- [x] 1.1 新增 `--json` 和 `--quiet` 参数到 argparse
- [x] 1.2 重构 `print_day_overview` 支持 JSON 输出
- [x] 1.3 重构 `print_day_detail` 支持 JSON 输出
- [x] 1.4 重构 `search` 命令支持 JSON 输出
- [x] 1.5 重构 `practice_questions` / `mock` 支持 JSON 输出（非交互模式）
- [x] 1.6 重构 `progress` 命令支持 JSON 输出
- [x] 1.7 验证所有命令：默认模式行为不变 + JSON 模式输出合法

## 2. Qoder Skill

- [x] 2.1 创建 `.qoder/skills/interview/SKILL.md`，定义 `interview` 斜杠命令
- [x] 2.2 Skill 内容：描述可用题库、CLI 调用方式、JSON 解析指引
- [x] 2.3 验证 Skill 可被 Qoder 发现和加载

## 3. 集成验证与文档

- [x] 3.1 端到端测试：每个命令 × 两种模式（默认/JSON）
- [x] 3.2 更新 README.md：新增 JSON 输出说明和示例
- [x] 3.3 Git commit 并推送
