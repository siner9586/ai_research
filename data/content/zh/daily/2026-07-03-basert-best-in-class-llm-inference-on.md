---
title: "提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-07-03"
target_date: "2026-07-01"
actual_date: "2026-07-01"
fallback_from: ""
lang: "zh"
slug: "2026-07-03-basert-best-in-class-llm-inference-on"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "rag", "reasoning", "safety", "systems", "training", "video-generation", "vision-generation"]
topics: ["agents", "code", "evaluation", "rag", "reasoning", "safety", "systems", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-07-03-basert-best-in-class-llm-inference-on-sources/"
generated_at: "2026-07-02T22:17:31.149923+00:00"
page_type: "brief"
candidate_count: 393
featured_count: 6
mentions_count: 20
featured_paper_titles: ["BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal", "The Illusion of High Utility in Safety Alignment of Text-to-Image Diffusion Models", "Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?", "From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion Planning", "Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs", "EquiSteer: Cross-Attention Steering Towards a Fairer Text-Guided Image Generation"]
featured_paper_urls: ["https://arxiv.org/abs/2607.00501", "https://arxiv.org/abs/2607.00402", "https://arxiv.org/abs/2607.01211", "https://arxiv.org/abs/2607.00776", "https://arxiv.org/abs/2607.00555", "https://arxiv.org/abs/2607.01147"]
featured_paper_titles_zh: ["BaseRT ：通过Native Metal对Apple Silicon进行一流的LLM推断", "高实用性在文本图像扩散模型安全对齐中的错觉", "性能优化基准是否可靠地衡量编码代理？", "从预测不确定性到安全运动规划的适形距离场", "Rise 来自 The Ashes：基于 LLM 的 Static Analysis 面向 Deep Learning 框架 Bugs", "EquiSteer ：交叉注意力转向更公平的文本引导图像生成"]
---

# 提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal (Prabod Rathnayaka, Fabian Waschkowski, Lukas Wesemann)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.00501">2607.00501</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.00501">PDF</a></p>

中文标题：BaseRT ：通过Native Metal对Apple Silicon进行一流的LLM推断

信号显示：我们展示了BaseRT ，这是Apple Silicon上大语言模型(LLM)的原生金属推理运行时，并报告了迄今为止该硬件上最高的推理吞吐量。关键词：inference、deployment、latency、code。代码/数据可用性需查看原文确认。

### 2. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>The Illusion of High Utility in Safety Alignment of Text-to-Image Diffusion Models (Adeel Yousaf, Soumik Ghosh, James Beetham, Amrit Singh Bedi, Mubarak Shah)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.00402">2607.00402</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.00402">PDF</a></p>

中文标题：高实用性在文本图像扩散模型安全对齐中的错觉

信号显示：文本到图像（ T2I ）扩散模型的安全对齐旨在抑制有害世代，同时保持对良性提示的实用性。关键词：serving、alignment、safety、evaluation。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents? (Zhi Chen, Zhensu Sun, Yuling Shi, David Lo, Lingxiao Jiang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.01211">2607.01211</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.01211">PDF</a></p>

中文标题：性能优化基准是否可靠地衡量编码代理？

信号显示：存储库级性能优化基准（如GSO、SWE-Perf和SWE-效率）通过将补丁应用于真实存储库并将运行时间与未优化的基线和官方参考补丁进行比较来评估编码代理。关键词：agent、rag、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion Planning (Jaeuk Shin, Yoonseok Ra, Insoon Yang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.00776">2607.00776</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.00776">PDF</a></p>

中文标题：从预测不确定性到安全运动规划的适形距离场

信号显示：动态环境中的安全运动规划需要在不牺牲实时性能的情况下推理预测障碍物运动的不确定性。关键词：rag、safety、benchmark、planning。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs (Shaoyu Yang, Haifeng Lin, Chunrong Fang, Xiang Chen, Wei Cheng, Jiawei Liu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.00555">2607.00555</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.00555">PDF</a></p>

中文标题：Rise 来自 The Ashes：基于 LLM 的 Static Analysis 面向 Deep Learning 框架 Bugs

信号显示：深度学习（ DL ）框架是关键的人工智能基础设施，通常会隐藏具有严重安全影响的漏洞。关键词：agent、workflow、rag、retrieval。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>EquiSteer: Cross-Attention Steering Towards a Fairer Text-Guided Image Generation (Tatiana Gaintseva, Akshit Achara, Gregory Slabaugh, Jiankang Deng, Ismail Elezi)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.01147">2607.01147</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.01147">PDF</a></p>

中文标题：EquiSteer ：交叉注意力转向更公平的文本引导图像生成

信号显示：文本到图像的扩散模型为日常创意任务提供了动力，但它们仍然在训练数据中重现了人口统计学偏差。关键词：rag、inference、alignment、code。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Seahorse: A Unified Benchmarking Framework for Spatiotemporal Event Modeling](https://arxiv.org/abs/2607.01022)
中文标题：Seahorse：A Unified 基准ing 框架 面向 Spatiotemporal Event Modeling
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Human-Machine Collaboration on Generative Meta-Learning: Model and Algorithm](https://arxiv.org/abs/2607.00926)
中文标题：生成元学习中的人机协作：模型和算法
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ClinRAG-GRAPH: Clinical-prior Retrieval-Augmented Graph Model with Domain Adversarial Learning for Breast pCR Prediction](https://arxiv.org/abs/2607.00798)
中文标题：ClinRAG-GRAPH ：乳腺pCR预测领域对抗学习的临床先验检索-增强图模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Phantom References: Hallucinated Citations That Survive Peer Review at Top-Tier Conferences](https://arxiv.org/abs/2607.00738)
中文标题：幻影引用：在顶级会议上经得起同行评审的幻觉引用
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [From Structural Equation Modelling to Double Machine Learning: Robustness Analysis for Survey-Based Research](https://arxiv.org/abs/2607.00512)
中文标题：从结构方程建模到双机学习：基于调查研究的鲁棒性分析
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [PAPA: Online Personalized Active Preference Alignment](https://arxiv.org/abs/2607.00486)
中文标题：PAPA ：在线个性化主动偏好调整
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Beyond the Prompt: Jailbreaking Function-Calling LLMs via Simulated Moderation Traces](https://arxiv.org/abs/2607.00481)
中文标题：超越提示：通过模拟审核跟踪越狱功能调用LLM
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Learning Gait-Aware Quadruped Locomotion with Temporal Logic Specifications](https://arxiv.org/abs/2607.00442)
中文标题：使用时间逻辑规格学习步态感知四足运动
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [LIST3R: Long-sequence Instance-aware 3D Reconstruction](https://arxiv.org/abs/2607.00375)
中文标题：LIST3R ：长序列实例感知3D重建
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SoK: Attack and Defense Landscape of Mobile On-device AI Systems](https://arxiv.org/abs/2607.00362)
中文标题：SoK：Attack 与 Defense Landscape of Mobile On-device AI Systems
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Managed Autonomy at Runtime: Gear-Based Safety and Governance for Single- and Multi-Agent Cyber-Physical Systems](https://arxiv.org/abs/2607.00334)
中文标题：Managed Autonomy at Runtime：Gear-Based Safety 与 Governance 面向 Single- 与 Multi-Agent Cyber-Physical Systems
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Autonomous Scientific Discovery via Iterative Meta-Reflection](https://arxiv.org/abs/2607.01131)
中文标题：通过迭代元反射实现自主科学发现
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [MemSyco-Bench: Benchmarking Sycophancy in Agent Memory](https://arxiv.org/abs/2607.01071)
中文标题：MemSyco-Bench：基准ing Sycophancy in Agent Memory
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology](https://arxiv.org/abs/2607.01033)
中文标题：模式生物体彩票：模式生物体的可解释性很大程度上取决于培训方法
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Svarna: An Open Corpus Workbench for Modern Greek](https://arxiv.org/abs/2607.00970)
中文标题：Svarna：An Open Corpus Workbench 面向 Modern Greek
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Meta-Transfer Learning for mmWave Beam Alignment](https://arxiv.org/abs/2607.00860)
中文标题：Meta-Transfer Learning 面向 mmWave Beam Alignment
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts](https://arxiv.org/abs/2607.00666)
中文标题：领域算法：环境变化下的一次性VLA适应
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Active Spatial Guidance: Eliminating Injected Positional Mechanisms in Vision Transformers](https://arxiv.org/abs/2607.00580)
中文标题：主动空间引导：消除视觉变压器中的注入位置机制
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [HARC: Coupling Harmfulness and Refusal Directions for Robust Safety Alignment](https://arxiv.org/abs/2607.00572)
中文标题：HARC：Coupling Harmfulness 与 Refusal Directions 面向 Robust Safety Alignment
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [MedCAGD: Context-Aware Gated Decoder for Efficient Medical Image Segmentation](https://arxiv.org/abs/2607.00409)
中文标题：MedCAGD：Context-Aware Gated Decoder 面向 Efficient Medical Image Segmentation
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
