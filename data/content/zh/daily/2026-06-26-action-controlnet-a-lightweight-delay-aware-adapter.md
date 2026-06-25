---
title: "增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-06-26"
target_date: "2026-06-24"
actual_date: "2026-06-24"
fallback_from: ""
lang: "zh"
slug: "2026-06-26-action-controlnet-a-lightweight-delay-aware-adapter"
summary: "今天主要跟进：增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "data-engineering", "evaluation", "multimodal", "reasoning", "robotics", "systems", "training", "video-generation"]
topics: ["agents", "data-engineering", "evaluation", "multimodal", "reasoning", "robotics", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-06-26-action-controlnet-a-lightweight-delay-aware-adapter-sources/"
generated_at: "2026-06-25T22:43:31.498679+00:00"
page_type: "brief"
candidate_count: 337
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Action ControlNet: A Lightweight Delay-Aware Adapter for Smooth Asynchronous Control in Vision-Language-Action Models", "Dual Agreement Consistency Learning for Semi-Supervised Fetal Ultrasound Segmentation", "Leaking Circuit Secrets: Gradient Leakage Attacks on Graph Neural Networks", "From Sparse and Imperfect 2D Anchors to Consistent 3D Gaussian Street Scenes: Support-Aware Appearance", "Dual Distribution Estimation for Zero-shot Noisy Test-Time Adaptation with VLMs", "Efficient Real-World Dehazing via Physics-Inspired Global-Local Decoupling"]
featured_paper_urls: ["https://arxiv.org/abs/2606.25985", "https://arxiv.org/abs/2606.25254", "https://arxiv.org/abs/2606.25589", "https://arxiv.org/abs/2606.26007", "https://arxiv.org/abs/2606.25758", "https://arxiv.org/abs/2606.25732"]
featured_paper_titles_zh: ["Action ControlNet：A Lightweight Delay-Aware Adapter 面向 Smooth Asynchronous Control in 视觉-语言-动作模型", "半监督胎儿超声分割的双协议一致性学习", "泄漏电路秘密：对图神经网络的梯度泄漏攻击", "从稀疏和不完美的2D锚点到一致的3D高斯街景：支持感知外观", "使用VLM进行零点噪声测试时间适应的双重分布估计", "通过物理启发的全球-局部解耦实现高效的真实世界除雾"]
---

# 增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Action ControlNet: A Lightweight Delay-Aware Adapter for Smooth Asynchronous Control in Vision-Language-Action Models (Tiecheng Guo, Meng Guo)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.25985">2606.25985</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.25985">PDF</a></p>

中文标题：Action ControlNet：A Lightweight Delay-Aware Adapter 面向 Smooth Asynchronous Control in 视觉-语言-动作模型

信号显示：视觉-语言-动作（ VLA ）模型已显示出通用机器人操纵的强大潜力，但其推理延迟仍然是稳定高频控制的主要障碍。关键词：inference、latency、vision-language、robot。代码/数据可用性需查看原文确认。

### 2. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Dual Agreement Consistency Learning for Semi-Supervised Fetal Ultrasound Segmentation (Fangyijie Wang, Guénolé Silvestre, Ziyang Wang, Kathleen M. Curran)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.25254">2606.25254</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.25254">PDF</a></p>

中文标题：半监督胎儿超声分割的双协议一致性学习

信号显示：母胎超声是监测胎儿发育的主要成像方式，但由于像素级注释的稀缺性，精确的自动分割仍然具有挑战性。关键词：rag、deployment、alignment、code。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Leaking Circuit Secrets: Gradient Leakage Attacks on Graph Neural Networks (Rupesh Raj Karn, Johann Knechtel, Ozgur Sinanoglu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.25589">2606.25589</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.25589">PDF</a></p>

中文标题：泄漏电路秘密：对图神经网络的梯度泄漏攻击

信号显示：随着图神经网络（ GNN ）成为电路设计和分析中关键任务的标准工具，其安全和隐私风险需要仔细关注。关键词：serving、compression、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 4. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>From Sparse and Imperfect 2D Anchors to Consistent 3D Gaussian Street Scenes: Support-Aware Appearance (Long Cao, Zhongquan Wang, Jie Li, Yuhan Chen, Kefei Qian, Xiangfei Huang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.26007">2606.26007</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.26007">PDF</a></p>

中文标题：从稀疏和不完美的2D锚点到一致的3D高斯街景：支持感知外观

信号显示：图像先验可以合成3D高斯街景的目标条件，但独立编辑的视图不会定义相干的3D目标。关键词：inference、deployment、alignment、evaluation。代码/数据可用性需查看原文确认。

### 5. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Dual Distribution Estimation for Zero-shot Noisy Test-Time Adaptation with VLMs (Wenjie Zhu, Yabin Zhang, Liang Xu, Xin Jin, Wenjun Zeng, Lei Zhang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.25758">2606.25758</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.25758">PDF</a></p>

中文标题：使用VLM进行零点噪声测试时间适应的双重分布估计

信号显示：虽然测试时间适应（ TTA ）使视觉语言模型能够适应而无需昂贵的再培训，但它仍然非常容易受到现实应用中普遍存在的分布外（ OOD ）异常值的影响。关键词：inference、benchmark、code、vision-language。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Efficient Real-World Dehazing via Physics-Inspired Global-Local Decoupling (Yifei Qu, Ru Li, Junjie Chen, Jinyuan Wu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.25732">2606.25732</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.25732">PDF</a></p>

中文标题：通过物理启发的全球-局部解耦实现高效的真实世界除雾

信号显示：由于散射的空间和光谱变化，真实世界的单图像去雾定位非常糟糕，而实际部署需要轻量级和低延迟模型。关键词：rag、inference、deployment、latency。代码/数据可用性需查看原文确认。

## 其他值得关注
- [OPERA: Aligning Open-Ended Reasoning via Objective Perplexity-based Reinforcement Learning](https://arxiv.org/abs/2606.25757)
中文标题：OPERA ：通过基于客观困惑的强化学习来调整开放式推理
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MedGuards: Multi-Agent System for Reliable Medical Error Detection and Correction](https://arxiv.org/abs/2606.25651)
中文标题：MedGuards：Multi-Agent System 面向 Reliable Medical Error Detection 与 Correction
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SSMNBench: Diagnosing Image-based Cross-View Human-Object Understanding via Single-View Sufficiency and Multi-View Necessity](https://arxiv.org/abs/2606.25634)
中文标题：SSMNBench ：通过单视图充分性和多视图必要性来诊断基于图像的跨视图人体-对象理解
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [TACO: Towards Task-Consistent Open-Vocabulary Adaptation in Video Recognition](https://arxiv.org/abs/2606.25478)
中文标题：TACO ：在视频识别中实现任务一致的开放式词汇适应
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [PolicyAlign: Direct Policy-Based Safety Alignment for Large Language Models](https://arxiv.org/abs/2606.25442)
中文标题：PolicyAlign：Direct Policy-Based Safety Alignment 面向 Large Language Models
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Beyond Visual Forensics: Auditing Multimodal Robustness for Synthetic Medical Image Detection](https://arxiv.org/abs/2606.25375)
中文标题：超越视觉取证：审核合成医学图像检测的多模式鲁棒性
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning](https://arxiv.org/abs/2606.25319)
中文标题：V-Zero ：使用对比证据选通进行细粒度视觉推理的无答案标签政策性蒸馏
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos](https://arxiv.org/abs/2606.25245)
中文标题：OrthoTrack ：锚定在公共正射照片中的连续6自由度无人机轨迹估计
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Autodata: An agentic data scientist to create high quality synthetic data](https://arxiv.org/abs/2606.25996)
中文标题：Autodata ：代理数据科学家，创建高质量的合成数据
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation](https://arxiv.org/abs/2606.26087)
中文标题：MVTrack4Gen：Multi-View Point Tracking as Geometric Supervision 面向 4D Video Generation
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models](https://arxiv.org/abs/2606.26079)
中文标题：相同的证据，不同的答案：多式联运大型语言模型中的审核顺序敏感性
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems](https://arxiv.org/abs/2606.26057)
中文标题：不可触发的安全内核：人工智能代理和其他可逃避的人工智能系统的执行时间AI对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations](https://arxiv.org/abs/2606.26041)
中文标题：OCR推理有多强大？评估视觉扰动下视觉语言模型的OCR推理鲁棒性
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Detect, Unlearn, Restore: Defending Text Summarization Models Against Data Poisoning](https://arxiv.org/abs/2606.26036)
中文标题：检测、取消学习、还原：保护文本摘要模型免受数据中毒
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It](https://arxiv.org/abs/2606.26027)
中文标题：为什么要使用多步骤工具-使用强化学习崩溃以及监督信号如何修复它
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries](https://arxiv.org/abs/2606.26021)
中文标题：表格基础模型中注意层的隐私漏洞和高风险查询的保护
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SpeechEQ: Benchmarking Emotional Intelligence Quotient in Socially Aware Voice Conversational Models](https://arxiv.org/abs/2606.25990)
中文标题：SpeechEQ：基准ing Emotional Intelligence Quotient in Socially Aware Voice Conversational Models
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Pulmonary Embolism Risk Stratification from CTPA and Medical Records: Vascular Graphs Are Not All You Need](https://arxiv.org/abs/2606.25956)
中文标题：Pulmonary Embolism Risk Stratification 来自 CTPA 与 Medical Records：Vascular Graphs Are Not All You Need
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [DSP-SLAM++: A Unified Framework for Multi-Class, High-Fidelity Object SLAM in the Wild](https://arxiv.org/abs/2606.25953)
中文标题：DSP-SLAM + + ：野外多类高保真对象SLAM的统一框架
关注理由：涉及数据工程中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [USS: Unified Spatial-Semantic Prompts for Embodied Visual Tracking with Latent Dynamics Learning](https://arxiv.org/abs/2606.25880)
中文标题：USS ：具有潜在动态学习的体验式视觉跟踪的统一空间语义提示
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
