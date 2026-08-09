---
title: "让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力"
date: "2026-08-10"
target_date: "2026-08-08"
actual_date: "2026-08-06"
fallback_from: "2026-08-08"
lang: "zh"
slug: "2026-08-10-lawm-3d-learning-3d-aware-latent-actions"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "systems", "training", "video-generation"]
topics: ["agents", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-08-10-lawm-3d-learning-3d-aware-latent-actions-sources/"
generated_at: "2026-08-09T21:45:20.104368+00:00"
page_type: "brief"
candidate_count: 388
featured_count: 6
mentions_count: 20
featured_paper_titles: ["LAWM-3D: Learning 3D-Aware Latent Actions from Human Videos for Generalizable Robot World Models", "DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model", "DistMedVL: Distributional Vision-Language Alignment for Uncertainty-Aware Medical Image Segmentation", "ChronoVision: Temporal Reasoning via Latent State Reconstruction", "SkillHEX: Improving Agent Skills via Hypothesis-Driven Autonomous Exploration and Exploitation", "TruthLens: Object Hallucination Detection via Self-Evaluating Truthfulness Scores in LVLMs"]
featured_paper_urls: ["https://arxiv.org/abs/2608.05706", "https://arxiv.org/abs/2608.05695", "https://arxiv.org/abs/2608.05683", "https://arxiv.org/abs/2608.05631", "https://arxiv.org/abs/2608.05628", "https://arxiv.org/abs/2608.05616"]
featured_paper_titles_zh: ["LAWM-3D：Learning 3D-Aware Latent Actions 来自 Human Videos 面向 Generalizable Robot 世界模型", "DreamGuard ：通过风险意识世界模型为LLM代理提供高效的运行时保护栏", "DistMedVL：Distributional Vision-Language Alignment 面向 Uncertainty-Aware Medical Image Segmentation", "ChronoVision ：通过潜伏状态重建进行时间推理", "SkillHEX：Improving Agent Skills via Hypothesis-Driven Autonomous Exploration 与 Exploitation", "TruthLens ：通过LVLM中的自我评估真实性评分进行物体幻觉检测"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>LAWM-3D: Learning 3D-Aware Latent Actions from Human Videos for Generalizable Robot World Models (Jiarui Yang, Jiale Zhange, Jiawei Li, Hang Guo, Wen Huang, Jinpeng Wang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.05706">2608.05706</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.05706">PDF</a></p>

中文标题：LAWM-3D：Learning 3D-Aware Latent Actions 来自 Human Videos 面向 Generalizable Robot 世界模型

信号显示：世界模型使座席能够在无需实际交互的情况下执行前瞻性推出和规划。关键词：agent、alignment、code、fine-tuning。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model (Wenhao Lin, Chenyu Yu, Xingwei Lin, Sicong Cao, Xiang Chen, Lei Xue, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.05695">2608.05695</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.05695">PDF</a></p>

中文标题：DreamGuard ：通过风险意识世界模型为LLM代理提供高效的运行时保护栏

信号显示：随着大语言模型（ LLM ）代理越来越多地调用外部工具并与现实世界的系统进行交互，不安全的操作可能会对外部状态、用户数据和下游服务造成不可逆转的后果。关键词：agent、rag、latency、safety。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>DistMedVL: Distributional Vision-Language Alignment for Uncertainty-Aware Medical Image Segmentation (Jiaxuan Li, Qing Xu, Xiangjian He, Yue Li, Daokun Zhang, Fiseha B. Tesema, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.05683">2608.05683</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.05683">PDF</a></p>

中文标题：DistMedVL：Distributional Vision-Language Alignment 面向 Uncertainty-Aware Medical Image Segmentation

信号显示：视觉和文本表示的跨模态对齐是多模态医学图像理解的基础，但在现实世界的临床条件下，这两种模式的不确定性仍然受到阻碍。关键词：rag、alignment、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>ChronoVision: Temporal Reasoning via Latent State Reconstruction (Yifan Shen, Jian Xu, Boyi Li, Yuner Zhang, Tianjiao Yu, Bingxuan Li, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.05631">2608.05631</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.05631">PDF</a></p>

中文标题：ChronoVision ：通过潜伏状态重建进行时间推理

信号显示：多模态大语言模型擅长被动感知，但难以处理需要多步时间推理的复杂视觉认知任务。关键词：alignment、benchmark、multimodal、fine-tuning。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>SkillHEX: Improving Agent Skills via Hypothesis-Driven Autonomous Exploration and Exploitation (Yuru Feng, Yaoqi Chen, Beidi Zhao, Qianxi Zhang, Xinjiang Wang, Jianan Lu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.05628">2608.05628</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.05628">PDF</a></p>

中文标题：SkillHEX：Improving Agent Skills via Hypothesis-Driven Autonomous Exploration 与 Exploitation

信号显示：虽然客服代表的技能为LLM提供了可重复使用的程序知识，但手动维护的成本高昂、无法扩展和错位。关键词：agent、rag、deployment、alignment。代码/数据可用性需查看原文确认。

### 6. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>TruthLens: Object Hallucination Detection via Self-Evaluating Truthfulness Scores in LVLMs (Yanqi Wu, Runhe Lai, Xinhua Lu, Qichao Chen, Zhiping Zhou, Jia-Xin Zhuang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.05616">2608.05616</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.05616">PDF</a></p>

中文标题：TruthLens ：通过LVLM中的自我评估真实性评分进行物体幻觉检测

信号显示：尽管大型视觉语言模型（ LVLM ）取得了显着进展，但物体幻觉仍然是一个阻碍其可信部署的根本挑战。关键词：inference、deployment、evaluation、benchmark。代码/数据可用性需查看原文确认。

## 其他值得关注
- [FOCUS: Decoupling Expert Personas in LLMs to Enhance Domain Expert Capabilities](https://arxiv.org/abs/2608.05611)
中文标题：重点：解耦LLM中的专家角色以增强领域专家能力
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Augmented Agentic Execution](https://arxiv.org/abs/2608.05573)
中文标题：SkillTV-Bench：基准ing How Well Judges Perform on Skill-Augmented Agentic Execution
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [From Sports to Safety: Benchmarking Proactive Risk Inference in MLLMs](https://arxiv.org/abs/2608.05560)
中文标题：从运动到安全：对标传销中的主动风险推断
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [VideoArgus: Agentic Rubric-Grounded Unified Evaluation for Video Generation and Editing](https://arxiv.org/abs/2608.05485)
中文标题：VideoArgus：Agentic Rubric-Grounded Unified 评测 面向 Video Generation 与 Editing
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Scalable estimation of VARMA models](https://arxiv.org/abs/2608.06340)
中文标题：可扩展 estimation of VARMA models
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Minimax Optimal Early-Stopped Gradient Descent for Gaussian Mixture Classification](https://arxiv.org/abs/2608.06250)
中文标题：用于高斯混合分类的最小最优早期停止梯度下降
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models](https://arxiv.org/abs/2608.06243)
中文标题：DASH：Divergence-Adaptive Supervision Horizons 面向 On-Policy Self-Distillation of Reasoning Models
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Reversible Unlearnable Examples: Towards the Copyright Protection in Deep Learning Era](https://arxiv.org/abs/2608.06211)
中文标题：可逆不可学习的例子：走向深度学习时代的版权保护
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Beyond Marginal Validity: Finite-Sample Guarantees for Localized Conformal Prediction](https://arxiv.org/abs/2608.06206)
中文标题：超越边际效度：本地化保形预测的有限样本保证
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CFGPNet: Cross-Attention-Based Fused Gradient Programmed Network Framework for Multispectral Object Detection](https://arxiv.org/abs/2608.06205)
中文标题：CFGPNet：Cross-Attention-Based Fused Gradient Programmed Network 框架 面向 Multispectral Object Detection
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [EvReflection: Event-Driven Micro-Dynamics for Reflection Removal](https://arxiv.org/abs/2608.06184)
中文标题：EvReflection：Event-Driven Micro-Dynamics 面向 Reflection Removal
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Routing Is Least Learnable Where It Is Most Valuable: Bounds on Representation Routing for Web Agents](https://arxiv.org/abs/2608.06171)
中文标题：Routing Is Least Learnable Where It Is Most Valuable：Bounds on Representation Routing 面向 Web Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [LLM Inference Under Bursty Workload Distribution: Modifying the WAIT Algorithm](https://arxiv.org/abs/2608.06135)
中文标题：突发工作负载分布下的LLM推理：修改WAIT算法
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Is Self-Pretraining really useful to improve diagnosis in medical Time Series?](https://arxiv.org/abs/2608.06122)
中文标题：自我预训练是否真的有助于改善医疗时间序列的诊断？
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [BioKD: Selective Physiology-to-Video Knowledge Distillation via Reliability Gate for Emotion Recognition](https://arxiv.org/abs/2608.06023)
中文标题：BioKD ：通过情感识别的可靠性门户进行选择性生理学到视频知识蒸馏
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Iterate or Widen? When Test-Time Refinement Helps LiDAR Scene Completion: A Controlled Study of Evidence Geometry, Training Coverage, and Compute](https://arxiv.org/abs/2608.06014)
中文标题：Iterate or Widen? When Test-Time Refinement Helps LiDAR Scene Completion：A Controlled Study of Evidence Geometry，Training Coverage，与 Compute
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Wan-Animate-2: Pushing the Application Boundaries of Character Animation](https://arxiv.org/abs/2608.06009)
中文标题：Wan-Animate-2 ：突破角色动画的应用边界
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Operating Multi-Node Full Fine-Tuning on NVIDIA B300: A Field Report on Telemetry-Based Triage, Negative Results, and Operational Hardening](https://arxiv.org/abs/2608.05944)
中文标题：Operating Multi-Node Full Fine-Tuning on NVIDIA B300：A Field Report on Telemetry-Based Triage，Negative Results，与 Operational Hardening
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Floating Radiance Networks](https://arxiv.org/abs/2608.05920)
中文标题：浮动辐射网络
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [GSBF: Gaussian Splatting for Environment-Aware Beamforming](https://arxiv.org/abs/2608.05896)
中文标题：GSBF：Gaussian Splatting 面向 Environment-Aware Beamforming
关注理由：涉及数据工程中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
