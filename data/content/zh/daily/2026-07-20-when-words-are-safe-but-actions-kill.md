---
title: "让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力、提升代码生成、执行反馈和自动修复能力"
date: "2026-07-20"
target_date: "2026-07-18"
actual_date: "2026-07-16"
fallback_from: "2026-07-18"
lang: "zh"
slug: "2026-07-20-when-words-are-safe-but-actions-kill"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力、提升代码生成、执行反馈和自动修复能力。"
tags: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "robotics", "speech-audio", "training", "video-generation", "vision-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "robotics", "speech-audio", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-07-20-when-words-are-safe-but-actions-kill-sources/"
generated_at: "2026-07-19T22:08:12.888714+00:00"
page_type: "brief"
candidate_count: 326
featured_count: 6
mentions_count: 20
featured_paper_titles: ["When Words Are Safe But Actions Kill: Probing Physical Danger Beyond Text Safety in Hidden-State Risk Space", "Self-Evolving Human-Centered Framework for Explainable Depression Symptom Annotation", "MedFailBench: A Clinician-Built Open-Source Benchmark for Medical AI Safety Boundary Inspection", "On-Policy Delta Distillation", "DriftWorld: Fast World Modeling through Drifting", "JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting"]
featured_paper_urls: ["https://arxiv.org/abs/2607.15218", "https://arxiv.org/abs/2607.15202", "https://arxiv.org/abs/2607.15166", "https://arxiv.org/abs/2607.15161", "https://arxiv.org/abs/2607.15065", "https://arxiv.org/abs/2607.14990"]
featured_paper_titles_zh: ["当言语是安全的，但行动是致命的：在隐藏状态风险空间中探测文本安全之外的物理危险", "可解释抑郁症症状注释的自我进化以人为中心的框架", "MedFailBench：A Clinician-Built Open-Source 基准 面向 Medical AI Safety Boundary Inspection", "随机三角洲蒸馏", "漂移世界：通过漂移快速建模世界", "JADE-GS ：由3D高斯拼接事件引导的联合交替去模糊"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力、提升代码生成、执行反馈和自动修复能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力、提升代码生成、执行反馈和自动修复能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>When Words Are Safe But Actions Kill: Probing Physical Danger Beyond Text Safety in Hidden-State Risk Space (Weimeng Wang, Ziqiang Wang, Zihang Zhan, Chuanpu Fu, Qi Li, Ke Xu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.15218">2607.15218</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.15218">PDF</a></p>

中文标题：当言语是安全的，但行动是致命的：在隐藏状态风险空间中探测文本安全之外的物理危险

信号显示：大语言模型（ LLM ）越来越多地成为具体代理的高级规划者，一旦在物理世界中接地，语言良性的指令可能会变得不安全。关键词：agent、safety、benchmark、agents。代码/数据可用性需查看原文确认。

### 2. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Self-Evolving Human-Centered Framework for Explainable Depression Symptom Annotation (Hoang-Loc Cao, Van Pham, Truong Thanh Hung Nguyen, Phuc Truong Loc Nguyen, Phuc Ho, Veronica Whitford, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.15202">2607.15202</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.15202">PDF</a></p>

中文标题：可解释抑郁症症状注释的自我进化以人为中心的框架

信号显示：注释质量是构建用于心理健康研究的可靠且可解释的人工智能（ XAI ）系统的主要瓶颈。关键词：alignment、evaluation、memory、eval。代码/数据可用性需查看原文确认。

### 3. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>MedFailBench: A Clinician-Built Open-Source Benchmark for Medical AI Safety Boundary Inspection (Goktug Ozkan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.15166">2607.15166</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.15166">PDF</a></p>

中文标题：MedFailBench：A Clinician-Built Open-Source 基准 面向 Medical AI Safety Boundary Inspection

信号显示：大多数医学AI基准衡量模型是否知道正确答案。关键词：safety、benchmark、open-source、data。代码/数据可用性需查看原文确认。

### 4. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>On-Policy Delta Distillation (Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.15161">2607.15161</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.15161">PDF</a></p>

中文标题：随机三角洲蒸馏

信号显示：策略提取是强化学习中的一种替代后训练方法，通过从教师模型提供令牌级监督来减轻奖励模型施加的约束。关键词：benchmark、code、post-training、training。代码/数据可用性需查看原文确认。

### 5. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>DriftWorld: Fast World Modeling through Drifting (Susie Lu, Haonan Chen, Weirui Ye, Yilun Du)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.15065">2607.15065</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.15065">PDF</a></p>

中文标题：漂移世界：通过漂移快速建模世界

信号显示：预测世界模型使机器人能够通过想象其行动的结果来进行规划，但它们对控制的价值取决于快速生成许多部署。关键词：rag、inference、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 6. 改进图像生成、视觉理解和可控渲染

<p class="paper-meta-line"><span>JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting (Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.14990">2607.14990</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.14990">PDF</a></p>

中文标题：JADE-GS ：由3D高斯拼接事件引导的联合交替去模糊

信号显示：当相机在曝光期间快速移动时，模糊会破坏3D模型恢复锐利场景所需的曝光内运动，而事件相机则以微秒分辨率准确捕获此信号。关键词：serving、benchmark、rendering、vision-generation。代码/数据可用性需查看原文确认。

## 其他值得关注
- [CoSimRec: Measuring Coordinated-Content Penetration in Recommender Feedback Loops](https://arxiv.org/abs/2607.15114)
中文标题：CoSimRec ：测量推荐者反馈循环中的协调内容渗透率
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Demographically-Conditioned Synthetic Medical Images for Bias Mitigation and Bias Detection in Disease Classifiers](https://arxiv.org/abs/2607.14984)
中文标题：用于疾病分类器中偏差缓解和偏差检测的人口统计学条件合成医学图像
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [RW-Voice-EQ Bench: A Real World Benchmark for Evaluating Voice AI Systems](https://arxiv.org/abs/2607.14846)
中文标题：RW-Voice-EQ Bench：A Real World 基准 面向 Evaluating Voice AI Systems
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Physics-Informed Diffusion for Biomechanically Plausible 3D Sign Language Generation](https://arxiv.org/abs/2607.14836)
中文标题：Physics-Informed Diffusion 面向 Biomechanically Plausible 3D Sign Language Generation
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Evaluating Epistemic Uncertainty: Beyond OOD Detection and Active Learning](https://arxiv.org/abs/2607.14817)
中文标题：评估认知不确定性：超越OOD检测和主动学习
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Transcoders for Investigating Deception in Language Models](https://arxiv.org/abs/2607.14791)
中文标题：用于调查语言模型中欺骗的转码器
关注理由：涉及可解释性中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Rare Concept Generation via Counterfactual Inference in Diffusion Models](https://arxiv.org/abs/2607.14765)
中文标题：扩散模型中通过反事实推断的罕见概念生成
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [AE-UAV: An Air-to-Air Event-Based UAV Tracking Benchmark and a Real-Time Frequency-Domain Tracker](https://arxiv.org/abs/2607.14726)
中文标题：AE-UAV：An Air-to-Air Event-Based UAV Tracking 基准 与 a Real-Time Frequency-Domain Tracker
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Causal-Adversarial Probing of Clinical Covariates for Prostate MRI Grading](https://arxiv.org/abs/2607.14720)
中文标题：Causal-Adversarial Probing of Clinical Covariates 面向 Prostate MRI Grading
关注理由：涉及可解释性中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Reinforcement Learning for the Full Strawberry Harvesting Process: Obstacle Separation, Detachment, and Placement](https://arxiv.org/abs/2607.14708)
中文标题：完整草莓收获过程的强化学习：障碍物分离、分离和放置
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Harnessing LLMs for Reliable Academic Supervision: A Comparative Study](https://arxiv.org/abs/2607.14707)
中文标题：利用法学硕士进行可靠的学术监督：一项比较研究
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Dendrite: A Real-Time Python Application for Online Brain-Computer Interface Research and Development](https://arxiv.org/abs/2607.14655)
中文标题：Dendrite：A Real-Time Python Application 面向 Online Brain-Computer Interface Research 与 Development
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [NavCMPO: Critic-Guided MeanFlow Policy Optimization for Adaptive Navigation](https://arxiv.org/abs/2607.14643)
中文标题：NavCMPO：Critic-Guided MeanFlow Policy Optimization 面向 Adaptive Navigation
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ExaGEMM: Exploration Framework for CPU-Driven ML Inference via Associative In-Register Computing for Low-Bit GEMM](https://arxiv.org/abs/2607.14622)
中文标题：ExaGEMM ：基于低位GEMM关联寄存器内计算的CPU驱动ML推理探索框架
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Auditing Fairness-Privacy Trade-offs: Subpopulation-Level Effects of Fairness-Enhancing Algorithms](https://arxiv.org/abs/2607.14607)
中文标题：审计公平性-隐私权衡：公平性增强算法的亚群级影响
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Breaking the Model Forgetting Cycle in Long-Incremental 3D Object Detection](https://arxiv.org/abs/2607.14560)
中文标题：打破长增量三维目标检测中的模型遗忘循环
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Multi-Scale ViT Inference with Habitat-Fit Priors and kNN Retrieval for Multi-Species Plant Identification](https://arxiv.org/abs/2607.14509)
中文标题：基于栖息地拟合先验的多尺度ViT推断和多物种植物鉴定的kNN检索
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Hierarchical Denoising For Multi-Step Visual Reasoning](https://arxiv.org/abs/2607.15278)
中文标题：多步骤视觉推理的分层去噪
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Bridge Evidence: Static Retrieval Utility Does Not Predict Causal Utility in Multi-Step Agentic Search](https://arxiv.org/abs/2607.15253)
中文标题：桥接证据：静态检索实用程序无法预测多步代理搜索中的因果效用
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ARMOR++: Agentic Orchestration of a Multi-Domain Primitive Set for Transferable Attacks on Deepfake Detectors](https://arxiv.org/abs/2607.15246)
中文标题：ARMOR++：Agentic Orchestration of a Multi-Domain Primitive Set 面向 Transferable Attacks on Deepfake Detectors
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
