---
title: "提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力"
date: "2026-06-17"
target_date: "2026-06-15"
actual_date: "2026-06-15"
fallback_from: ""
lang: "zh"
slug: "2026-06-17-activesam-image-conditional-class-pruning-for-fast"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "safety", "training", "video-generation", "vision-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "safety", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-06-17-activesam-image-conditional-class-pruning-for-fast-sources/"
generated_at: "2026-06-16T22:57:39.493746+00:00"
page_type: "brief"
candidate_count: 465
featured_count: 6
mentions_count: 20
featured_paper_titles: ["ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation", "ARB4WM: An Adversarial Robustness Benchmark for World Models in Continuous Control", "When Confidence Lacks Concepts: Interpretable OOD Detection via Representation Perturbations", "Selection Without Signal, Recovery Through Expression: A Measurement Study of Post-Hoc Falsification Operators for Frozen Small Code Models", "Semantic Flip: Synthetic OOD Generation for Robust Refusal in Embodied Question Answering and Spatial Localization", "Decoupling Semantics from Distortions: Multi-Scale Two-Stream Vision-Language Alignment for AI-Generated Image Quality Assessment"]
featured_paper_urls: ["https://arxiv.org/abs/2606.16996", "https://arxiv.org/abs/2606.16605", "https://arxiv.org/abs/2606.16196", "https://arxiv.org/abs/2606.16999", "https://arxiv.org/abs/2606.16898", "https://arxiv.org/abs/2606.16799"]
featured_paper_titles_zh: ["ActiveSAM：面向快速准确开放词汇分割的图像条件类别剪枝", "ARB4WM：面向连续控制世界模型的对抗鲁棒性基准", "当置信度缺少概念：基于表征扰动的可解释分布外检测", "无信号选择与表达恢复：面向冻结小型代码模型的事后证伪算子测量研究", "语义翻转：面向具身问答与空间定位鲁棒拒答的合成式分布外样本生成", "解耦语义与失真：面向 AI 生成图像质量评估的多尺度双流视觉语言对齐"]
---

# 提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation (Tran Dinh Tien, Zhiqiang Shen)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.16996">2606.16996</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.16996">PDF</a></p>

核心：这篇论文主要解决提升 RAG 检索和知识库问答可靠性这一方向中的具体研究问题；方法上通过题名、摘要和公开信号中的 rag、inference、deployment、benchmark 等线索来组织训练与后训练任务、数据或评测流程实现提升 RAG 检索和知识库问答可靠性；主要论点是标题、摘要和公开信号显示：Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution decoding is typically run over the entire dataset voc。关键词：rag、inference、deployment、benchmark。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>ARB4WM: An Adversarial Robustness Benchmark for World Models in Continuous Control (Junjian Zhang, Hao Tan, Ruonan Li, Dong Zhu, Aiping Li, Zhaoquan Gu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.16605">2606.16605</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.16605">PDF</a></p>

核心：这篇论文主要解决让 Agent 更可靠地调用工具和复用技能这一方向中的具体研究问题；方法上通过题名、摘要和公开信号中的 agent、deployment、safety、evaluation 等线索来组织基准与评测任务、数据或评测流程实现让 Agent 更可靠地调用工具和复用技能；主要论点是标题、摘要和公开信号显示：World models are widely used in robotic and agentic engineering control systems due to their ability to learn latent dynamics for planning and decision-making。关键词：agent、deployment、safety、evaluation。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>When Confidence Lacks Concepts: Interpretable OOD Detection via Representation Perturbations (Anju Chhetri, Pratik Shrestha, Ramesh Rana, Prashnna Gyawali, Binod Bhattarai)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.16196">2606.16196</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.16196">PDF</a></p>

核心：这篇论文主要解决提升 RAG 检索和知识库问答可靠性这一方向中的具体研究问题；方法上通过题名、摘要和公开信号中的 rag、inference、deployment、alignment 等线索来组织安全与对齐任务、数据或评测流程实现提升 RAG 检索和知识库问答可靠性；主要论点是标题、摘要和公开信号显示：Deep neural networks have achieved remarkable performance across medical imaging tasks, yet their tendency to overgeneralize under distributional shifts poses a major obstacle to safe clinical deployment。关键词：rag、inference、deployment、alignment。代码/数据可用性需查看原文确认。

### 4. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Selection Without Signal, Recovery Through Expression: A Measurement Study of Post-Hoc Falsification Operators for Frozen Small Code Models (Mehmet Iscan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.16999">2606.16999</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.16999">PDF</a></p>

核心：这篇论文主要解决提升模型推理、规划和验证能力这一方向中的具体研究问题；方法上通过题名、摘要和公开信号中的 rag、alignment、benchmark、code 等线索来组织代码智能任务、数据或评测流程实现提升模型推理、规划和验证能力；主要论点是标题、摘要和公开信号显示：Frozen small code models (<=1.5B parameters, run locally without fine-tuning) suit offline and privacy-constrained use, but often emit plausible-but-wrong programs。关键词：rag、alignment、benchmark、code。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Semantic Flip: Synthetic OOD Generation for Robust Refusal in Embodied Question Answering and Spatial Localization (Dongbin Na, Chanwoo Kim, Giyun Choi, Dooyoung Hong)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.16898">2606.16898</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.16898">PDF</a></p>

核心：这篇论文主要解决让 Agent 更可靠地调用工具和复用技能这一方向中的具体研究问题；方法上通过题名、摘要和公开信号中的 agent、deployment、benchmark、code 等线索来组织数据工程任务、数据或评测流程实现让 Agent 更可靠地调用工具和复用技能；主要论点是标题、摘要和公开信号显示：Detecting unanswerable user queries remains essential for the reliable deployment of real-world embodied agents。关键词：agent、deployment、benchmark、code。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Decoupling Semantics from Distortions: Multi-Scale Two-Stream Vision-Language Alignment for AI-Generated Image Quality Assessment (Zijie Meng)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.16799">2606.16799</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.16799">PDF</a></p>

核心：这篇论文主要解决提升 RAG 检索和知识库问答可靠性这一方向中的具体研究问题；方法上通过题名、摘要和公开信号中的 rag、alignment、evaluation、benchmark 等线索来组织多模态模型任务、数据或评测流程实现提升 RAG 检索和知识库问答可靠性；主要论点是标题、摘要和公开信号显示：Existing vision-language model (VLM)-based AI-generated image quality assessment (AIGIQA) methods suffer from a fundamental semantic-distortion dimensional conflict: monolithic representations optimized for semantic discrimination inherently entangle compositi。关键词：rag、alignment、evaluation、benchmark。代码/数据可用性需查看原文确认。

## 其他值得关注
- [TuneJury: An Open Metric for Improving Music Generation Preference Alignment](https://arxiv.org/abs/2606.17006)：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [A Multi-Center Benchmark for Abdominal Disease Diagnosis and Report Generation from Non-Contrast CT](https://arxiv.org/abs/2606.16991)：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [An Open-Source Monitoring Framework for Data Exploration and Progress Tracking in Multi-Center Radiology Studies](https://arxiv.org/abs/2606.16861)：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [ROSA-RL: Uncertainty-Aware Roundabout Optimized Speed Advisory with Reinforcement Learning](https://arxiv.org/abs/2606.16558)：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Active Reference Acquisition in Few-Shot Font Generation](https://arxiv.org/abs/2606.16502)：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [AuAu: A Benchmark for Auditing Authoritarian Alignment in Large Language Models](https://arxiv.org/abs/2606.16127)：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Benchmarking LLM Agents on Meta-Analysis Articles from Nature Portfolio](https://arxiv.org/abs/2606.17041)：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Beyond the Smile: A Hybrid Convolutional VAE for Crypto Volatility Surfaces](https://arxiv.org/abs/2606.16961)：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Compositional Reasoning Depth Predicts Clinical AI Failure: Empirical Evidence Consistent with Transformer Compositionality Limits in Electronic Health Record Question Answering](https://arxiv.org/abs/2606.16890)：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Adaptive and Explicit safe: Triggering Latent Safety Awareness in Large Reasoning Models](https://arxiv.org/abs/2606.16808)：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [GD$^2$PO: Mitigating Multi-Reward Conflicts via Group-Dynamic reward-Decoupled Policy Optimization](https://arxiv.org/abs/2606.16771)：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Structure-aware Knowledge-guided Heterogeneous Mamba for Zygomaticomaxillary Suture Assessment](https://arxiv.org/abs/2606.16749)：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SUP-MCRL: Subject-aware Unified Pseudo-feature Coded Multimodal Contrastive Representation Learning for EEG Visual Decoding](https://arxiv.org/abs/2606.16615)：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [DifferAD-R1: A Difference-Guided IndustrialAnomaly Localization with Multimodal LargeLanguage Models](https://arxiv.org/abs/2606.16601)：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [DoubtProbe: Black-Box Jailbreak Defense via Structural Verification and Semantic Auditing](https://arxiv.org/abs/2606.16527)：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Lost at the End: Primacy Bias in Multimodal Retrieval-Augmented Question Answering](https://arxiv.org/abs/2606.16494)：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [PaperJury: Due-Process Review for Bounded LaTeX Revision](https://arxiv.org/abs/2606.16322)：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Structure-Semantic Co-optimized Latent Diffusion Model for Fast Visual Anagram Synthesis](https://arxiv.org/abs/2606.16241)：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234)：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [PolyMerge: Compressing 3D Gaussian Splats with Polytope Coverings for Provably Safe Resource-Constrained Navigation](https://arxiv.org/abs/2606.16232)：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
