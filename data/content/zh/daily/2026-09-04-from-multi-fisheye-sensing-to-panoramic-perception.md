---
title: "提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-09-04"
target_date: "2026-09-02"
actual_date: "2026-09-02"
fallback_from: ""
lang: "zh"
slug: "2026-09-04-from-multi-fisheye-sensing-to-panoramic-perception"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "safety", "speech-audio", "training", "video-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "safety", "speech-audio", "training", "video-generation"]
sources_page: "/zh/daily/2026-09-04-from-multi-fisheye-sensing-to-panoramic-perception-sources/"
generated_at: "2026-09-03T23:15:19.255506+00:00"
page_type: "brief"
candidate_count: 355
featured_count: 6
mentions_count: 20
featured_paper_titles: ["From Multi-Fisheye Sensing to Panoramic Perception: A Parallax-Aware Onboard Platform for Ultra-Low-Altitude UAVs", "H3DNAS: Hardware-Aware ONNX-Native 3D Point Cloud Model Compression", "Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds", "Bilevel Coordinated Reflection: A Game-Theoretic Approach to Multi-Agent LLM Systems", "Removing Speech, Keeping Activities: A Privacy Firewall for Acoustic Sensing in Assisted Living", "YesTrack: Referring Multi-Object Tracking via MLLM-based Yes/No Verification"]
featured_paper_urls: ["https://arxiv.org/abs/2609.02319", "https://arxiv.org/abs/2609.02684", "https://arxiv.org/abs/2609.02302", "https://arxiv.org/abs/2609.02750", "https://arxiv.org/abs/2609.02376", "https://arxiv.org/abs/2609.02318"]
featured_paper_titles_zh: ["从多鱼眼感知到全景感知：超低空无人机的视差感知机载平台", "H3DNAS ：硬件感知ONNX原生3D点云模型压缩", "利用推理时间计算和部署支架提高评估真实性", "双层协调反思：多Agent LLM系统的博弈论方法", "消除言语，保持活动：辅助生活中声音传感的隐私防火墙", "YesTrack ：通过基于MLLM的Yes/No验证引用多对象跟踪"]
---

# 提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>From Multi-Fisheye Sensing to Panoramic Perception: A Parallax-Aware Onboard Platform for Ultra-Low-Altitude UAVs (Dun Dai, Ze Lu, Cheng He, Yaowen Wang, Quan Quan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.02319">2609.02319</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.02319">PDF</a></p>

中文标题：从多鱼眼感知到全景感知：超低空无人机的视差感知机载平台

信号显示：超低空无人机（ UAV ）需要在建筑物、植被和其他障碍物附近进行环绕视觉。关键词：alignment、evaluation、open-source、eval。代码/数据可用性需查看原文确认。

### 2. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>H3DNAS: Hardware-Aware ONNX-Native 3D Point Cloud Model Compression (Anchit Mulye, Rhythm Baghel, Sujay Kumar Ingle, Hardik Jain)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.02684">2609.02684</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.02684">PDF</a></p>

中文标题：H3DNAS ：硬件感知ONNX原生3D点云模型压缩

信号显示：在NVIDIA Jetson Orin Nano等边缘硬件上部署3D点云模型受到计算和内存预算的严重制约。关键词：inference、compression、code、memory。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds (Axel Ahlqvist, Richard Guan, Juan-Pablo Rivera, Adeline Kassler, Dmitrii Troitskii, Alexandra Souly, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.02302">2609.02302</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.02302">PDF</a></p>

中文标题：利用推理时间计算和部署支架提高评估真实性

信号显示：对齐评估的一个核心障碍是评估意识：有能力的模型可以告诉他们何时正在测试而不是部署，从而削弱了安全评估可以支持的结论。关键词：agent、inference、deployment、alignment。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Bilevel Coordinated Reflection: A Game-Theoretic Approach to Multi-Agent LLM Systems (Yihang Chen, Yuxiang Chen, Yuxuan Huang, Meng Fang, Weilin Luo, Jun Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.02750">2609.02750</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.02750">PDF</a></p>

中文标题：双层协调反思：多Agent LLM系统的博弈论方法

信号显示：多代理LLM系统通常使用编排器来分解工作团队的任务，然后通过文本反思进行改进。关键词：agent、evaluation、code、memory。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Removing Speech, Keeping Activities: A Privacy Firewall for Acoustic Sensing in Assisted Living (Pavlos Nicolaou, Christos Efstratiou)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.02376">2609.02376</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.02376">PDF</a></p>

中文标题：消除言语，保持活动：辅助生活中声音传感的隐私防火墙

信号显示：声学传感为监控老年人的日常活动提供了一种有前途的非侵入式方法，但语音隐私问题仍然是现实世界部署的关键障碍。关键词：serving、deployment、evaluation、code。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>YesTrack: Referring Multi-Object Tracking via MLLM-based Yes/No Verification (Quansheng Hu, Qin Sun, Qiansen Dai, Jin Ding, Wan Zhang, Xue Zhou, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.02318">2609.02318</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.02318">PDF</a></p>

中文标题：YesTrack ：通过基于MLLM的Yes/No验证引用多对象跟踪

信号显示：引用多对象跟踪（ RMOT ）旨在跟踪视频中与给定语言表达式匹配的每个实例。关键词：rag、latency、alignment、code。代码/数据可用性需查看原文确认。

## 其他值得关注
- [If It Moves, Radar Knows: A Physics-Aware Radar Transformer for Class-Agnostic Moving-Object Detection](https://arxiv.org/abs/2609.02289)
中文标题：If It Moves，Radar Knows：A Physics-Aware Radar Transformer 面向 Class-Agnostic Moving-Object Detection
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails](https://arxiv.org/abs/2609.02246)
中文标题：LLM-as-a-Judge不是神谕：为什么自我完善的代理人需要确定性的护栏
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [TAME: Temporal-Aware Mixture-of-Experts for Text-Video Retrieval](https://arxiv.org/abs/2609.02204)
中文标题：TAME：Temporal-Aware Mixture-of-Experts 面向 Text-Video Retrieval
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Beyond Modality Harmony: Orthogonal Purification and Topology-Guided MoE for Conflict-Aware Multimodal Recommendation](https://arxiv.org/abs/2609.02152)
中文标题：Beyond Modality Harmony：Orthogonal Purification 与 Topology-Guided MoE 面向 Conflict-Aware Multimodal Recommendation
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Transfer Safety Awareness for Cross-Modal Safety Drift in Multimodal Large Language Models](https://arxiv.org/abs/2609.02082)
中文标题：多式联运大型语言模型中跨模式安全漂移的转移安全意识
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Benchmarking RAW and RGB Restoration in Image Signal Processors](https://arxiv.org/abs/2609.02831)
中文标题：基准ing RAW 与 RGB Restoration in Image Signal Processors
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [SPADE: SPaT Attack Detection from the Connected Vehicle's Perspective](https://arxiv.org/abs/2609.02741)
中文标题：SPADE ：从联网车辆的角度进行SPaT攻击检测
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Rethinking the Teacher-Student Framework for Test-Time Adaptation](https://arxiv.org/abs/2609.02507)
中文标题：重新思考教师-学生的考试时间适应框架
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SCX Router: Streaming Zero-Shot Model Selection with a Decoder-KV Classifier and a Real-World Task Ontology](https://arxiv.org/abs/2609.02292)
中文标题：SCX路由器：使用解码器-KV分类器和真实任务本体进行流式零拍摄模型选择
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Signal or Noise? Auditing Rotation-Induced Saliency Drift in Medical and Aerial Imaging](https://arxiv.org/abs/2609.02224)
中文标题：信号或噪声？审核医疗和航空成像中的旋转诱导的显著性漂移
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [DynG-Diff: A State-Aware Dynamic Guidance Diffusion Framework for Probabilistic Time Series Forecasting](https://arxiv.org/abs/2609.02068)
中文标题：DynG-Diff：A State-Aware Dynamic Guidance Diffusion 框架 面向 Probabilistic Time Series Forecasting
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Train What You Deploy: Closing the MLP Reachability Gap in Low-Rank Clone Distillation](https://arxiv.org/abs/2609.02006)
中文标题：培训您部署的内容：缩小低排名克隆蒸馏中的MLP可达性差距
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [GRADSOLVE: fast exact gradients for ODE ensembles on GPUs](https://arxiv.org/abs/2609.02876)
中文标题：GRADSOLVE：fast exact gradients 面向 ODE ensembles on GPUs
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment](https://arxiv.org/abs/2609.02786)
中文标题：SafeEvolve：Harness-Policy Co-Evolution 来自 Agent Experience 面向 Safety Alignment
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding](https://arxiv.org/abs/2609.02780)
中文标题：ShallowStream：Index Shallow then Answer Deep 面向 Streaming Video Understanding
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Video-Based Palm-Vein Authentication under Challenging Conditions](https://arxiv.org/abs/2609.02776)
中文标题：挑战条件下基于视频的Palm-Vein身份验证
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation](https://arxiv.org/abs/2609.02774)
中文标题：CodePoisonRAG ：检索增强代码生成中的知识中毒攻击
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [RVSD: Retrieval Vision Sparse Decoding for Mitigating Visual Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2609.02731)
中文标题：RVSD：Retrieval Vision Sparse Decoding 面向 Mitigating Visual Hallucinations in Large Vision-Language Models
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CORAL: An LLM-Native Harness for Production Recommender Systems](https://arxiv.org/abs/2609.02730)
中文标题：CORAL：An LLM-Native Harness 面向 Production Recommender Systems
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations](https://arxiv.org/abs/2609.02664)
中文标题：四维高斯表示中复杂对象分割的查询重写
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
