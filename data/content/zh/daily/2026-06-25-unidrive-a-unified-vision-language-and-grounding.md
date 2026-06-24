---
title: "提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性"
date: "2026-06-25"
target_date: "2026-06-23"
actual_date: "2026-06-23"
fallback_from: ""
lang: "zh"
slug: "2026-06-25-unidrive-a-unified-vision-language-and-grounding"
summary: "今天主要跟进：提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "systems", "training", "video-generation", "vision-generation"]
topics: ["agents", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "systems", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-06-25-unidrive-a-unified-vision-language-and-grounding-sources/"
generated_at: "2026-06-24T22:38:22.314175+00:00"
page_type: "brief"
candidate_count: 364
featured_count: 6
mentions_count: 20
featured_paper_titles: ["UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving", "AdversaBench: Automated LLM Red-Teaming with Multi-Judge Confirmation and Cross-Model Transferability", "UniTranslator: A Unified Multi-modal Framework for End-to-end In-Image Machine Translation", "Transformer-Based Language Models Across Domain Verticals: Architectures, Applications and Critical Assessment", "CANDLE: Character-level Arabic Noise Deduplication using Lightweight Encoder", "ASALT: Adaptive State Alignment for Lateral Transfer in Multi-agent Reinforcement Learning"]
featured_paper_urls: ["https://arxiv.org/abs/2606.24759", "https://arxiv.org/abs/2606.24589", "https://arxiv.org/abs/2606.24333", "https://arxiv.org/abs/2606.24331", "https://arxiv.org/abs/2606.24758", "https://arxiv.org/abs/2606.24601"]
featured_paper_titles_zh: ["UniDrive：A Unified Vision-Language 与 落地 框架 面向 Interpretable Risk Understanding in Autonomous Driving", "AdversaBench ：具有多法官确认和跨模型可转移性的自动LLM红队", "UniTranslator：A Unified Multi-modal 框架 面向 End-to-end In-Image Machine Translation", "Transformer-Based Language Models Across Domain Verticals：Architectures，Applications 与 Critical 评估", "CANDLE：Character-level Arabic Noise Deduplication 使用 Lightweight Encoder", "ASALT：Adaptive State Alignment 面向 Lateral Transfer in Multi-agent Reinforcement Learning"]
---

# 提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving (Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth, Stephen Law, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.24759">2606.24759</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.24759">PDF</a></p>

中文标题：UniDrive：A Unified Vision-Language 与 落地 框架 面向 Interpretable Risk Understanding in Autonomous Driving

信号显示：最近的多模态大语言模型（ MLLM ）在自动驾驶场景理解方面显示出强大的潜力，但现有方法仍面临着时间推理和空间精度之间的根本权衡。关键词：safety、benchmark、code、multimodal。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>AdversaBench: Automated LLM Red-Teaming with Multi-Judge Confirmation and Cross-Model Transferability (Khanak Khandelwal)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.24589">2606.24589</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.24589">PDF</a></p>

中文标题：AdversaBench ：具有多法官确认和跨模型可转移性的自动LLM红队

信号显示：扩展大语言模型的对抗性评估既需要一种生成硬输入的方法，也需要一种可靠的方法来确认由此产生的失败是真实的。关键词：tool use、rag、evaluation、code。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>UniTranslator: A Unified Multi-modal Framework for End-to-end In-Image Machine Translation (Jiahao Lyu, Pei Fu, Zhenhang Li, Shaojie Zhang, Jiahui Yang, Yu Zhou, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.24333">2606.24333</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.24333">PDF</a></p>

中文标题：UniTranslator：A Unified Multi-modal 框架 面向 End-to-end In-Image Machine Translation

信号显示：图像内机器翻译（ IIMT ）旨在翻译图像中的场景文本，并将翻译后的文本渲染回原始区域，同时保持整体视觉外观。关键词：rag、serving、alignment、benchmark。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Transformer-Based Language Models Across Domain Verticals: Architectures, Applications and Critical Assessment (Guruprakash J, Krithika L. B)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.24331">2606.24331</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.24331">PDF</a></p>

中文标题：Transformer-Based Language Models Across Domain Verticals：Architectures，Applications 与 Critical 评估

信号显示：基于Transformer的语言模型已成为自然语言处理的默认基础，新版本的速度使得从业者很难将持久的想法与增量公告的噪音分开。关键词：retrieval、deployment、alignment、benchmark。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>CANDLE: Character-level Arabic Noise Deduplication using Lightweight Encoder (Faris Alasmary, Taif Nono, Orjuwan Zaafarani, Kholood Al Tabash, Ahmad Ghannam, Anas Salamah, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.24758">2606.24758</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.24758">PDF</a></p>

中文标题：CANDLE：Character-level Arabic Noise Deduplication 使用 Lightweight Encoder

信号显示：处理文本中的重复字符可能很棘手，因为它们可以代表单词的正确拼写或社交媒体帖子中常见的非正式字符扩展。关键词：inference、alignment、benchmark、code。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>ASALT: Adaptive State Alignment for Lateral Transfer in Multi-agent Reinforcement Learning (Anurag Akula, Satheesh K. Perepu, Abhishek Sarkar, Kaushik Dey)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.24601">2606.24601</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.24601">PDF</a></p>

中文标题：ASALT：Adaptive State Alignment 面向 Lateral Transfer in Multi-agent Reinforcement Learning

信号显示：多代理强化学习(MARL)解决了培训多个代理以实现协作、竞争或混合目标的问题。关键词：agent、alignment、benchmark、agents。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Are We Ready For An Agent-Native Memory System?](https://arxiv.org/abs/2606.24775)
中文标题：Are We Ready 面向 An Agent-Native Memory System?
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Evaluating the Interpretability of Sparse Autoencoders with Concept Annotations](https://arxiv.org/abs/2606.24716)
中文标题：使用概念注释评估稀疏自动编码器的可解释性
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Privacy-Preserving RAG via Multi-Agent Semantic Rewriting: Achieving Confidentiality Without Compromising Contextual Fidelity](https://arxiv.org/abs/2606.24623)
中文标题：通过多代理语义重写保护隐私的RAG ：在不损害上下文保真度的情况下实现机密性
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Boosting Text-Driven Video Segmentation via Geometry-Aware Distillation](https://arxiv.org/abs/2606.24464)
中文标题：通过几何感知蒸馏提升文本驱动的视频分割
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [REDI-Match: Rotation-Equivariant Distillation for Efficient and Robust Dense Matching](https://arxiv.org/abs/2606.24330)
中文标题：REDI-Match：Rotation-Equivariant Distillation 面向 Efficient 与 Robust Dense Matching
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Probing the Misaligned Thinking Process of Language Models](https://arxiv.org/abs/2606.24251)
中文标题：探究语言模型的不一致思维过程
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Towards Fast and Effective Long Video Understanding of Multimodal Large Language Models via Adaptive Quasi-Gaussian Sampling](https://arxiv.org/abs/2606.24187)
中文标题：通过自适应准高斯采样实现对多模态大型语言模型的快速有效的长视频理解
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [DramaDirector: Geometry-Guided Short Drama Generation](https://arxiv.org/abs/2606.24107)
中文标题：DramaDireCTor ：几何指导短剧生成
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Progressive Pixel-Neighborhood Deformable Cross-Attention for Multispectral Object Detection](https://arxiv.org/abs/2606.24092)
中文标题：用于多光谱目标检测的渐进像素邻域可变形交叉注意
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](https://arxiv.org/abs/2606.24874)
中文标题：FLUX3D ：具有扩散对准稀疏表示的高保真3D高斯生成
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [BioMedVR: Confusion-Aware Mixture-of-Prompt Experts for Biomedical Visual Reprogramming](https://arxiv.org/abs/2606.24740)
中文标题：BioMedVR：Confusion-Aware Mixture-of-Prompt Experts 面向 Biomedical Visual Reprogramming
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning](https://arxiv.org/abs/2606.24570)
中文标题：Jolia：Concept-Level Vision-Language Alignment 面向 3D CT Contrastive Learning
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [UOL@IDEM at BEA 2026 Shared Task 1: Neural Fusion and Feature-Rich Modeling for L1-Aware Vocabulary Difficulty Prediction](https://arxiv.org/abs/2606.24501)
中文标题：UOL@IDEM at BEA 2026 Shared Task 1：Neural Fusion 与 Feature-Rich Modeling 面向 L1-Aware Vocabulary Difficulty Prediction
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [VistaRef: Boosting Visual Spatial Orientation Awareness for Pointing-to-Object Detection](https://arxiv.org/abs/2606.24498)
中文标题：VistaRef：Boosting Visual Spatial Orientation Awareness 面向 Pointing-to-Object Detection
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Advancing WordArt-Oriented Scene Text Recognition: Datasets and Methods](https://arxiv.org/abs/2606.24484)
中文标题：推进面向艺术的场景文本识别：数据集和方法
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [TrOCR for Medieval HTR: A Systematic Ablation Study with Cross-Dataset Validation](https://arxiv.org/abs/2606.24302)
中文标题：中世纪HTR的TrOCR ：一项具有交叉数据集验证的系统消融研究
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [ActiveScope: Actively Seeking and Correcting Perception for MLLMs](https://arxiv.org/abs/2606.24292)
中文标题：ActiveScope：Actively Seeking 与 Correcting Perception 面向 MLLMs
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Navigating User Behavior toward Personalized Multimodal Generation](https://arxiv.org/abs/2606.24196)
中文标题：引导用户行为转向个性化多模式生成
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Zero-Shot Test-Time Canonicalization using Out-of-Distribution Scoring](https://arxiv.org/abs/2606.24178)
中文标题：使用分布外评分进行零拍测试时间规范化
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Dual-Branch Cross-Projection Debiasing through Diffusion-based Disentanglement](https://arxiv.org/abs/2606.24161)
中文标题：通过基于扩散的解缠结实现双分支交叉投影去偏
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
