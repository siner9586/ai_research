---
title: "让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性"
date: "2026-11-08"
target_date: "2026-11-06"
actual_date: "2026-11-05"
fallback_from: "2026-11-06"
lang: "zh"
slug: "2026-11-08-dataset-collection-and-fine-tuning-of-nllb"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "safety", "speech-audio", "systems", "training"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "safety", "speech-audio", "systems", "training"]
sources_page: "/zh/daily/2026-11-08-dataset-collection-and-fine-tuning-of-nllb-sources/"
generated_at: "2026-11-07T16:18:53.929746+00:00"
page_type: "brief"
candidate_count: 499
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Dataset Collection and Fine-Tuning of NLLB for German--English Translation", "Automated Video-to-QA Pipeline: End-to-End Question Generation and Verification Using Large Language Models", "Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes", "Multimodal Information Interactions Bottleneck for Multimodal Self-Supervised Learning", "Simple Meta-Learning for HPO and CASH Using Performance Representations", "ACSeL: Adaptive Configuration Search for Hardware-Constrained LLM Inference"]
featured_paper_urls: ["https://arxiv.org/abs/2611.07797", "https://arxiv.org/abs/2611.07755", "https://arxiv.org/abs/2611.07730", "https://arxiv.org/abs/2611.07718", "https://arxiv.org/abs/2611.07659", "https://arxiv.org/abs/2611.07570"]
featured_paper_titles_zh: ["Dataset Collection 与 Fine-Tuning of NLLB 面向 German--English Translation", "自动视频到QA管道：使用大型语言模型进行端到端问题生成和验证", "超越下一步：多Agent场景中的世界模型引导的人性化导航", "多模态自监督学习的多模态信息交互瓶颈", "Simple Meta-Learning 面向 HPO 与 CASH 使用 Performance Representations", "ACSeL：Adaptive Configuration Search 面向 Hardware-Constrained LLM Inference"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Dataset Collection and Fine-Tuning of NLLB for German--English Translation (SK Deeraj, Yash Ingle, Pruthwik Mishra)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.07797">2611.07797</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.07797">PDF</a></p>

中文标题：Dataset Collection 与 Fine-Tuning of NLLB 面向 German--English Translation

信号显示：本文描述了OPUS Books中高质量平行语料库的策展以及Meta的NLLB-200模型在德语-英语翻译中的微调。关键词：serving、deployment、evaluation、code。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Automated Video-to-QA Pipeline: End-to-End Question Generation and Verification Using Large Language Models (Jaival Chauhan, Vikram Singh, Pruthwik Mishra)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.07755">2611.07755</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.07755">PDF</a></p>

中文标题：自动视频到QA管道：使用大型语言模型进行端到端问题生成和验证

信号显示：在YouTube等平台上，教育和信息视频内容呈指数级增长，这对高效的知识检索和评估提出了挑战。关键词：retrieval、code、synthetic data、fine-tuning。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes (Seong-Eun Hong, JuYeong Hwang, Jinhyun Kim, Hanyoung Jang, HyeongYeop Kang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.07730">2611.07730</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.07730">PDF</a></p>

中文标题：超越下一步：多Agent场景中的世界模型引导的人性化导航

信号显示：在人满为患的场景中选择下一个动作不仅仅是避免当前阻碍的问题：一个动作在当地是可行的，但可以漂移到道路上而不是人行横道上，切成人行横道的小溪，或者在狭窄的街道上设置瓶颈。关键词：agent、inference、deployment、evaluation。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Multimodal Information Interactions Bottleneck for Multimodal Self-Supervised Learning (Liangjian Wen, Jiangtao Zheng, Jiang Duan, Qun Dai, Yong Dai, Jianzhuang Liu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.07718">2611.07718</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.07718">PDF</a></p>

中文标题：多模态自监督学习的多模态信息交互瓶颈

信号显示：多模态自我监督学习受到图像、文本、音频和表格数据等多模态数据源的异构性、不平等信息性和复杂信息交互的挑战。关键词：rag、benchmark、code、multimodal。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Simple Meta-Learning for HPO and CASH Using Performance Representations (Emiel Witting, Cheng Yan, Tom Julian Viering)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.07659">2611.07659</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.07659">PDF</a></p>

中文标题：Simple Meta-Learning 面向 HPO 与 CASH 使用 Performance Representations

信号显示：超参数优化（ HPO ）以及组合算法选择和超参数优化（ CASH ）的贝叶斯优化通常依赖于显式超参数编码作为替代输入。关键词：benchmark、code、coding、Code Intelligence。代码/数据可用性需查看原文确认。

### 6. 评测视频生成的时间一致性和运动真实感

<p class="paper-meta-line"><span>ACSeL: Adaptive Configuration Search for Hardware-Constrained LLM Inference (Bokun Wang, Hung-Yueh Chiang, Diana Marculescu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.07570">2611.07570</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.07570">PDF</a></p>

中文标题：ACSeL：Adaptive Configuration Search 面向 Hardware-Constrained LLM Inference

信号显示：在包括边缘设备在内的紧凑内存和延迟服务级别目标（ SLO ）下为大语言模型（ LLM ）提供服务，需要共同选择模型大小、批量大小、量化算法和混合精度量化方案。关键词：inference、serving、deployment、latency。代码/数据可用性需查看原文确认。

## 其他值得关注
- [MetricTrail: Revisiting the Power of Metric Depth and Local Optimization for Long-Sequence Streaming 3D Reconstruction](https://arxiv.org/abs/2611.07555)
中文标题：MetriCTrAIl ：重新审视长序列流3D重建的度量深度和局部优化的力量
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model](https://arxiv.org/abs/2611.07513)
中文标题：Concertina：Embodying Manipulation 与 Cognition in One Diffusion Vision-Language Model
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Signed but Not Safe: Requirement Integrity in Multi-Agent LLM Handoffs](https://arxiv.org/abs/2611.07483)
中文标题：已签名但不安全： Multi-Agent LLM Handoff中的要求完整性
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SAVeR$^2$: Reasoning-based Safety Alignment for Large Reasoning Models via Verifiable Rewards](https://arxiv.org/abs/2611.07482)
中文标题：SAVeR $ ^ 2 $ ：通过可验证奖励实现基于推理的大型推理模型的安全一致性
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [BRIDGE: Bridging the Semantic Quantization Gap for Generative Recommendation](https://arxiv.org/abs/2611.07425)
中文标题：桥梁：弥合生成推荐的语义量化差距
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [WeLM-Image: A Unified Image Generation Model towards Visual Intelligence](https://arxiv.org/abs/2611.07392)
中文标题：WeLM-Image ：面向视觉智能的统一图像生成模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ReproBridge: Building Reproducibility into ML Research Artifacts](https://arxiv.org/abs/2611.08452)
中文标题：ReproBridge：Building 可复现性 into ML Research Artifacts
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Hybrid Machine Learning for Imbalanced Landing-Phase Safety Event Prediction from Flight Data](https://arxiv.org/abs/2611.08386)
中文标题：基于飞行数据的不平衡着陆阶段安全事件预测的混合机器学习
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [SpecCTMC: Exact Speculative Simulation of Diffusion Language Model Continuous-Time Markov Chains](https://arxiv.org/abs/2611.08362)
中文标题：SpecCTMC ：扩散语言模型连续时间马尔可夫链的精确推测仿真
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks](https://arxiv.org/abs/2611.08281)
中文标题：Multimodal-SEA：基准ing AI Agent Security under Multimodal Social Engineering Attacks
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [LeanContext: Disentangling Mathematical Resources from Local Formal Context in Lean Whole-Proof Generation](https://arxiv.org/abs/2611.08277)
中文标题：LeanContext：Disentangling Mathematical Resources 来自 Local Formal Context in Lean Whole-Proof Generation
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Terminal-style Mathematical Modeling Bench: The First Agentic and Verifiable Benchmark for Mathematical Modeling](https://arxiv.org/abs/2611.08237)
中文标题：终端式数学建模平台：第一个代理和可验证的数学建模基准
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ProQuant: Progressive Quantization-aware Training for Edge MLLMs](https://arxiv.org/abs/2611.08216)
中文标题：ProQuant：Progressive Quantization-aware Training 面向 Edge MLLMs
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [A Generative Foundation Model for Multimodal Tokamak Tasks](https://arxiv.org/abs/2611.08153)
中文标题：多式联运托卡马克任务的生成基础模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Gabor Gabor: E-Gaborformer, a Strictly Causal Speech Recognizer with Gabor-Dictionary Convolutions and Delta-Rule Memory](https://arxiv.org/abs/2611.08092)
中文标题：Gabor Gabor ： E-Gaborformer ，具有Gabor字典卷积和三角规则记忆的严格因果语音识别器
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [MUSS: A Multi-scale and Sequence-based Model for Single-cell Gene Regulation](https://arxiv.org/abs/2611.08086)
中文标题：MUSS：A Multi-scale 与 Sequence-based Model 面向 Single-cell Gene Regulation
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Probabilistic Relevance Decisions for Semantic Retrieval](https://arxiv.org/abs/2611.08014)
中文标题：语义检索的概率相关性决策
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Symmetry-Aware Surrogate-Assisted Testing of UAVs](https://arxiv.org/abs/2611.08012)
中文标题：无人机的对称感知代理辅助测试
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [How Far Can Lightweight LLMs Go in Intent-to-SLO Translation?](https://arxiv.org/abs/2611.07982)
中文标题：轻量级LLM在Intent-to-SLO翻译中可以走多远？
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Circe: Training-Free LLM Self-Evaluation via Component Interaction Consistency](https://arxiv.org/abs/2611.07948)
中文标题：Circe ：通过组件交互一致性进行免费培训LLM自我评估
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
