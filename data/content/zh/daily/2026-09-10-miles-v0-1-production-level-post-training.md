---
title: "让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、改进图像生成、视觉理解和可控渲染"
date: "2026-09-10"
target_date: "2026-09-08"
actual_date: "2026-09-08"
fallback_from: ""
lang: "zh"
slug: "2026-09-10-miles-v0-1-production-level-post-training"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "robotics", "safety", "systems", "training"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "robotics", "safety", "systems", "training"]
sources_page: "/zh/daily/2026-09-10-miles-v0-1-production-level-post-training-sources/"
generated_at: "2026-09-09T23:11:08.982566+00:00"
page_type: "brief"
candidate_count: 398
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Miles v0.1: Production-Level Post-Training", "ExecCritic: Learn to Test, Test to Improve for Coding Agents", "From Coordinates to Candidate Regions: Temporal Change Localization via Region Selection in Remote Sensing Multimodal LLMs", "Supervised Cross-Modal Feature Alignment for Zero-Wearable Freezing of Gait Detection in Parkinsonism", "What Eviction Destroys: A Restore-Counterfactual Audit of Forgetting in Agent Memory", "SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?"]
featured_paper_urls: ["https://arxiv.org/abs/2609.08368", "https://arxiv.org/abs/2609.09133", "https://arxiv.org/abs/2609.08391", "https://arxiv.org/abs/2609.08317", "https://arxiv.org/abs/2609.08279", "https://arxiv.org/abs/2609.09113"]
featured_paper_titles_zh: ["Miles v0.1 ：生产级培训后", "ExecCritic：Learn to Test，Test to Improve 面向 Coding Agents", "从坐标到候选区域：通过遥感多模态LLM中的区域选择进行时间变化定位", "用于帕金森氏症中步态检测的零穿戴式冻结的监督交叉模式特征对齐", "驱逐摧毁了什么：对代理记忆中遗忘的恢复-反事实审计", "SAEScientist-Bench ：人工智能代理可以进行自主SAE可解释性研究吗？"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、改进图像生成、视觉理解和可控渲染

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Miles v0.1: Production-Level Post-Training (RadixArk, :, Tom Chen, Mao Cheng, Shi Dong, Kangrui Du, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.08368">2609.08368</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.08368">PDF</a></p>

中文标题：Miles v0.1 ：生产级培训后

信号显示：我们推出了Miles v0.1 ，这是一个用于前沿后培训的全栈生产就绪系统。关键词：agent、deployment、alignment、fine-tuning。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>ExecCritic: Learn to Test, Test to Improve for Coding Agents (Leitian Tao, Baolin Peng, Haorui Wang, Hang Wang, Hao Cheng, Wenlin Yao, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.09133">2609.09133</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.09133">PDF</a></p>

中文标题：ExecCritic：Learn to Test，Test to Improve 面向 Coding Agents

信号显示：执行反馈可以引导编码代理进行正确的存储库修复，但仅当测试捕获问题请求的行为时。关键词：agent、evaluation、code、post-training。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>From Coordinates to Candidate Regions: Temporal Change Localization via Region Selection in Remote Sensing Multimodal LLMs (Juwan Chung, Sungjune Park, Yeongyun Kim, Yong Man Ro)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.08391">2609.08391</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.08391">PDF</a></p>

中文标题：从坐标到候选区域：通过遥感多模态LLM中的区域选择进行时间变化定位

信号显示：遥感多模态大语言模型（ RS-MLLM ）在卫星图像上具有先进的场景理解和视觉问答功能，但定位特定物体或变化的区域仍然具有挑战性。关键词：rag、evaluation、code、multimodal。代码/数据可用性需查看原文确认。

### 4. 改进图像生成、视觉理解和可控渲染

<p class="paper-meta-line"><span>Supervised Cross-Modal Feature Alignment for Zero-Wearable Freezing of Gait Detection in Parkinsonism (Aryan Singh, Chandan Biswas)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.08317">2609.08317</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.08317">PDF</a></p>

中文标题：用于帕金森氏症中步态检测的零穿戴式冻结的监督交叉模式特征对齐

信号显示：帕金森病（ PD ）步态冻结（ FoG ）的客观评估主要依赖于可穿戴的惯性测量单元（ IMU ）。关键词：inference、deployment、alignment、evaluation。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>What Eviction Destroys: A Restore-Counterfactual Audit of Forgetting in Agent Memory (Chen Shen)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.08279">2609.08279</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.08279">PDF</a></p>

中文标题：驱逐摧毁了什么：对代理记忆中遗忘的恢复-反事实审计

信号显示：当历史记录超出固定令牌预算时，代理内存系统必须丢弃存储的信息。关键词：agent、retrieval、benchmark、memory。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research? (Yuqiao Tan, Shizhu He, Jun Zhao, Kang Liu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.09113">2609.09113</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.09113">PDF</a></p>

中文标题：SAEScientist-Bench ：人工智能代理可以进行自主SAE可解释性研究吗？

信号显示：虽然递归自我改进（ RSI ）的研究主要是自动化模型培训管道，但可靠的自主开发需要缺少一个支柱：事后监控和审计，以了解哪些模型学习并确保安全对齐。关键词：agent、alignment、evaluation、code。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Evaluation Principles for MRI-MRA Registration in Trigeminal Neuralgia: An ROI-Centered Neurovascular Benchmark](https://arxiv.org/abs/2609.08805)
中文标题：评测 Principles 面向 MRI-MRA Registration in Trigeminal Neuralgia：An ROI-Centered Neurovascular 基准
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Structural Jailbreaks Generalize but Do Not Compound: A cross-provider and multilingual study of Involuntary In-Context Learning](https://arxiv.org/abs/2609.08373)
中文标题：结构性越狱泛化但不复合：非自愿上下文学习的跨提供者和多语言研究
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [A Measurement Study of LLM Inference Trade-offs Across Edge Continuum Hardware](https://arxiv.org/abs/2609.08307)
中文标题：一种Measurement Study of LLM Inference Trade-offs Across Edge Continuum Hardware
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Human-Centric Image Captioning with Subject-Centered Spatial Understanding](https://arxiv.org/abs/2609.08300)
中文标题：以人为本的图像字幕与以主体为中心的空间理解
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Beyond Coherence: Benchmarking Professional Editing-Technique Execution in Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2609.08275)
中文标题：超越一致性：对标专业编辑-多镜头音频视频生成中的技术执行
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SchemeArena: Factorized Stress Testing of Scheming in LLM Agents](https://arxiv.org/abs/2609.08126)
中文标题：SchemeArena ： LLM代理商中Scheming的因素压力测试
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails](https://arxiv.org/abs/2609.09134)
中文标题：共同发展的线束和模型：政策纠正有助于较弱的模型追赶模仿失败的地方
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [TASTE2: Text-Aligned Speech Modeling and Deployment toward Full-Duplex Voice Interaction](https://arxiv.org/abs/2609.08956)
中文标题：TASTE2：Text-Aligned Speech Modeling 与 Deployment 面向 Full-Duplex Voice Interaction
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CoSA: Correlation-Guided Change A ttention with Learnable Residual Gating for Remote Sensing Change Detection](https://arxiv.org/abs/2609.08914)
中文标题：CoSA ：相关性引导的变化利用可学习的残差选通进行遥感变化检测
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [SynthRCT: Scalable Conditional Deformation Synthesis for Synthetic Repeat CT Generation](https://arxiv.org/abs/2609.08627)
中文标题：SynthRCT：可扩展 Conditional Deformation Synthesis 面向 Synthetic Repeat CT Generation
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Do New Attention Mechanisms Actually Fix Attention Sinks at Million-Token Context?](https://arxiv.org/abs/2609.08574)
中文标题：新的注意力机制实际上修复了百万代币背景下的注意力下沉吗？
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Beyond Agent Harnesses: Cross-Substrate Authority for Multi-Agent Systems](https://arxiv.org/abs/2609.08472)
中文标题：Beyond Agent Harnesses：Cross-Substrate Authority 面向 多智能体系统
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Safe Task Planning with Long-Term Graph Memory for Embodied Agents](https://arxiv.org/abs/2609.08444)
中文标题：为具体代理提供长期图形内存的安全任务规划
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [To Adapt or Not to Adapt? Selective Adaptation for Vision-Language Models](https://arxiv.org/abs/2609.08367)
中文标题：适应还是不适应？视觉语言模型的选择性适应
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Rank Without an Oracle: Deviation-Aware Interaction-Rank Selection from Offline Multi-Agent Logs](https://arxiv.org/abs/2609.08358)
中文标题：Rank Without an Oracle：Deviation-Aware Interaction-Rank Selection 来自 Offline Multi-Agent Logs
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [HoneyRoute: Honeypot-Model Routing for Adversarial LLM Serving](https://arxiv.org/abs/2609.08306)
中文标题：HoneyRoute：Honeypot-Model Routing 面向 Adversarial LLM Serving
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Qiushi Engine on AstaBench E2E-Bench-Hard](https://arxiv.org/abs/2609.08196)
中文标题：AstaBench E2E-Bench-Hard上的Qiushi发动机
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Snugi-AI-v2 @ eRisk 2026 Task 2: Early Depression Detection via a Learned Stopping Policy with Sustained Confidence Gate](https://arxiv.org/abs/2609.08161)
中文标题：Snugi-AI-v2 @ eRisk 2026任务2 ：通过持续信心门禁的学习停止策略进行早期抑郁症检测
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators](https://arxiv.org/abs/2609.09155)
中文标题：SyncWorld：Visual Calibration Enables 世界模型 as Zero-Shot Simulators
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [MeClear: Cooperative Game-Theoretic Attribution and Risk-Aware Memory Clearance for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.09115)
中文标题：MeClear：Cooperative Game-Theoretic Attribution 与 Risk-Aware Memory Clearance 面向 Long-Horizon LLM Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
