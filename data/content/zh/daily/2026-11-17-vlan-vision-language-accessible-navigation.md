---
title: "让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力"
date: "2026-11-17"
target_date: "2026-11-15"
actual_date: "2026-11-13"
fallback_from: "2026-11-15"
lang: "zh"
slug: "2026-11-17-vlan-vision-language-accessible-navigation"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "systems", "training"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "systems", "training"]
sources_page: "/zh/daily/2026-11-17-vlan-vision-language-accessible-navigation-sources/"
generated_at: "2026-11-16T16:54:35.345856+00:00"
page_type: "brief"
candidate_count: 344
featured_count: 6
mentions_count: 20
featured_paper_titles: ["VLAN: Vision-Language Accessible Navigation", "Superfluid: Local AI Server for Distributed LLM Inference", "Box-conditional Hypothesis Testing for Out-of-Distribution Object Detection", "Interactive Program Induction with Language Model Priors", "Aligning AI Teams", "Evaluating Large Language Models for Scientific Paper Search: Retrieval Success and Inference Latency on Mac Studio and NVIDIA A100"]
featured_paper_urls: ["https://arxiv.org/abs/2611.18346", "https://arxiv.org/abs/2611.17753", "https://arxiv.org/abs/2611.18519", "https://arxiv.org/abs/2611.18485", "https://arxiv.org/abs/2611.17820", "https://arxiv.org/abs/2611.17929"]
featured_paper_titles_zh: ["VLAN：视觉-语言无障碍导航", "Superfluid：Local AI Server 面向 Distributed LLM Inference", "用于检测分布外对象的框条件假设检验", "基于语言模型先验的交互式程序归纳", "协调人工智能团队", "Evaluating Large Language Models 面向 Scientific Paper Search：Retrieval Success 与 Inference Latency on Mac Studio 与 NVIDIA A100"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>VLAN: Vision-Language Accessible Navigation (Jie Hu, Yu Zheng, Wenzhi Wu, Weixing Feng, Cunlei Cheng, Jiaming Zhang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.18346">2611.18346</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.18346">PDF</a></p>

中文标题：VLAN：视觉-语言无障碍导航

信号显示：无障碍出行取决于使用者而非场景本身，因为对一种出行方式来说可通行的路径，对另一种出行方式来说可能就是不可通行的。关键词：agent、alignment、safety、evaluation。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Superfluid: Local AI Server for Distributed LLM Inference (Prabod Rathnayaka, Isura Manchanayake, Srikandabala Kogul, Steve Siu, Fabian Waschkowski, Lukas Wesemann)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.17753">2611.17753</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.17753">PDF</a></p>

中文标题：Superfluid：Local AI Server 面向 Distributed LLM Inference

信号显示：在本地设备上运行大语言模型（LLM）可以保护数据隐私、消除按令牌计费的成本、降低网络延迟，并能够在没有网络连接的情况下继续工作。关键词：agent、inference、serving、latency。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Box-conditional Hypothesis Testing for Out-of-Distribution Object Detection (Donghoon Lee, Jusung Park, Shinjin Kang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.18519">2611.18519</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.18519">PDF</a></p>

中文标题：用于检测分布外对象的框条件假设检验

信号显示：检测分布外（OOD）对象对于确保目标检测器在现实世界部署中的可靠性和安全性至关重要。关键词：deployment、safety、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Interactive Program Induction with Language Model Priors (Robin Shing Moon Chan, Ryan Cotterell)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.18485">2611.18485</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.18485">PDF</a></p>

中文标题：基于语言模型先验的交互式程序归纳

信号显示：程序归纳是指学习者旨在从几个给定的输入-输出示例中恢复程序的过程。关键词：agent、serving、benchmark、code。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Aligning AI Teams (Siddarth Srinivasan, Morgan Jane Matthews, Jascha Sohl-Dickstein, Erik Jones)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.17820">2611.17820</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.17820">PDF</a></p>

中文标题：协调人工智能团队

信号显示：先前的研究表明，对单个大语言模型（LLM）智能体的对齐训练可能无法迁移到多智能体环境中。关键词：agent、alignment、safety、agents。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Evaluating Large Language Models for Scientific Paper Search: Retrieval Success and Inference Latency on Mac Studio and NVIDIA A100 (Frederic Andriantseheno Rakoto, Yannis Bendi-Ouis, Xavier Hinaut)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.17929">2611.17929</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.17929">PDF</a></p>

中文标题：Evaluating Large Language Models 面向 Scientific Paper Search：Retrieval Success 与 Inference Latency on Mac Studio 与 NVIDIA A100

信号显示：科学文献检索可以受益于本地部署的 LLM 助手，这些助手可以减少对托管模型提供商的依赖，同时让研究团队对其数据和基础设施有更大的掌控权。关键词：retrieval、inference、latency、memory。代码/数据可用性需查看原文确认。

## 其他值得关注
- [AI Reviews Are Biased Towards the Appendix](https://arxiv.org/abs/2611.17811)
中文标题：人工智能审稿偏向于附录
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Ego2Flow: Benchmarking the Traffic-System Impact of Autonomous Driving on Maps Distilled from Real-World Roads](https://arxiv.org/abs/2611.17720)
中文标题：Ego2Flow：对从真实道路中提取的地图进行自动驾驶对交通系统影响的基准测试
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Toward On-Device Markerless 6DoF Tracking of a Physical Manipulative on a Mixed-Reality Headset: A Preliminary Study](https://arxiv.org/abs/2611.18438)
中文标题：面向 On-Device Markerless 6DoF Tracking of a Physical Manipulative on a Mixed-Reality Headset：A Preliminary Study
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [PerfArena: Ranking LLMs by Code Performance](https://arxiv.org/abs/2611.18030)
中文标题：PerfArena：按代码性能对 LLM 进行排名
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [UltraBERT-JEV: Encoder models for System One Applications](https://arxiv.org/abs/2611.17867)
中文标题：UltraBERT-JEV：Encoder models 面向 System One Applications
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [FlexCast: Flexible Context Learning for Time Series Foundation Models](https://arxiv.org/abs/2611.17862)
中文标题：FlexCast：Flexible Context Learning 面向 Time Series Foundation Models
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [WeightBench: Evaluating Language Models as Weight-Space Programmers](https://arxiv.org/abs/2611.18553)
中文标题：WeightBench：将语言模型评估为权重空间编程器
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Alignment by Socialization: Learning Tradeoffs Under Selection](https://arxiv.org/abs/2611.18531)
中文标题：通过社会化实现一致：在选择中学习权衡
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [EventSpikeSeg: Memory-Aware Mixed-Signal Architecture for Event-Camera Spiking Segmentation](https://arxiv.org/abs/2611.18524)
中文标题：EventSpikeSeg：Memory-Aware Mixed-Signal Architecture 面向 Event-Camera Spiking Segmentation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ARCHER: From Rationale Imitation to Executable Reasoning in Small Language Models](https://arxiv.org/abs/2611.18494)
中文标题：ARCHER：来自 Rationale Imitation to Executable Reasoning in Small Language Models
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Adaptable Watermarking: Transforming Image Watermarking Models via Lightweight Adapters](https://arxiv.org/abs/2611.18363)
中文标题：自适应水印：通过轻量级适配器转化图像水印模型
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Causal AI-Driven Secure mmWave Beam Alignment with Defensive Variational Autoencoders](https://arxiv.org/abs/2611.18321)
中文标题：基于因果关系人工智能的安全毫米波波束对准，采用防御性变分自编码器
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [PrivacyPR: A Dataset of Real-World Privacy Fixes for Benchmarking Privacy-Aware Code Review](https://arxiv.org/abs/2611.18293)
中文标题：PrivacyPR：A Dataset of Real-World Privacy Fixes 面向 基准ing Privacy-Aware Code Review
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Right Token, Right Time: From Per-Token Gating to Trajectory-Aware Activation Steering](https://arxiv.org/abs/2611.18274)
中文标题：正确的代币，正确的时间：从基于代币的门控到基于轨迹的激活引导
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Structural Self-Teaching for Compositional Generation in Unified Multimodal Models](https://arxiv.org/abs/2611.18261)
中文标题：统一多模态模型中用于生成构成的结构性自学
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [NeoResearch: Literature- and Experience-Guided Autonomous Time Series Model Discovery](https://arxiv.org/abs/2611.18235)
中文标题：NeoResearch：Literature- 与 Experience-Guided Autonomous Time Series Model Discovery
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [STaG: Human-Annotation-Free Unsupervised Domain Adaptation for Text-Based Person Retrieval](https://arxiv.org/abs/2611.18172)
中文标题：STaG：Human-Annotation-Free Unsupervised Domain Adaptation 面向 Text-Based Person Retrieval
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [A Multi-Layered AI Pipeline for BPMN Generation from Natural Language](https://arxiv.org/abs/2611.18157)
中文标题：一种Multi-Layered AI Pipeline 面向 BPMN Generation 来自 Natural Language
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Compiling Specialized GPU-Initiated Networking](https://arxiv.org/abs/2611.18145)
中文标题：编译由 GPU 发起的专用网络
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [VEPO: Mitigating Multilingual Hallucinations in LVLMs via Visual Evidence-guided Preference Optimization](https://arxiv.org/abs/2611.18096)
中文标题：VEPO：通过视觉证据引导的偏好优化来缓解大型视觉语言模型的多语言幻觉
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
