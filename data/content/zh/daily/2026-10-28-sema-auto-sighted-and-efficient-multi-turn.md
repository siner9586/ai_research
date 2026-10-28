---
title: "提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力"
date: "2026-10-28"
target_date: "2026-10-26"
actual_date: "2026-10-26"
fallback_from: ""
lang: "zh"
slug: "2026-10-28-sema-auto-sighted-and-efficient-multi-turn"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "rag", "safety", "systems", "training", "video-generation", "vision-generation"]
topics: ["agents", "code", "evaluation", "rag", "safety", "systems", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-10-28-sema-auto-sighted-and-efficient-multi-turn-sources/"
generated_at: "2026-10-28T00:28:50.226164+00:00"
page_type: "brief"
candidate_count: 530
featured_count: 6
mentions_count: 20
featured_paper_titles: ["SEMA-Auto: Sighted and Efficient Multi-Turn Attack with Autonomy", "Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents", "Multi-Objective Reinforcement Learning Using Routed Ensembles and Trajectory Attribution", "TRACE: Memory-Efficient Time Series Class-Incremental Learning via Temporal-Spectral Reconstruction", "The Agent in the Middle: How AI-Mediated Access Reshapes Web Vulnerability Exploitation", "Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation"]
featured_paper_urls: ["https://arxiv.org/abs/2610.35743", "https://arxiv.org/abs/2610.34817", "https://arxiv.org/abs/2610.35733", "https://arxiv.org/abs/2610.35727", "https://arxiv.org/abs/2610.35541", "https://arxiv.org/abs/2610.34674"]
featured_paper_titles_zh: ["SEMA-Auto ：具有自主性的瞄准和高效的多回合攻击", "沉默且成本高昂：表征和检测LLM代理中的提示缓存错误集成", "使用路由集成和轨迹归因的多目标强化学习", "TRACE ：通过时间谱重建进行记忆效率的时间序列类增量学习", "中间代理： AI介导的访问如何重塑Web漏洞利用", "对标家用机器人导航中的障碍安全"]
---

# 提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>SEMA-Auto: Sighted and Efficient Multi-Turn Attack with Autonomy (Mingqian Feng, Xiaodong Liu, Weiwei Yang, Chenliang Xu, Jialin Song, Qiyao Ma, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.35743">2610.35743</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.35743">PDF</a></p>

中文标题：SEMA-Auto ：具有自主性的瞄准和高效的多回合攻击

信号显示：现有的越狱攻击者分为两类：静态规划者提前修复其单回合或多回合对抗计划，保持简单但忽略受害者的回复，浪费回合并限制可转移性；交互式生成器读取。关键词：rag、safety、code、fine-tuning。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents (Ying Zhang, Ruoqi Guo, Yi Liu, Gelei Deng, Yuekang Li, Yepang Liu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.34817">2610.34817</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.34817">PDF</a></p>

中文标题：沉默且成本高昂：表征和检测LLM代理中的提示缓存错误集成

信号显示：大语言模型（ LLM ）服务处理大量用户请求，导致大量推理成本。关键词：agent、inference、latency、evaluation。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Multi-Objective Reinforcement Learning Using Routed Ensembles and Trajectory Attribution (Zhenshuo Zhang, Ruoxuan Xiong, Hongyang R. Zhang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.35733">2610.35733</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.35733">PDF</a></p>

中文标题：使用路由集成和轨迹归因的多目标强化学习

信号显示：多目标强化学习是现代人工智能的一个基本问题，其应用涵盖后训练、推理模型和机器人控制。关键词：rag、alignment、safety、benchmark。代码/数据可用性需查看原文确认。

### 4. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>TRACE: Memory-Efficient Time Series Class-Incremental Learning via Temporal-Spectral Reconstruction (Junhui Mao, Junru Zhang, Liming Ye, Cheng Peng, Haoran Shi, Xiaoli Tang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.35727">2610.35727</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.35727">PDF</a></p>

中文标题：TRACE ：通过时间谱重建进行记忆效率的时间序列类增量学习

信号显示：网络连接的传感应用程序不断生成具有不断发展的行为类别的多变量时间序列，使得时间序列类增量学习（ TSCIL ）对于适应新课程而不会忘记以前获得的知识至关重要。关键词：serving、benchmark、code、memory。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>The Agent in the Middle: How AI-Mediated Access Reshapes Web Vulnerability Exploitation (Ruozhao Yang, Jiongchi Yu, Ming Hu, Xiaofei Xie)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.35541">2610.35541</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.35541">PDF</a></p>

中文标题：中间代理： AI介导的访问如何重塑Web漏洞利用

信号显示：Web服务越来越多地暴露后端接口，允许用户将任务委托给AI代理，这些代理无需导航网站即可直接调用服务操作。关键词：agent、workflow、serving、benchmark。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation (Hyunwoong Bae, Jisu Han, Jiyeon Choi, Dohoon Kim, Taesup Moon)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.34674">2610.34674</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.34674">PDF</a></p>

中文标题：对标家用机器人导航中的障碍安全

信号显示：安全的家用导航需要机器人根据障碍物是什么以及障碍物有多近来调节间隙和速度，而不需要不必要的保守主义。关键词：inference、safety、evaluation、benchmark。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Distributed Predictive Flocking for a Swarm of Miniature Vibration-Driven Robots in a Confined Arena](https://arxiv.org/abs/2610.35582)
中文标题：在密闭竞技场中对一群微型振动驱动机器人进行分布式预测植绒
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [TP-JSCC: Efficient Token Pruning and Joint Source-Channel Coding for LVLMs-based 3D-VQA in Cloud-Edge Collaboration](https://arxiv.org/abs/2610.35489)
中文标题：TP-JSCC：Efficient Token Pruning 与 Joint Source-Channel Coding 面向 LVLMs-based 3D-VQA in Cloud-Edge Collaboration
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [RepoTrace: Improving Requirement Tracing in Multi-Round Agent Interactions](https://arxiv.org/abs/2610.35333)
中文标题：RepoTrace ：改进多轮代理交互中的需求跟踪
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Safe by Benchmark, Unsafe in Practice: Lessons from 1331 Child-Related AI Incidents](https://arxiv.org/abs/2610.34705)
中文标题：Safe by 基准，Unsafe in Practice：Lessons 来自 1331 Child-Related AI Incidents
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MatAnyone-E: Sparse Memory Propagation for Efficient High-Resolution Video Matting](https://arxiv.org/abs/2610.35724)
中文标题：MatAnyone-E：Sparse Memory Propagation 面向 Efficient High-Resolution Video Matting
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Constrained Decoding: Harmful or Beneficial? Revisiting Its Impact on LLM Performance](https://arxiv.org/abs/2610.35328)
中文标题：约束解码：有害还是有益？重新审视其对LLM绩效的影响
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Identities, Not Pairs: Distribution-Free False-Accept Control for Embedding-Based Verification](https://arxiv.org/abs/2610.35277)
中文标题：身份，而不是配对：基于嵌入式验证的无分布虚假接受控制
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MechAlign: Evaluating Semantic Alignment at the Project Level in Mathematical Formalization](https://arxiv.org/abs/2610.35269)
中文标题：MechAlign ：在数学形式化中评估项目层面的语义对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [MuSID-KD: Multigranularity Knowledge Distillation for Generative Recommendation with Semantic IDs](https://arxiv.org/abs/2610.35218)
中文标题：MuSID-KD ：使用语义ID生成推荐的多粒度知识蒸馏
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [SimPOTrans: Self-Adaptation for Offline-to-Simultaneous Speech Translation via Reinforcement Learning](https://arxiv.org/abs/2610.35042)
中文标题：SimPOTrans ：通过强化学习实现离线到同步语音翻译的自适应
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [SPARTA: A Sparse Ternary LLM Accelerator with Adaptive Attention and Unified Datapath for Long-Context Edge Inference](https://arxiv.org/abs/2610.34824)
中文标题：SPARTA ：具有自适应注意力和用于长上下文边缘推理的统一数据路径的稀疏三元LLM加速器
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Position Matters More Than Channel: Talking a Language Model Out of a Correct Answer](https://arxiv.org/abs/2610.34809)
中文标题：定位比渠道更重要：从正确答案中说出一个语言模型
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [TimeWorld: Towards Action-Conditioned Multimodal World Models for Time Series Forecasting](https://arxiv.org/abs/2610.34797)
中文标题：TimeWorld：Towards Action-Conditioned Multimodal 世界模型 面向 Time Series Forecasting
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [ToDoPro: Faster and Better Reference-Based Generation: Early Token Reduction via Downsampled Self-Probing](https://arxiv.org/abs/2610.34782)
中文标题：ToDoPro ：更快、更好的基于参考的生成：通过降采样自探测进行早期代币减少
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Scope-Gap Injection: Exploiting Evaluator Channel Blind Spots in the OpenClaw Agent Security Competition](https://arxiv.org/abs/2610.34777)
中文标题：Scope-Gap注入：利用OpenClaw Agent安全竞争中的评估者渠道盲点
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [The Right Fact, the Wrong Decision: SciValidityBench for Scientific Agent Memory](https://arxiv.org/abs/2610.34767)
中文标题：Right Fact，the Wrong Decision：SciValidityBench 面向 Scientific Agent Memory
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware](https://arxiv.org/abs/2610.34717)
中文标题：VLA-HWBench ： VLA模型在边缘硬件上运行时的时间
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling](https://arxiv.org/abs/2610.35866)
中文标题：自动研究竞技场：语言建模中的基准测试和推进自动研究
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [OSWAM: An Effective World Action Model with One-Step Action Generation](https://arxiv.org/abs/2610.35850)
中文标题：OSWAM ：具有一步动作生成的有效世界动作模式
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [MedVTok: A General-Purpose Medical Visual Tokenizer](https://arxiv.org/abs/2610.35842)
中文标题：MedVTok ：通用医学视觉标记器
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
