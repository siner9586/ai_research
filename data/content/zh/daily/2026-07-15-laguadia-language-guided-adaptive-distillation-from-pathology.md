---
title: "增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力"
date: "2026-07-15"
target_date: "2026-07-13"
actual_date: "2026-07-13"
fallback_from: ""
lang: "zh"
slug: "2026-07-15-laguadia-language-guided-adaptive-distillation-from-pathology"
summary: "今天主要跟进：增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "safety", "systems", "training", "vision-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "safety", "systems", "training", "vision-generation"]
sources_page: "/zh/daily/2026-07-15-laguadia-language-guided-adaptive-distillation-from-pathology-sources/"
generated_at: "2026-07-14T22:10:13.781486+00:00"
page_type: "brief"
candidate_count: 374
featured_count: 6
mentions_count: 20
featured_paper_titles: ["LaGuadia: Language-Guided Adaptive Distillation from Pathology Foundation Models", "MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents", "RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM", "MAGIC: Transition-Aware Generation of Navigable Multi-Scene Game Worlds with Large Language Models", "TreeThink: A Modular Tree Search Library for Mathematical Reasoning with LLMs", "Input-Aware Dynamic Backdoor Attack Against Quantum Neural Networks"]
featured_paper_urls: ["https://arxiv.org/abs/2607.11257", "https://arxiv.org/abs/2607.11818", "https://arxiv.org/abs/2607.11683", "https://arxiv.org/abs/2607.11594", "https://arxiv.org/abs/2607.11258", "https://arxiv.org/abs/2607.11843"]
featured_paper_titles_zh: ["LaGuadia：Language-Guided Adaptive Distillation 来自 Pathology Foundation Models", "MM-ToolSandBox：A Unified 框架 面向 Evaluating Visual Tool-Calling Agents", "RAGU ：采用紧凑型领域适应型LLM的多步GraphRAG引擎", "MAGIC ：使用大型语言模型生成可导航的多场景游戏世界的过渡感知", "TreeThink ：使用LLM进行数学推理的模块化树搜索库", "针对量子神经网络的输入感知动态后门攻击"]
---

# 增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>LaGuadia: Language-Guided Adaptive Distillation from Pathology Foundation Models (Gangsu Kim, Won-Ki Jeong)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.11257">2607.11257</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.11257">PDF</a></p>

中文标题：LaGuadia：Language-Guided Adaptive Distillation 来自 Pathology Foundation Models

信号显示：病理学基础模型（ PFM ）提供强大的全幻灯片图像（ WSI ）表示，但面临巨大的计算成本。关键词：alignment、code、vision-language、image。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents (Kaixin Ma, Di Feng, Alexander Metz, Jiarui Lu, Eshan Verma, Afshin Dehghan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.11818">2607.11818</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.11818">PDF</a></p>

中文标题：MM-ToolSandBox：A Unified 框架 面向 Evaluating Visual Tool-Calling Agents

信号显示：我们推出了MM-ToolSandBox ，这是一个可视化接地工具调用代理的基准和评估框架。关键词：agent、workflow、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM (Mikhail Komarov, Ivan Bondarenko, Stanislav Shtuka, Oleg Sedukhin, Roman Shuvalov, Yana Dementyeva, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.11683">2607.11683</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.11683">PDF</a></p>

中文标题：RAGU ：采用紧凑型领域适应型LLM的多步GraphRAG引擎

信号显示：图检索增强生成（ GraphRAG ）通过结构化知识增强大语言模型，但现有系统在单个提取通道中构建知识图，产生噪声实体和脆性检索。关键词：rag、retrieval、code、open-source。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>MAGIC: Transition-Aware Generation of Navigable Multi-Scene Game Worlds with Large Language Models (Tsz Hei Fan, Choi Wing Fung, Yuxuan Wan, Shuqing Li, Michael R. Lyu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.11594">2607.11594</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.11594">PDF</a></p>

中文标题：MAGIC ：使用大型语言模型生成可导航的多场景游戏世界的过渡感知

信号显示：多场景导航（在一个有界空间中清除目标，然后穿过入口进入下一个）是当代3D游戏的一个定义特征，但创作它是一项艰巨的任务：每个入口必须在两侧都有一致的端点，每个内部。关键词：agent、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 5. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>TreeThink: A Modular Tree Search Library for Mathematical Reasoning with LLMs (Burak S. Akbudak, Zeynel A. Uluşan, Can S. Erer, Gözde Gül Şahin)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.11258">2607.11258</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.11258">PDF</a></p>

中文标题：TreeThink ：使用LLM进行数学推理的模块化树搜索库

信号显示：树搜索算法可以系统地探索神经定理证明中的证明空间。关键词：inference、evaluation、code、open-source。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Input-Aware Dynamic Backdoor Attack Against Quantum Neural Networks (Junrui Zhang, Zemin Chen, Lusi Li, Mohammad Ghasemigol, Daniel Takabi, Rui Ning)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.11843">2607.11843</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.11843">PDF</a></p>

中文标题：针对量子神经网络的输入感知动态后门攻击

信号显示：量子神经网络（ QNN ）是近期量子设备上量子机器学习的一个有前途的框架，但其安全风险仍未得到充分了解。关键词：rag、deployment、fine-tuning、visual。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Technical Report on the CVPR 2026@AdvML Workshop Challenge](https://arxiv.org/abs/2607.11560)
中文标题：关于CVPR 2026 @ AdvML研讨会挑战的技术报告
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ToFu: A White-Box, Token-Efficient Agent Harness for Researchers](https://arxiv.org/abs/2607.11423)
中文标题：ToFu：A White-Box，Token-Efficient Agent Harness 面向 Researchers
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [HASTE: A Platform for Rapid Post-Disaster Building Damage Assessment](https://arxiv.org/abs/2607.11838)
中文标题：HASTE：A 平台 面向 Rapid Post-Disaster Building Damage 评估
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming](https://arxiv.org/abs/2607.11698)
中文标题：Agent Hacks Agent：Autoresearch 面向 Production-Agent Red-Teaming
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [HyperSafe: Inference-Time Safety Recovery for Fine-Tuned Language Models](https://arxiv.org/abs/2607.11475)
中文标题：HyperSafe：Inference-Time Safety Recovery 面向 Fine-Tuned Language Models
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [HierCAD: Hierarchical Text-to-CAD Design via Structure Alignment and Parameter Grounding](https://arxiv.org/abs/2607.11339)
中文标题：HierCAD ：通过结构对齐和参数接地实现分层文本到CAD设计
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [SISA-Rec: A Semantically Integrated Sequential Recommender with Contrastive Alignment](https://arxiv.org/abs/2607.11168)
中文标题：SISA-Rec ：具有对比对齐的语义集成顺序推荐器
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [SynCLIP: Synonym-Coherent Language-Image Pretraining for Robust Open-Vocabulary Dense Perception](https://arxiv.org/abs/2607.11008)
中文标题：SynCLIP：Synonym-Coherent Language-Image Pretraining 面向 Robust Open-Vocabulary Dense Perception
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [PREF-Gate: Provenance-Constrained Relational Evidence Fusion with Validation-Gated Selection for Graph Fraud Detection](https://arxiv.org/abs/2607.11212)
中文标题：PREF-Gate：Provenance-Constrained Relational Evidence Fusion with Validation-Gated Selection 面向 Graph Fraud Detection
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Amplitude-Only FFN Intervention for Tool-Structured LLM Inference Method: Gated Evaluation Protocol, and Cross-Model Empirical Results](https://arxiv.org/abs/2607.11183)
中文标题：Amplitude-Only FFN Intervention 面向 Tool-Structured LLM Inference Method：Gated 评测 Protocol，与 Cross-Model Empirical Results
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Revisiting Matching Response and Swept Feature Volumes for Wide-baseline Omnidirectional Stereo](https://arxiv.org/abs/2607.11097)
中文标题：重新审视宽基线全向立体声的匹配响应和扫描功能音量
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [BackendForge: Benchmarking Agentic End-to-End Code Generation with Backend Services](https://arxiv.org/abs/2607.11042)
中文标题：BackendForge ：使用后端服务对Agentic端到端代码生成进行基准测试
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [TreeSoc: Tree-Structured Dynamic Reasoning and Tool Synergy for Soccer Video Understanding](https://arxiv.org/abs/2607.10990)
中文标题：TreeSoc：Tree-Structured Dynamic Reasoning 与 Tool Synergy 面向 Soccer Video Understanding
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation](https://arxiv.org/abs/2607.11886)
中文标题：Read It Back：Pretrained MLLMs Are Zero-Shot Reward Models 面向 Text-to-Image Generation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Evidence-Backed Video Question Answering](https://arxiv.org/abs/2607.11862)
中文标题：证据支持的视频问题答案
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MicroCharNet: Less is More for License Plate Character Detection](https://arxiv.org/abs/2607.11830)
中文标题：MicroCharNet：Less is More 面向 License Plate Character Detection
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Higher-Order Cell Tracking Transformer](https://arxiv.org/abs/2607.11754)
中文标题：高阶单元跟踪变压器
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems](https://arxiv.org/abs/2607.11751)
中文标题：当本地监视器错过成分危害时：诊断多Agent系统中的分布式后门
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [GFR-SAM: Training-Free Referring Camouflaged Object Segmentation via Cross-Image Prompting](https://arxiv.org/abs/2607.11732)
中文标题：GFR-SAM ：通过交叉图像提示进行无培训的引用伪装对象分割
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [FoundationGeo: Learning Spatial Pixel-Wise Fields for Monocular Metric Geometry](https://arxiv.org/abs/2607.11588)
中文标题：FoundationGeo：Learning Spatial Pixel-Wise Fields 面向 Monocular Metric Geometry
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
