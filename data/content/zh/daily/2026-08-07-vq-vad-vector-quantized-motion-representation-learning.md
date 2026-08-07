---
title: "提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-08-07"
target_date: "2026-08-05"
actual_date: "2026-08-05"
fallback_from: ""
lang: "zh"
slug: "2026-08-07-vq-vad-vector-quantized-motion-representation-learning"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "safety", "training", "vision-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "safety", "training", "vision-generation"]
sources_page: "/zh/daily/2026-08-07-vq-vad-vector-quantized-motion-representation-learning-sources/"
generated_at: "2026-08-07T01:30:35.194764+00:00"
page_type: "brief"
candidate_count: 479
featured_count: 6
mentions_count: 20
featured_paper_titles: ["VQ-VAD: Vector-quantized Motion Representation Learning for Human-centric Video Anomaly Detection", "Unified Planning-Learning Framework for Robust UUV Navigation Under Partial Observability", "Guideline-as-Oracle: Zero-Annotation Training of an Ophthalmic Telephone Triage Agent", "Toward Integrating Adaptive Experience Replay and Online Uncertainty Estimation in Safe Actor-Critic Optimal Control", "RepoProbe: Benchmarking Architecture-Aware Repository Comprehension with Checklists", "Dense Metric Depth Completion from Sparse Direct Time-of-Flight Sensors"]
featured_paper_urls: ["https://arxiv.org/abs/2608.05069", "https://arxiv.org/abs/2608.05365", "https://arxiv.org/abs/2608.04772", "https://arxiv.org/abs/2608.04732", "https://arxiv.org/abs/2608.04783", "https://arxiv.org/abs/2608.04737"]
featured_paper_titles_zh: ["VQ-VAD：Vector-quantized Motion Representation Learning 面向 Human-centric Video Anomaly Detection", "Unified Planning-Learning 框架 面向 Robust UUV Navigation Under Partial Observability", "Guideline-as-Oracle：Zero-Annotation Training of an Ophthalmic Telephone Triage Agent", "将适应性体验重播和在线不确定性估计集成到安全的演员-批评者最佳控制中", "RepoProbe ：使用清单对架构感知存储库进行基准测试", "稀疏直接飞行时间传感器的密集度量深度完成"]
---

# 提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>VQ-VAD: Vector-quantized Motion Representation Learning for Human-centric Video Anomaly Detection (Narges Rashvand, Ghazal Alinezhad Noghre, Shanle Yao, Gabriel Maldonado, Hamed Tabkhi)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.05069">2608.05069</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.05069">PDF</a></p>

中文标题：VQ-VAD：Vector-quantized Motion Representation Learning 面向 Human-centric Video Anomaly Detection

信号显示：视频异常检测（ VAD ）本质上具有挑战性，因为异常很少，监控镜头具有很大的视觉可变性，包括光线、视角和人体外观的变化。关键词：evaluation、benchmark、code、eval。代码/数据可用性需查看原文确认。

### 2. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Unified Planning-Learning Framework for Robust UUV Navigation Under Partial Observability (Md Ether Deowan, Eleni Kelasidi)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.05365">2608.05365</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.05365">PDF</a></p>

中文标题：Unified Planning-Learning 框架 面向 Robust UUV Navigation Under Partial Observability

信号显示：本文提出了动态水下环境中无人水下航行器（ UUV ）导航的纯观测自主框架，该框架集成了持续占用映射、全球清理感知规划和风险感知本地控制。关键词：safety、evaluation、benchmark、training。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Guideline-as-Oracle: Zero-Annotation Training of an Ophthalmic Telephone Triage Agent (Chenyu Wang, Yi Liu, Baoqing Li, Min Tu, Diping Song)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.04772">2608.04772</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.04772">PDF</a></p>

中文标题：Guideline-as-Oracle：Zero-Annotation Training of an Ophthalmic Telephone Triage Agent

信号显示：由于专家对话注释成本高昂且临床对话受隐私限制，因此很难对多轮医疗代理进行规模化监督。关键词：agent、inference、serving、safety。代码/数据可用性需查看原文确认。

### 4. 识别并缓解模型安全、越狱和对齐风险

<p class="paper-meta-line"><span>Toward Integrating Adaptive Experience Replay and Online Uncertainty Estimation in Safe Actor-Critic Optimal Control (Mahshad Rastegarmoghaddam, Davoud Nikkhouy, Shima Samadzadeh)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.04732">2608.04732</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.04732">PDF</a></p>

中文标题：将适应性体验重播和在线不确定性估计集成到安全的演员-批评者最佳控制中

信号显示：安全的行为者-批评者控制通常将屏障过滤、不确定性估计和体验重放视为单独的模块，即使每个模块都会更改用于学习和控制的数据。关键词：safety、evaluation、benchmark、post-training。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>RepoProbe: Benchmarking Architecture-Aware Repository Comprehension with Checklists (Yuexi Yang, Alyssa Wu, Ji Luo, Richeng Xuan, Zhichao Hu, Yuhong Liu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.04783">2608.04783</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.04783">PDF</a></p>

中文标题：RepoProbe ：使用清单对架构感知存储库进行基准测试

信号显示：将大语言模型（ LLM ）集成到软件工程中，已将重点从函数级生成转移到存储库规模的辅助。关键词：alignment、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Dense Metric Depth Completion from Sparse Direct Time-of-Flight Sensors (Hakyeong Kim, Ruicheng Wang, Chengtang Yao, Jiaolong Yang, Min H. Kim)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.04737">2608.04737</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.04737">PDF</a></p>

中文标题：稀疏直接飞行时间传感器的密集度量深度完成

信号显示：直接飞行时间（ dToF ）传感器提供高度精确的度量深度，并且在具有挑战性的实际条件下比间接ToF系统更坚固。关键词：code、robotics、synthetic data、open-source。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning](https://arxiv.org/abs/2608.05139)
中文标题：迈向技能本土LLM ：用于基准测试和培训长远推理的技能熵
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings](https://arxiv.org/abs/2608.04735)
中文标题：在隐性影响设置中，思维链监控可能不可靠
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [A GitOps-Driven Annotation Catalog for Fully Automatic Railway Operations](https://arxiv.org/abs/2608.04724)
中文标题：一种GitOps-Driven Annotation Catalog 面向 Fully Automatic Railway Operations
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CSGen: A Multi-Domain Curvilinear Structure Generation Model via Hierarchical Multimodal Diffusion](https://arxiv.org/abs/2608.04655)
中文标题：CSGen ：基于分层多模态扩散的多域曲线结构生成模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [DAC-Pose: Dual-Agent Collaborative Framework for Pose-Guided Human Generation](https://arxiv.org/abs/2608.04622)
中文标题：DAC-Pose：Dual-Agent Collaborative 框架 面向 Pose-Guided Human Generation
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents](https://arxiv.org/abs/2608.04574)
中文标题：当记忆说谎时： VLM代理中空间记忆失效的实证研究
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Not All Redundant Tokens Are Alike: Analyzing Visual Token Pruning through Token Roles](https://arxiv.org/abs/2608.04483)
中文标题：并非所有冗余令牌都是一样的：通过令牌角色分析可视化令牌修剪
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [MCHA: A Memory-Centric Hierarchical Architecture for Parallel-Sequential Computing](https://arxiv.org/abs/2608.04443)
中文标题：MCHA：A Memory-Centric Hierarchical Architecture 面向 Parallel-Sequential Computing
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [A Foundational EDM2-Based Generative Model for High-Resolution Synthetic Fetal Ultrasound Imaging from Open Datasets](https://arxiv.org/abs/2608.05471)
中文标题：一种Foundational EDM2-Based Generative Model 面向 High-Resolution Synthetic Fetal Ultrasound Imaging 来自 Open Datasets
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Robust Context-Aware Detection of Malicious Instructions in Text](https://arxiv.org/abs/2608.05430)
中文标题：强大的上下文感知检测功能，可检测文本中的恶意指令
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Teaching Nemotron Greek: Mining a Corpus, Adapting Retrieval, and Grounding Generation for Modern Greek across Specialist Domains](https://arxiv.org/abs/2608.05138)
中文标题：Teaching Nemotron Greek：Mining a Corpus，Adapting Retrieval，与 落地 Generation 面向 Modern Greek across Specialist Domains
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [RepairFormer: Automated Repair of Structured Inputs Using Transformers](https://arxiv.org/abs/2608.05060)
中文标题：RepairFormer：Automated Repair of Structured Inputs 使用 Transformers
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Gradient Immunity: Null-Space Resistance to Malicious Fine-Tuning](https://arxiv.org/abs/2608.05045)
中文标题：梯度免疫：无效空间抵抗恶意微调
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Short-term load forecasting under EU-AI Act Requirements in Safety-Critical Environments: Results from a 41-day live challenge on the aggregated German transmission-grid load](https://arxiv.org/abs/2608.05018)
中文标题：欧盟-人工智能法案要求下的安全关键环境短期负荷预测：德国输电网总负荷41天实时挑战的结果
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [A 6G Integrated Sensing and Communication Framework for Railway Intrusion Detection and Collision Prediction](https://arxiv.org/abs/2608.04710)
中文标题：用于铁路入侵检测和碰撞预测的6G集成感知和通信框架
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [The First EgoCross Challenge at EgoVis 2026: Cross-Domain Egocentric Video Question Answering](https://arxiv.org/abs/2608.04589)
中文标题：EgoVis 2026的首个EgoCross挑战：跨领域以自我为中心的视频问答
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [GUARD: Grounding Uncertainty and Ablation-Based Risk Detection for Diffusion-Based VLAs](https://arxiv.org/abs/2608.04510)
中文标题：GUARD：落地 Uncertainty 与 Ablation-Based Risk Detection 面向 Diffusion-Based VLAs
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Architectural Implications of Agentic AI Workflows](https://arxiv.org/abs/2608.04458)
中文标题：Agentic AI工作流程的架构影响
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [OmniRouting: A Semantic-Coupled Multimodal Benchmark for Constraint-Aware Spatial Reasoning in PCB Routing](https://arxiv.org/abs/2608.04434)
中文标题：OmniRouting：A Semantic-Coupled Multimodal 基准 面向 Constraint-Aware Spatial Reasoning in PCB Routing
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Predict, Then Retrieve: Cross-Instance Future-State Retrieval from Video Prefixes](https://arxiv.org/abs/2608.04426)
中文标题：预测，然后检索：从视频前缀进行跨实例未来状态检索
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
