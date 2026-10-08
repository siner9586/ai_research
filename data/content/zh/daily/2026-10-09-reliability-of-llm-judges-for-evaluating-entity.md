---
title: "提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性"
date: "2026-10-09"
target_date: "2026-10-07"
actual_date: "2026-10-07"
fallback_from: ""
lang: "zh"
slug: "2026-10-09-reliability-of-llm-judges-for-evaluating-entity"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "code", "evaluation", "multimodal", "safety", "training", "vision-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "safety", "training", "vision-generation"]
sources_page: "/zh/daily/2026-10-09-reliability-of-llm-judges-for-evaluating-entity-sources/"
generated_at: "2026-10-08T16:16:04.211755+00:00"
page_type: "brief"
candidate_count: 628
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Reliability of LLM Judges for Evaluating Entity Alignment", "Open-MMUnlearning: Unifying Methods and Evaluation for MLLM Unlearning", "SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing", "A Probabilistic Perspective on Wasserstein-Based Evidential Uncertainty for Out-of-Distribution Segmentation", "MIRROR: From Imitation to Internalization in LLM Personalization", "Why VLMs Miss Small Objects, and When Zooming In Is Safe"]
featured_paper_urls: ["https://arxiv.org/abs/2610.09554", "https://arxiv.org/abs/2610.10358", "https://arxiv.org/abs/2610.10345", "https://arxiv.org/abs/2610.10116", "https://arxiv.org/abs/2610.09795", "https://arxiv.org/abs/2610.09313"]
featured_paper_titles_zh: ["LLM法官评估实体一致性的可靠性", "Open-MMUnlearning：Unifying Methods 与 评测 面向 MLLM Unlearning", "SLDR ：通过选择性图层恢复和动态路由防御恶意微调", "一种Probabilistic Perspective on Wasserstein-Based Evidential Uncertainty 面向 Out-of-Distribution Segmentation", "镜像： LLM个性化从模仿到内化", "为什么VLM会错过小物体，以及何时放大是安全的"]
---

# 提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Reliability of LLM Judges for Evaluating Entity Alignment (Vaibhava Lakshmi Ravideshik, Mayank Kejriwal)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.09554">2610.09554</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.09554">PDF</a></p>

中文标题：LLM法官评估实体一致性的可靠性

信号显示：实体对齐（ EA ）识别知识图形中的等效实体，对于知识库集成和本体合并至关重要。关键词：alignment、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 2. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Open-MMUnlearning: Unifying Methods and Evaluation for MLLM Unlearning (Junkai Chen, Yuhao He, Qianshan Wei, Junxiang You, Jingwen Shao, Junkai Lin, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.10358">2610.10358</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.10358">PDF</a></p>

中文标题：Open-MMUnlearning：Unifying Methods 与 评测 面向 MLLM Unlearning

信号显示：随着多模态大语言模型（ MLLM ）变得更加强大和广泛部署，对隐私和安全的担忧变得越来越紧迫。关键词：rag、inference、serving、safety。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing (Hui Zhang, Yachao Yuan, Jiayun Wang, Yuanzhuo Li, Hongtao Wang, Yali Yuan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.10345">2610.10345</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.10345">PDF</a></p>

中文标题：SLDR ：通过选择性图层恢复和动态路由防御恶意微调

信号显示：微调即服务使用户能够使对齐的大语言模型（ LLM ）适应专业任务，但恶意微调可能会侵蚀拒绝行为，同时保持合法输入的任务执行。关键词：rag、inference、serving、safety。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>A Probabilistic Perspective on Wasserstein-Based Evidential Uncertainty for Out-of-Distribution Segmentation (Arnold Brosch, Abdelrahman Eldesokey, Michael Felsberg, Kira Maag)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.10116">2610.10116</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.10116">PDF</a></p>

中文标题：一种Probabilistic Perspective on Wasserstein-Based Evidential Uncertainty 面向 Out-of-Distribution Segmentation

信号显示：语义分割网络在一组固定的类上运行，因此在部署过程中出现不分布（ OOD ）对象时失败，这是自动驾驶等安全关键应用的一个关键限制。关键词：rag、serving、deployment、safety。代码/数据可用性需查看原文确认。

### 5. 评测视频生成的时间一致性和运动真实感

<p class="paper-meta-line"><span>MIRROR: From Imitation to Internalization in LLM Personalization (Huayi Lai, Jicheng Yang, Min Yi, Chong Meng)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.09795">2610.09795</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.09795">PDF</a></p>

中文标题：镜像： LLM个性化从模仿到内化

信号显示：对个性化LLM的需求正在从模仿风格转向内容质量。关键词：serving、alignment、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Why VLMs Miss Small Objects, and When Zooming In Is Safe (Junzhe Shi, Yuan Gan, Shida Jiang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.09313">2610.09313</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.09313">PDF</a></p>

中文标题：为什么VLM会错过小物体，以及何时放大是安全的

信号显示：视觉语言模型（ VLM ）通常会错过大图像中的小物体。关键词：agent、rag、code、vision-language。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Temporal Residual Bottleneck for Robust Asynchronous Collaborative Perception](https://arxiv.org/abs/2610.10090)
中文标题：强大的异步协作感知的时间剩余瓶颈
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Few-Shot Learning for Personalised Automated Pain Assessment](https://arxiv.org/abs/2610.09692)
中文标题：用于个性化自动疼痛评估的少量学习
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Activation-Aware Weight Tensorization: A Calibration-Time Preconditioner for Tensor-Network LLM Compression](https://arxiv.org/abs/2610.10085)
中文标题：激活感知权重张量：张量网络LLM压缩的校准时间预处理器
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Purifying Backdoored Large Vision-Language Models by Removing Hijacked Directions](https://arxiv.org/abs/2610.09941)
中文标题：通过删除被劫持的方向净化后门大视觉语言模型
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Do Better Visual Representations Always Lead to Better End-to-End Autonomous Driving?](https://arxiv.org/abs/2610.09695)
中文标题：更好的视觉表现是否总能带来更好的端到端自动驾驶？
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Coding-Agent Benchmarks Should Match Their Users' Task Flows](https://arxiv.org/abs/2610.09633)
中文标题：Coding-Agent 基准s Should Match Their Users' Task Flows
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models](https://arxiv.org/abs/2610.10526)
中文标题：行动前重新措辞：表征和减轻视觉-语言-行动模型中的语言敏感性
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Safe Meta-Policy Design with Risk Control](https://arxiv.org/abs/2610.10393)
中文标题：具有风险控制功能的安全元策略设计
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [$Δ$Representation: Geometry Supervised Representation Learning of Phenotypes via Counterfactual Reasoning for Medical VLMs](https://arxiv.org/abs/2610.10286)
中文标题：$ Δ $表示：通过医学VLM的反事实推理进行表型的几何监督表示学习
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Geometry-Supervised Visual Representation Learning for Multi-Phenotype Lesion Interpretation in Medical VLMs](https://arxiv.org/abs/2610.10238)
中文标题：医学VLM中多表型病变解释的几何监督视觉表示学习
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [MOTIF: Person-of-Interest Deepfake Detection Beyond 3DMM Coefficients](https://arxiv.org/abs/2610.09830)
中文标题：MOTIF ： 3DMM系数之外的利益相关者Deepfake检测
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Reproducible LLM Inference Benchmarking: A Sequential Isolation Protocol for Regression Testing](https://arxiv.org/abs/2610.09778)
中文标题：可重复LLM推理基准：回归测试的顺序隔离协议
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [AeroEval: Staged Program and Execution Validation for AI-Generated Drone Missions](https://arxiv.org/abs/2610.09764)
中文标题：AeroEval：Staged Program 与 Execution Validation 面向 AI-Generated Drone Missions
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [CircuitGate: Logic-Consistent Circuit-Level Functional Modeling for And-Inverter Graphs](https://arxiv.org/abs/2610.09549)
中文标题：CircuitGate：Logic-Consistent Circuit-Level Functional Modeling 面向 与-Inverter Graphs
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models](https://arxiv.org/abs/2610.09335)
中文标题：SearchWorld ：通过世界模型进行无人机物体搜索的空间价值基础想象
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [QuadTok: Quadtree Visual Tokenizer for Autoregressive Image Generation](https://arxiv.org/abs/2610.10497)
中文标题：QuadTok：Quadtree Visual Tokenizer 面向 Autoregressive Image Generation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Before They Can Solve: Predicting Post-Training Coding-Agent Performance from Base Models](https://arxiv.org/abs/2610.10478)
中文标题：Before They Can Solve：Predicting Post-Training Coding-Agent Performance 来自 Base Models
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [TaoD2C-Bench: Benchmarking MLLMs for Industrial UI Code Generation Beyond Visual Fidelity](https://arxiv.org/abs/2610.10374)
中文标题：TaoD2C-Bench：基准ing MLLMs 面向 Industrial UI Code Generation Beyond Visual Fidelity
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation with User Intent](https://arxiv.org/abs/2610.10355)
中文标题：MIRA：A Musical Intent Refinement Agent 面向 Aligning Text-to-Music Generation with User Intent
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [How Private is Private? A Comparative Study for Face De-Identification](https://arxiv.org/abs/2610.10334)
中文标题：私密性有多高？人脸去识别对比研究
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
