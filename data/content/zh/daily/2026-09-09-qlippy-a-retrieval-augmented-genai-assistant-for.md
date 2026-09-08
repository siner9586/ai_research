---
title: "让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力、提升 RAG 检索和知识库问答可靠性"
date: "2026-09-09"
target_date: "2026-09-07"
actual_date: "2026-09-04"
fallback_from: "2026-09-07"
lang: "zh"
slug: "2026-09-09-qlippy-a-retrieval-augmented-genai-assistant-for"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "systems", "training", "video-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-09-09-qlippy-a-retrieval-augmented-genai-assistant-for-sources/"
generated_at: "2026-09-08T23:22:47.761310+00:00"
page_type: "brief"
candidate_count: 352
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Qlippy: A Retrieval-Augmented GenAI Assistant for Reproducible Quantum Workflows and Experiment Tracking", "BIT.UA at BioASQ 14B: Modular Retrieval with pg_textsearch and Qdrant, and Agent-Based Answer Generation", "A Tree-based RAG Framework for Evidence-Intensive QA via Adaptive Planning and Topology-Aware Evidence Gathering", "SAM-D2Q: Aligning Multimodal Doc2Query with Search Demand and Conversion for E-commerce", "MCPO: Modality-Contrastive Preference Optimization for Multimodal Chain-of-Thought Compression", "One Diffusion Model, Two Roles: Guided Trajectory Planning and Safety-Critical Scenario Generation in Closed-Loop Simulation"]
featured_paper_urls: ["https://arxiv.org/abs/2609.05039", "https://arxiv.org/abs/2609.04999", "https://arxiv.org/abs/2609.04981", "https://arxiv.org/abs/2609.04961", "https://arxiv.org/abs/2609.04947", "https://arxiv.org/abs/2609.04921"]
featured_paper_titles_zh: ["Qlippy：A Retrieval-Augmented GenAI Assistant 面向 Reproducible Quantum Workflows 与 Experiment Tracking", "BioASQ 14B的BIT.UA ：使用pg_textsearch和Qdrant进行模块化检索，以及基于Agent的应答生成", "基于树的RAG框架，通过自适应规划和拓扑感知证据收集实现证据密集型QA", "SAM-D2Q ：使多式联运Doc2Query与电子商务的搜索需求和转换保持一致", "MCPO：Modality-Contrastive Preference Optimization 面向 Multimodal Chain-of-Thought Compression", "One Diffusion Model，Two Roles：Guided Trajectory Planning 与 Safety-Critical Scenario Generation in 闭环仿真"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Qlippy: A Retrieval-Augmented GenAI Assistant for Reproducible Quantum Workflows and Experiment Tracking (Mahee Gamage, Vlad Stirbu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.05039">2609.05039</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.05039">PDF</a></p>

中文标题：Qlippy：A Retrieval-Augmented GenAI Assistant 面向 Reproducible Quantum Workflows 与 Experiment Tracking

信号显示：量子软件开发是迭代的，容易出错。关键词：workflow、retrieval、serving、deployment。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>BIT.UA at BioASQ 14B: Modular Retrieval with pg_textsearch and Qdrant, and Agent-Based Answer Generation (André Ribeiro, Rúben Garrido, Alexander Christiansen, Richard A. A. Jonker, Sérgio Matos)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.04999">2609.04999</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.04999">PDF</a></p>

中文标题：BioASQ 14B的BIT.UA ：使用pg_textsearch和Qdrant进行模块化检索，以及基于Agent的应答生成

信号显示：本文描述了来自阿威罗大学的BIT.UA团队参与第14届BioASQ任务B生物医学问答挑战。关键词：agent、rag、retrieval、code。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>A Tree-based RAG Framework for Evidence-Intensive QA via Adaptive Planning and Topology-Aware Evidence Gathering (Songeun Lee, Kyungjin Min, Injae Na, Suyeong Lee, Chiyoung Kim, Woohwan Jung)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.04981">2609.04981</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.04981">PDF</a></p>

中文标题：基于树的RAG框架，通过自适应规划和拓扑感知证据收集实现证据密集型QA

信号显示：最近的结构化RAG方法利用基于树或图的推理结构来改进多跳QA。关键词：rag、retrieval、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>SAM-D2Q: Aligning Multimodal Doc2Query with Search Demand and Conversion for E-commerce (Hui Zhou, Jian Hui Ji, Lei Ma, Rong Xiao, Xiaoyi Zeng)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.04961">2609.04961</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.04961">PDF</a></p>

中文标题：SAM-D2Q ：使多式联运Doc2Query与电子商务的搜索需求和转换保持一致

信号显示：由于短标题无法完全覆盖多样化的用户表达或视觉产品属性，电子商务搜索通常会遇到用户查询与商家撰写的产品标题词汇不匹配的问题。关键词：rag、retrieval、alignment、multimodal。代码/数据可用性需查看原文确认。

### 5. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>MCPO: Modality-Contrastive Preference Optimization for Multimodal Chain-of-Thought Compression (Guangheng Yang, Zhenliang Ni, Zhenkai Wu, Han Shu, Juan Feng, Wenming Yang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.04947">2609.04947</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.04947">PDF</a></p>

中文标题：MCPO：Modality-Contrastive Preference Optimization 面向 Multimodal Chain-of-Thought Compression

信号显示：最近，多模态大规模推理模型在通过长思维链（ M-CoT ）解决复杂任务方面表现出了非凡的能力。关键词：inference、serving、compression、alignment。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>One Diffusion Model, Two Roles: Guided Trajectory Planning and Safety-Critical Scenario Generation in Closed-Loop Simulation (Arka Pal, Rajesh Kumar, Hannes Eriksson, Rémi Lacombe, Arvid Laveno Ling, Ankit Gupta, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.04921">2609.04921</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.04921">PDF</a></p>

中文标题：One Diffusion Model，Two Roles：Guided Trajectory Planning 与 Safety-Critical Scenario Generation in 闭环仿真

信号显示：扩散概率模型可以捕捉驾驶场景中联合未来轨迹的多模态、交互丰富的分布。关键词：agent、rag、inference、serving。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Artificial Intelligence in Equity and Crypto Markets: Progress, Profitability Evidence, and the Limits of Automated Investing](https://arxiv.org/abs/2609.04917)
中文标题：股票和加密市场中的人工智能：进展、盈利能力证据和自动化投资的局限性
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Adaptation Interfaces for In-Context Tabular Foundation Models in Time-to-Event Prediction](https://arxiv.org/abs/2609.04901)
中文标题：事件时间预测中上下文表格基础模型的适应接口
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [RefactorPlatform: An Open-Source Harness for Controlled Evaluation of Repository-Scale Refactoring Agents](https://arxiv.org/abs/2609.04898)
中文标题：Refactor平台：An Open-Source Harness 面向 Controlled 评测 of Repository-Scale Refactoring Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [AutoLR: Automating the Path from Research to Launch Review in Industrial Recommender Systems](https://arxiv.org/abs/2609.04871)
中文标题：AutoLR ：工业推荐系统从研究到发布审核的自动化路径
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use Agents](https://arxiv.org/abs/2609.04869)
中文标题：从交互跟踪到持久技能：计算机使用代理的在线演进
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [PRISM-Bench: An Audio-Centric Diagnostic Benchmark for Text-to-Audio-Video Generation](https://arxiv.org/abs/2609.04867)
中文标题：PRISM-Bench：An Audio-Centric Diagnostic 基准 面向 Text-to-Audio-Video Generation
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MM-IFEval-Pro: A Multilingual and Attack-Resistant Benchmark for Instruction-Following in Vision-Language Models](https://arxiv.org/abs/2609.04859)
中文标题：MM-IFEval-Pro：A Multilingual 与 Attack-Resistant 基准 面向 Instruction-Following in Vision-Language Models
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [CoLMIN: LLM-based Multi-Decision Path Negotiation for Cooperative Autonomous Driving](https://arxiv.org/abs/2609.04807)
中文标题：CoLMIN：基于 LLM 的 Multi-Decision Path Negotiation 面向 Cooperative Autonomous Driving
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Intrinsic Temporal Adaptation of CLIP for Partially Relevant Video Retrieval](https://arxiv.org/abs/2609.04800)
中文标题：用于部分相关视频检索的剪辑的内在时间适应
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Diffusion Language Models for Mobile Edge Agentic AI: Foundations, Applications, and Challenges](https://arxiv.org/abs/2609.04778)
中文标题：Diffusion Language Models 面向 Mobile Edge Agentic AI：Foundations，Applications，与 Challenges
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Shadow Queries for Private Retrieval in Vector Databases](https://arxiv.org/abs/2609.04767)
中文标题：在矢量数据库中进行私有检索的阴影查询
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Knowing What Not to Answer: Selective Non-Compliance in Vision-Language Models](https://arxiv.org/abs/2609.04720)
中文标题：知道不该回答的问题：视觉语言模型中的选择性违规行为
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [AngelFingerprint: A Traceable, Explainable, and White-Box Stealthy Watermark for Text-Guided Image Editing](https://arxiv.org/abs/2609.04709)
中文标题：AngelFingerprint：A Traceable，可解释，与 White-Box Stealthy Watermark 面向 Text-Guided Image Editing
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Beyond Code Generation: Reliability, Verification, and Cost Economics in the Agentic Software Development Lifecycle](https://arxiv.org/abs/2609.04681)
中文标题：超越代码生成： Agent软件开发生命周期中的可靠性、验证和成本经济性
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [How Developers Discuss Generative AI: A Longitudinal Study of the Visual Studio Code Community](https://arxiv.org/abs/2609.04680)
中文标题：开发人员如何讨论生成式AI ： Visual Studio代码社区的纵向研究
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ERPBench: Evaluating LLM Agents for Enterprise Decision-Making Across Competitive Market Ecologies](https://arxiv.org/abs/2609.04667)
中文标题：ERPBench：Evaluating LLM Agents 面向 Enterprise Decision-Making Across Competitive Market Ecologies
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Latent-Aligned Reasoning for Multimodal Recommendation](https://arxiv.org/abs/2609.04645)
中文标题：多式联运建议的潜在一致推理
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [CrossDepth: Geometry-Constrained Attention for Generalizable Multi-View Surround Depth Estimation](https://arxiv.org/abs/2609.05397)
中文标题：CrossDepth：Geometry-Constrained Attention 面向 Generalizable Multi-View Surround Depth Estimation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Think-Verify-Revise: Neuro-Symbolic Visual Reasoning with Vision-Language Models and Dynamic Logic Tensor Networks](https://arxiv.org/abs/2609.05388)
中文标题：Think-Verify-Revise ：使用视觉语言模型和动态逻辑张量网络的神经符号视觉推理
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Towards Neuro-Symbolic Procedural Reasoning for Long-Horizon Vision-Language-Action Manipulation](https://arxiv.org/abs/2609.05369)
中文标题：长视野视觉-语言-动作操作的神经符号程序推理
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
