---
title: "让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力"
date: "2026-10-17"
target_date: "2026-10-15"
actual_date: "2026-10-15"
fallback_from: ""
lang: "zh"
slug: "2026-10-17-dialfork-going-beyond-factuality-to-evaluate-procedural"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "interpretability", "multimodal", "rag", "reasoning", "robotics", "safety", "systems", "training", "video-generation", "vision-generation"]
topics: ["agents", "code", "evaluation", "interpretability", "multimodal", "rag", "reasoning", "robotics", "safety", "systems", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-10-17-dialfork-going-beyond-factuality-to-evaluate-procedural-sources/"
generated_at: "2026-10-16T23:32:33.116385+00:00"
page_type: "brief"
candidate_count: 611
featured_count: 6
mentions_count: 20
featured_paper_titles: ["DialFork: Going Beyond Factuality to Evaluate Procedural Hallucination in Conversational Agents", "Federated Art Chase: Privacy Leakage and Data Poisoning in Federated Fine-Tuning", "RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent", "Where, How, and When: Query-Guided Grounding for Video Understanding", "PocketTSLM: Deploying an On-Device Soft-Prompt Time-Series Language Model for Privacy-Preserving Smartphone Reasoning", "VALCON: Benchmarking and Enhancing Value Consistency in Large Language Models via Dual-Role Variation"]
featured_paper_urls: ["https://arxiv.org/abs/2610.21561", "https://arxiv.org/abs/2610.21547", "https://arxiv.org/abs/2610.21791", "https://arxiv.org/abs/2610.21422", "https://arxiv.org/abs/2610.21308", "https://arxiv.org/abs/2610.21304"]
featured_paper_titles_zh: ["DialFork ：超越事实，评估对话代理的程序性幻觉", "联合艺术追逐：联合微调中的隐私泄露和数据中毒", "RSIFlow ：使用不断发展的元代理的自适应自我改进工作流程", "地点、方式和时间：视频理解的查询引导基础", "PocketTSLM：Deploying an On-Device Soft-Prompt Time-Series Language Model 面向 隐私保护 Smartphone Reasoning", "VALCON ：通过双角色变异在大型语言模型中进行基准测试并提高价值一致性"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>DialFork: Going Beyond Factuality to Evaluate Procedural Hallucination in Conversational Agents (Sergio Burdisso, Esaú Villatoro-Tello, Dairazalia Sánchez-Cortés, Yanis Labrak, Jordi Luque, Milos Cernak, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.21561">2610.21561</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.21561">PDF</a></p>

中文标题：DialFork ：超越事实，评估对话代理的程序性幻觉

信号显示：作为会话代理部署的大语言模型（ LLM ）越来越被期望遵循程序逻辑。关键词：agent、retrieval、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 2. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Federated Art Chase: Privacy Leakage and Data Poisoning in Federated Fine-Tuning (Vasileios Perifanis, Nikolaos Pavlidis)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.21547">2610.21547</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.21547">PDF</a></p>

中文标题：联合艺术追逐：联合微调中的隐私泄露和数据中毒

信号显示：联合学习（ FL ）越来越多地用于使预训练、集中微调的模型适应用户设备上的数据，而不是从头开始训练模型。关键词：serving、code、fine-tuning、training。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent (Huan Zhang, Mingju Chen, Dongxu Zhou, Can Lv, Sen Cui, Faguo Wu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.21791">2610.21791</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.21791">PDF</a></p>

中文标题：RSIFlow ：使用不断发展的元代理的自适应自我改进工作流程

信号显示：大语言模型（ LLM ）客服代表在代码生成、工具使用和多跳问答等复杂任务中表现出强大的能力。关键词：agent、tool use、workflow、rag。代码/数据可用性需查看原文确认。

### 4. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Where, How, and When: Query-Guided Grounding for Video Understanding (Yogesh Kumar)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.21422">2610.21422</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.21422">PDF</a></p>

中文标题：地点、方式和时间：视频理解的查询引导基础

信号显示：了解视频内容需要在多个粒度级别进行推理，从识别对象到解释它们的互动以及在特定操作发生时进行本地化。关键词：retrieval、alignment、code、memory。代码/数据可用性需查看原文确认。

### 5. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>PocketTSLM: Deploying an On-Device Soft-Prompt Time-Series Language Model for Privacy-Preserving Smartphone Reasoning (Max Rosenblattl, Nikhil Krishnaswamy, Leon Nissen, Manuel Milling, Nicolas Zumarraga, Ning Wang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.21308">2610.21308</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.21308">PDF</a></p>

中文标题：PocketTSLM：Deploying an On-Device Soft-Prompt Time-Series Language Model 面向 隐私保护 Smartphone Reasoning

信号显示：消费手机和可穿戴设备越来越多地收集生理时间序列数据，但大多数移动系统将这些数据流视为摘要或文本，而不是时间证据。关键词：inference、serving、deployment、latency。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>VALCON: Benchmarking and Enhancing Value Consistency in Large Language Models via Dual-Role Variation (Junru Wu, Jingting Zheng, Yuqi Ren, Deyi Xiong)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.21304">2610.21304</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.21304">PDF</a></p>

中文标题：VALCON ：通过双角色变异在大型语言模型中进行基准测试并提高价值一致性

信号显示：大语言模型（ LLM ）的当前值一致性评估严重依赖输出合规性，忽略了LLM在生成器和评估器角色之间交替时是否保持价值一致性。关键词：agent、alignment、evaluation、benchmark。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Learning Self-Orchestration in Decentralized Agent Swarms](https://arxiv.org/abs/2610.22322)
中文标题：在去中心化Agent群中学习自编排
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Onboard Lightweight LLM Reasoning for Human-Aware Safe UAV Navigation](https://arxiv.org/abs/2610.22092)
中文标题：用于人性化安全无人机导航的机载轻量级LLM推理
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [ETH: Data-Balanced Heterogeneous Pipeline Parallelism for Training Large Models](https://arxiv.org/abs/2610.22035)
中文标题：ETH：Data-Balanced Heterogeneous Pipeline Parallelism 面向 Training Large Models
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MetaShare: Failure-Aware Collective Self-Improvement for Open-Ended Agents](https://arxiv.org/abs/2610.21887)
中文标题：MetaShare：Failure-Aware Collective Self-Improvement 面向 Open-Ended Agents
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [AgentPerturb: Evaluating LLM Agent Robustness under Controlled Interaction Perturbations](https://arxiv.org/abs/2610.21624)
中文标题：AgentPerturb ：评估受控交互扰动下的LLM专员鲁棒性
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition](https://arxiv.org/abs/2610.21565)
中文标题：BiShield-TEE ：关于TEE屏蔽LLM隔板中单侧重量混淆的（内部）安全性
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning](https://arxiv.org/abs/2610.22194)
中文标题：AutoSFT：An Agentic System 面向 Automated Data Research in Supervised Fine-Tuning
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [CLUE: Uncovering Social Context for Pragmatic Understanding](https://arxiv.org/abs/2610.22167)
中文标题：线索：揭示务实理解的社会背景
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [FALCON: FPGA-Accelerated Latency-Certifiable Occupancy Networks for Camera-Based Autonomous Driving](https://arxiv.org/abs/2610.22143)
中文标题：FALCON：FPGA-Accelerated Latency-Certifiable Occupancy Networks 面向 Camera-Based Autonomous Driving
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Are You Sure Your LLM Is Sure? Repairing and Auditing Confidence](https://arxiv.org/abs/2610.22139)
中文标题：你确定你的LLM是肯定的吗？维修和审核置信度
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [CIM-Embed: Learning Instruction-Conditioned Multimodal Embeddings for Clustering](https://arxiv.org/abs/2610.21805)
中文标题：CIM-Embed：Learning Instruction-Conditioned Multimodal Embeddings 面向 Clustering
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ContextLift: Breaking the Spurious Correlation Behind Conditional Emergent Misalignment](https://arxiv.org/abs/2610.21633)
中文标题：ContextLift ：打破条件性紧急错位背后的虚假关联
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Decoding What iOS Location Services Send to Apple: An LLM Is an Unreliable Analyst but a Useful Toolmaker](https://arxiv.org/abs/2610.21597)
中文标题：解码iOS定位服务发送给Apple的内容： LLM是一个不可靠的分析师，但却是一个有用的工具制造商
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Decoupled Safety Control: A Safety-Control Algorithm for Training-Free Safety Guidance](https://arxiv.org/abs/2610.21569)
中文标题：解耦安全控制：无需培训的安全指导的安全控制算法
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Loud and Clear: Making Visual Evidence Count in Multimodal Document RAG](https://arxiv.org/abs/2610.21318)
中文标题：响亮而清晰：在多式联运文件RAG中计算视觉证据
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [TimeCap: A Scalable Open-Source Pipeline for Captioning Wearable Health Time-Series Data](https://arxiv.org/abs/2610.21274)
中文标题：TimeCap：A 可扩展 Open-Source Pipeline 面向 Captioning Wearable Health Time-Series Data
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [System1-Arena: Which Decisions Can Be Left to System 1?](https://arxiv.org/abs/2610.21244)
中文标题：System1-Arena ：哪些决策可以留给System1 ？
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Representation Redistribution in Sparse Autoencoders](https://arxiv.org/abs/2610.21240)
中文标题：稀疏自动编码器中的表示重分布
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Who May Release an Agent's Promise? Standing over Commitments in Multi-Party Chat](https://arxiv.org/abs/2610.21203)
中文标题：谁可以放弃代理的承诺？在多方聊天中兑现承诺
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [When is a better LLM worth paying for? Stochastic Optimization with Switching Mixed-Fidelity Oracles](https://arxiv.org/abs/2610.21139)
中文标题：什么时候更好的LLM值得付费？使用切换混合保真预言机的随机优化
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
