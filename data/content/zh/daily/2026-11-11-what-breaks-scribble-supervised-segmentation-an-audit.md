---
title: "提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力"
date: "2026-11-11"
target_date: "2026-11-09"
actual_date: "2026-11-09"
fallback_from: ""
lang: "zh"
slug: "2026-11-11-what-breaks-scribble-supervised-segmentation-an-audit"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "robotics", "safety", "speech-audio", "training", "video-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "robotics", "safety", "speech-audio", "training", "video-generation"]
sources_page: "/zh/daily/2026-11-11-what-breaks-scribble-supervised-segmentation-an-audit-sources/"
generated_at: "2026-11-10T16:10:53.931761+00:00"
page_type: "brief"
candidate_count: 469
featured_count: 6
mentions_count: 20
featured_paper_titles: ["What Breaks Scribble-Supervised Segmentation? An Audit-Informed Benchmark for Scribble Annotation Robustness", "HyInv Technical Report", "Double Blind Evals: Resolving the Dual Confidentiality Dilemma in AI Safety Auditing", "WaveGen: Truly End-to-End Waveform Generation via Internal Spectral Trajectory Learning", "Correct First, Fast Second: What a Local 7B Code Model Can and Cannot Do for GPU Kernel Optimization", "HyPLM Technical Report"]
featured_paper_urls: ["https://arxiv.org/abs/2611.12674", "https://arxiv.org/abs/2611.11997", "https://arxiv.org/abs/2611.12604", "https://arxiv.org/abs/2611.12527", "https://arxiv.org/abs/2611.12079", "https://arxiv.org/abs/2611.12000"]
featured_paper_titles_zh: ["什么会破坏涂写监督分割？涂鸦注释鲁棒性的审计知情基准", "HyInv技术报告", "双盲Evals ：解决人工智能安全审计中的双重保密困境", "WaveGen ：通过内部频谱轨迹学习实现真正的端到端波形生成", "正确的第一，快速的第二：本地7B代码模型对GPU内核优化可以做什么和不能做什么", "HyPLM技术报告"]
---

# 提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>What Breaks Scribble-Supervised Segmentation? An Audit-Informed Benchmark for Scribble Annotation Robustness (Minheng Wu, Di Wen, Ruiping Liu, Junwei Zheng, Yufan Chen, Kailun Yang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.12674">2611.12674</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.12674">PDF</a></p>

中文标题：什么会破坏涂写监督分割？涂鸦注释鲁棒性的审计知情基准

信号显示：涂鸦监督分割通常使用固定注释集进行评估，对鲜明的语义和几何瑕疵的鲁棒性知之甚少。关键词：rag、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>HyInv Technical Report (Haowei Lin, Cai Zhou, Xiangxin Zhou)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.11997">2611.11997</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.11997">PDF</a></p>

中文标题：HyInv技术报告

信号显示：反向折叠为给定的蛋白质骨架设计氨基酸序列，筛选需要许多既多样又折叠良好的候选者。关键词：agent、rag、inference、benchmark。代码/数据可用性需查看原文确认。

### 3. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Double Blind Evals: Resolving the Dual Confidentiality Dilemma in AI Safety Auditing (Andrew Trask, Sol Messing, Vai Pahwa, Pegah Maham, Rene Kolga, Austin Frantz, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.12604">2611.12604</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.12604">PDF</a></p>

中文标题：双盲Evals ：解决人工智能安全审计中的双重保密困境

信号显示：人工智能安全评估通常涉及敏感提示和专有模型。关键词：inference、safety、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>WaveGen: Truly End-to-End Waveform Generation via Internal Spectral Trajectory Learning (Sang-Hoon Lee, Ha-Yeong Choi)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.12527">2611.12527</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.12527">PDF</a></p>

中文标题：WaveGen ：通过内部频谱轨迹学习实现真正的端到端波形生成

信号显示：这项工作提出了WaveGen ，这是一个完全基于端到端扩散的基于光谱强迫的文本到波形框架，它在单个模型中共同学习内部光谱轨迹和目标波形轨迹，从而实现直接的端到端文本-。关键词：alignment、benchmark、code、open-source。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Correct First, Fast Second: What a Local 7B Code Model Can and Cannot Do for GPU Kernel Optimization (Jui-Chien Tsou, Po-Yi Wu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.12079">2611.12079</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.12079">PDF</a></p>

中文标题：正确的第一，快速的第二：本地7B代码模型对GPU内核优化可以做什么和不能做什么

信号显示：我们研究了围绕固定的、本地托管的7B参数代码模型（ Qwen2.5-Coder-7B-Instruct ）的交互策略对其用自定义CUDA内核替换PyTorch运算符的能力有多大影响。关键词：agent、rag、retrieval、evaluation。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>HyPLM Technical Report (Haowei Lin, Cai Zhou, Xiangxin Zhou)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.12000">2611.12000</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.12000">PDF</a></p>

中文标题：HyPLM技术报告

信号显示：蛋白质语言模型（ PLM ）是用于变异效应预测、蛋白质注释和设计的标准工具，但训练和服务它们所需的计算量不断增长。关键词：agent、inference、evaluation、code。代码/数据可用性需查看原文确认。

## 其他值得关注
- [MUTE: Multi-Level Alignment Uncoupling Against Talking-Head Exploitation for Voice Protection](https://arxiv.org/abs/2611.11989)
中文标题：静音：针对语音保护的对话头剥削的多级对齐解耦
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [AnyBreak: Towards Jailbreaking Any T2I Model for Any Concept](https://arxiv.org/abs/2611.11980)
中文标题：AnyBreak：Towards Jailbreaking Any T2I Model 面向 Any Concept
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Proactive Dimension-Adaptive Denoising for Graph Collaborative Filtering via Representation Coherence](https://arxiv.org/abs/2611.11801)
中文标题：通过表示一致性进行图协同过滤的主动维度自适应去噪
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Where Does Alignment Emerge and What Does It Mean? A Closer Look at the Platonic Representation Hypothesis](https://arxiv.org/abs/2611.12869)
中文标题：一致性在哪里出现，这意味着什么？仔细研究柏拉图式表示假设
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Agent4Crypto: A Dual-Reflective and Market-Feedback-Aligned LLM-Based Multi-Agent System for Cryptocurrency Trading](https://arxiv.org/abs/2611.12269)
中文标题：Agent4Crypto ：用于加密货币交易的基于LLM的双反射和市场反馈的多代理系统
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [CADMA: Capacity-Aware Coverage Decomposition for Generative Model Assessment](https://arxiv.org/abs/2611.12243)
中文标题：CADMA：Capacity-Aware Coverage Decomposition 面向 Generative Model 评估
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Adaptive Entropy-Sparing for Efficient Reasoning](https://arxiv.org/abs/2611.11901)
中文标题：自适应熵保留实现高效推理
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [ARMOR: Adaptive Curriculum Meta-Learning for Noise-Robust RAG Reasoning](https://arxiv.org/abs/2611.11771)
中文标题：ARMOR：Adaptive Curriculum Meta-Learning 面向 Noise-Robust RAG Reasoning
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Safe Reinforcement Learning for Multi-Turn Clinical Agents: When Dense Rewards Beat Outcome Rewards](https://arxiv.org/abs/2611.12728)
中文标题：多转向临床代理的安全强化学习：当密集奖励超过结果奖励时
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [A local language model layered with rule-based and neural detectors for clinical text de-identification: an open-source toolkit and evaluation](https://arxiv.org/abs/2611.12709)
中文标题：基于规则和神经检测器的本地语言模型，用于临床文本去识别：开源工具包和评估
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [National-Scale Crop Type Mapping in Morocco Using Google AlphaEarth Foundations Embeddings and the Fields of the World Field Boundary Map](https://arxiv.org/abs/2611.12681)
中文标题：National-Scale Crop Type Mapping in Morocco 使用 Google AlphaEarth Foundations Embeddings 与 the Fields of the World Field Boundary Map
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [MoSTE: Mixture of Spatio-Temporal Experts for Deepfake Detection in Videos](https://arxiv.org/abs/2611.12443)
中文标题：MoSTE：Mixture of Spatio-Temporal Experts 面向 Deepfake Detection in Videos
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [UniOMA: Unified Optimal-Transport Multi-Modal Structural Alignment for Robot Perception](https://arxiv.org/abs/2611.12351)
中文标题：UniOMA：Unified Optimal-Transport Multi-Modal Structural Alignment 面向 Robot Perception
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [TMT: Adapting CLIP to Infrared Imagery via Text-Derived Modality Knowledge Transfer](https://arxiv.org/abs/2611.12345)
中文标题：TMT ：通过文本衍生模态知识转移使CLIP适应红外图像
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Odds-Structured Distributional Regression for Interpretable Time-to-Event Prediction](https://arxiv.org/abs/2611.12268)
中文标题：用于可解释事件时间预测的赔率结构分布回归
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Embodied First Exam](https://arxiv.org/abs/2611.12177)
中文标题：体验式首次检查
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [GPU-Accelerated Non-Interactive Encrypted Neural Network Training with Batched Diagonal Packing](https://arxiv.org/abs/2611.12161)
中文标题：使用批量对角包装的GPU加速非交互式加密神经网络训练
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MIRIX-2.0: Multi-Agent Memory System](https://arxiv.org/abs/2611.12068)
中文标题：MIRIX-2.0 ：多Agent内存系统
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model](https://arxiv.org/abs/2611.11964)
中文标题：3R适配器：检索、重新布线和优化，以高效适应3D重建模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SpinSCI: Mask-Conditioned Spatial-Temporal Spin Transformer for Video Snapshot Compressive Imaging](https://arxiv.org/abs/2611.11753)
中文标题：SpinSCI：Mask-Conditioned Spatial-Temporal Spin Transformer 面向 Video Snapshot Compressive Imaging
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
