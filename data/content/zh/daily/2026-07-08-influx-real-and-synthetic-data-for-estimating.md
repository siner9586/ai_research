---
title: "提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-07-08"
target_date: "2026-07-06"
actual_date: "2026-07-06"
fallback_from: ""
lang: "zh"
slug: "2026-07-08-influx-real-and-synthetic-data-for-estimating"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "interpretability", "multimodal", "rag", "reasoning", "robotics", "training", "video-generation", "vision-generation"]
topics: ["agents", "code", "evaluation", "interpretability", "multimodal", "rag", "reasoning", "robotics", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-07-08-influx-real-and-synthetic-data-for-estimating-sources/"
generated_at: "2026-07-07T22:21:34.388431+00:00"
page_type: "brief"
candidate_count: 369
featured_count: 6
mentions_count: 20
featured_paper_titles: ["InFlux++: Real and Synthetic Data for Estimating Dynamic Camera Intrinsics", "ReCal3R: Reliability-Calibrated Learning Rates for Streaming 3D Reconstruction", "Toward Trustworthy Large Language Model Agents in Healthcare", "TGRIP: A Text-Guided Approach to Vehicle Instance Prediction in Autonomous Driving", "From Open Loop to Closed Loop: A Test-Time Iterative Optimization Framework for Reference-Consistent Image Generation", "QSVideo: Query-Conditioned Semantic Temporal Retrieval for Video Understanding"]
featured_paper_urls: ["https://arxiv.org/abs/2607.05389", "https://arxiv.org/abs/2607.05356", "https://arxiv.org/abs/2607.05055", "https://arxiv.org/abs/2607.04812", "https://arxiv.org/abs/2607.04691", "https://arxiv.org/abs/2607.04559"]
featured_paper_titles_zh: ["InFlux++：Real 与 Synthetic Data 面向 Estimating Dynamic Camera Intrinsics", "ReCal3R：Reliability-Calibrated Learning Rates 面向 Streaming 3D Reconstruction", "迈向可信赖的医疗保健大型语言模型代理", "TGRIP ：自动驾驶车辆实例预测的文本引导方法", "从开环到闭环：用于参考一致图像生成的测试时迭代优化框架", "QSVideo：Query-Conditioned Semantic Temporal Retrieval 面向 Video Understanding"]
---

# 提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>InFlux++: Real and Synthetic Data for Estimating Dynamic Camera Intrinsics (Erich Liang, Caleb Kha-Uong, Chinmaya Saran, Sreemanti Dey, David W. Liu, Junhan Ouyang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.05389">2607.05389</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.05389">PDF</a></p>

中文标题：InFlux++：Real 与 Synthetic Data 面向 Estimating Dynamic Camera Intrinsics

信号显示：摄像头内在特性对于从2D视频中恢复3D结构至关重要。关键词：benchmark、code、synthetic data、eval。代码/数据可用性需查看原文确认。

### 2. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>ReCal3R: Reliability-Calibrated Learning Rates for Streaming 3D Reconstruction (Xinze Li, Yiyuan Wang, Pengxu Chen, Wentao Fan, Weifeng Su, Weisi Lin, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.05356">2607.05356</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.05356">PDF</a></p>

中文标题：ReCal3R：Reliability-Calibrated Learning Rates 面向 Streaming 3D Reconstruction

信号显示：流式3D重建依赖于紧凑的循环场景状态，以线性时间和有界内存处理长图像流。关键词：serving、alignment、code、memory。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Toward Trustworthy Large Language Model Agents in Healthcare (Hadi Hasan, Safaa Salman, Adam Tai Abou Dargham, Ammar Mohanna, Ali Chehab)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.05055">2607.05055</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.05055">PDF</a></p>

中文标题：迈向可信赖的医疗保健大型语言模型代理

信号显示：医疗预约安排仍然是一个持续存在的运营瓶颈，其驱动因素包括手动协调、分散的遗留系统和高昂的管理开销。关键词：agent、workflow、rag、retrieval。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>TGRIP: A Text-Guided Approach to Vehicle Instance Prediction in Autonomous Driving (Miguel Antunes-García, Santiago Montiel-Marín, Fabio Sánchez-García, Rodrigo Gutiérrez-Moreno, Rafael Barea, Luis M. Bergasa)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.04812">2607.04812</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.04812">PDF</a></p>

中文标题：TGRIP ：自动驾驶车辆实例预测的文本引导方法

信号显示：鸟瞰图（ BEV ）端到端实例预测已成为自动驾驶感知的强大范例，有效缓解了传统模块化管道固有的误差传播。关键词：agent、code、vision-language、temporal。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>From Open Loop to Closed Loop: A Test-Time Iterative Optimization Framework for Reference-Consistent Image Generation (Baixuan Zhao, Xinyu Zhang, Huayu Zheng, Shuaicheng Liu, Xiongkuo Min, Guangtao Zhai, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.04691">2607.04691</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.04691">PDF</a></p>

中文标题：从开环到闭环：用于参考一致图像生成的测试时迭代优化框架

信号显示：虽然可控图像生成通过结合视觉参考条件取得了重大进展，但现有方法主要作为开环系统运行。关键词：serving、alignment、evaluation、code。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>QSVideo: Query-Conditioned Semantic Temporal Retrieval for Video Understanding (Wei Ao, Lan Wang, Vishnu Naresh Boddeti)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.04559">2607.04559</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.04559">PDF</a></p>

中文标题：QSVideo：Query-Conditioned Semantic Temporal Retrieval 面向 Video Understanding

信号显示：随着视频时长的增加，视觉语言模型（ VLM ）在视频理解中的性能会下降，因为与查询无关的视频时刻会混淆其语言组件。关键词：retrieval、alignment、benchmark、code。代码/数据可用性需查看原文确认。

## 其他值得关注
- [G2VD: Generalizable AI-Generated Video Detection via Counterfactual Intervention and Causal Disentanglement](https://arxiv.org/abs/2607.04607)
中文标题：G2VD ：通过反事实干预和因果分离进行可推广的人工智能生成视频检测
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Displacement Preserving Relational Distillation for Robust Medical Segmentation](https://arxiv.org/abs/2607.04599)
中文标题：位移保持关系蒸馏用于强大的医学分段
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Multiplayer Interactive World Models with Representation Autoencoders](https://arxiv.org/abs/2607.05352)
中文标题：多人互动世界模型与表征自动编码器
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Dynamic Airspace Management for UAVs in Evolving Urban Environments: Collaborative Coordination and Human Safety](https://arxiv.org/abs/2607.04825)
中文标题：不断变化的城市环境中无人机的动态空域管理：协作协调与人身安全
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model](https://arxiv.org/abs/2607.05396)
中文标题：从固定摄像头到自由摄像头：无校准视野-健壮的视觉-语言动作模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SPEARBench: A Benchmark for Naturalness Evaluation in Streaming Speech-to-Speech Language Models](https://arxiv.org/abs/2607.05365)
中文标题：SPEARBench：A 基准 面向 Naturalness 评测 in Streaming Speech-to-Speech Language Models
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [REDDIT: Correcting Model-Generated Timestamp Drift in ASR without Forgetting via Replay-Based Distribution Editing](https://arxiv.org/abs/2607.05364)
中文标题：REDDIT ：通过基于重播的分发编辑纠正ASR中模型生成的时间戳漂移而不会忘记
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent, Platform Mediation, and Consent Constraints](https://arxiv.org/abs/2607.05363)
中文标题：SovereignPA-Bench：Evaluating User-Owned Personal Agents under Evolving Intent，平台 Mediation，与 Consent Constraints
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Selective Disclosure Watermarking for Large Language Models](https://arxiv.org/abs/2607.05353)
中文标题：大型语言模型的选择性披露水印
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Deep Learning for Semen Analysis in Male Infertility: Computer Vision, Multimodal Fusion, and Clinical Translation](https://arxiv.org/abs/2607.05311)
中文标题：男性不孕症精液分析的深度学习：计算机视觉、多模式融合和临床翻译
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Evaluating and Understanding Model Editing for Medical Vision Language Models](https://arxiv.org/abs/2607.05310)
中文标题：评估和理解医学视觉语言模型的模型编辑
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Biologically Informed Deep Neural Networks for Multi-Omic Integration, Pathway Activity Inference and Risk Stratification in Cancer](https://arxiv.org/abs/2607.05306)
中文标题：用于癌症多组学整合、通路活动推断和风险分层的生物信息深度神经网络
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Routing Anonymity and Identifiability of Noisy Quantum Hardware](https://arxiv.org/abs/2607.05281)
中文标题：噪声量子硬件的路由匿名性和可识别性
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SteelBench: Evaluating Vision-Language Models in Real-World Industrial Environments](https://arxiv.org/abs/2607.05264)
中文标题：SteelBench ：评估真实工业环境中的视觉语言模型
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Streaming Neural Speech Codecs through Time-Invariant Representations](https://arxiv.org/abs/2607.05250)
中文标题：通过时间不变表示流式传输神经语音编解码器
关注理由：涉及可解释性中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Unified Audio Intelligence Without Regressing on Text Intelligence](https://arxiv.org/abs/2607.05196)
中文标题：不回归文本智能的统一音频智能
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents](https://arxiv.org/abs/2607.05189)
中文标题：当爪子记住但不告诉时：持久性个人代理的隐形记忆注射
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [VLM-CASE: Vision-Language Model Enabled Context-Adaptive Safety Envelopes for Anticipatory Safe Autonomous Driving](https://arxiv.org/abs/2607.05180)
中文标题：VLM-CASE：Vision-Language Model Enabled Context-Adaptive Safety Envelopes 面向 Anticipatory Safe Autonomous Driving
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [On the risk of coding before testing: An empirical study on LLM-based test generation workflow](https://arxiv.org/abs/2607.05139)
中文标题：测试前编码的风险：基于LLM的测试生成工作流程的实证研究
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [LangLoc: "Tell Me What You See"](https://arxiv.org/abs/2607.05077)
中文标题：LangLoc ： “告诉我你看到了什么”
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
