---
title: "让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性"
date: "2026-09-07"
target_date: "2026-09-05"
actual_date: "2026-09-03"
fallback_from: "2026-09-05"
lang: "zh"
slug: "2026-09-07-two-truths-and-a-lie-benchmarking-off"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "code", "data-engineering", "evaluation", "rag", "reasoning", "robotics", "speech-audio", "systems", "training", "video-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "rag", "reasoning", "robotics", "speech-audio", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-09-07-two-truths-and-a-lie-benchmarking-off-sources/"
generated_at: "2026-09-06T22:53:39.549491+00:00"
page_type: "brief"
candidate_count: 405
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Two Truths and A Lie? Benchmarking Off-the-Shelf LLMs for Requirements Quality Assessment: Performance, False Alarms, and Misses", "Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised Dense Video Captioning", "Rethinking On-Policy Distillation of Large Language Models II: One Training Example", "SENTINEL-RL: Offloading Topological Reasoning from LLM Agents in the Security Operations Center", "Hardware-Aware FP4 FlashAttention-4", "A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors"]
featured_paper_urls: ["https://arxiv.org/abs/2609.03230", "https://arxiv.org/abs/2609.04183", "https://arxiv.org/abs/2609.04172", "https://arxiv.org/abs/2609.04159", "https://arxiv.org/abs/2609.04105", "https://arxiv.org/abs/2609.03884"]
featured_paper_titles_zh: ["两个真相和一个谎言？对现成的LLM进行基准测试，以进行要求质量评估：绩效、误报和漏报", "合成前观察： VLM引导的过渡事件发现，用于弱监督密集视频字幕", "重新思考大型语言模型的政策性提炼II ：一个培训示例", "SENTINEL-RL ：从安全运营中心的LLM代理卸载拓扑推理", "硬件感知FP4 FlashAttention-4", "盲目信任，血腥推力：当攻击者控制的钩子更新时，引导AI Agent利用恶意行为"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Two Truths and A Lie? Benchmarking Off-the-Shelf LLMs for Requirements Quality Assessment: Performance, False Alarms, and Misses (Jannatul Shefa, Alejandro Salado, Paul Wach, Taylan G. Topcu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.03230">2609.03230</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.03230">PDF</a></p>

中文标题：两个真相和一个谎言？对现成的LLM进行基准测试，以进行要求质量评估：绩效、误报和漏报

信号显示：需求工程（ RE ）管理系统工程（ SE ）中下游所有内容的质量；在审核周期中存活的缺陷需求会蔓延到设计返工、进度延迟和成本超支。关键词：agent、evaluation、benchmark、eval。代码/数据可用性需查看原文确认。

### 2. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised Dense Video Captioning (Ye-Chan Kim, Seunghee Choi, SeungJu Cha, Si-Woo Kim, Hwiseon Kim, Hyungee Kim, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.04183">2609.04183</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.04183">PDF</a></p>

中文标题：合成前观察： VLM引导的过渡事件发现，用于弱监督密集视频字幕

信号显示：弱监督密集视频字幕旨在对未修剪视频中的多个事件进行本地化和描述，每个视频只提供有序的事件级字幕集。关键词：rag、alignment、vision-language、video。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Rethinking On-Policy Distillation of Large Language Models II: One Training Example (Zixuan Fu, Bingxiang He, Yuxin Zuo, Haohuan Huang, Jinqian Zhang, Ruhang Xiao, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.04172">2609.04172</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.04172">PDF</a></p>

中文标题：重新思考大型语言模型的政策性提炼II ：一个培训示例

信号显示：随机蒸馏（ OPD ）将学生生成的推出与教师的密集令牌级监督相结合。关键词：rag、alignment、post-training、training。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>SENTINEL-RL: Offloading Topological Reasoning from LLM Agents in the Security Operations Center (Uday Vallabhaneni, Cassie L. Cagwin, David J. Wild)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.04159">2609.04159</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.04159">PDF</a></p>

中文标题：SENTINEL-RL ：从安全运营中心的LLM代理卸载拓扑推理

信号显示：大语言模型（ LLM ）代理越来越多地被提议作为自主SOC分析师，但有两个限制使它们在企业规模上不可靠：有限的上下文窗口无法容纳多千主机身份验证图，以及自由形式生成报价。关键词：agent、deployment、code、data。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Hardware-Aware FP4 FlashAttention-4 (Robert Hu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.04105">2609.04105</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.04105">PDF</a></p>

中文标题：硬件感知FP4 FlashAttention-4

信号显示：Blackwell的4位浮点（ FP4 ）张量核不会自动更快地引起注意，因为一旦其矩阵产品收缩， softmax转换和片上依赖性就会占主导地位。关键词：inference、throughput、quantization、systems。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors (Pengxun Li, Litian Zhang, Jianwei Hou, Shujiang Wu, Song Li, Zifeng Kang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.03884">2609.03884</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.03884">PDF</a></p>

中文标题：盲目信任，血腥推力：当攻击者控制的钩子更新时，引导AI Agent利用恶意行为

信号显示：现代AI代理利用暴露生命周期钩子，将shell命令绑定到运行时事件，如会话启动、工具调用和文件编辑。关键词：agent、open-source、tool、agents。代码/数据可用性需查看原文确认。

## 其他值得关注
- [The Shape of Time: Video-Token Contrast for Temporal Understanding in VideoLMs](https://arxiv.org/abs/2609.04110)
中文标题：Shape of Time：Video-Token Contrast 面向 Temporal Understanding in VideoLMs
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Compressing Streaming Neural Audio Encoders via Latent-Space Distillation](https://arxiv.org/abs/2609.04102)
中文标题：通过潜在空间蒸馏压缩流式神经音频编码器
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Subspace Inference Enables Efficient Active Reward Learning from Preferences](https://arxiv.org/abs/2609.04066)
中文标题：子空间推理可实现从偏好中进行有效的主动奖励学习
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [InSituMeasure: Probing Situated Measurement Grounding in Industrial Scenes with Multimodal Large Language Models](https://arxiv.org/abs/2609.04014)
中文标题：InSituMeasure ：使用多模式大型语言模型探测工业场景中的位置测量接地
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Fairness Evaluation of Edge-AI Implementation for Cleft Lip and Palate Speech ASR](https://arxiv.org/abs/2609.03982)
中文标题：Fairness 评测 of Edge-AI Implementation 面向 Cleft Lip 与 Palate Speech ASR
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [RARF: Region-Aware Rectified Flows for 3D Brain MRI Inpainting](https://arxiv.org/abs/2609.03956)
中文标题：RARF：Region-Aware Rectified Flows 面向 3D Brain MRI Inpainting
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [RealCADBench: Benchmarking Parametric CAD Modeling from Industrial Design Intents](https://arxiv.org/abs/2609.03773)
中文标题：RealCADBench：基准ing Parametric CAD Modeling 来自 Industrial Design Intents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?](https://arxiv.org/abs/2609.03715)
中文标题：MINERVA：How Small Can a Manipulation Policy Be 与 Still Solve LIBERO?
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Counterfactual Routing Using Integer Programming with Constraint Generation](https://arxiv.org/abs/2609.03707)
中文标题：使用带约束生成的整数规划的反事实路由
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SignSeek: Learning Transferable Representations for Sign Dictionary Retrieval](https://arxiv.org/abs/2609.03695)
中文标题：SignSeek：Learning Transferable Representations 面向 Sign Dictionary Retrieval
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CoFiE: Coarse-to-Fine Evidence Selection for Efficient Streaming Video Understanding](https://arxiv.org/abs/2609.03675)
中文标题：CoFiE：Coarse-to-Fine Evidence Selection 面向 Efficient Streaming Video Understanding
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Toward Physically Grounded JEPA World Models for Goal-Conditioned Robotic Planning](https://arxiv.org/abs/2609.03565)
中文标题：面向 Physically Grounded JEPA 世界模型 面向 Goal-Conditioned Robotic Planning
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [NeoRed: A Knowledge-Logic-Alignment Multimodal Large Language Model for Neonatal Respiratory Disease Diagnosis](https://arxiv.org/abs/2609.03527)
中文标题：NeoRed：A Knowledge-Logic-Alignment Multimodal Large Language Model 面向 Neonatal Respiratory Disease Diagnosis
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [What Matters for Aggressive Decoding-Time KV Eviction? Temporal Aggregation and Ranking Preservation](https://arxiv.org/abs/2609.03515)
中文标题：激进解码时间KV驱逐的重要性是什么？时间聚合和排名保存
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Lost in Reordering: Structural Sensitivity of Multilingual LLMs under Semantics-Preserving Perturbations](https://arxiv.org/abs/2609.03511)
中文标题：Lost in Reordering ：语义保留扰动下多语言LLM的结构敏感性
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Building and Evaluating Fixed-Voice Thai TTS from Synthetic Speech](https://arxiv.org/abs/2609.03502)
中文标题：Building 与 Evaluating Fixed-Voice Thai TTS 来自 Synthetic Speech
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Towards a Statistical Understanding of Mixture-of-Experts](https://arxiv.org/abs/2609.03501)
中文标题：对Mixture-of-Experts的统计理解
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [BRIDGE: An Open-Source Humanoid Platform via Morphology-Control Co-Design for Physical AI](https://arxiv.org/abs/2609.03497)
中文标题：BRIDGE：An Open-Source Humanoid 平台 via Morphology-Control Co-Design 面向 Physical AI
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [GrowPage: On-Demand KV Budgeting for Efficient LLM Reasoning Serving](https://arxiv.org/abs/2609.03494)
中文标题：GrowPage：On-Demand KV Budgeting 面向 Efficient LLM Reasoning Serving
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [When Retrieval Helps: Selective Retrieval for Single-Turn Mental-Health QA](https://arxiv.org/abs/2609.03454)
中文标题：检索帮助时：一次性心理健康QA的选择性检索
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
