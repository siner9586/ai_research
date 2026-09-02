---
title: "让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力"
date: "2026-09-03"
target_date: "2026-09-01"
actual_date: "2026-09-01"
fallback_from: ""
lang: "zh"
slug: "2026-09-03-compile-don-t-memorize-a-context-compilation"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力、提升代码生成、执行反馈和自动修复能力。"
tags: ["agents", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "robotics", "safety", "training", "vision-generation"]
topics: ["agents", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "robotics", "safety", "training", "vision-generation"]
sources_page: "/zh/daily/2026-09-03-compile-don-t-memorize-a-context-compilation-sources/"
generated_at: "2026-09-02T23:17:36.591645+00:00"
page_type: "brief"
candidate_count: 486
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Compile, Don't Memorize: A Context Compilation Architecture (CCA) for In-Context Learning", "Benchmarking Spatial, Spectral, and Self-Supervised Cues for Face Forgery Detection under Realistic Degradation", "RadMatch: Auditable Radiology Report Evaluation via Finding-Level Matching", "Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds", "On the Design Fundamentals of Pixel Text Representation Learning", "P-PatchDiff: Progressive Patch Diffusion Models for Low-light Image Enhancement"]
featured_paper_urls: ["https://arxiv.org/abs/2609.00759", "https://arxiv.org/abs/2609.01511", "https://arxiv.org/abs/2609.01470", "https://arxiv.org/abs/2609.01453", "https://arxiv.org/abs/2609.01147", "https://arxiv.org/abs/2609.01123"]
featured_paper_titles_zh: ["Compile，Don't Memorize：A Context Compilation Architecture (CCA) 面向 In-Context Learning", "对真实退化下的面部伪造检测的空间、光谱和自我监督线索进行基准测试", "RadMatch ：通过发现级匹配进行可审核放射学报告评估", "模仿学习是否在灵巧操纵中保持了时间鲁棒性？跨任务执行速度的专家学习者比较", "论像素文本表示学习的设计基础", "P-PatchDiff：Progressive Patch Diffusion Models 面向 Low-light Image Enhancement"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力、提升代码生成、执行反馈和自动修复能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Compile, Don&#x27;t Memorize: A Context Compilation Architecture (CCA) for In-Context Learning (Jinhu Qi, Minda Hu, Wentao Zhang, Weiqiang Jin, Yanyu Chen, Junli Wang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.00759">2609.00759</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.00759">PDF</a></p>

中文标题：Compile，Don't Memorize：A Context Compilation Architecture (CCA) 面向 In-Context Learning

信号显示：大语言模型（ LLM ）越来越多地处理上下文学习（ ICL ）任务，其中冗长、新颖的上下文定义了一系列问题的规则、知识和输出模式。关键词：agent、retrieval、benchmark、code。代码/数据可用性需查看原文确认。

### 2. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Benchmarking Spatial, Spectral, and Self-Supervised Cues for Face Forgery Detection under Realistic Degradation (Lucas Cunha, Lucas Sotomaior, Lucas Gasperin, Beatriz Caldas, Eduardo Pianovski, Rayson Laroca)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.01511">2609.01511</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.01511">PDF</a></p>

中文标题：对真实退化下的面部伪造检测的空间、光谱和自我监督线索进行基准测试

信号显示：人脸伪造检测仪通常在受控基准上取得强劲结果，但其在真实图像退化下的可靠性仍然有限。关键词：compression、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 3. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>RadMatch: Auditable Radiology Report Evaluation via Finding-Level Matching (Charles Corbière, Léo Machado, Aubin Charley, Baptiste Callard, Pierre Manceron, Corentin Dancette)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.01470">2609.01470</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.01470">PDF</a></p>

中文标题：RadMatch ：通过发现级匹配进行可审核放射学报告评估

信号显示：随着人工智能系统越来越多地用于起草放射学报告，可靠地评估其临床质量仍然是一个关键挑战。关键词：deployment、safety、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 4. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds (Clinton Enwerem, John S. Baras, Calin Belta)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.01453">2609.01453</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.01453">PDF</a></p>

中文标题：模仿学习是否在灵巧操纵中保持了时间鲁棒性？跨任务执行速度的专家学习者比较

信号显示：通过模仿学习的灵巧操纵策略通常会被评估为对场景、对象或指令变化的鲁棒性，但它们在任务执行速度上的表现不太经常被检查。关键词：alignment、evaluation、code、robot。代码/数据可用性需查看原文确认。

### 5. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>On the Design Fundamentals of Pixel Text Representation Learning (Chaohao Yuan, Ruifeng Yuan, Zhuoxu Huang, Yu Rong, Hong Cheng, Hou Pong Chan, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.01147">2609.01147</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.01147">PDF</a></p>

中文标题：论像素文本表示学习的设计基础

信号显示：文本丰富的视觉输入需要能够直接在像素空间中读取、检索和压缩语言的模型，但现有的像素文本编码器难以解决固定分辨率预训练、视觉快捷学习、弱视觉接地和多语言视觉。关键词：compression、alignment、evaluation、code。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>P-PatchDiff: Progressive Patch Diffusion Models for Low-light Image Enhancement (Ruoyu Guo, Haonan Zhong, Maurice Pagnucco, Yang Song)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.01123">2609.01123</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.01123">PDF</a></p>

中文标题：P-PatchDiff：Progressive Patch Diffusion Models 面向 Low-light Image Enhancement

信号显示：弱光图像增强的最新进展利用了扩散模型，因为它们具有生成感知逼真、细致图像的强大能力。关键词：rag、alignment、code、memory。代码/数据可用性需查看原文确认。

## 其他值得关注
- [One Prompt Is Enough: Watermark Laundering Through Foundation Image Models](https://arxiv.org/abs/2609.01249)
中文标题：一个提示就足够了：通过基础图像模型进行水印清洗
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Dotting the Eye: An Intent-Driven Image Retouching Agent for Visual Focus Enhancement](https://arxiv.org/abs/2609.01148)
中文标题：Dotting the Eye：An Intent-Driven Image Retouching Agent 面向 视觉聚焦 Enhancement
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Post-hoc Alignment of LLM-judges to Human Judgment Distribution](https://arxiv.org/abs/2609.01073)
中文标题：LLM评委与人类判断分布的事后一致性
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [On-the-Fly3R: Towards Robust Online 3D Reconstruction with Feed-Forward 3R Models for Large-Scale UAV Scenarios](https://arxiv.org/abs/2609.00923)
中文标题：On-the-Fly3R：Towards Robust Online 3D Reconstruction with Feed-Forward 3R Models 面向 Large-Scale UAV Scenarios
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [A multicenter benchmark and clinically structured metric for coronary CTA report generation](https://arxiv.org/abs/2609.00909)
中文标题：一种multicenter 基准 与 clinically structured metric 面向 coronary CTA report generation
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Escaping Redundant Reasoning: Structure-Aware Search for Inference-Time LLMs](https://arxiv.org/abs/2609.00738)
中文标题：逃避冗余推理：结构感知搜索推理时间LLM
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [SCoNE: Selective Context-aware Neuron Editing for Robust Retrieval-Augmented Generation](https://arxiv.org/abs/2609.00689)
中文标题：SCoNE：Selective Context-aware Neuron Editing 面向 Robust Retrieval-Augmented Generation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [DGNet: Dual-knowledge Guided Network for Infrared Small Target Detection](https://arxiv.org/abs/2609.00666)
中文标题：DGNet：Dual-knowledge Guided Network 面向 Infrared Small Target Detection
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [REVISE: Validity-Guided Recovery for Online Revisions in Agent Workflows](https://arxiv.org/abs/2609.00643)
中文标题：REVISE：Validity-Guided Recovery 面向 Online Revisions in Agent Workflows
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [EM^2Mem: Event-Centric Multimodal Memory for Large Language Models](https://arxiv.org/abs/2609.00551)
中文标题：EM^2Mem：Event-Centric Multimodal Memory 面向 Large Language Models
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Closing Cost-Quality Gap in Document VLMs: Difficulty-Aware Data Curation and Quality-Adjusted Deployment Economics](https://arxiv.org/abs/2609.01575)
中文标题：缩小文档VLM的成本-质量差距：难度感知数据整理和质量调整的部署经济学
关注理由：涉及数据工程中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Gradient-Update Mismatch: Rethinking Conflict-Free Training of Physics-Informed Neural Networks](https://arxiv.org/abs/2609.01558)
中文标题：梯度-更新不匹配：重新思考物理知情神经网络的无冲突训练
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Bandits in Prod: Hyperparameter Optimization at Inference Time](https://arxiv.org/abs/2609.01335)
中文标题：PROD中的Bandits ：推理时间的超参数优化
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [CopyShield: A Cross-Level Benchmark of Copyright Defenses in LLMs](https://arxiv.org/abs/2609.01161)
中文标题：CopyShield：A Cross-Level 基准 of Copyright Defenses in LLMs
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [HiveTraceGuard-Pro: A Compact Generative Guardrail for Prompt Injection, Jailbreaks, and Adversarial Obfuscation](https://arxiv.org/abs/2609.01046)
中文标题：HiveTraceGuard-Pro：A Compact Generative Guardrail 面向 Prompt Injection，Jailbreaks，与 Adversarial Obfuscation
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [ReFlowSET: Representation-Aligned Latent Flow Matching for SAR-to-EO Image Translation](https://arxiv.org/abs/2609.00968)
中文标题：ReFlowSET：Representation-Aligned Latent Flow Matching 面向 SAR-to-EO Image Translation
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Candidate-Expanding Routing with Permutation-Stabilized Experts for Mixed-Format Medical VQA](https://arxiv.org/abs/2609.00959)
中文标题：针对混合格式医疗VQA的排列稳定专家的候选人扩展路由
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Differentially Private Paired Table-Image Multimodal Synthesis](https://arxiv.org/abs/2609.00708)
中文标题：差异化私有配对表图像多模态合成
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Trust Your Guide Only When Certain: Uncertainty-Aware Sparse Alignment at Inference Time](https://arxiv.org/abs/2609.00624)
中文标题：仅在确定时才信任您的向导：在推理时具有不确定性感知的稀疏对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation](https://arxiv.org/abs/2609.01603)
中文标题：通过轨迹感知评估进行高效的SWE Agent基准测试
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
