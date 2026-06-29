## 1. 知识库素材提取（三方向并行）

- [x] 1.1 从 `ai_infra_learning/docs/` 提取 LLM 方向核心面试题（Transformer、RL 后训练、Scaling Law、PyTorch 实现），生成题目索引
- [x] 1.2 从 `ai_infra_learning/docs/` 提取 AI Infra 方向核心面试题（vLLM、Megatron、CUDA、C++、系统设计），生成题目索引
- [x] 1.3 从 `ai_infra_learning/docs/agent/` 和 `docs/interview/` 提取 Agent 方向补充题（Benchmark、Agentic 推理、Transformer 深度），生成题目索引
- [x] 1.4 从知识库中提取三套项目叙事素材，统一脱敏

## 2. LLM 题库生成

- [x] 2.1 生成 `llm/question.md`：按分类编写 80+ 题，含项目叙事
- [x] 2.2 生成 `llm/plan.md`：14 天执行清单，每天只记录行为约束
- [x] 2.3 验证：脚本加载 + 敏感词扫描 + 题号连续性

## 3. AI Infra 题库生成

- [x] 3.1 生成 `ai-infra/question.md`：按分类编写 100+ 题，含项目叙事
- [x] 3.2 生成 `ai-infra/plan.md`：14 天执行清单，每天只记录行为约束
- [x] 3.3 验证：脚本加载 + 敏感词扫描 + 题号连续性

## 4. Agent 题库升级

- [x] 4.1 向 `agent/question.md` 新增 Transformer 深度题（10+）、Benchmark 题（5+）、Agentic 推理题（3+）
- [x] 4.2 更新 `agent/plan.md`：在相关 Day 中增加新增主题练习安排
- [x] 4.3 验证：脚本加载 + 题号重编号 + 敏感词扫描

## 5. 集成验证

- [x] 5.1 三套题库分别用 `--data-dir` 加载，确认 overview 和题目解析正常
- [x] 5.2 全仓库敏感词扫描（agent + ai-infra + llm）
- [x] 5.3 更新 README.md：说明三套题库的定位和使用方式
- [x] 5.4 Git commit 并推送
