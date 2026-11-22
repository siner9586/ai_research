---
title: "评测视频生成的时间一致性和运动真实感、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-11-23"
target_date: "2026-11-21"
actual_date: "2026-11-19"
fallback_from: "2026-11-21"
lang: "zh"
slug: "2026-11-23-reinforcement-aligned-probabilistic-weather-forecasting-with-discrete"
summary: "今天主要跟进：评测视频生成的时间一致性和运动真实感、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "data-engineering", "evaluation", "rag", "reasoning", "robotics", "training"]
topics: ["agents", "code", "data-engineering", "evaluation", "rag", "reasoning", "robotics", "training"]
sources_page: "/zh/daily/2026-11-23-reinforcement-aligned-probabilistic-weather-forecasting-with-discrete-sources/"
generated_at: "2026-11-22T17:00:28.608528+00:00"
page_type: "brief"
candidate_count: 586
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Reinforcement-Aligned Probabilistic Weather Forecasting with Discrete Tokens", "TwoPass: Draft-Guided Few-Step Video Prediction for Robotic Manipulation", "LM-based Personalized Travel Planner", "WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming", "A Wolf in Sheep's Pixels: Visual Camouflage Attacks via HDR Gain Maps", "ActMem: From Latent Memory Reasoning to Grounded Robotic Action"]
featured_paper_urls: ["https://arxiv.org/abs/2611.25570", "https://arxiv.org/abs/2611.25553", "https://arxiv.org/abs/2611.25531", "https://arxiv.org/abs/2611.25476", "https://arxiv.org/abs/2611.25469", "https://arxiv.org/abs/2611.25461"]
featured_paper_titles_zh: ["使用离散标记的强化对齐概率天气预报", "TwoPass：Draft-Guided Few-Step Video Prediction 面向 Robotic Manipulation", "基于大语言模型的个性化行程规划工具", "WeightCode：通过权重空间编程将新功能安装到神经网络中", "披着羊皮的狼像素：通过 HDR 增益图进行的视觉伪装攻击", "ActMem：来自 Latent Memory Reasoning to Grounded Robotic Action"]
---

# 评测视频生成的时间一致性和运动真实感、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：评测视频生成的时间一致性和运动真实感、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 评测视频生成的时间一致性和运动真实感

<p class="paper-meta-line"><span>Reinforcement-Aligned Probabilistic Weather Forecasting with Discrete Tokens (Jinhan Li, Zhisheng Chen, Yuxuan Li, Yuan Gao, Fan Xu, Hao Wu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.25570">2611.25570</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.25570">PDF</a></p>

中文标题：使用离散标记的强化对齐概率天气预报

信号显示：全球中程天气预报不仅必须高效地生成集合，以表征未来状态的不确定性，还必须为极端事件预警和跨圈耦合模拟等下游应用提供服务。关键词：inference、alignment、benchmark、post-training。代码/数据可用性需查看原文确认。

### 2. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>TwoPass: Draft-Guided Few-Step Video Prediction for Robotic Manipulation (Yijun Liu, Shijia Ge, Tongtong Feng, Xin Wang, Yuan Meng, Yuwei Liu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.25553">2611.25553</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.25553">PDF</a></p>

中文标题：TwoPass：Draft-Guided Few-Step Video Prediction 面向 Robotic Manipulation

信号显示：基于动作的视频预测使机器人能够预测其动作的视觉后果，以便进行规划和策略评估。关键词：inference、evaluation、code、robot。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>LM-based Personalized Travel Planner (Amandi Nimasha, Oshadha Wijerathne, Dushan Fernando, Nisansa de Silva, Srinath Perera)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.25531">2611.25531</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.25531">PDF</a></p>

中文标题：基于大语言模型的个性化行程规划工具

信号显示：有效的旅行规划需要处理多个信息来源、管理限制因素，并根据用户的偏好量身定制建议。关键词：agent、retrieval、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming (Bo Li, Taoyong Cui, Bob Zhang, Mengran Li, Chengyang Zhang, Yang Zhang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.25476">2611.25476</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.25476">PDF</a></p>

中文标题：WeightCode：通过权重空间编程将新功能安装到神经网络中

信号显示：神经网络在其权重中编码所学到的能力，但利用显式任务知识来扩展这些能力仍然是一项基本挑战。关键词：rag、serving、code、fine-tuning。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>A Wolf in Sheep&#x27;s Pixels: Visual Camouflage Attacks via HDR Gain Maps (Qi Shen, Yujia Gong, Yue Zhao, Tong Liu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.25469">2611.25469</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.25469">PDF</a></p>

中文标题：披着羊皮的狼像素：通过 HDR 增益图进行的视觉伪装攻击

信号显示：图像可能会通过自动安全检查，但向人类观看者显示有害内容。关键词：agent、rag、safety、benchmark。代码/数据可用性需查看原文确认。

### 6. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>ActMem: From Latent Memory Reasoning to Grounded Robotic Action (Linfeng Dong, Jianwei Niu, Jiuyi Zhao, Ruibing Feng, Xinghao Wu, Wu Yang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.25461">2611.25461</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.25461">PDF</a></p>

中文标题：ActMem：来自 Latent Memory Reasoning to Grounded Robotic Action

信号显示：视觉-语言-行动（VLA）模型在现实世界的长时域操纵方面取得了令人鼓舞的成果，其中记忆发挥着至关重要的作用。关键词：rag、inference、code、vision-language。代码/数据可用性需查看原文确认。

## 其他值得关注
- [RemoteVLPG: How to Obtain a Specific VLM for Language-Guided Path Generation on Remote Sensing Images?](https://arxiv.org/abs/2611.25458)
中文标题：RemoteVLPG：How to Obtain a Specific VLM 面向 Language-Guided Path Generation on Remote Sensing Images?
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Protein Functional Semantic Alignment via Representation Rectification](https://arxiv.org/abs/2611.25396)
中文标题：通过表征校正实现蛋白质功能语义对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [HOPD: Historical On-Policy Distillation for SAR MLLM Continual Learning](https://arxiv.org/abs/2611.25391)
中文标题：HOPD：Historical On-Policy Distillation 面向 SAR MLLM Continual Learning
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs](https://arxiv.org/abs/2611.25387)
中文标题：TuringSpace：通过交互式CAPTCHA将空间智能付诸实践
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [AppSci-Bench: Can LLMs Build AI Agents and Make Them Better?](https://arxiv.org/abs/2611.25360)
中文标题：AppSci-Bench：Can LLMs Build AI Agents 与 Make Them Better?
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [When Should Deployed BCI Decoders Adapt? A Resource-Priced Ladder for Frozen EEG Trunks](https://arxiv.org/abs/2611.25315)
中文标题：When Should Deployed BCI Decoders Adapt? A Resource-Priced Ladder 面向 Frozen EEG Trunks
关注理由：涉及数据工程中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Posterior Matching Distillation](https://arxiv.org/abs/2611.26629)
中文标题：后验匹配蒸馏
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)](https://arxiv.org/abs/2611.26553)
中文标题：Replication of Agentic Security Events：Audit 与 Investigation (ROGUE-AI)
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Backtracking Agent Applications Security Incidents](https://arxiv.org/abs/2611.26525)
中文标题：回溯代理应用程序安全事件
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Direct3D-V3: Latent-Free Diffusion Transformers in the Native Voxel Domain](https://arxiv.org/abs/2611.26511)
中文标题：DireCT3D-V3：原生体素域中的无潜在扩散变换器
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Held While Waiting: What LLM Agent Sessions Reserve on Serverless and Agent Runtimes](https://arxiv.org/abs/2611.26480)
中文标题：Held While Waiting：What LLM Agent Sessions Reserve on Serverless 与 Agent Runtimes
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience](https://arxiv.org/abs/2611.26420)
中文标题：Awaken-HI：通过全身人类体验扩展类人智能
关注理由：涉及机器人与具身智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Democratizing Cross-Project Knowledge for Transforming Water Governance and Climate Resilience: an Agentic AI Ecosystem](https://arxiv.org/abs/2611.26398)
中文标题：Democratizing Cross-Project Knowledge 面向 Transforming Water Governance 与 Climate Resilience：an Agentic AI Ecosystem
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SpecFlow: Flow Matching in the Acceleration Spectrum for Multi-Agent Trajectory Forecasting](https://arxiv.org/abs/2611.26390)
中文标题：SpecFlow：Flow Matching in the Acceleration Spectrum 面向 Multi-Agent Trajectory Forecasting
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Alignment Drives Reuse: Learning Generalizable Robot-Use Agents from Heterogeneous Experience](https://arxiv.org/abs/2611.26376)
中文标题：对齐驱动重用：从异构经验中学习可泛化的机器人使用智能体
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs](https://arxiv.org/abs/2611.26363)
中文标题：HiSA：稀疏化大语言模型 (LLM) 中 RoPE 注意力的隐藏维度
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Static Analysis Guidance for Secure LLM Code Generation](https://arxiv.org/abs/2611.26312)
中文标题：用于安全LLM代码生成的静态分析指南
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [A Statistical Framework for Training Data Auditing of Large Language Models](https://arxiv.org/abs/2611.26264)
中文标题：大型语言模型训练数据审计的统计框架
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Teaching Vision-Language-Action Models to Stop Safely](https://arxiv.org/abs/2611.26239)
中文标题：训练视觉-语言-动作模型安全停车
关注理由：涉及机器人与具身智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [SlotFlow-GB: A Neural Framework for Trans-Dimensional Inference of Overlapping Galactic Binaries](https://arxiv.org/abs/2611.26057)
中文标题：SlotFlow-GB：A Neural 框架 面向 Trans-Dimensional Inference of Overlapping Galactic Binaries
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
