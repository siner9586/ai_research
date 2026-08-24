---
title: "让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性"
date: "2026-08-25"
target_date: "2026-08-23"
actual_date: "2026-08-21"
fallback_from: "2026-08-23"
lang: "zh"
slug: "2026-08-25-large-language-models-at-the-intersection-of"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "safety", "systems", "training", "video-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "safety", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-08-25-large-language-models-at-the-intersection-of-sources/"
generated_at: "2026-08-24T21:40:15.866618+00:00"
page_type: "brief"
candidate_count: 304
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Large Language Models at the Intersection of Software Engineering and Software Security:An Evidence-Centered Structured Survey and Research Agenda", "Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration", "ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models", "When Adaptation Hurts: Connecting Representational Drift to OOD Failures in MedSAM Fine-Tuning", "Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems", "PromptResponse: Optimizing Prompts for LLM Coding Tasks"]
featured_paper_urls: ["https://arxiv.org/abs/2608.21107", "https://arxiv.org/abs/2608.21208", "https://arxiv.org/abs/2608.21100", "https://arxiv.org/abs/2608.21300", "https://arxiv.org/abs/2608.21095", "https://arxiv.org/abs/2608.21074"]
featured_paper_titles_zh: ["软件工程和软件安全交叉领域的大型语言模型：以证据为中心的结构化调查和研究议程", "跨LLM开发代理的规范可移植性：规范驱动软件迁移中的跨代理兼容性", "ReFrame ：多模式大型语言模型中的循证引导测试时间安全对齐", "当适应受到伤害时：在MedSAM微调中将表征漂移连接到OOD失败", "Trustworthy RAG：An 评测 Agent 面向 Detecting Misinformation 与 Knowledge Poisoning in Generative AI Systems", "PromptResponse：Optimizing Prompts 面向 LLM Coding Tasks"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Large Language Models at the Intersection of Software Engineering and Software Security:An Evidence-Centered Structured Survey and Research Agenda (Wei Lin, Tao Zhou, Zhaofei Xie, Changgui Hong)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.21107">2608.21107</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.21107">PDF</a></p>

中文标题：软件工程和软件安全交叉领域的大型语言模型：以证据为中心的结构化调查和研究议程

信号显示：大语言模型（ LLM ）正在从代码完成转向存储库规模的代理，这些代理可检索上下文、编辑文件、执行工具并参与安全敏感的工作流。关键词：agent、workflow、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration (Oleg Grynets, Oleksii Ilchuk, Dariia Zatulna, Vasyl Lyashkevych)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.21208">2608.21208</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.21208">PDF</a></p>

中文标题：跨LLM开发代理的规范可移植性：规范驱动软件迁移中的跨代理兼容性

信号显示：本文研究了使用Oracle到PostgreSQL迁移作为受控软件转换任务的跨代理规范可移植性。关键词：agent、workflow、retrieval、compression。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models (Wenzheng Jiang, Xuankun Rong, Yuanzhao Zhai, Dawei Feng, Huaimin Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.21100">2608.21100</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.21100">PDF</a></p>

中文标题：ReFrame ：多模式大型语言模型中的循证引导测试时间安全对齐

信号显示：虽然多模态大语言模型（ MLLM ）将模型功能扩展到文本之外，但它们也使安全对齐变得越来越具有挑战性。关键词：agent、serving、alignment、safety。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>When Adaptation Hurts: Connecting Representational Drift to OOD Failures in MedSAM Fine-Tuning (Marko Haralović, Sounic Akkaraju, Carlo Baretta, Vasil Zapryanov, Alexia Briassouli)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.21300">2608.21300</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.21300">PDF</a></p>

中文标题：当适应受到伤害时：在MedSAM微调中将表征漂移连接到OOD失败

信号显示：医学图像分割的基础模型，如基于提示的MedSAM ，可以很好地泛化各个领域和模式，通常在零或少量设置中进行。关键词：serving、alignment、benchmark、code。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems (Balkrishna Giri, Md Toufique Hasan, Jussi Rasku, Muhammad Waseem, Pekka Abrahamsson)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.21095">2608.21095</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.21095">PDF</a></p>

中文标题：Trustworthy RAG：An 评测 Agent 面向 Detecting Misinformation 与 Knowledge Poisoning in Generative AI Systems

信号显示：检索-增强生成（ RAG ）将大语言模型（ LLM ）输出作为外部知识的基础，但RAG系统通常会信任他们检索到的任何内容，从而造成安全可靠性差距：高语义相关性并不能保证事实真相。关键词：agent、rag、retrieval、inference。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>PromptResponse: Optimizing Prompts for LLM Coding Tasks (Erik Thureck, Robert Kühnen, Tim Jacobowitz)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.21074">2608.21074</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.21074">PDF</a></p>

中文标题：PromptResponse：Optimizing Prompts 面向 LLM Coding Tasks

信号显示：大语言模型（ LLM ）越来越多地用于研究工作流程和软件开发管道，但其输出对输入提示的变化仍然敏感。关键词：workflow、alignment、evaluation、code。代码/数据可用性需查看原文确认。

## 其他值得关注
- [AudioWorldSim: Realistic Binaural Audio Datasets For World Models](https://arxiv.org/abs/2608.21075)
中文标题：AudioWorldSim：Realistic Binaural Audio Datasets 面向 世界模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [RDANet: Relative Degradation Aware Network for Infrared Small Target Detection](https://arxiv.org/abs/2608.20870)
中文标题：RDANet：Relative Degradation Aware Network 面向 Infrared Small Target Detection
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Automated Trajectory Evaluation for Mobile Agents via Step-Level Consequence Reasoning and Aggregation](https://arxiv.org/abs/2608.20797)
中文标题：通过分步结果推理和聚合对移动座席进行自动轨迹评估
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [CoST: Semantic-Aware Urban Understanding via Spatial-Temporal Alignment](https://arxiv.org/abs/2608.21041)
中文标题：CoST ：通过时空对齐的语义感知城市理解
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Trojaning the Alignment: Stealthy Backdoor Attacks against Graph Foundation Models](https://arxiv.org/abs/2608.20991)
中文标题：特洛伊木马对齐：针对Graph Foundation模型的隐形后门攻击
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Breaking High Confidence: Practical Face Impersonation under High-Security Thresholds](https://arxiv.org/abs/2608.20884)
中文标题：打破高置信度：高安全阈值下的实际面部模拟
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [BC-Bench: Evaluating Agentic Engineering in a Domain-Specific Language for ERP](https://arxiv.org/abs/2608.20851)
中文标题：BC-Bench：Evaluating Agentic Engineering in a Domain-Specific Language 面向 ERP
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Routing Before Looking: Query-Adaptive Evidence Acquisition for Long-form Video Understanding](https://arxiv.org/abs/2608.20805)
中文标题：查询前路由：长视频理解的查询自适应证据采集
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Generating Multi-view Adversarial Examples for Visual Geometry Grounded Transformer](https://arxiv.org/abs/2608.20748)
中文标题：Generating Multi-view Adversarial Examples 面向 Visual Geometry Grounded Transformer
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [AsmEvo: Agentic Assembly-Level Optimization of AMD GPU Kernels with Functional Equivalence Verification](https://arxiv.org/abs/2608.20711)
中文标题：AsmEvo ：通过功能等效验证对AMD GPU内核进行代理装配级优化
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [TopoSurfel: Closing the Loop between Gaussian Surfels and Meshes for Surface Reconstruction](https://arxiv.org/abs/2608.20687)
中文标题：TopoSurfel ：关闭高斯表面和网格之间的循环以进行表面重建
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [DreamBench-SWE: A Multi-Session Memory-Hygiene Benchmark for Software Agents](https://arxiv.org/abs/2608.20664)
中文标题：DreamBench-SWE：A Multi-Session Memory-Hygiene 基准 面向 Software Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [RiskTraf: Risk-Extrapolated Residual Learning for Multi-Variate Traffic Flow Prediction](https://arxiv.org/abs/2608.20656)
中文标题：RiskTraf：Risk-Extrapolated Residual Learning 面向 Multi-Variate Traffic Flow Prediction
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Meta-clustering of milk mid-infrared spectra identifies dairy cow groups associated with negative energy balance in early lactation](https://arxiv.org/abs/2608.20653)
中文标题：乳汁中红外光谱的元聚类识别与早期哺乳期负能量平衡相关的奶牛群
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Rethinking Expressivity and Efficiency in Test-Time Training](https://arxiv.org/abs/2608.21308)
中文标题：重新思考测试时间培训中的表现力和效率
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [VT-MUSE: Multimodal Unified Sequential Visuotactile Representation Learning for Manipulation](https://arxiv.org/abs/2608.21290)
中文标题：VT-MUSE：Multimodal Unified Sequential Visuotactile Representation Learning 面向 Manipulation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment](https://arxiv.org/abs/2608.21278)
中文标题：CLEAR：Continuous Latent Adapter Routing 面向 Utility-Preserving LLM Safety Alignment
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [EnSI-RAG: Entity-Structure-Indexed Retrieval-Augmented Generation for Long-Document Question Answering](https://arxiv.org/abs/2608.21252)
中文标题：EnSI-RAG：Entity-Structure-Indexed Retrieval-Augmented Generation 面向 Long-Document Question Answering
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Benchmarking Patent Drafting from Inventor-Style Disclosures](https://arxiv.org/abs/2608.21249)
中文标题：根据发明人样式披露对专利起草进行基准测试
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Personalized Privacy Control in LLMs via Attention Head Intervention](https://arxiv.org/abs/2608.21209)
中文标题：通过Attention Head干预实现LLM中的个性化隐私控制
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
