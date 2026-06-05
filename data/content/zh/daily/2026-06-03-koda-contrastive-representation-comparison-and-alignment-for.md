---
title: "增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性"
date: "2026-06-03"
target_date: "2026-06-03"
actual_date: "2026-06-02"
fallback_from: "2026-06-03"
lang: "zh"
slug: "2026-06-03-koda-contrastive-representation-comparison-and-alignment-for"
summary: "今天主要跟进：增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "safety", "systems", "training"]
topics: ["agents", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "safety", "systems", "training"]
sources_page: "/zh/daily/2026-06-03-koda-contrastive-representation-comparison-and-alignment-for-sources/"
generated_at: "2026-06-05T16:22:27.853890+00:00"
page_type: "brief"
candidate_count: 264
featured_count: 5
mentions_count: 15
---

# 增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。建议先看每篇的原文链接、摘要、评测设置和代码/数据是否可用，再决定是否深入复现。

## 重点论文：题目、看点与核验线索

### 1. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>KODA: Contrastive Representation Comparison and Alignment for Vision-Language Foundation Models (Youqi Wu, Mohammad Jalali, Farzan Farnia)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.04180">2606.04180</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.04180">PDF</a></p>

增强多模态模型理解图表和文档的能力。摘要显示：Vision-language foundation models such as CLIP and SigLIP provide widely used representations for multimodal learning systems. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>The Impact of Configuring Agentic AI Coding Tools on Build-vs-Buy Decisions: A Study Protocol (Jai Lal Lulla, Matthias Galster, Jie M. Zhang, Sebastian Baltes, Christoph Treude)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.03907">2606.03907</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.03907">PDF</a></p>

让 Agent 更可靠地调用工具和复用技能。摘要显示：Agentic AI coding tools write code with increasing autonomy and in doing so decide when to import a library and when to implement functionality from scratch. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Automating Information Extraction and Retrieval for Industrial Spare Parts Pooling (Dyuman Bulloni, Rocco Felici, Oliver Avram, Anna Valente)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.03367">2606.03367</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.03367">PDF</a></p>

提升 RAG 检索和知识库问答可靠性。摘要显示：Maintenance organizations in manufacturing try to avoid downtime and unnecessary purchasing by reusing existing assets, but the main obstacle is not a lack of parts but a lack of actionable visibility across sites and partners. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Stationarity-Aware Retrieval-Augmented Time Series Forecasting (Shiqiao Zhou, Holger Schöner, Zipeng Wu, Edouard Fouché, IAG Wilson, Shuo Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.04135">2606.04135</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.04135">PDF</a></p>

提升 RAG 检索和知识库问答可靠性。摘要显示：Time series forecasting relies on historical patterns, but real-world series often exhibit non-stationarity and regime shifts that challenge fully parametric forecasters. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Entropy Gate: Entropy Quenching for Near-Lossless Token Compression in LLM Pipelines (Justice Owusu Agyemang, Jerry John Kponyo, Kwame Opuni-Boachie Obour Agyekum, Francisca Adoma Acheampong, Kwame Agyeman-Prempeh Agyekum, James Dzisi Gadze)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.03739">2606.03739</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.03739">PDF</a></p>

让 Agent 更可靠地调用工具和复用技能。摘要显示：LLM pipelines waste substantial token budgets on low-information content: repeated context, verbose responses, and redundant boilerplate. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

## 其他值得关注
- [VLESA: Vision-Language Embodied Safety Agent for Human Activity Monitoring](https://arxiv.org/abs/2606.03954)：关注模型安全、护栏路由、风险分类或治理评测，适合跟进安全评测与治理工具链。
- [MM-BizRAG: Rethinking Multimodal Retrieval-Augmented Generation for General Purpose Enterprise Q&A](https://arxiv.org/abs/2606.04231)：关注检索、知识库问答与证据可靠性，适合跟进 RAG 评测和企业知识系统。
- [MimeLens: Position-Agnostic Content-Type Detection for Binary Fragments](https://arxiv.org/abs/2606.04171)：关注检索、知识库问答与证据可靠性，适合跟进 RAG 评测和企业知识系统。
- [When Autoregressive Consistency Hurts Safety Alignment](https://arxiv.org/abs/2606.04168)：关注模型安全、护栏路由、风险分类或治理评测，适合跟进安全评测与治理工具链。
- [End-to-End Text Line Detection and Ordering](https://arxiv.org/abs/2606.04166)：关注检索、知识库问答与证据可靠性，适合跟进 RAG 评测和企业知识系统。
- [Expert-Aware Refusal Steering](https://arxiv.org/abs/2606.04160)：关注模型安全、护栏路由、风险分类或治理评测，适合跟进安全评测与治理工具链。
- [HighTide: An Agent-Curated Open-Source VLSI Benchmark Suite](https://arxiv.org/abs/2606.04126)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [UltraEP: Unleash MoE Training and Inference on Rack-Scale Nodes with Near-Optimal Load Balancing](https://arxiv.org/abs/2606.04101)：关注推理成本、延迟、吞吐和部署约束，适合跟进系统优化。
- [MAOAM: Unified Object and Material Selection with Vision-Language Models](https://arxiv.org/abs/2606.04880)：关注检索、知识库问答与证据可靠性，适合跟进 RAG 评测和企业知识系统。
- [Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill](https://arxiv.org/abs/2606.03980)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [Agentic Chain-of-Thought Steering for Efficient and Controllable LLM Reasoning](https://arxiv.org/abs/2606.03965)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [AgenticRL: Self-Refining Agentic Reinforcement Learning for Vision-Conditioned UAV Navigation](https://arxiv.org/abs/2606.03963)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [SEAOTTER: Sensor Embedded Autoencoding with One-Time Transcode for Efficient Reconstruction](https://arxiv.org/abs/2606.03940)：关注多模态模型中的新任务、数据或系统线索，适合快速判断是否值得阅读全文。
- [Visual Instruction Tuning Aligns Modalities through Abstraction](https://arxiv.org/abs/2606.03871)：关注训练与后训练中的新任务、数据或系统线索，适合快速判断是否值得阅读全文。
- [Leveraging BART to Assess CS1 C++ Programming Assignments using Rubric-based Criteria](https://arxiv.org/abs/2606.03814)：关注检索、知识库问答与证据可靠性，适合跟进 RAG 评测和企业知识系统。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
