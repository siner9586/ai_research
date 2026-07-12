---
title: "提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险"
date: "2026-07-13"
target_date: "2026-07-11"
actual_date: "2026-07-09"
fallback_from: "2026-07-11"
lang: "zh"
slug: "2026-07-13-a-safety-oriented-hypothetico-deductive-framework-for"
summary: "今天主要跟进：提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险。"
tags: ["agents", "data-engineering", "evaluation", "rag", "reasoning", "safety", "speech-audio", "systems", "training", "video-generation", "vision-generation"]
topics: ["agents", "data-engineering", "evaluation", "rag", "reasoning", "safety", "speech-audio", "systems", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-07-13-a-safety-oriented-hypothetico-deductive-framework-for-sources/"
generated_at: "2026-07-12T22:04:44.650289+00:00"
page_type: "brief"
candidate_count: 291
featured_count: 6
mentions_count: 20
featured_paper_titles: ["A safety-oriented hypothetico-deductive framework for AI-assisted differential diagnosis", "From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents", "Structured Pruning of Large Language Models via Power Transformation and Sign-Preserving Score Aggregation with Adaptive Feature Retention", "Beware What You Autocomplete: Forensic Attribution of Backdoored Code Completions", "LTM: Large-scale Terrain Model for Wildfire-prone Landscapes", "UltraX: Refining Pre-Training Data at Scale with Adaptive Programmatic Editing"]
featured_paper_urls: ["https://arxiv.org/abs/2607.08038", "https://arxiv.org/abs/2607.08028", "https://arxiv.org/abs/2607.08027", "https://arxiv.org/abs/2607.08011", "https://arxiv.org/abs/2607.08711", "https://arxiv.org/abs/2607.08646"]
featured_paper_titles_zh: ["一种safety-oriented hypothetico-deductive 框架 面向 AI-assisted differential diagnosis", "从提示到合同：可审计企业LLM代理的线束工程", "通过自适应特征保留的权力转换和符号保留分数聚合对大型语言模型进行结构化修剪", "小心您自动完成的内容：后门代码完成的取证归因", "LTM：Large-scale Terrain Model 面向 Wildfire-prone Landscapes", "UltraX ：使用自适应编程编辑大规模优化预训练数据"]
---

# 提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险

## 今天最值得跟进的方向

今天的高分论文主要指向：提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>A safety-oriented hypothetico-deductive framework for AI-assisted differential diagnosis (Fan Ma, Mauro Giuffrè, Donald Wright, Kent McCann, Mark Iscoe, Lingfei Qian, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.08038">2607.08038</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.08038">PDF</a></p>

中文标题：一种safety-oriented hypothetico-deductive 框架 面向 AI-assisted differential diagnosis

信号显示：诊断错误是患者安全的主要威胁，但目前的大语言模型（ LLM ）系统通常将诊断视为一次性预测任务，缺乏针对错过的高风险替代方案的保障措施或对其推理的严格验证。关键词：workflow、retrieval、safety、evaluation。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents (Joongho Ahn, Moonsoo Kim)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.08028">2607.08028</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.08028">PDF</a></p>

中文标题：从提示到合同：可审计企业LLM代理的线束工程

信号显示：企业大语言模型（ LLM ）应用程序通常以原型开始，其行为由提示和检索上下文承载。关键词：agent、retrieval、safety、code。代码/数据可用性需查看原文确认。

### 3. 识别并缓解模型安全、越狱和对齐风险

<p class="paper-meta-line"><span>Structured Pruning of Large Language Models via Power Transformation and Sign-Preserving Score Aggregation with Adaptive Feature Retention (Ryota Kobayashi, Tsubasa Hirakawa, Takayoshi Yamashita, Hironobu Fujiyoshi, Yasunori Ishii, Tomoyuki Okuno, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.08027">2607.08027</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.08027">PDF</a></p>

中文标题：通过自适应特征保留的权力转换和符号保留分数聚合对大型语言模型进行结构化修剪

信号显示：本文提出了一种改进的大语言模型（ LLM ）结构化修剪方法，该方法解决了将自适应特征保留（ AFR ） （一种非结构化修剪技术）适应结构化修剪的关键挑战。关键词：inference、serving、alignment、systems。代码/数据可用性需查看原文确认。

### 4. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Beware What You Autocomplete: Forensic Attribution of Backdoored Code Completions (Anjun Gao, Yueyang Quan, Zhuqing Liu, Minghong Fang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.08011">2607.08011</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.08011">PDF</a></p>

中文标题：小心您自动完成的内容：后门代码完成的取证归因

信号显示：大语言模型支持强大的代码完成系统，通过预测后续代码行来帮助开发人员。关键词：deployment、evaluation、code、fine-tuning。代码/数据可用性需查看原文确认。

### 5. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>LTM: Large-scale Terrain Model for Wildfire-prone Landscapes (Xiao Fu, Yue Hu, Meida Chen, Peter Anthony Beerel, Barath Raghavan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.08711">2607.08711</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.08711">PDF</a></p>

中文标题：LTM：Large-scale Terrain Model 面向 Wildfire-prone Landscapes

信号显示：在评估野火危险时，准确的3D地形图对于应急响应至关重要。关键词：rag、alignment、evaluation、eval。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>UltraX: Refining Pre-Training Data at Scale with Adaptive Programmatic Editing (Xinlong Zhao, Dongsheng Liu, Hengyu Zhao, Zixuan Fu, Zheng Wang, Jie Cai, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.08646">2607.08646</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.08646">PDF</a></p>

中文标题：UltraX ：使用自适应编程编辑大规模优化预训练数据

信号显示：随着可用的训练数据接近其物理极限，缩放定律的收益已开始减少。关键词：rag、inference、alignment、data。代码/数据可用性需查看原文确认。

## 其他值得关注
- [It Takes Few to TANGO: A Quantized Distributed Model for Binaural Speech Enhancement](https://arxiv.org/abs/2607.08645)
中文标题：探戈很少：双耳语音增强的量化分布式模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [BiSCo-LLM: Lookup-Free Binary Spherical Coding for Extreme Low-Bit Large Language Model Compression](https://arxiv.org/abs/2607.08643)
中文标题：BiSCo-LLM：Lookup-Free Binary Spherical Coding 面向 Extreme Low-Bit Large Language Model Compression
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ImputeViz: A Visual Analytics Dashboard for Diagnosing Missing Data and Comparing Imputation Methods](https://arxiv.org/abs/2607.08579)
中文标题：ImputeViz：A Visual Analytics Dashboard 面向 Diagnosing Missing Data 与 Comparing Imputation Methods
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [SHAP-Weighted Cross-Modal Expert Fusion for Emotion and Sentiment Recognition: Evidence and Limits](https://arxiv.org/abs/2607.08573)
中文标题：SHAP-Weighted Cross-Modal Expert Fusion 面向 Emotion 与 Sentiment Recognition：Evidence 与 Limits
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric Scheduling](https://arxiv.org/abs/2607.08565)
中文标题：SMetric ：重新思考LLM调度，为具有平衡会话中心调度的座席提供服务
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [VocaDet: Sample-Driven Open-Vocabulary Object Detection and Segmentation via Visual Tokenization and Vector Database Retrieval](https://arxiv.org/abs/2607.08541)
中文标题：VocaDet ：通过可视化标记和矢量数据库检索进行样本驱动的开放词汇表对象检测和分割
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Systematic Evaluation of Learning Rate Scheduling Strategies Across Heterogeneous Architectures](https://arxiv.org/abs/2607.08511)
中文标题：跨异构架构的学习率调度策略的系统评估
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [The Context Access Divide: Interaction-Level Architecture as a Complementary Dimension of Agentic Inequality](https://arxiv.org/abs/2607.08495)
中文标题：上下文访问鸿沟：交互级架构作为代理不平等的补充维度
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Ensemble Diversity Optimization for Subjective Supervision](https://arxiv.org/abs/2607.08493)
中文标题：主观监督的集合多样性优化
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MatBind: A Shared Embedding Space for Multimodal Materials Characterization](https://arxiv.org/abs/2607.08470)
中文标题：MatBind：A Shared Embedding Space 面向 Multimodal Materials Characterization
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [When Synthetic Speech Is All You Have: Better Call GRPO](https://arxiv.org/abs/2607.08409)
中文标题：当你只有合成语音时：更好地调用GRPO
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [On Exploring Input Resolution Scaling For Anytime LiDAR Object Detection](https://arxiv.org/abs/2607.08391)
中文标题：关于探索随时激光雷达物体检测的输入分辨率缩放
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [H3D: Benchmarking Unsupervised Text Hashing for Fine-Grained Document Deduplication](https://arxiv.org/abs/2607.08382)
中文标题：H3D ：对无监督文本哈希进行基准测试，以实现细粒度文档重复数据删除
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MobiDiff: Semantic-Aware Multi-Channel Discrete Diffusion for Human Mobility Data Generation](https://arxiv.org/abs/2607.08357)
中文标题：MobiDiff：Semantic-Aware Multi-Channel Discrete Diffusion 面向 Human Mobility Data Generation
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ArtMine: Discovering and Formalizing Artistic Processes](https://arxiv.org/abs/2607.08331)
中文标题：ArtMine：Discovering 与 Formalizing Artistic Processes
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [On the Design of Mixture-of-Experts for Dynamic Gaussian Splatting](https://arxiv.org/abs/2607.08250)
中文标题：动态高斯溅射混合专家的设计
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [TVTA: Trajectory-Aware Viseme-Guided Temporal Aggregation for Event-Based Lip Reading](https://arxiv.org/abs/2607.08236)
中文标题：TVTA：Trajectory-Aware Viseme-Guided Temporal Aggregation 面向 Event-Based Lip Reading
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [RhyMix: A Lightweight Adaptive Multi-Rhythm Network for Long-Term Time Series Forecasting](https://arxiv.org/abs/2607.08234)
中文标题：RhyMix：A Lightweight Adaptive Multi-Rhythm Network 面向 Long-Term Time Series Forecasting
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Multimodal 3D LUT Generation via StatLUT with Statistical Features for Photorealistic Style Transfer](https://arxiv.org/abs/2607.08227)
中文标题：通过StatLUT生成多模态3D LUT ，具有用于逼真风格转移的统计特征
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Benchmark Evaluation of Feredated Learning on Multi-organ Images](https://arxiv.org/abs/2607.08219)
中文标题：多器官图像上自由学习的基准评估
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
