---
title: "识别并缓解模型安全、越狱和对齐风险、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能"
date: "2026-07-06"
target_date: "2026-07-04"
actual_date: "2026-07-02"
fallback_from: "2026-07-04"
lang: "zh"
slug: "2026-07-06-knnguard-turning-llm-hidden-activations-into-a"
summary: "今天主要跟进：识别并缓解模型安全、越狱和对齐风险、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "safety", "training", "video-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "safety", "training", "video-generation"]
sources_page: "/zh/daily/2026-07-06-knnguard-turning-llm-hidden-activations-into-a-sources/"
generated_at: "2026-07-05T22:12:44.428709+00:00"
page_type: "brief"
candidate_count: 445
featured_count: 6
mentions_count: 20
featured_paper_titles: ["kNNGuard: Turning LLM Hidden Activations into a Training-Free Configurable Guardrail", "OpenSafeIntent: Evaluating Intent-Calibrated Safe Completion Across Dual-Use Prompt Sets", "Traceable Fault Diagnosis for Battery Energy Storage Systems via Retrieval-Augmented Multi-Agent O&M Assistant", "Assessing VLM Reliability for Medical Image Quality Evaluation Under Corruption and Bias", "Object Aligner: A Configurable JSON Schema Similarity Score for Graphs, Applied to LLM Prompt Optimization", "ContextSniper: AntTrail's Token-Efficient Code Memory for Repository-Level Program Repair"]
featured_paper_urls: ["https://arxiv.org/abs/2607.02072", "https://arxiv.org/abs/2607.02047", "https://arxiv.org/abs/2607.01992", "https://arxiv.org/abs/2607.01973", "https://arxiv.org/abs/2607.01972", "https://arxiv.org/abs/2607.01916"]
featured_paper_titles_zh: ["kNNGuard：将LLM隐藏激活转化为无需训练的可配置防护罩", "OpenSafeIntent ：评估两用提示集的意图校准安全完成情况", "通过检索增强型多代理运维助手对电池储能系统进行可追溯的故障诊断", "评估VLM在医学图像质量评价中对腐败和偏见的可靠性", "Object Aligner：A Configurable JSON Schema Similarity Score 面向 Graphs，Applied to LLM Prompt Optimization", "ContextSniper：AntTrail's Token-Efficient Code Memory 面向 Repository-Level Program Repair"]
---

# 识别并缓解模型安全、越狱和对齐风险、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：识别并缓解模型安全、越狱和对齐风险、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 识别并缓解模型安全、越狱和对齐风险

<p class="paper-meta-line"><span>kNNGuard: Turning LLM Hidden Activations into a Training-Free Configurable Guardrail (Mahmoud Abdelfattah, Hamid Nasiri, Peter Garraghan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.02072">2607.02072</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.02072">PDF</a></p>

中文标题：kNNGuard：将LLM隐藏激活转化为无需训练的可配置防护罩

信号显示：大语言模型（ LLM ）越来越多地部署在需要护栏来检测不安全、偏离主题或对抗性提示的领域。关键词：inference、latency、safety、fine-tuning。代码/数据可用性需查看原文确认。

### 2. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>OpenSafeIntent: Evaluating Intent-Calibrated Safe Completion Across Dual-Use Prompt Sets (Rheeya Uppaal, Seungwoo Lyu, Selina Sung, Junjie Hu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.02047">2607.02047</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.02047">PDF</a></p>

中文标题：OpenSafeIntent ：评估两用提示集的意图校准安全完成情况

信号显示：安全完成任务要求模型在提供有用帮助的同时避免造成伤害，但仅凭孤立的提示很难评估这种行为。关键词：rag、safety、benchmark、risk。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Traceable Fault Diagnosis for Battery Energy Storage Systems via Retrieval-Augmented Multi-Agent O&amp;M Assistant (Jiangdi Ru, Bing Li, Yage Huang, Ding Wang, Keru Hua)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.01992">2607.01992</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.01992">PDF</a></p>

中文标题：通过检索增强型多代理运维助手对电池储能系统进行可追溯的故障诊断

信号显示：大型电池储能系统（ BESS ）需要结合警报、电池级测量、设备拓扑、诊断表、历史案例和维护文档的运维决策。关键词：agent、rag、retrieval、evaluation。代码/数据可用性需查看原文确认。

### 4. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Assessing VLM Reliability for Medical Image Quality Evaluation Under Corruption and Bias (Sofiane Ouaari, Kevin Vorwalder, Nico Pfeifer)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.01973">2607.01973</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.01973">PDF</a></p>

中文标题：评估VLM在医学图像质量评价中对腐败和偏见的可靠性

信号显示：视觉语言模型（ VLM ）越来越多地应用于病理描述、报告生成和视觉问答等医疗任务。关键词：serving、deployment、safety、evaluation。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Object Aligner: A Configurable JSON Schema Similarity Score for Graphs, Applied to LLM Prompt Optimization (Jan Drchal)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.01972">2607.01972</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.01972">PDF</a></p>

中文标题：Object Aligner：A Configurable JSON Schema Similarity Score 面向 Graphs，Applied to LLM Prompt Optimization

信号显示：大语言模型（ LLM ）经常被要求生成符合固定模式的JSON ，支持信息提取、工具调用、代理规划和知识图构建。关键词：agent、alignment、code、open-source。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>ContextSniper: AntTrail&#x27;s Token-Efficient Code Memory for Repository-Level Program Repair (Chiwang Luk, Matin Mohammad Najafi, Zhifeng Jia, Wei Yang, Xiuchang Li, Jinwei Zhu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.01916">2607.01916</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.01916">PDF</a></p>

中文标题：ContextSniper：AntTrail's Token-Efficient Code Memory 面向 Repository-Level Program Repair

信号显示：大语言模型代理可以修复真实的存储库问题，但它们通常在整个文件读取、广泛搜索和长终端输出上花费大量的上下文预算，其中有用的证据与不相关的代码和日志混合在一起。关键词：agent、retrieval、serving、code。代码/数据可用性需查看原文确认。

## 其他值得关注
- [NeoMap: Training-free Novel-View Synthesis from Single Images and Videos](https://arxiv.org/abs/2607.01962)
中文标题：NeoMap：Training-free Novel-View Synthesis 来自 Single Images 与 Videos
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Spec-AUF: Accept-Until-Fail Training under Train-Inference Misalignment for Masked Block Drafters](https://arxiv.org/abs/2607.01893)
中文标题：Spec-AUF：Accept-Until-Fail Training under Train-Inference Misalignment 面向 Masked Block Drafters
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Descriptor: LYNRED Mobility Dataset Multimodal Detection Subset (LYNRED-MDS)](https://arxiv.org/abs/2607.01871)
中文标题：描述符： LYNRED Mobility Dataset Multimodal DeteCTion Subset （ LYNRED-MDS ）
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [CLAP: Closed-Loop Training, Evaluation, and Release Control for Domain Agent Post-training](https://arxiv.org/abs/2607.01846)
中文标题：CLAP：Closed-Loop Training，评测，与 Release Control 面向 Domain Agent Post-training
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Pre-Flight: A Benchmark for Evaluating Large Language Models on Aviation Operational Knowledge](https://arxiv.org/abs/2607.01829)
中文标题：飞行前：评估航空运营知识大型语言模型的基准
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Predicting Closed-Loop Performance of Latent World Models: Offline Checkpoint Selection for MPC and Model-Based RL Under Non-Markovian Rewards in LunarLander](https://arxiv.org/abs/2607.01736)
中文标题：Predicting Closed-Loop Performance of Latent 世界模型：Offline Checkpoint Selection 面向 MPC 与 Model-Based RL Under Non-Markovian Rewards in LunarLander
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Frequency Shift Physics-Informed Extreme Learning Machine for Solving High-Frequency Partial Differential Equations](https://arxiv.org/abs/2607.01694)
中文标题：频移物理-求解高频偏微分方程的知情极限学习机
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Separating Expert Retention from Autonomous Source Inference in Raw-ECG-Replay-Free Continual ECG Deployment](https://arxiv.org/abs/2607.01674)
中文标题：Separating Expert Retention 来自 Autonomous Source Inference in Raw-ECG-Replay-Free Continual ECG Deployment
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Temporal and Cross-Modal Alignment for Enhanced Audiovisual Video Captioning](https://arxiv.org/abs/2607.01667)
中文标题：用于增强视听视频字幕的时间和跨模式对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [DeadPool: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint](https://arxiv.org/abs/2607.01646)
中文标题：DeadPool ：通过零开销检查点进行热插拔的弹性LLM培训
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SINA: A Fully Automated Circuit Schematic Image to Netlist Generator Using Artificial Intelligence](https://arxiv.org/abs/2607.01609)
中文标题：新浪：使用人工智能的全自动电路原理图到网表生成器
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Alignment Is All You Need For X-to-4D Generation](https://arxiv.org/abs/2607.02516)
中文标题：对齐是X到4D一代所需的一切
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning](https://arxiv.org/abs/2607.02513)
中文标题：LACUNA：A Testbed 面向 Evaluating Localization Precision 面向 LLM Unlearning
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas](https://arxiv.org/abs/2607.02504)
中文标题：推理法学硕士提高长篇电视剧演讲者的认知度
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning](https://arxiv.org/abs/2607.02490)
中文标题：通过强化学习实现视觉语言模型的视觉基础自我反思
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Combating Textual Noise and Redundancy: Entropy-Aware Dense Visual Token Pruning](https://arxiv.org/abs/2607.02484)
中文标题：消除文本噪音和冗余：熵感知密集视觉令牌修剪
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs](https://arxiv.org/abs/2607.02466)
中文标题：在学会做之前学会移动： VLA的任务无关预训练
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Adoption and Ecosystem Health: A Longitudinal Analysis of Open-Source Multi-Agent Frameworks](https://arxiv.org/abs/2607.02453)
中文标题：采用与生态系统健康：开源多Agent框架的纵向分析
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Self-Auditing Residual Drifting for Pathology-Preserving Accelerated Knee MRI](https://arxiv.org/abs/2607.02428)
中文标题：Self-Auditing Residual Drifting 面向 Pathology-Preserving Accelerated Knee MRI
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition](https://arxiv.org/abs/2607.02426)
中文标题：QFedAgent：Quantum-Enhanced Personalized Federated Learning 面向 Multi-Agent Activity Recognition
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
