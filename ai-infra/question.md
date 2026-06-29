# AI Infra 系统工程高频问答题库

> 适用对象：AI Infra / LLM 推理引擎 / 训练平台方向候选人
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

### Q1. 你为什么适合 AI Infra 方向？

#### 回答要点

- 对推理引擎（vLLM/SGLang）有源码级理解，能从 PagedAttention、Scheduler、量化等维度分析系统设计。
- 有分布式训练实践经验，理解 TP/PP/EP/DP 的取舍和 Megatron 的核心抽象。
- 对 CUDA 编程和 GPU 性能优化有实战经验，能做 Kernel 级别的调优。
- 能把模型架构变化和 Infra 约束联系起来分析系统瓶颈。

### Q2. 你为什么想做 AI Infra，而不是纯算法或纯后端？

#### 回答要点

- AI Infra 是算法和工程的交汇点——模型架构决定系统瓶颈，系统设计约束算法能做多大。
- 纯算法更关注模型能力上限，纯后端更关注通用服务质量，而 AI Infra 要把不稳定、快速变化的模型能力转化为可靠的工程系统。
- 自己最擅长的是在显存、带宽、计算三者之间找最优解。

### Q3. 你理解的 AI Infra 工程师需要哪些核心能力？

#### 回答要点

- 模型理解：知道 Transformer 的每个组件为什么这样设计。
- 系统能力：理解 GPU 内存层次、并行计算、分布式通信。
- 工程能力：CUDA/C++ 编程、性能分析（Nsight）、框架源码阅读。
- 全局视角：能从模型→训练→推理→Serving 整条链路分析瓶颈。

### Q4. 你如何看待 AI Infra 的发展方向？

#### 回答要点

- 推理引擎从通用 Serving 走向场景化优化（Agentic、RL Rollout、长上下文）。
- 训练系统从单一框架走向多框架协同（Megatron + RL 框架 + 推理引擎）。
- 硬件适配从 NVIDIA 独大走向多元芯片（国产 GPU、TPU、NPU）。
- 系统优化的粒度越来越细：从框架级到 Kernel 级到硬件级。

---

## 3. 项目与经历

### Q5. 你做过的推理优化项目，核心挑战是什么？

#### 回答要点

- 描述一个真实项目：目标、约束、关键技术决策。
- 重点讲"为什么选这个方案"而不是"做了什么"。
- 能说出一个失败模式或尚未解决的问题。

### Q6. 你如何分析推理引擎的性能瓶颈？

#### 回答要点

- 先分 Prefill 和 Decode 两个阶段分析。
- Prefill 看 compute-bound 还是 memory-bound（roofline model）。
- Decode 主要看 memory bandwidth（KV Cache 读取 + 权重读取）。
- 用 Nsight Systems / Nsight Compute 定位具体 kernel 和瓶颈类型。

### Q7. 你在项目中如何处理显存不足的问题？

#### 回答要点

- 分析显存构成：权重、KV Cache、激活值、CUDA context。
- 优先减 KV Cache：PagedAttention、量化（FP8 KV）、缩短上下文。
- 然后减权重：量化（AWQ/GPTQ/INT8）、模型并行。
- 最后优化激活值：gradient checkpointing、static cache。

### Q8. 你对比过 vLLM 和 SGLang 吗？结论是什么？

#### 回答要点

- 核心差异在 KV Cache 管理：PagedAttention vs RadixAttention。
- vLLM 通用场景更成熟，SGLang 在长前缀/多轮/结构化输出场景更好。
- 公开 benchmark 结论不一，不能简单说谁更快，要看具体负载。
- 实际选型要根据 workload 特征和运维生态。

### Q9. 你在项目中用过哪些量化工具？效果如何？

#### 回答要点

- AWQ/GPTQ（weight-only W4A16）：显存减半，Decode TPS +50%+。
- FP8（QAT）：需要量化感知训练，精度损失可控。
- INT8 KV Cache：KV Cache 显存减半，精度影响较小。
- 关键 trade-off：通用性 vs 极致性能 vs 精度损失。

---

## 4. 推理引擎

### Q10. vLLM 的 PagedAttention 是怎么工作的？

#### 回答要点

- 把 KV Cache 分成固定大小 block（默认 16 token），通过 block table 管理逻辑连续、物理离散的映射。
- 解决了传统连续分配导致的 60-80% 显存碎片浪费。
- 支持 Copy-on-Write 前缀共享和动态长度分配。
- Attention kernel 有 20-26% 额外开销（indirect indexing）。

### Q11. vLLM 的 Scheduler 是怎么调度的？

#### 回答要点

- Continuous Batching：请求完成即退出，新请求随时插入。
- 默认优先 prefill 以降低 TTFT，代价是 decode 请求可能 stall。
- 支持抢占（preemption）：显存不足时 swap 或 recompute 低优先级请求。
- Chunked Prefill：长 prefill 分 chunk 与 decode 交替执行。

### Q12. SGLang 的 RadixAttention 和 PagedAttention 有什么区别？

#### 回答要点

- RadixAttention 用 Radix Tree 组织 KV Cache，支持任意前缀路径的复用和多分支共享。
- PagedAttention 是 block-level（粒度粗），RadixAttention 是 token/路径级（粒度细）。
- RadixAttention 在长 system prompt、多轮对话、结构化生成场景优势明显。
- PagedAttention 在通用场景更成熟，生态更丰富。

### Q13. vLLM 的 Prefix Caching 在什么场景下有效？

#### 回答要点

- 多个请求共享相同 system prompt 或 few-shot examples。
- Agent 场景、RL Rollout（多个采样共享 prompt）、多轮对话。
- block-level 匹配：前缀长度必须是 block size 的整数倍。
- 异构负载下 exact prefix match 很少，收益有限。

### Q14. Continuous Batching 为什么能提升吞吐？

#### 回答要点

- Static Batching 等整个 batch 完成才处理下一个，GPU 利用率低。
- Continuous Batching 请求完成即退出、新请求随时插入，GPU 始终满载。
- 吞吐提升可达 4x（vLLM 社区数据）。
- 代价：调度复杂度增加，需要 PagedAttention 支持动态 KV Cache。

### Q15. vLLM 有哪些设计 trade-off？

#### 回答要点

- PagedAttention：内存效率 vs kernel 效率（20-26% overhead）。
- Block size=16：内部碎片 vs GPU 利用率 vs 前缀共享概率。
- Continuous Batching：吞吐 vs decode 延迟抖动。
- Prefix Caching：计算节省 vs 管理复杂度 vs 缓存命中率。
- Prefill 优先：低 TTFT vs 高 TBT。

### Q16. vLLM 的 block size 怎么选？有什么 trade-off？

#### 回答要点

- Block 太小：GPU 并行利用率低。
- Block 太大：内部碎片增加，前缀共享概率降低。
- 实验结论：ShareGPT 场景 16-128 都较好，Alpaca（短序列）16-32 最好。
- 默认 16 是大多数 workload 的甜点。

### Q17. Prefill/Decode 分离（PD 分离）的意义是什么？

#### 回答要点

- Prefill 是 compute-bound，Decode 是 memory-bound，两者对硬件的需求不同。
- 分离后可以针对各自特点优化：Prefill 用高算力 GPU，Decode 用高带宽 GPU。
- 减少 Prefill 对 Decode 的阻塞，降低 TBT。
- Mooncake、DistServe、Splitwise 都实现了 PD 分离。

### Q18. Mooncake 的 KVCache-centric 架构是什么？

#### 回答要点

- 以 KV Cache 为中心设计推理服务架构。
- PD 分离：Prefill 节点生成 KV Cache，通过 Transfer Engine 传输到 Decode 节点。
- Prefix Caching 跨节点复用 KV Cache，减少重复 prefill。
- Transfer Engine 优化 KV Cache 传输效率（RDMA、内存池）。

### Q19. vLLM 和 TensorRT-LLM 有什么区别？

#### 回答要点

- vLLM：开源、模型支持广、社区大、灵活性强。
- TensorRT-LLM：NVIDIA 官方、极致性能优化、需要编译、灵活性差。
- TensorRT-LLM 通常在特定模型上更快（kernel 级优化），但新模型适配慢。
- 实际选择看团队能力和运维成本。

### Q20. 推理引擎的 CUDA Graph 支持有什么挑战？

#### 回答要点

- CUDA Graph 要求 tensor shape 固定，但 dynamic batch 和 variable length 导致 shape 变化。
- Decode 阶段 benefit 最大（大量小 kernel，CPU launch overhead 占比高）。
- 解决方案：StaticCache 预分配、固定 batch size padding、分场景捕获多个 graph。
- 在 vLLM 中 CUDA Graph 和 dynamic batch 的兼容是持续的工程挑战。

### Q21. SGLang 的 Zero-overhead Scheduler 是什么？

#### 回答要点

- 传统 scheduler 在 Python 层面做调度决策，有 GIL 和解释器开销。
- SGLang 把调度逻辑与 GPU 计算重叠，隐藏调度延迟。
- Cache-aware load balancing：根据 KV Cache 状态做负载均衡。
- 在高并发小模型场景下优势明显（解决了 GIL 瓶颈）。

### Q22. DualPath（双路径 KV-Cache 加载）解决什么问题？

#### 回答要点

- Agentic 推理场景下，KV Cache 需要从 Prefill 节点传输到 Decode 节点。
- 传统方式通过 PCIe/NVLink 传输，带宽是瓶颈。
- DualPath 用两条路径并行加载 KV Cache，聚合带宽。
- 关键优化：分块传输、预取、与计算重叠。

---

## 5. 分布式训练

### Q23. Tensor Parallel（TP）的原理是什么？

#### 回答要点

- 把单层的参数矩阵（Q/K/V/FFN）按列或行切分到同节点内的多张 GPU。
- Column Parallel：按输出维度切，前向不需要 AllReduce。
- Row Parallel：按输入维度切，前向需要 AllReduce。
- 标准 Llama Transformer Block 前向需要 2 次 AllReduce。

### Q24. Pipeline Parallel（PP）的原理是什么？

#### 回答要点

- 把模型按层切分到不同 GPU，形成流水线。
- 数据以 micro-batch 形式在流水线上传递。
- 关键问题是 bubble（流水线空闲时间）：GPipe 的 bubble 比例 = (P-1)/M。
- 1F1B（one forward one backward）和 Interleaved 1F1B 可以减少 bubble。

### Q25. Expert Parallel（EP）和 TP 的区别？

#### 回答要点

- TP 切分 dense 模型的权重矩阵，EP 把 MoE 的不同 expert 分配到不同 GPU。
- EP 需要 all-to-all 通信（token dispatch 和 combine），TP 需要 all-reduce。
- EP 适合跨节点（all-to-all 对带宽需求相对低），TP 适合同节点（all-reduce 需要高带宽）。

### Q26. Data Parallel（DP）和 FSDP 有什么区别？

#### 回答要点

- 标准 DP（DDP）：每张 GPU 保存完整模型副本，梯度同步。
- FSDP（ZeRO-3）：模型参数、梯度、优化器状态都分片到不同 GPU。
- FSDP 大幅减少显存冗余，但需要 all-gather 参数做前向/反向。
- ZeRO Stage 1/2/3 逐步增加分片程度。

### Q27. Megatron-LM 的核心架构是什么？

#### 回答要点

- 支持 TP + PP + EP + DP + SP（Sequence Parallel）的完整组合。
- TP 在同节点内做模型并行，PP 跨节点做流水线，DP 做数据并行。
- Sequence Parallel：把 LayerNorm 和 Dropout 也切分到 TP 维度上，减少激活值显存。
- 关键设计：通信-计算重叠、micro-batch 调度。

### Q28. Ring AllReduce 通信量是多少？怎么推导？

#### 回答要点

- 两阶段：scatter-reduce + all-gather。
- 每阶段 P-1 步，每步通信 DataSize/P。
- 总通信量 ≈ 2 × (P-1)/P × DataSize × 2 ≈ 4(P-1)/P × DataSize。
- 关键 insight：通信量与 P 近似无关，瓶颈在带宽。

### Q29. All-to-All 通信量怎么算？MoE 里为什么重要？

#### 回答要点

- All-to-All：每个 GPU 向其他所有 GPU 发送不同的数据块。
- 通信量 ≈ (P-1)/P × DataSize（每 GPU 发送和接收）。
- MoE 中 all-to-all 用于 token dispatch 和 combine，通信量与 expert 数量和 top-K 成正比。
- 跨节点 all-to-all 受限于 IB 带宽，是 MoE 规模化的核心瓶颈。

### Q30. 为什么跨节点 AllReduce 实际带宽跑不满标称 IB？

#### 回答要点

- 协议开销（IB headers、acknowledgments）。
- 小消息时 latency-bound，不是 bandwidth-bound。
- 网络拥塞和路由不均衡。
- GPU 到 NIC 的 PCIe 带宽可能成为瓶颈。
- NCCL 的配置和环境因素。

### Q31. ZeRO Stage 1/2/3 分别做什么？

#### 回答要点

- Stage 1：分片优化器状态（Adam m, v）。
- Stage 2：分片优化器状态 + 梯度。
- Stage 3：分片优化器状态 + 梯度 + 模型参数。
- Stage 越高显存越省，但通信开销越大（需要 all-gather 参数）。

### Q32. Activation Checkpointing 是什么？

#### 回答要点

- 训练时不保存中间激活值，反向传播时重新计算。
- 节省激活值显存（可减少约 60%），但增加约 33% 计算量。
- 选择性 Checkpointing：只对显存大的层（如 Attention）做 checkpoint。
- 和 gradient accumulation 配合使用可以进一步减少显存。

### Q33. NVLink、PCIe、IB 在 GPU 通信中的角色？

#### 回答要点

- NVLink：同节点 GPU 间高速互联（900 GB/s for H100）。
- PCIe：GPU 到 CPU/NIC 的连接（64 GB/s for PCIe 5.0 x16）。
- InfiniBand（IB）：跨节点通信（400 Gbps for NDR）。
- 带宽层级：NVLink >> IB > PCIe，决定了 TP 同节点、EP 跨节点的基本策略。

---

## 6. KV Cache 与显存工程

### Q34. KV Cache 的大小怎么计算？

#### 回答要点

- KV Cache = 2 × n_layers × n_kv_heads × d_head × seq_len × dtype_size。
- GQA 减少 n_kv_heads，KV Cache 成比例缩小。
- MLA 通过低秩压缩进一步减小（约 93%）。
- 以 Llama 2 7B FP16 为例：每 token 约 0.5 MB。

### Q35. 训练时显存由哪些部分组成？

#### 回答要点

- 模型参数（2P bytes for FP16）。
- 梯度（2P bytes）。
- 优化器状态（Adam FP32 m+v = 8P bytes，是显存大户）。
- 激活值（与 batch、seq_len、层数相关）。
- 以 Llama 2 7B FP16 + AdamW 为例：总计约 94-114 GB。

### Q36. Adam 优化器状态为什么占 8P？

#### 回答要点

- 一阶矩 m（FP32）：4P bytes。
- 二阶矩 v（FP32）：4P bytes。
- 主权重（FP16）：2P bytes。
- 总计 10P bytes（含权重），优化器状态占 8P。
- 8-bit Adam（如 bitsandbytes）可以减到 2P。

### Q37. FP8 KV Cache 有什么优势和风险？

#### 回答要点

- 优势：KV Cache 显存减半，memory bandwidth 需求减半。
- 风险：精度损失，特别是对 attention score 分布敏感的任务。
- 工程实现：需要处理 quantization/dequantization 的开销。
- 在大多数推理场景下精度影响可接受。

### Q38. 4090 上跑 Qwen3-8B 的显存分布是什么样的？

#### 回答要点

- BF16 权重约 16.4 GB。
- CUDA context、PyTorch allocator、cuDNN workspace 约 2-3 GB。
- 剩余约 5.6 GB 给 KV Cache。
- 天然适合练习显存预算和带宽瓶颈分析。

### Q39. GPU 显存碎片怎么产生的？怎么解决？

#### 回答要点

- PyTorch 的动态内存分配（不同大小的 tensor 频繁 alloc/free）。
- 传统 KV Cache 连续分配导致外部碎片。
- 解决：PagedAttention（block-level 管理）、PyTorch caching allocator、预分配 StaticCache。
- 监控：`torch.cuda.memory_stats()` 查看碎片比例。

### Q40. KV Cache offloading 到 CPU 内存可行吗？

#### 回答要点

- 可行，但 PCIe 带宽（~64 GB/s）是瓶颈。
- Decode 每 step 需要读取全部 KV Cache，offloading 后延迟大幅增加。
- 适合 batch 较小或 KV Cache 可以部分 offload 的场景。
- FlexGen 等工作探索了 offloading 的最优策略。

---

## 7. CUDA / GPU 编程

### Q41. GPU 的内存层次是什么？

#### 回答要点

- Global Memory（HBM）：最大最慢，所有线程可见。
- Shared Memory（SRAM）：block 内共享，延迟低（~20 cycles）。
- Register：线程私有，最快。
- L1/L2 Cache：硬件管理，部分可配置。
- 优化核心：把数据从 HBM 搬到 Shared Memory / Register，减少 HBM 访问。

### Q42. SIMT 模型是什么？

#### 回答要点

- Single Instruction, Multiple Threads：32 个线程组成一个 warp，执行相同指令。
- 分支会导致 warp divergence：不同线程走不同路径，串行执行。
- 优化核心：减少 warp divergence，保证 coalesced memory access。

### Q43. Memory Coalescing 是什么？

#### 回答要点

- warp 内 32 个线程同时访问连续内存地址时，可以合并为一次大的内存事务。
- 非 coalesced 访问（如 stride access）会导致多次小的内存事务，效率低。
- 优化：保证 thread i 访问 address[i]（连续），避免 address[i*stride]。

### Q44. Bank Conflict 是什么？怎么避免？

#### 回答要点

- Shared Memory 被分成 32 个 bank，每个 bank 每 cycle 只能服务一次访问。
- 如果 warp 内多个线程访问同一 bank 的不同地址，就会产生 bank conflict。
- 避免方法：padding、调整 stride、保证相邻线程访问相邻 bank。

### Q45. Tensor Core 和 CUDA Core 的区别？

#### 回答要点

- CUDA Core：标量/向量运算，通用计算。
- Tensor Core：矩阵乘加运算（如 4×4×4 MMA），专为深度学习设计。
- Tensor Core 的吞吐远高于 CUDA Core 做同等矩阵运算。
- 使用 WMMA API 或 `__mma_sync` 调用，需要对齐数据（16 字节对齐）。

### Q46. FlashAttention 的 IO 分析怎么做？

#### 回答要点

- 标准 Attention：HBM 读写 O(N²)（写 attention matrix）。
- FlashAttention：Tiling 后在 SRAM 中完成，HBM 读写降到 O(N²d/M)。
- M 是 SRAM 大小，d 是 head dim。
- 核心思想：IO-aware 算法设计，不改变数学结果但大幅减少 HBM 访问。

### Q47. Online Softmax 的分块更新原理？

#### 回答要点

- 标准 softmax 需要两遍遍历：先求 max，再求 exp 和 sum。
- Online softmax 一遍遍历同时维护 running max 和 running sum。
- 每读入新 block 时更新 max 并 rescale 之前的 sum。
- 是 FlashAttention 能在 SRAM 中逐 block 计算 attention 的数学基础。

### Q48. GEMM 为什么是 LLM 推理的核心？

#### 回答要点

- LLM 的前向传播中，Linear 层（QKV projection、FFN、output projection）都是 GEMM。
- GEMM 占总 FLOPs 的 90% 以上（Dense 模型）。
- 优化 GEMM 的效率直接决定推理速度。
- cuBLAS 是标准库，Tensor Core 加速是关键。

### Q49. Nsight Systems 和 Nsight Compute 的区别？

#### 回答要点

- Nsight Systems（nsys）：系统级 profiling，看 CPU/GPU 交互、kernel 时序、通信。
- Nsight Compute（ncu）：Kernel 级 profiling，看单个 kernel 的 SM 利用率、内存吞吐、warp stall。
- 先用 nsys 定位热点 kernel，再用 ncu 分析该 kernel 的瓶颈。

### Q50. Triton 和 CUDA 的区别？什么时候用哪个？

#### 回答要点

- Triton：Python 编写 GPU kernel，自动做 tiling、shared memory 管理。
- CUDA：C++ 编写，完全手动控制，灵活但开发成本高。
- Triton 适合快速原型和中等复杂度的 kernel，CUDA 适合极致优化的核心 kernel。
- Triton 生成的代码效率接近手写 CUDA，但不是所有场景都能覆盖。

### Q51. Hopper 和 Blackwell 架构相比 Ampere 有什么改进？

#### 回答要点

- Hopper（H100）：TMA（Tensor Memory Accelerator）、Thread Block Cluster、FP8、NVLink 4.0。
- Blackwell（B200）：更大的 SM 数量、FP4 支持、NVLink 5.0（1.8 TB/s）。
- 关键趋势：更多的 Tensor Core 吞吐、更大的 HBM 带宽、更强的互联。
- 对 kernel 编程的影响：需要适配新的内存访问模式和并行策略。

### Q52. Warp Stall 有哪些常见原因？

#### 回答要点

- Memory dependency：等待全局内存数据。
- Instruction overhead：指令发射延迟。
- Barrier：等待其他 warp 到达同步点。
- Branch resolving：分支预测失败。
- 用 Nsight Compute 的 Warp State Statistics 分析。

---

## 8. C++ 与性能工程

### Q53. std::move 和 std::forward 的区别？

#### 回答要点

- std::move：无条件转换为右值引用，表示"这个对象可以被移动"。
- std::forward：条件转换，保持原始值类别（左值/右值），用于完美转发。
- move 用在你知道不再需要的对象上，forward 用在模板函数参数上。

### Q54. unique_ptr 和 shared_ptr 的使用场景？

#### 回答要点

- unique_ptr：独占所有权，零开销，不可拷贝只能移动。
- shared_ptr：共享所有权，引用计数，可拷贝，有额外开销。
- 默认用 unique_ptr，只在需要共享所有权时用 shared_ptr。
- weak_ptr 配合 shared_ptr 解决循环引用。

### Q55. 虚函数表原理？多重继承时 vtable 怎么排布？

#### 回答要点

- 每个有虚函数的类有一个 vtable，对象存储指向 vtable 的指针。
- 虚函数调用通过 vtable 间接跳转（runtime 确定）。
- 多重继承时对象有多个 vptr，每个指向对应基类的 vtable。
- 性能影响：间接跳转阻止内联和分支预测。

### Q56. False Sharing 是什么？怎么避免？

#### 回答要点

- 多个线程修改不同变量，但这些变量在同一 cache line（64 bytes）内。
- 导致 cache line 在核之间频繁传递（cache bouncing），性能下降。
- 避免：alignas(64) 对齐、padding、把共享变量分开存放。
- 用 perf c2c 或 VTune 检测。

### Q57. 无锁队列怎么实现？ABA 问题怎么解决？

#### 回答要点

- 用 CAS（Compare-And-Swap）实现原子操作。
- ABA 问题：值从 A 变成 B 再变回 A，CAS 认为没变。
- 解决：版本号（tagged pointer）、hazard pointer、RCU。
- std::atomic 提供基础的无锁原语。

### Q58. memory_order 有哪些？acquire/release 语义是什么？

#### 回答要点

- relaxed：无顺序保证，只保证原子性。
- acquire：读操作，之后的读写不会被重排到此之前。
- release：写操作，之前的读写不会被重排到此之后。
- seq_cst：最强，全局顺序一致。
- acquire/release 配对可以实现无锁同步。

### Q59. C++ 协程（Coroutine）的原理？

#### 回答要点

- 协程是可暂停和恢复的函数，用 co_await/co_yield/co_return。
- 编译器把协程体转换成状态机，局部变量存储在 heap-allocated frame 中。
- 适合异步 I/O、生成器、协作式多任务。
- 性能考虑：heap allocation 开销、HALO（Heap Allocation eLision Optimization）。

### Q60. SIMD 是什么？SSE/AVX/AVX-512 的区别？

#### 回答要点

- SIMD（Single Instruction Multiple Data）：一条指令处理多个数据。
- SSE：128-bit 寄存器，AVX：256-bit，AVX-512：512-bit。
- 适合向量化计算（矩阵运算、信号处理、图像）。
- 编译器自动向量化有限，手写 intrinsics 可以获得更好性能。

### Q61. CRTP（Curiously Recurring Template Pattern）是什么？

#### 回答要点

- 派生类把自己作为模板参数传给基类：`class Derived : public Base<Derived>`。
- 实现编译期多态，避免虚函数的运行时开销。
- 常用于 mixin、static interface、enable_shared_from_this。
- 局限：不能用于运行期动态多态。

### Q62. 编译优化中 -O2 和 -O3 的区别？

#### 回答要点

- -O2：大部分安全优化（内联、循环展开、常量传播、死代码消除）。
- -O3：更激进的优化（自动向量化、更激进的内联和循环变换）。
- -O3 可能增加编译时间和二进制大小，不一定更快（过度优化可能伤害 cache）。
- 生产环境通常用 -O2，性能关键路径可以单独 -O3。

### Q63. 什么是 NUMA 架构？对程序有什么影响？

#### 回答要点

- Non-Uniform Memory Access：每个 CPU socket 有自己的本地内存。
- 访问本地内存快，访问远端内存慢（延迟差 2-3x）。
- 影响：线程绑核、内存分配策略（numactl）、GPU 和 NIC 的 NUMA 节点对齐。
- AI Infra 中 GPU 和 NIC 应该在同一 NUMA 节点，避免跨节点数据传输。

### Q64. C++ 的 RAII 是什么？为什么重要？

#### 回答要点

- Resource Acquisition Is Initialization：资源获取即初始化。
- 把资源管理（内存、文件、锁、GPU buffer）绑定到对象的生命周期。
- 析构函数自动释放资源，避免泄漏。
- 在 CUDA 编程中特别重要：GPU 内存、stream、event 都需要 RAII 管理。

---

## 9. 系统设计

### Q65. 如何设计一个高吞吐的 LLM 推理服务？

#### 回答要点

- 核心组件：请求路由、推理引擎（vLLM/SGLang）、KV Cache 管理、负载均衡。
- 关键优化：Continuous Batching、Prefix Caching、量化、Chunked Prefill。
- 高可用：多实例部署、健康检查、优雅降级。
- 可观测：TTFT、TBT、吞吐、显存使用、请求队列长度。

### Q66. 如何设计一个 RL 训练的 GPU 调度系统？

#### 回答要点

- 多角色协同：Rollout、Actor、Critic、Reward 各自需要 GPU。
- 调度策略：空间分离（OpenRLHF）vs 时分复用（veRL）。
- 权重同步：Actor 训练后同步到 Rollout Engine。
- 关键挑战：GPU 利用率最大化、减少等待时间。

### Q67. 如何设计一个训练平台的任务调度器？

#### 回答要点

- 任务抽象：训练 job（资源需求、优先级、依赖关系）。
- 调度策略：FIFO、优先级抢占、公平共享、拓扑感知。
- GPU 拓扑：同节点 NVLink、跨节点 IB，尽量把同一 job 的 GPU 放在同拓扑域。
- 容错：checkpoint 定期保存、故障自动重启。

### Q68. 如何保护一个被 Agent 高频调用的 Tool 服务？

#### 回答要点

- 做超时、重试、熔断和限流。
- 做场景级和内容级缓存。
- 区分只读和有副作用工具。
- 做幂等保护和降级路径。
- 用 trace 和指标观察热点与失败模式。

### Q69. 重试为什么有时候很危险？

#### 回答要点

- 非幂等操作会被重复执行。
- 下游已经高负载时，盲目重试会雪上加霜。
- 如果没有退避（backoff）和预算控制，会放大故障。
- 解决：幂等保护、指数退避、重试预算、断路器。

### Q70. 幂等如何设计？

#### 回答要点

- 使用唯一请求 ID 或业务去重键。
- 对写操作保存状态和执行结果。
- 重试时能识别"已执行过"。
- 明确哪些操作天然不幂等，需要额外保护。

### Q71. 限流、降级、熔断分别解决什么问题？

#### 回答要点

- 限流：控制流量上限，保护系统。
- 降级：资源不足时保核心路径，放弃非核心功能。
- 熔断：下游异常时快速失败，防止级联故障。
- 三者配合使用，构成服务保护的完整策略。

### Q72. 如何设计一个 GPU 集群的监控系统？

#### 回答要点

- 硬件指标：GPU 利用率、显存使用、温度、功耗、ECC 错误。
- 训练指标：loss、learning rate、gradient norm、throughput（samples/sec）。
- 通信指标：NCCL 带宽、allreduce 延迟、IB 拥塞。
- 工具：DCGM Exporter + Prometheus + Grafana。

---

## 10. OS / 体系结构

### Q73. 进程和线程的本质区别？切换开销差在哪里？

#### 回答要点

- 进程是资源分配单位（独立地址空间），线程是调度单位（共享进程地址空间）。
- 进程切换需要 TLB flush、页表切换，开销大。
- 线程切换只需切换寄存器和栈，开销小。
- 协程更轻：用户态调度，无内核参与。

### Q74. 虚拟内存、物理内存、MMU、TLB 的关系？

#### 回答要点

- 虚拟内存：每个进程看到的地址空间，通过页表映射到物理内存。
- MMU（Memory Management Unit）：硬件做虚拟→物理地址转换。
- TLB（Translation Lookaside Buffer）：缓存最近的页表项，加速转换。
- TLB miss 会导致额外的内存访问（walk page table），影响性能。

### Q75. select/poll/epoll 的区别？

#### 回答要点

- select：fd 数量限制（通常 1024），每次调用需要复制全部 fd 集合。
- poll：无 fd 数量限制，但仍需复制全部 fd。
- epoll：内核维护 fd 集合，只返回就绪的 fd，O(1) 复杂度。
- epoll 有 LT（Level Triggered）和 ET（Edge Triggered）两种模式。

### Q76. 零拷贝是什么？sendfile 减少了哪些拷贝？

#### 回答要点

- 传统 I/O：数据从磁盘→内核 buffer→用户 buffer→socket buffer→网卡，4 次拷贝。
- sendfile：数据从磁盘→内核 buffer→socket buffer→网卡，减少到 3 次。
- mmap + write：减少到 3 次但可能触发 page fault。
- DMA scatter-gather：最彻底，减少到 2 次。

### Q77. CPU 流水线冒险有哪些？

#### 回答要点

- 数据冒险（RAW/WAR/WAW）：后续指令依赖前序结果。
- 控制冒险：分支指令导致流水线无法确定下一条指令。
- 结构冒险：多条指令同时竞争同一硬件资源。
- 解决：forwarding、分支预测、乱序执行。

### Q78. L1/L2/L3 Cache 的区别？

#### 回答要点

- L1：最小最快（~1 cycle），分 I-cache 和 D-cache。
- L2：中等（~10 cycles），通常 per-core。
- L3：最大最慢（~30-40 cycles），多核共享。
- AI Infra 中关注 L3 的 False Sharing 和 NUMA 对 cache 的影响。

### Q79. MESI 协议是什么？

#### 回答要点

- Modified：本 cache line 被修改，其他 cache 中无效。
- Exclusive：本 cache line 有效且独占。
- Shared：多个 cache 中都有，且一致。
- Invalid：本 cache line 无效。
- 用于多核间维护 cache 一致性。

### Q80. 分支预测器有哪些？2-bit 饱和计数器怎么工作？

#### 回答要点

- 静态预测：总是预测 taken/not taken。
- 动态预测：2-bit 饱和计数器（strong not → weak not → weak taken → strong taken）。
- 两级预测器：用历史 pattern 索引不同的计数器表。
- 现代 CPU 用 TAGE 等高级预测器。

### Q81. 什么是 RDMA？RoCE 和 InfiniBand 的区别？

#### 回答要点

- RDMA（Remote Direct Memory Access）：远程直接访问内存，绕过 CPU 和 OS。
- InfiniBand：独立的网络协议和硬件，高带宽低延迟。
- RoCE（RDMA over Converged Ethernet）：在以太网上跑 RDMA，复用现有网络。
- AI 训练集群通常用 InfiniBand（更好的延迟和拥塞控制）。

### Q82. TIME_WAIT 状态的作用？

#### 回答要点

- TCP 主动关闭连接后进入 TIME_WAIT，持续 2×MSL（通常 60s）。
- 作用：确保最后的 ACK 到达对端；让网络中残留的包过期。
- 大量 TIME_WAIT 会消耗端口和内存。
- 解决：SO_REUSEADDR、tcp_tw_reuse、连接池。

---

## 11. 量化与推理加速

### Q83. PTQ 和 QAT 有什么区别？

#### 回答要点

- PTQ（Post-Training Quantization）：训练后直接量化，不需要重训。
- QAT（Quantization-Aware Training）：在训练中模拟量化误差，模型学会适应。
- PTQ 快速但精度损失可能大，QAT 慢但精度更好。
- FP8 通常需要 QAT（训练时用 FP8 模拟），INT4/INT8 可以 PTQ。

### Q84. 量化的 calibration 是什么？

#### 回答要点

- 用一小批代表性数据确定量化的 scale 和 zero-point。
- 方法：min-max、percentile、MSE 最优。
- Calibration 数据的选择直接影响量化精度。
- AWQ 根据激活值的分布来保护重要权重。

### Q85. Speculative Decoding 的加速比怎么计算？

#### 回答要点

- 加速比 ≈ 1 + α × (K - 1)，其中 α 是接受率，K 是 draft 长度。
- α 取决于 draft model 和 target model 的分布相似度。
- 理论上 K 越大越好，但 rejected token 的计算是浪费。
- Tree-based speculative decoding（EAGLE-2）可以提高有效接受率。

### Q86. FP8 训练和推理的现状？

#### 回答要点

- FP8 有两种格式：E4M3（精度优先）和 E5M2（范围优先）。
- 训练：需要 QAT，用 Transformer Engine 自动处理。
- 推理：FP8 权重 + FP8 KV Cache，显存和带宽都减半。
- Hopper/Blackwell 原生支持 FP8 Tensor Core。

### Q87. vLLM 支持哪些量化方法？

#### 回答要点

- AWQ（W4A16）：activation-aware，快速，推荐。
- GPTQ（W4A16/W8A16）：基于 Hessian，精度好。
- FP8（W8A8）：需要 QAT，Hopper 支持。
- INT8 KV Cache：KV Cache 量化，显存减半。
- bitsandbytes（NF4/INT8）：灵活但性能一般。

### Q88. 量化后的模型精度怎么评估？

#### 回答要点

- Perplexity（PPL）：语言模型的标准指标。
- 下游 benchmark：MMLU、HumanEval、GSM8K 等。
- 对比量化前后的差异，而不是绝对值。
- 关注 outlier token 和特定任务的表现。

---

## 12. 算法与 Coding

### Q89. 面试中如何快速讲清复杂度？

#### 回答要点

- 先说核心数据结构。
- 再说主循环和嵌套关系。
- 分析最坏时间复杂度和空间复杂度。
- 如果有剪枝或预处理，再单独说明。

### Q90. BFS 变种题应该先想什么？

#### 回答要点

- 状态是什么。
- 一步操作的定义是什么。
- 边怎么扩展。
- 是否需要去重或剪枝。
- 是否满足最短路性质。

### Q91. 字符串格式化类题的高频坑点有哪些？

#### 回答要点

- 空格合并规则。
- 标点前后空格。
- 行长边界。
- 跨行断词规则。
- 输入规模大时不能反复拷贝大字符串。

### Q92. 写完代码后你会先检查什么？

#### 回答要点

- 输入边界。
- 空数据和极值。
- 重复元素或重复访问。
- 溢出风险。
- 时间复杂度是否真的符合约束。

### Q93. GEMM 从 Naive 到 cuBLAS 的优化链有哪些阶段？

#### 回答要点

- Naive 三重循环 → Tiling（shared memory）→ 向量化加载。
- Double buffering → Tensor Core（WMMA）→ warp-level 优化。
- cuBLAS 是高度优化的库实现，包含 auto-tuning。
- 面试中通常要求手写 Tiling 版本。

---

## 13. 反问面试官

### Q94. 面试最后可以反问什么？

#### 回答要点

- 团队当前最重视的 Infra 问题是什么。
- 推理引擎是自研还是基于 vLLM/SGLang 二次开发。
- 训练和推理的 GPU 资源是如何分配和调度的。
- 当前最大的性能瓶颈在哪（显存、带宽、通信、调度）。
- 团队更希望这个岗位在 3 到 6 个月内解决哪类问题。

### Q95. 哪些反问比较有质量？

#### 回答要点

- 围绕推理引擎优化、训练 Infra、GPU 调度、量化实践提问。
- 避免只问福利、流程或 title。
- 反问最好能体现你真的理解 AI Infra 的工程挑战，而不是泛泛问业务情况。

---

## 12a. 补充：训练工程与调度

### Q96. Megatron 的 Interleaved 1F1B 调度是什么？

#### 回答要点

- 标准 1F1B：每个 stage 先做完所有 micro-batch 的 forward，再做 backward。
- Interleaved 1F1B：把每个 stage 分成多个 virtual stage，交替做 forward 和 backward。
- 减少 pipeline bubble 比例，从 (P-1)/M 降到 (P-1)/(V×M)。
- 代价是通信量增加（更多的 activation 传递）。

### Q97. Sequence Parallel（SP）是什么？和 TP 怎么配合？

#### 回答要点

- TP 只切分了 Attention 和 FFN 的权重，LayerNorm 和 Dropout 仍然是冗余计算。
- SP 把 LayerNorm 和 Dropout 也切分到 sequence 维度上。
- 配合 TP 使用：TP 在 hidden dim 上切，SP 在 sequence dim 上切。
- 减少激活值显存，在大 batch 长序列场景下收益显著。

### Q98. Context Parallel 和 Sequence Parallel 的区别？

#### 回答要点

- Sequence Parallel：切分 LayerNorm/Dropout 的激活值，配合 TP 使用。
- Context Parallel：把输入序列切分到不同 GPU，每 GPU 处理一段，解决长序列训练。
- Context Parallel 需要跨 GPU 交换 KV（ring attention 或 all-to-all）。
- 两者可以组合使用。

### Q99. FlashAttention 在 Megatron 中怎么集成的？

#### 回答要点

- Megatron 通过 attention backend 抽象层集成 FlashAttention。
- 训练时用 FlashAttention-2/3 加速 attention 计算。
- 需要适配 TP/SP/CP 的切分方式。
- FlashAttention 的 IO 优化在训练中的收益比推理更显著（因为反向传播也需要 attention）。

### Q100. 训练中的 Gradient Accumulation 和 Pipeline Parallel 如何配合？

#### 回答要点

- Gradient Accumulation：多个 micro-batch 累积梯度后再更新参数。
- PP 中每个 stage 天然就有 micro-batch 级别的梯度累积。
- 两者结合时，有效 batch size = micro_batch × accumulation × DP_size。
- 需要正确设置 learning rate scaling。

---

## 12b. 补充：网络与通信深度

### Q101. NCCL 的 Ring 和 Tree 算法分别在什么场景用？

#### 回答要点

- Ring AllReduce：带宽最优，延迟与 P 成正比，适合大消息。
- Tree AllReduce：延迟最优（log P 步），带宽次优，适合小消息。
- NCCL 自动选择：小消息用 tree，大消息用 ring。
- 实际中 Ring 更常用（训练中的梯度通常是大消息）。

### Q102. 为什么 NVLink 对 TP 很重要？

#### 回答要点

- TP 需要高频 AllReduce（每个 Transformer Block 2 次）。
- AllReduce 对带宽敏感，NVLink 提供 900 GB/s（H100）。
- 跨节点 TP 受限于 IB 带宽（~50 GB/s），延迟高。
- 所以 TP 通常限制在同节点内（最多 8 GPU），跨节点用 PP/EP。

### Q103. RDMA 在 AI 训练中的作用？

#### 回答要点

- RDMA 让 GPU 直接访问远程内存，绕过 CPU 和 OS 内核。
- 减少延迟（~1μs vs ~10μs for TCP），提高带宽利用率。
- GPUDirect RDMA：GPU 内存直接通过 NIC 传输，不经过 CPU 内存。
- 是大规模分布式训练的基础设施要求。

### Q104. DeepSpeed ZeRO-Offload 和 ZeRO-Infinity 是什么？

#### 回答要点

- ZeRO-Offload：把优化器状态和计算 offload 到 CPU 内存和 NVMe SSD。
- ZeRO-Infinity：进一步 offload 模型参数到 NVMe，支持更大模型。
- 大幅降低 GPU 显存需求，但训练速度下降。
- 适合单卡或少量 GPU 训练大模型的场景。

### Q105. MoE 的通信-计算重叠怎么做？

#### 回答要点

- All-to-all 通信（token dispatch）和前向计算重叠。
- 方法：把 expert 计算分成两部分，一部分和通信并行。
- DualPipe 等方法实现了更彻底的通信-计算重叠。
- 关键：保证重叠不影响计算正确性，需要精细的 stream 管理。

---

## 14. 每日抽查清单

每天随机抽 10 题，自查是否达到下面标准：

- 30 秒内能给结论
- 2 分钟内能给结构化回答
- 能举出一个自己的项目例子
- 能说出一个 trade-off
- 能补一个失败模式或常见坑

如果一题只能说概念、说不出工程细节，说明还没有准备到位。
