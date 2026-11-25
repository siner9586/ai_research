---
title: "让 Agent 更可靠地调用工具和复用技能"
date: "2026-11-26"
target_date: "2026-11-24"
actual_date: "2026-11-24"
fallback_from: ""
lang: "zh"
slug: "2026-11-26-embodied-ai-fails-the-mirror-test-how"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "robotics", "safety", "speech-audio", "systems", "training", "video-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "robotics", "safety", "speech-audio", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-11-26-embodied-ai-fails-the-mirror-test-how-sources/"
generated_at: "2026-11-25T17:05:33.218530+00:00"
page_type: "brief"
candidate_count: 657
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies", "Not All Interpretation Methods Are Created Equal: Tiered Evaluation of AI Interpretability", "Xtream: An Explicit Metric State for Large-Scale Streaming Reconstruction", "Estimating GPU Roofline Arithmetic Intensity with Off-the-Shelf LLMs and Compiler Artifacts", "C3H: Compression-to-Consensus Criteria Hijacking in Multimodal LLM Recommender Systems", "XMind: Thinking Twice via Cross-Memory Reasoning for LLM-Based Autonomous Driving"]
featured_paper_urls: ["https://arxiv.org/abs/2611.33010", "https://arxiv.org/abs/2611.31833", "https://arxiv.org/abs/2611.31757", "https://arxiv.org/abs/2611.32975", "https://arxiv.org/abs/2611.32780", "https://arxiv.org/abs/2611.32209"]
featured_paper_titles_zh: ["具身人工智能无法通过镜子测试：一面简单的镜子如何打破机器人策略", "Not All Interpretation Methods Are Created Equal：Tiered 评测 of AI Interpretability", "Xtream：An Explicit Metric State 面向 Large-Scale Streaming Reconstruction", "使用现成 LLM 和编译器工件估算 GPU Roofline 算术强度", "C3H：多模态大语言模型推荐系统中的压缩到共识标准劫持", "XMind：Thinking Twice via Cross-Memory Reasoning 面向 基于 LLM 的 Autonomous Driving"]
---

# 让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies (Xuanchen Liu, Hejun Zhang, Boxuan Dong, Ying Wu, Heshuai Li, Wen Gao, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.33010">2611.33010</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.33010">PDF</a></p>

中文标题：具身人工智能无法通过镜子测试：一面简单的镜子如何打破机器人策略

信号显示：一面简单的镜子能否揭示当今机器人操纵策略的局限性？。关键词：agent、rag、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Not All Interpretation Methods Are Created Equal: Tiered Evaluation of AI Interpretability (Nicolas Sanchez, Bin Yu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.31833">2611.31833</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.31833">PDF</a></p>

中文标题：Not All Interpretation Methods Are Created Equal：Tiered 评测 of AI Interpretability

信号显示：随着人工智能向社会技术部署的过渡，不可解释的模型对可靠性、公众信任和可质疑性构成严重威胁。关键词：agent、workflow、deployment、safety。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Xtream: An Explicit Metric State for Large-Scale Streaming Reconstruction (Ernesto Lozano, Alberto Jaenal, Javier Civera)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.31757">2611.31757</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.31757">PDF</a></p>

中文标题：Xtream：An Explicit Metric State 面向 Large-Scale Streaming Reconstruction

信号显示：3D 基础模型（3DFM）能够在前馈传递中实现密集重建，但其有效跨度受到跨视图注意力的限制。关键词：rag、alignment、benchmark、memory。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Estimating GPU Roofline Arithmetic Intensity with Off-the-Shelf LLMs and Compiler Artifacts (Gregory Bolet, Giorgis Georgakoudis, Konstantinos Parasyris, Harshitha Menon, Niranjan Hasabnis, Kirk W. Cameron, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.32975">2611.32975</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.32975">PDF</a></p>

中文标题：使用现成 LLM 和编译器工件估算 GPU Roofline 算术强度

信号显示：GPU 开发人员使用性能分析来了解计算和数据移动情况，但访问目标硬件可能会延迟优化。关键词：agent、latency、code、memory。代码/数据可用性需查看原文确认。

### 5. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>C3H: Compression-to-Consensus Criteria Hijacking in Multimodal LLM Recommender Systems (Guowei Guan, Yurong Hao, Jiaming Zhang, Fuyao Zhang, Wei Yang Bryan Lim)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.32780">2611.32780</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.32780">PDF</a></p>

中文标题：C3H：多模态大语言模型推荐系统中的压缩到共识标准劫持

信号显示：多模态大语言模型（MLLM）正在将推荐系统转变为内容感知型决策系统。关键词：inference、compression、code、multimodal。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>XMind: Thinking Twice via Cross-Memory Reasoning for LLM-Based Autonomous Driving (Zuyi Guo, Xianjie Dai, Lei Yang, Xiaocong Zhao, Jingguang Li, Kitae Jang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.32209">2611.32209</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.32209">PDF</a></p>

中文标题：XMind：Thinking Twice via Cross-Memory Reasoning 面向 基于 LLM 的 Autonomous Driving

信号显示：具备增强记忆的大语言模型（LLM）驱动的智能体可以复用过去的经验，但当交通状况发生变化时，先前学到的修正往往无法迁移。关键词：agent、rag、retrieval、evaluation。代码/数据可用性需查看原文确认。

## 其他值得关注
- [IMPACT-Seg: Consistent Anatomical Segmentation and Representation Learning Across CT, CBCT, and MRI](https://arxiv.org/abs/2611.32903)
中文标题：IMPACT-Seg：Consistent Anatomical Segmentation 与 Representation Learning Across CT，CBCT，与 MRI
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Back to Raw Motion: Latent-Free Diffusion Transformers for Text-to-Motion and Exact Conditional Generation](https://arxiv.org/abs/2611.32793)
中文标题：Back to Raw Motion：Latent-Free Diffusion Transformers 面向 Text-to-Motion 与 Exact Conditional Generation
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [TESS: Query-Guided Temporal Event-Structured Frame Selection for Long-Video Understanding](https://arxiv.org/abs/2611.32410)
中文标题：TESS：Query-Guided Temporal Event-Structured Frame Selection 面向 Long-Video Understanding
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [SoccerNarrate: Event-Grounded Streaming Soccer Commentary with Macro-Window Preference Alignment](https://arxiv.org/abs/2611.32153)
中文标题：SoccerNarrate：基于赛事、具有宏观窗口偏好对齐的足球解说流媒体
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [RISE: Reasoning with Implicit State Embeddings for GUI Agents](https://arxiv.org/abs/2611.32102)
中文标题：RISE：使用隐式状态嵌入进行推理的 GUI 代理
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [RepoEviAgent: Scalable Synthesis of Evidence-Grounded Repository-Level Question Answering Tasks](https://arxiv.org/abs/2611.31873)
中文标题：RepoEviAgent：可扩展 Synthesis of Evidence-Grounded Repository-Level Question Answering Tasks
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [VISOR: A Vision-Language Selector for Multimodal Time-Series Forecasting](https://arxiv.org/abs/2611.31780)
中文标题：VISOR：A Vision-Language Selector 面向 Multimodal Time-Series Forecasting
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ROAM-Bench: Evaluating Embodied Active Spatial Intelligence through Evidence Verification](https://arxiv.org/abs/2611.33143)
中文标题：ROAM-Bench：通过证据验证评估具身主动空间智能
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SALSA: Sampling Adversarial Suffixes from Learned Distributions for LLM Safety Assessment](https://arxiv.org/abs/2611.33030)
中文标题：SALSA：Sampling Adversarial Suffixes 来自 Learned Distributions 面向 LLM Safety 评估
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Beyond Static Semantics: Instance-Adaptive Vision-Language Alignment for Building Damage Assessment](https://arxiv.org/abs/2611.32777)
中文标题：超越静态语义：用于建筑物损毁评估的实例自适应视觉-语言对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [MargEmbed-Akan: Bridging Twi Questions and English Knowledge through Cross-Lingual Score Distillation](https://arxiv.org/abs/2611.32630)
中文标题：MargEmbed-Akan：Bridging Twi Questions 与 English Knowledge through Cross-Lingual Score Distillation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ViTacLab: Physically Consistent Visuo-Tactile Simulation, Benchmarking, and Representation Learning for Robotic Manipulation](https://arxiv.org/abs/2611.32476)
中文标题：ViTacLab：Physically Consistent Visuo-Tactile Simulation，基准ing，与 Representation Learning 面向 Robotic Manipulation
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [DiCT: Teaching X-ray Vision-Language Models to Reason via Imagining CT](https://arxiv.org/abs/2611.32344)
中文标题：DiCT：通过想象CT来训练X射线视觉-语言模型进行推理
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Query-Guided Visual Minimization for Selective Disclosure to Cloud VLMs](https://arxiv.org/abs/2611.32302)
中文标题：针对云端 VLM 的选择性披露的查询引导式视觉最小化
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [From Memory Access to Evidence Sufficiency: Diagnosing and Addressing Demand--Evidence Misalignment](https://arxiv.org/abs/2611.32088)
中文标题：从记忆提取到证据充分性：诊断和解决需求与证据不匹配的问题
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [BEARING: Who Is Talking to Whom? Grounding Acoustic Direction in Vision for Online Multi-Party Conversation](https://arxiv.org/abs/2611.31735)
中文标题：方位：谁在和谁说话？将声音方向与视觉相结合，用于在线多方对话
关注理由：涉及语音与音频中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](https://arxiv.org/abs/2611.33145)
中文标题：校园迷路：评估视觉-语言模型在真实环境中的具身空间推理能力
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MetaFORGE: A Meta-Learning Framework for Harness Optimization in Automated Code Generation for Parallel Computing](https://arxiv.org/abs/2611.33119)
中文标题：MetaFORGE：A Meta-Learning 框架 面向 Harness Optimization in Automated Code Generation 面向 Parallel Computing
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Understanding Clipping In Zeroth-Order Optimization](https://arxiv.org/abs/2611.33062)
中文标题：了解零阶优化中的截断
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [E-MAPS: Event-Based Promptable Video Segmentation with Memory-as-Prompt](https://arxiv.org/abs/2611.33017)
中文标题：E-MAPS：基于事件的“以记忆为提示”可提示视频分割
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
