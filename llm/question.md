# LLM 理论与后训练高频问答题库

> 适用对象：LLM 研究 / 后训练 / 模型优化方向候选人
> 目标：把面试中的高频问题准备成可直接口述的题库
> 使用方式：
> 1. 先自己口头回答题目
> 2. 再看"回答要点"检查是否漏项
> 3. 最后补成 1 分钟版和 3 分钟版

---

## 1. 使用说明

建议每道题至少准备三层表达：

- `30 秒版`：先给结论，适合快问快答
- `2 分钟版`：给定义、场景、权衡
- `追问版`：补充失败模式、工程细节、trade-off

回答时优先使用以下结构：

1. 先定义问题
2. 再说明为什么重要
3. 再讲工程上的常见做法
4. 最后讲边界和权衡

---

## 2. 岗位匹配与动机

### Q1. 你为什么适合 LLM 后训练方向？

#### 回答要点

- 对 Transformer 架构有源码级理解，能从 Attention 变体、位置编码、MoE 等维度分析模型设计取舍。
- 有 RL 后训练实践经验，理解 SFT → DPO → PPO → GRPO 的演进逻辑和工程挑战。
- 关注 Scaling Law 和推理模型的前沿趋势，理解 Test-time Compute 和 CoT 数据合成的工程含义。
- 能把算法选择和 Infra 约束联系起来分析，不只是跑公式。

#### 一句话版

我适合这个方向，是因为我对模型架构、后训练算法和训练 Infra 三者之间的耦合关系有系统理解，而不只是会调超参。

### Q2. 你为什么想做 LLM 后训练，而不是预训练或纯推理？

#### 回答要点

- 预训练更关注数据、规模和架构，推理更关注 Serving 效率，而后训练是"把通用能力转化为任务能力"的关键环节。
- 后训练是算法和 Infra 耦合最紧的地方——PPO 需要 4 模型协同，GRPO 需要 Rollout Engine，算法选择直接决定系统设计。
- 后训练也是模型能力快速迭代的瓶颈，直接影响产品表现。

### Q3. 你理解的 RL 后训练是什么？

#### 回答要点

- RL 后训练是在 SFT 之后，用奖励信号或偏好数据进一步调整模型行为的训练范式。
- 它至少要解决三类问题：对齐人类偏好、提升推理能力、控制模型行为边界。
- 从工程角度，它的核心挑战是多模型协同训练、采样效率、训练稳定性和评估闭环。

### Q4. 你认为 LLM 后训练最重要的工程能力是什么？

#### 回答要点

- 理解算法和 Infra 的耦合关系——不是先选算法再配 Infra，而是两者共同设计。
- 能做训练稳定性分析，识别 reward hacking、KL 漂移、方差爆炸等问题。
- 能搭建从数据构造、训练、评估到反馈的完整闭环。

---

## 3. 项目与经历

### Q5. 你做过的 LLM 训练或推理优化项目，核心挑战是什么？

#### 回答要点

- 描述一个真实项目：目标、约束、关键技术决策。
- 重点讲"为什么选这个方案"而不是"做了什么"。
- 能说出一个失败模式或尚未解决的问题。

### Q6. 你在项目中如何处理训练不稳定的问题？

#### 回答要点

- 具体描述遇到的不稳定现象（loss 抖动、reward hacking、KL 爆炸）。
- 分析根因：数据质量、学习率、KL 系数、advantage 方差。
- 采取的应对措施和效果。

### Q7. 你如何评估后训练的效果？

#### 回答要点

- 不只看 reward 曲线，还要看下游 benchmark 表现。
- 区分 in-distribution 和 out-of-distribution 的表现。
- 关注 reward hacking 信号：reward 上升但 benchmark 不升或下降。
- 结合人工评估和自动化评估。

### Q8. 你对比过不同后训练方法吗？结论是什么？

#### 回答要点

- 对比过的方法及其在不同维度上的表现。
- 关键 trade-off：数据需求、Infra 复杂度、效果上限。
- 什么场景下选什么方法。

### Q9. 你在项目中如何处理数据和 reward model 的关系？

#### 回答要点

- 偏好数据的构造方式和质量控制。
- Reward model 的训练方法和评估。
- 如何检测和缓解 reward hacking。

---

## 4. Transformer 架构

### Q10. Scaled Dot-Product Attention 的计算过程是什么？

#### 回答要点

- Q、K、V 的来源和形状。
- 计算 Attention scores = Q @ K^T / sqrt(d_k)。
- Softmax + mask（如果是 causal）。
- 加权求和 V。
- 复杂度是 O(N²d)，瓶颈在 N² 的 attention matrix。

### Q11. MHA、MQA、GQA 的区别是什么？为什么需要演进？

#### 回答要点

- MHA：每个 head 都有独立的 Q/K/V。
- MQA：所有 head 共享一组 K/V，Q 各自独立。KV Cache 大幅减小。
- GQA：介于 MHA 和 MQA 之间，G 个 Q head 共享一组 K/V。
- 演进动力是 KV Cache 的显存压力，尤其在长上下文和高并发场景。

### Q12. MLA（Multi-head Latent Attention）的核心设计是什么？

#### 回答要点

- 用低秩压缩把 K/V 投影到低维 latent space，KV Cache 压缩约 93%。
- Decoupled RoPE：把 RoPE 从 Q/K 的内容维度分离出来，只加到 query/key 的额外维度上。
- Weight Absorption：把 up-projection 吸收到 Q/K/V 的权重里，减少推理时的计算量。
- 代价是需要更复杂的训练和实现。

### Q13. RoPE（Rotary Position Encoding）的原理和优势是什么？

#### 回答要点

- 对 Q 和 K 的相邻维度对施加旋转，旋转角度与位置成正比。
- 优势：相对位置编码（内积只依赖相对距离）、可外推、实现简单。
- 局限：绝对位置信息表达有限，长上下文外推需要 YaRN 等辅助。

### Q14. ALiBi 和 RoPE 有什么区别？什么场景用哪个？

#### 回答要点

- ALiBi：在 attention score 上加线性偏置，不需要 position embedding。
- RoPE：旋转位置编码，更灵活、外推性更好。
- 大多数现代 LLM 选 RoPE（Llama、Qwen 等），ALiBi 在 BLOOM 等早期模型中使用。

### Q15. MoE（Mixture of Experts）的核心设计是什么？

#### 回答要点

- 每个 token 由 router 选择 top-K 个 expert 处理，其余 expert 不激活。
- 优势：总参数量大但每次激活参数少，推理 FLOPs 低。
- 挑战：负载均衡（expert 利用率不均）、all-to-all 通信、expert 权重存储。
- 共享 expert（shared expert）可以缓解负载不均。

### Q16. MoE 的负载均衡怎么做？

#### 回答要点

- Load Balancing Loss：惩罚 token 分配不均匀的路由。
- 冗余专家（redundant experts）：在线统计负载，动态调整 expert 分布。
- Expert capacity：限制每个 expert 处理的 token 上限。
- 辅助 loss + 路由正则化。

### Q17. FlashAttention 的核心思想是什么？

#### 回答要点

- 核心：Tiling + Online Softmax，避免把 N×N attention matrix 写入 HBM。
- 把 Q/K/V 分成 block，在 SRAM 中完成 attention 计算，只写回最终结果。
- 减少 HBM 读写次数，从 O(N²) 降到 O(N²d/M)（M 是 SRAM 大小）。
- IO-aware 的算法设计，不改变数学结果但大幅提速。

### Q18. FlashAttention 2 相比 1 有什么改进？

#### 回答要点

- 减少非 matmul FLOPs：调整内外循环顺序。
- 提高并行度：在 batch 和 head 维度上并行。
- 更好的 warp 利用率：减少 warp 间的同步。
- 整体速度提升约 2x。

### Q19. Decoder-Only 架构为什么成为 LLM 的主流？

#### 回答要点

- Encoder-Decoder：适合 seq2seq，但自回归生成时 encoder 的计算不能复用。
- Decoder-Only：统一用 causal mask，训练和推理一致，预训练效率高。
- 2020 年后的 GPT 系列证明了 Decoder-Only 在大规模下的 scaling 优势。
- 主要代价是双向信息的缺失，但 causal LM 足够覆盖大部分任务。

### Q20. 残差连接和 LayerNorm 在 Transformer 中的作用是什么？

#### 回答要点

- 残差连接：缓解深层网络的梯度消失，让信息能跳过中间层直接传递。
- LayerNorm：稳定训练，归一化激活值的分布。
- Pre-Norm vs Post-Norm：Pre-Norm（先 Norm 再计算）训练更稳定，Post-Norm 理论上表达力更强但需要更精细的学习率。
- RMSNorm：简化的 LayerNorm，去掉均值中心化，只保留缩放，计算更快。

### Q21. FFN 和激活函数在 Transformer 中的角色是什么？

#### 回答要点

- FFN 提供非线性扩展能力，通常是 d_model → 4*d_model → d_model。
- ReLU → GELU → SwiGLU 的演进：SwiGLU 引入门控机制，效果更好但参数多 50%。
- FFN 参数量占总参数的约 2/3（两个 Linear 层）。

### Q22. 长上下文技术有哪些主要方向？

#### 回答要点

- 滑动窗口注意力（Mistral）：只看最近 W 个 token。
- 稀疏注意力（Longformer、DSA）：选择性地 attend 到重要 token。
- KV Cache 压缩（MLA、CSA+HCA）：减少 KV 存储。
- 位置编码外推（YaRN、PI）：让 RoPE 支持更长序列。
- 线性注意力（Mamba、KDA）：O(N) 复杂度替代 O(N²)。

### Q23. Mamba 和线性注意力的核心思想是什么？

#### 回答要点

- Mamba：选择性状态空间模型（SSM），用 input-dependent 的 A/B/C 矩阵替代固定参数。
- 线性注意力：用 kernel function 替代 softmax，把 O(N²) 降到 O(N)。
- 优势：O(N) 复杂度，适合超长序列。
- 劣势：recall 能力弱于 full attention，在需要精确检索的任务上表现差。

### Q24. KV Cache 的计算方式是什么？怎么估算显存占用？

#### 回答要点

- KV Cache 大小 = 2 × n_layers × n_kv_heads × d_head × seq_len × dtype_size。
- 以 Llama 2 7B（32 层、32 KV heads、128 d_head、FP16）为例：每 token 约 0.5 MB。
- GQA 减少 KV heads 数量，KV Cache 成比例缩小。
- MLA 通过低秩压缩进一步减小。

### Q25. PagedAttention 解决了什么问题？

#### 回答要点

- 传统 KV Cache 需要连续显存，导致大量碎片和预留浪费（60-80%）。
- PagedAttention 把 KV Cache 分成固定大小 block，通过 block table 实现逻辑连续、物理离散。
- 支持 Copy-on-Write 共享前缀、动态长度分配。
- Attention kernel 有 20-26% 额外开销（indirect indexing）。

### Q26. Prefill 和 Decode 的计算特征有什么区别？

#### 回答要点

- Prefill：处理全部输入 token，compute-bound，大矩阵运算，吞吐优先。
- Decode：逐 token 生成，memory-bound，读取 KV Cache 和权重，延迟敏感。
- Prefill 复杂度 O(N²d)，Decode 每 step 复杂度 O(Nd)（N 是已有序列长度）。
- 长序列下 Prefill 的 TTFT 和 Decode 的 TBT 需要分别优化。

### Q27. 为什么长上下文推理昂贵？

#### 回答要点

- Prefill 阶段处理更多 token，计算量 O(N²)。
- KV Cache 更大，占更多显存。
- Decode 每步需要读取更长的 KV Cache，memory bandwidth 瓶颈。
- 容易引入无关信息，影响输出质量。

### Q28. 显存主要消耗在哪些方面（推理场景）？

#### 回答要点

- 模型权重（最大头，BF16 下 2P bytes）。
- KV Cache（随序列长度和并发数增长）。
- 中间激活和运行时缓冲。
- CUDA context、cuDNN workspace 等固定开销。

### Q29. 显存不够时你会考虑哪些方向？

#### 回答要点

- 缩短上下文或做更严格的 context engineering。
- 量化：INT8/INT4/FP8 权重、FP8 KV Cache。
- 减小 batch 或并发。
- PagedAttention 减少碎片。
- KV Cache offloading 到 CPU memory。
- 换更小模型或分层路由。

---

## 5. RL 后训练

### Q30. RLHF 完整流程是什么？每个阶段的作用？

#### 回答要点

- Stage 1：SFT——用高质量对话数据微调基础模型。
- Stage 2：Reward Model 训练——用人类偏好数据训练评分模型。
- Stage 3：RL 优化（PPO）——用 RM 作为 reward 信号，优化 policy model。
- 每个阶段的目标：SFT 让模型学会格式和基本能力，RM 学习人类偏好，RL 让模型行为对齐偏好。

### Q31. Reward Model 的 loss 怎么写？为什么用 pairwise loss？

#### 回答要点

- 给定一对 (chosen, rejected) response，RM 分别打分。
- Loss = -log(sigmoid(r_chosen - r_rejected))，即 Bradley-Terry 模型。
- 用 pairwise 而不是 pointwise 的原因：人类更容易比较两个回答的优劣，而不是给单个回答打绝对分。

### Q32. PPO 为什么需要 4 个模型？

#### 回答要点

- Policy Model（当前训练的模型）：生成回答。
- Reference Model（冻结的 SFT 模型）：计算 KL 惩罚，防止偏离太远。
- Reward Model（冻结）：给回答打分。
- Value/Critic Model：估计 state value，计算 advantage。
- 4 个模型同时存在是显存压力的主要来源。

### Q33. PPO 的 clipped surrogate objective 怎么理解？

#### 回答要点

- 标准 policy gradient 的 ratio 可能很大，导致训练不稳定。
- Clip 把 ratio 限制在 [1-ε, 1+ε] 范围内，防止单步更新过大。
- 本质是一种 trust region 的近似，比 KL 约束更简单。

### Q34. DPO 的核心思想是什么？和 PPO 的本质区别？

#### 回答要点

- DPO 把 RL 问题转化为分类问题：直接在偏好数据上优化 policy，不需要显式 RM。
- 数学上证明了最优 policy 可以用 reference model 和 reward 的闭式解表示，从而绕过 RM 训练。
- Loss 只需要 reference model 和 policy model 的 log probability ratio。
- 优势：Infra 简单（只需 2 个模型），训练更稳定。劣势：离线方法，效果上限可能不如 PPO。

### Q35. GRPO 和 PPO 的区别？为什么可以去掉 Critic？

#### 回答要点

- GRPO（Group Relative Policy Optimization）：对每个 prompt 采样一组回答，用组内标准化作为 advantage。
- 不需要 Critic 模型，因为 advantage 通过组内比较计算，不需要 value function。
- 少一个模型意味着显存释放，但组内采样增加了 Rollout 负担。

### Q36. RL 后训练中 reward hacking 怎么解决？

#### 回答要点

- KL 惩罚：限制 policy 偏离 reference model 太远。
- Reward model ensembling：多个 RM 投票减少偏差。
- 迭代更新 RM：用新数据重新训练 RM，消除已知 hacking 模式。
- 过程奖励模型（PRM）：对推理过程的每一步打分，而不只是最终结果。

### Q37. OpenRLHF 和 veRL 的架构差异？

#### 回答要点

- OpenRLHF（空间分离）：不同 GPU 组分别跑 Rollout、Actor、Critic、Reward，通过 Ray Object Store 通信。
- veRL（时分复用）：同一组 GPU 交替做训练和推理，通过 resharding 切换并行策略。
- OpenRLHF 优势：各模块独立优化；劣势：GPU 利用率低（有空闲等待）。
- veRL 优势：GPU 利用率高；劣势：切换有开销。

### Q38. Rollout Engine 为什么要用 vLLM？权重同步怎么做？

#### 回答要点

- vLLM 的 PagedAttention 和 Continuous Batching 提供高吞吐的文本生成。
- Rollout 是 RL 训练中最耗时的环节之一，推理速度直接影响训练效率。
- 权重同步：Actor 训练后更新权重，需要同步到 vLLM 的 Rollout Engine。
- 方式包括：全量同步、增量同步、prefix caching 复用。

### Q39. PPO 训练不稳定时你会怎么调？

#### 回答要点

- 检查 KL 系数 β：太小导致偏离过远，太大导致学不动。
- 检查 advantage 的方差：用 clip 或 normalization 控制。
- 检查 reward 分布：如果 reward 方差太大，考虑 reward clipping。
- 降低学习率、增加 warmup、用 gradient clipping。
- 检查数据质量：低质量偏好数据是常见根因。

### Q40. 端侧 RL 和云端 RL 的主要差异？

#### 回答要点

- 模型规模：端侧通常 1-7B，云端 70B+。
- 训练资源：端侧受限（手机/边缘设备），云端 GPU 集群。
- 数据隐私：端侧数据不能上传，需要联邦学习或本地训练。
- 推理时搜索：端侧可能无法承担 Best-of-N 或 MCTS 的计算开销。

### Q41. 过程奖励模型（PRM）和结果奖励模型（ORM）有什么区别？

#### 回答要点

- ORM：只对最终输出打分，适合有明确正确答案的任务。
- PRM：对推理过程的每一步打分，适合需要中间推理的任务（数学、代码）。
- PRM 能提供更细粒度的反馈，缓解 reward hacking。
- PRM 的训练数据更难构造，需要步骤级标注。

### Q42. Scaling Law 对后训练有什么指导意义？

#### 回答要点

- Chinchilla Law：给定计算预算，模型大小和训练数据量应该同步增长。
- 后训练的 Scaling Law：更多的 RL 数据和更长的训练不一定线性提升效果。
- Test-time Compute Scaling：推理时投入更多计算（如 Best-of-N、MCTS）可以显著提升表现。
- GRPO 的规模化：更大的 group size 和更多的 rollout 可以提升效果。

### Q43. Test-time Compute 的核心思想是什么？

#### 回答要点

- 推理时投入更多计算来提升输出质量，而不是只训练更大的模型。
- 方法：Best-of-N sampling、MCTS、Self-consistency、Chain-of-Thought。
- 关键 insight：某些任务在推理时 scaling 比训练时 scaling 更有效。
- 工程挑战：如何在延迟和成本约束下最大化推理时的计算收益。

### Q44. CoT 数据合成有哪些常见方法？

#### 回答要点

- 用强模型（如 GPT-4）生成 reasoning trace，作为弱模型的训练数据。
- Self-play：模型自己生成问题并回答，筛选高质量的。
- Rejection sampling：生成多个回答，只保留正确的作为训练数据。
- 关键挑战：合成数据的多样性和质量平衡。

---

## 6. PyTorch 实现

### Q45. PyTorch 中如何实现 causal attention？

#### 回答要点

- 用 `torch.triu(ones, diagonal=1).bool()` 创建上三角 mask。
- 在 attention scores 上 `masked_fill(mask, float('-inf'))`。
- 然后 softmax + matmul with V。
- 面试高频考点：mask 的形状、broadcasting、-inf vs 0 的区别。

### Q46. GQA 在 PyTorch 中怎么实现？

#### 回答要点

- K/V 的 head 数少于 Q 的 head 数。
- 用 `repeat_interleave` 把 K/V 扩展到和 Q 相同的 head 数。
- 或者 reshape 让 Q 分组共享 K/V。
- 关键是形状对齐和内存效率。

### Q47. LoRA 的原理和 PyTorch 实现？

#### 回答要点

- 冻结原始权重 W，额外训练低秩矩阵 A（d×r）和 B（r×d）。
- 前向：output = xW + xA·B·(α/r)。
- 优势：训练参数量大幅减少，可以合并回原始权重。
- 关键超参：rank r、scaling α、target modules。

### Q48. 混合精度训练在 PyTorch 中怎么做？

#### 回答要点

- `torch.autocast(device_type='cuda', dtype=torch.bfloat16)` 自动选择 FP16/BF16 计算。
- 梯度用 FP32 累积，避免精度损失。
- BF16 比 FP16 更好：指数范围相同，不需要 loss scaling。
- 关键：哪些操作保持 FP32（softmax、LayerNorm、loss 计算）。

### Q49. KV Cache 在推理中怎么实现？

#### 回答要点

- 缓存每层的 K 和 V tensor，新 token 只需要计算自己的 Q/K/V。
- 用 `torch.cat` 拼接历史 K/V，或者用 StaticCache 预分配。
- StaticCache 避免每次重新分配内存，也是 CUDA Graph 能捕获的前提。
- PagedAttention 进一步优化：block-level 管理，减少碎片。

### Q50. 如何用 PyTorch 实现完整的 GPT 模型？

#### 回答要点

- Token Embedding + Position Embedding → N × TransformerBlock → LayerNorm → Linear(vocab)。
- 每个 TransformerBlock：Norm → Attention → Residual → Norm → FFN → Residual。
- 生成：自回归，每步取最后一个 token 的 logits，sample 或 greedy。
- 训练：teacher forcing，cross_entropy loss。

### Q51. 梯度累积的原理和实现？

#### 回答要点

- 把大 batch 拆成多个小 batch，累积梯度后再更新参数。
- `loss = loss / accumulation_steps` → `loss.backward()` → 每 N 步 `optimizer.step()`。
- 等价于大 batch 训练，但显存只占小 batch 的量。
- 注意：BatchNorm 的行为在梯度累积下可能不一致（用 GroupNorm 替代）。

---

## 7. 推理优化理论

### Q52. 投机解码（Speculative Decoding）的原理是什么？

#### 回答要点

- 用一个小模型（draft model）快速生成多个候选 token。
- 用大模型（target model）并行验证这些 token。
- 数学上保证输出分布与只用大模型相同。
- 加速比取决于 draft model 的接受率。

### Q53. EAGLE 和标准投机解码有什么区别？

#### 回答要点

- 标准投机解码：draft model 独立生成，target model 验证。
- EAGLE：在 target model 的特征空间上做 draft，利用 target model 的内部状态。
- EAGLE-2：用 tree-based 验证，一次验证多个候选路径。
- 优势：draft 更准确，接受率更高，加速比更好。

### Q54. Prefix Caching 在什么场景下有效？

#### 回答要点

- 多个请求共享相同的 system prompt 或 few-shot examples。
- Agent 场景中 system prompt 通常很长且固定。
- RL Rollout 中多个采样共享相同 prompt。
- vLLM 用 block-level APC，SGLang 用 RadixAttention（token-level）。

### Q55. Chunked Prefill 解决什么问题？

#### 回答要点

- 长 prefill 会阻塞 decode 请求，导致 TBT 飙升。
- Chunked Prefill 把长 prefill 分成多个 chunk，与 decode 交替执行。
- 降低 decode 请求的等待时间，改善 TBT。
- 代价是 prefill 的吞吐略有下降。

### Q56. Continuous Batching 和 Static Batching 的区别？

#### 回答要点

- Static Batching：等一个 batch 全部完成后才处理下一个 batch。
- Continuous Batching：请求完成即退出，新请求随时插入。
- Continuous Batching 显著提高 GPU 利用率（可达 4x 吞吐提升）。
- 代价：调度复杂度增加，需要 PagedAttention 支持动态 KV Cache。

### Q57. Quantization（量化）的基本原理是什么？

#### 回答要点

- 把 FP16/BF16 权重或激活值映射到 INT8/INT4/FP8 等低精度。
- 减少显存占用和 memory bandwidth 需求。
- 方式：PTQ（训练后量化，不需要重训）vs QAT（量化感知训练）。
- 关键挑战：精度损失控制，特别是 outlier 特征的处理。

### Q58. AWQ 和 GPTQ 有什么区别？

#### 回答要点

- AWQ（Activation-aware Weight Quantization）：根据激活值的重要性选择性保护权重。
- GPTQ：基于二阶信息（Hessian）逐层量化。
- AWQ 更快（不需要 Hessian 计算），GPTQ 精度通常更好。
- 两者都是 weight-only 量化（W4A16），不量化激活值。

### Q59. CUDA Graph 在推理中的作用和限制？

#### 回答要点

- CUDA Graph 捕获一系列 GPU 操作的执行图，之后重放时跳过 CPU 端的 kernel launch overhead。
- 在 decode 阶段效果显著：每 step 有大量小 kernel，CPU launch overhead 占比高。
- 限制：要求 tensor shape 固定（dynamic batching 不兼容），需要 StaticCache。
- 在 vLLM 中，CUDA Graph 和 dynamic batch 的兼容是工程挑战。

---

## 8. 算法与 Coding

### Q60. 面试中如何快速讲清复杂度？

#### 回答要点

- 先说核心数据结构。
- 再说主循环和嵌套关系。
- 分析最坏时间复杂度和空间复杂度。
- 如果有剪枝或预处理，再单独说明。

### Q61. Attention 计算的复杂度是多少？瓶颈在哪？

#### 回答要点

- 标准 Attention：O(N²d) 计算，O(N²) 显存。
- 瓶颈在 N² 的 attention matrix，尤其是长序列。
- FlashAttention 不改变计算量，但减少 HBM 访问。
- 线性注意力（Mamba、KDA）降到 O(Nd)。

### Q62. Ring AllReduce 通信量是多少？

#### 回答要点

- Ring AllReduce 分两个阶段：scatter-reduce + all-gather。
- 每个阶段通信量 ≈ 2(P-1)/P × DataSize。
- 总通信量 ≈ 4(P-1)/P × DataSize，接近与 P 无关。
- 瓶颈在网络带宽，不在 P 的大小。

### Q63. Top-k 和 Top-p 采样的区别？

#### 回答要点

- Top-k：只保留概率最高的 k 个 token。
- Top-p（Nucleus Sampling）：保留累积概率达到 p 的最小 token 集合。
- Top-k 可能太死板（k 固定），Top-p 更灵活（动态数量）。
- 温度 T 控制分布的"尖锐程度"。

### Q64. Beam Search 的原理和局限？

#### 回答要点

- 每步保留 beam_size 个最优候选，而不是贪心选择。
- 优势：比 greedy 更好的全局最优。
- 局限：倾向短文本（长度惩罚）、多样性差、计算量 beam_size 倍。
- 在开放式生成中通常不如 sampling。

---

## 9. 前沿与趋势

### Q65. DualPipe（通信-计算重叠）是什么？

#### 回答要点

- 解决 MoE 模型训练中 all-to-all 通信和 PP 通信的重叠问题。
- 把 forward/backward 的计算和通信完全重叠，消除通信 bubble。
- 关键：每个 micro-batch 的通信和下一个 micro-batch 的计算并行。
- 使计算-通信比接近 1:1 时仍保持高 GPU 利用率。

### Q66. MoE 规模扩大后对 Infra 有什么影响？

#### 回答要点

- All-to-all 通信成为核心瓶颈。
- Expert Parallelism 规模扩大，EP + DP + PP 组合更复杂。
- 负载均衡成为关键（冗余专家、动态调整）。
- 显存压力从 KV Cache 转向模型权重。
- 计算密度降低，memory-bound / communication-bound 加剧。

### Q67. 扩散语言模型（Diffusion LM）是什么？

#### 回答要点

- 把扩散模型的思想应用到文本生成：从噪声逐步去噪生成 token。
- 优势：可以并行生成多个 token，不需要自回归。
- 劣势：生成质量目前不如自回归模型，训练更复杂。
- 研究方向：discrete diffusion、continuous relaxation。

### Q68. MTP（Multi-Token Prediction）的意义是什么？

#### 回答要点

- 训练时预测未来多个 token，而不是只预测下一个。
- 提供更丰富的训练信号，可能提升模型质量。
- 推理时可以做 speculative decoding 的 draft。
- 部分大模型在训练中使用了 MTP。

---

## 10. 反问面试官

### Q69. 面试最后可以反问什么？

#### 回答要点

- 团队当前最重视的后训练方向是什么（RLHF vs DPO vs GRPO）。
- 训练 Infra 是自研还是基于开源框架。
- 评估模型效果的闭环是怎么做的。
- 当前最大的训练稳定性挑战是什么。
- 团队更希望这个岗位在 3 到 6 个月内解决哪类问题。

### Q70. 哪些反问比较有质量？

#### 回答要点

- 围绕训练稳定性、Scaling Law 实践、评估体系、Infra 选型提问。
- 避免只问福利、流程或 title。
- 反问最好能体现你真的理解后训练的工程挑战，而不是泛泛问业务情况。

---

## 10a. 补充：PyTorch 与训练工程

### Q71. DataLoader 的 num_workers 和 pin_memory 怎么设置？

#### 回答要点

- num_workers：CPU 核心数和 I/O 瓶颈决定，太多反而争抢资源。
- pin_memory=True：把数据锁在 page-locked memory 中，加速 CPU→GPU 传输。
- 在 LLM 训练中 DataLoader 通常不是瓶颈（token 化后数据量小）。
- 但在多模态训练（图像+文本）中 I/O 可能成为瓶颈。

### Q72. 梯度裁剪（Gradient Clipping）为什么重要？

#### 回答要点

- 防止梯度爆炸导致训练崩溃。
- `torch.nn.utils.clip_grad_norm_(params, max_norm=1.0)`：按 norm 裁剪。
- 在 Transformer 训练中几乎必用，因为 attention 的梯度可能很大。
- max_norm 通常设为 1.0，RL 训练中可能需要更小的值。

### Q73. DDP（DistributedDataParallel）的原理？

#### 回答要点

- 每张 GPU 保存完整模型副本，各自处理不同的 data mini-batch。
- 反向传播后做 AllReduce 同步梯度，然后各自更新参数。
- 通信量 = 2 × 模型参数量（梯度），与 batch size 无关。
- 适合模型能放进单卡、需要加速训练的场景。

### Q74. FSDP 和 DDP 怎么选？

#### 回答要点

- DDP：模型能放进单卡时用，简单高效。
- FSDP：模型太大单卡放不下时用，分片参数/梯度/优化器。
- FSDP 的通信量更大（需要 all-gather 参数），但显存效率更高。
- ZeRO Stage 选择：Stage 1/2 通信量接近 DDP，Stage 3 显存最省。

### Q75. 混合精度训练中 loss scaling 是什么？为什么需要？

#### 回答要点

- FP16 的梯度范围太小，容易出现 underflow（梯度变成 0）。
- Loss scaling：把 loss 乘一个大的系数（如 65536），让梯度放大到 FP16 可表示范围。
- 反向传播后把梯度除回来，再用 FP32 更新参数。
- BF16 不需要 loss scaling（指数范围和 FP32 相同）。

---

## 10b. 补充：模型评估与对比

### Q76. Perplexity 是什么？怎么计算？

#### 回答要点

- Perplexity = exp(cross_entropy_loss)，衡量模型对文本的"困惑度"。
- 越低越好，表示模型对文本的预测更准确。
- 局限：不考虑生成质量和多样性，只在语言模型层面评估。
- 通常在不同数据集上分别计算（WikiText、C4 等）。

### Q77. MMLU 和 HumanEval 分别测什么？

#### 回答要点

- MMLU：57 个学科的多选题，测试广泛知识和推理能力。
- HumanEval：164 个编程题，测试代码生成能力（Pass@1）。
- MMLU 偏知识，HumanEval 偏推理和工程。
- 两者是 LLM 评估的基础 benchmark，但不够全面。

### Q78. 如何评估一个 RL 后训练模型的效果？

#### 回答要点

- Reward 曲线：训练过程中 reward 是否稳定上升。
- Benchmark 对比：和 SFT baseline、其他 RL 方法对比。
- KL 散度：policy 和 reference 的距离，太大说明偏离过远。
- 人工评估：对困难样本做 side-by-side 比较。
- 安全检查：确保模型没有产生有害内容。

### Q79. 什么是 reward hacking？怎么检测？

#### 回答要点

- Reward hacking：模型找到 reward model 的漏洞，获得高分但实际输出质量差。
- 检测方法：reward 上升但 benchmark 不升或下降、人工检查高分样本。
- 缓解方法：KL 惩罚、RM ensembling、迭代更新 RM、过程奖励。
- 是 RL 后训练中最常见的问题之一。

### Q80. 如何构造高质量的偏好数据？

#### 回答要点

- 来源：人工标注、模型生成 + 人工筛选、规则过滤。
- 质量要求：chosen 和 rejected 差异明显、覆盖多种能力维度、无标注偏差。
- 数量：通常几千到几万对，取决于模型大小和任务复杂度。
- 常见问题：标注不一致、chosen 和 rejected 太相似、数据泄露。

### Q81. DPO 的 loss 推导核心是什么？

#### 回答要点

- 从 RLHF 的目标出发：maximize expected reward - β × KL(policy || reference)。
- 推导出最优 policy 的闭式解：π*(y|x) ∝ π_ref(y|x) × exp(r(x,y)/β)。
- 反解出 reward = β × log(π(y|x)/π_ref(y|x)) + const。
- 代入 Bradley-Terry 模型，得到 DPO loss = -log σ(β × (log π_chosen/π_ref - log π_rejected/π_ref))。

### Q82. GRPO 的优势函数怎么算？为什么要组内标准化？

#### 回答要点

- 对每个 prompt 采样 G 个回答，计算每个回答的 reward。
- 优势 A_i = (r_i - mean(r)) / std(r)，即组内标准化。
- 标准化消除 prompt 间的 reward 基线差异，让优势只反映相对好坏。
- 不需要 Critic 模型来估计 value function，显存释放。

---

## 11. 每日抽查清单

每天随机抽 10 题，自查是否达到下面标准：

- 30 秒内能给结论
- 2 分钟内能给结构化回答
- 能举出一个自己的项目例子
- 能说出一个 trade-off
- 能补一个失败模式或常见坑

如果一题只能说概念、说不出工程细节，说明还没有准备到位。
