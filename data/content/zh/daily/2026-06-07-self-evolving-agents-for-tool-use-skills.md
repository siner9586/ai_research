---
title: "今日重点：让 Agent 更可靠地调用工具和复用技能；另含增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力"
date: "2026-06-07"
target_date: "2026-06-05"
actual_date: "2026-06-04"
fallback_from: "2026-06-05"
lang: "zh"
slug: "2026-06-07-self-evolving-agents-for-tool-use-skills"
summary: "本期从 18 篇候选论文中筛出 6 篇重点论文和 12 篇补充关注论文。重点不是泛泛列主题，而是围绕：让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力。"
tags: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "robotics", "safety", "systems", "training", "video-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "robotics", "safety", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-06-07-self-evolving-agents-for-tool-use-skills-sources/"
generated_at: "2026-06-05T10:06:29.761750+00:00"
page_type: "brief"
candidate_count: 18
featured_count: 6
mentions_count: 12
---

# 今日重点：让 Agent 更可靠地调用工具和复用技能；另含增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力

**日期**: 2026-06-07

## 一眼看懂本期

本期从 18 篇候选论文中筛出 6 篇重点论文和 12 篇补充关注论文。重点不是泛泛列主题，而是围绕：让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力。

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力。建议先看每篇的原文链接、摘要、评测设置和代码/数据是否可用，再决定是否深入复现。

## 重点论文：题目、看点与核验线索

### 1. 让 Agent 更可靠地调用工具和复用技能

- 原始论文标题: Self Evolving Agents for Tool Use Skills
- 作者/机构: Alice Chen, Bob Smith
- 归类: Agent 与工具调用
- arXiv: [2606.00001](https://arxiv.org/abs/2606.00001)
- PDF: [PDF](https://arxiv.org/pdf/2606.00001)
- 一句话看点: 重点在于：让 Agent 更可靠地调用工具和复用技能。摘要给出的直接线索是：Agents learn reusable tool use skills through iterative self improvement, unit tests, execution feedback, and evaluation.
- 它想解决什么: 它要解决的问题可以理解为：在真实研究或工程场景中，让 Agent 更可靠地调用工具和复用技能仍不稳定、不透明或成本较高。
- 大致怎么做: 方法线索来自标题、摘要和公开元数据；重点看它如何设计数据、评测、训练或系统流程，而不把摘要扩展成未验证结论。
- 可以怎样跟进: 从业者可优先检查三点：是否有可复现资产，评测是否贴近真实场景，以及方案是否能迁移到自己的模型、检索、Agent 或部署链路。
- 注意事项: 当前只是基于 arXiv 预印本元数据的筛选判断，不代表论文结论已经被同行评审或生产环境验证。
- 快速判断:
  - 一句话：让 Agent 更可靠地调用工具和复用技能。
  - 看点：摘要是否给出清晰任务、数据、评测或系统收益。
  - 核验：优先打开原文确认实验设置、基线和代码/数据是否可用。

### 2. 增强多模态模型理解图表和文档的能力

- 原始论文标题: Multimodal Safety Evaluation for Vision Language Models
- 作者/机构: Eva Green
- 归类: 安全与对齐
- arXiv: [2606.00004](https://arxiv.org/abs/2606.00004)
- PDF: [PDF](https://arxiv.org/pdf/2606.00004)
- 一句话看点: 重点在于：强化多模态模型对图表、文档和视觉信息的理解。摘要给出的直接线索是：A safety evaluation suite measures multimodal models across risky visual prompts, jailbreak attempts, and alignment failures.
- 它想解决什么: 它要解决的问题可以理解为：在真实研究或工程场景中，强化多模态模型对图表、文档和视觉信息的理解仍不稳定、不透明或成本较高。
- 大致怎么做: 方法线索来自标题、摘要和公开元数据；重点看它如何设计数据、评测、训练或系统流程，而不把摘要扩展成未验证结论。
- 可以怎样跟进: 从业者可优先检查三点：是否有可复现资产，评测是否贴近真实场景，以及方案是否能迁移到自己的模型、检索、Agent 或部署链路。
- 注意事项: 当前只是基于 arXiv 预印本元数据的筛选判断，不代表论文结论已经被同行评审或生产环境验证。
- 快速判断:
  - 一句话：强化多模态模型对图表、文档和视觉信息的理解。
  - 看点：摘要是否给出清晰任务、数据、评测或系统收益。
  - 核验：优先打开原文确认实验设置、基线和代码/数据是否可用。

### 3. 提升模型推理、规划和验证能力

- 原始论文标题: Efficient Long Context Inference with Cache Compression
- 作者/机构: Carol Li
- 归类: 系统与部署
- arXiv: [2606.00002](https://arxiv.org/abs/2606.00002)
- PDF: [PDF](https://arxiv.org/pdf/2606.00002)
- 一句话看点: 重点在于：改进模型推理、规划或验证过程。摘要给出的直接线索是：A systems method reduces memory and latency during long context model inference while preserving code reasoning accuracy.
- 它想解决什么: 它要解决的问题可以理解为：在真实研究或工程场景中，改进模型推理、规划或验证过程仍不稳定、不透明或成本较高。
- 大致怎么做: 方法线索来自标题、摘要和公开元数据；重点看它如何设计数据、评测、训练或系统流程，而不把摘要扩展成未验证结论。
- 可以怎样跟进: 从业者可优先检查三点：是否有可复现资产，评测是否贴近真实场景，以及方案是否能迁移到自己的模型、检索、Agent 或部署链路。
- 注意事项: 当前只是基于 arXiv 预印本元数据的筛选判断，不代表论文结论已经被同行评审或生产环境验证。
- 快速判断:
  - 一句话：改进模型推理、规划或验证过程。
  - 看点：摘要是否给出清晰任务、数据、评测或系统收益。
  - 核验：优先打开原文确认实验设置、基线和代码/数据是否可用。

### 4. 提升 RAG 检索和知识库问答可靠性

- 原始论文标题: RAG Evaluation under Noisy Retrieval
- 作者/机构: Dan Wang
- 归类: 基准与评测
- arXiv: [2606.00003](https://arxiv.org/abs/2606.00003)
- PDF: [PDF](https://arxiv.org/pdf/2606.00003)
- 一句话看点: 重点在于：提升检索增强生成和知识库问答的可靠性。摘要给出的直接线索是：A benchmark studies retrieval augmented generation reliability under noisy evidence, missing citations, and adversarial documents.
- 它想解决什么: 它要解决的问题可以理解为：在真实研究或工程场景中，提升检索增强生成和知识库问答的可靠性仍不稳定、不透明或成本较高。
- 大致怎么做: 方法线索来自标题、摘要和公开元数据；重点看它如何设计数据、评测、训练或系统流程，而不把摘要扩展成未验证结论。
- 可以怎样跟进: 从业者可优先检查三点：是否有可复现资产，评测是否贴近真实场景，以及方案是否能迁移到自己的模型、检索、Agent 或部署链路。
- 注意事项: 当前只是基于 arXiv 预印本元数据的筛选判断，不代表论文结论已经被同行评审或生产环境验证。
- 快速判断:
  - 一句话：提升检索增强生成和知识库问答的可靠性。
  - 看点：摘要是否给出清晰任务、数据、评测或系统收益。
  - 核验：优先打开原文确认实验设置、基线和代码/数据是否可用。

### 5. 提升代码生成、执行反馈和自动修复能力

- 原始论文标题: Code Model Repair with Execution Feedback
- 作者/机构: Frank Moore
- 归类: 代码智能
- arXiv: [2606.00005](https://arxiv.org/abs/2606.00005)
- PDF: [PDF](https://arxiv.org/pdf/2606.00005)
- 一句话看点: 重点在于：提升代码生成、执行反馈和自动修复能力。摘要给出的直接线索是：Code models improve patch generation through execution feedback loops, repository tests, and API-aware repair.
- 它想解决什么: 它要解决的问题可以理解为：在真实研究或工程场景中，提升代码生成、执行反馈和自动修复能力仍不稳定、不透明或成本较高。
- 大致怎么做: 方法线索来自标题、摘要和公开元数据；重点看它如何设计数据、评测、训练或系统流程，而不把摘要扩展成未验证结论。
- 可以怎样跟进: 从业者可优先检查三点：是否有可复现资产，评测是否贴近真实场景，以及方案是否能迁移到自己的模型、检索、Agent 或部署链路。
- 注意事项: 当前只是基于 arXiv 预印本元数据的筛选判断，不代表论文结论已经被同行评审或生产环境验证。
- 快速判断:
  - 一句话：提升代码生成、执行反馈和自动修复能力。
  - 看点：摘要是否给出清晰任务、数据、评测或系统收益。
  - 核验：优先打开原文确认实验设置、基线和代码/数据是否可用。

### 6. 改进训练数据筛选、合成和去重流程

- 原始论文标题: Synthetic Data Curation for Post Training
- 作者/机构: Henry Liu
- 归类: 数据工程
- arXiv: [2606.00007](https://arxiv.org/abs/2606.00007)
- PDF: [PDF](https://arxiv.org/pdf/2606.00007)
- 一句话看点: 重点在于：改进训练数据筛选、合成和去重流程。摘要给出的直接线索是：A data pipeline selects synthetic instruction data for fine-tuning and post-training with quality filters.
- 它想解决什么: 它要解决的问题可以理解为：在真实研究或工程场景中，改进训练数据筛选、合成和去重流程仍不稳定、不透明或成本较高。
- 大致怎么做: 方法线索来自标题、摘要和公开元数据；重点看它如何设计数据、评测、训练或系统流程，而不把摘要扩展成未验证结论。
- 可以怎样跟进: 从业者可优先检查三点：是否有可复现资产，评测是否贴近真实场景，以及方案是否能迁移到自己的模型、检索、Agent 或部署链路。
- 注意事项: 当前只是基于 arXiv 预印本元数据的筛选判断，不代表论文结论已经被同行评审或生产环境验证。
- 快速判断:
  - 一句话：改进训练数据筛选、合成和去重流程。
  - 看点：摘要是否给出清晰任务、数据、评测或系统收益。
  - 核验：优先打开原文确认实验设置、基线和代码/数据是否可用。

## 其他值得关注
- [让 Agent 更可靠地调用工具和复用技能](https://arxiv.org/abs/2606.00012) - Agent 与工具调用，score 6。关注理由： 重点在于：让 Agent 更可靠地调用工具和复用技能。摘要给出的直接线索是：Post-training with preference optimization reduces harmful tool calls and improves auditability.
- [识别并缓解模型安全、越狱和对齐风险](https://arxiv.org/abs/2606.00017) - 安全与对齐，score 6。关注理由： 重点在于：发现并缓解模型安全、越狱和对齐风险。摘要给出的直接线索是：A safety study evaluates jailbreak resistance, guardrail routing, and risk classification for open-source models.
- [提升 RAG 检索和知识库问答可靠性](https://arxiv.org/abs/2606.00013) - 检索与 RAG，score 5。关注理由： 重点在于：提升检索增强生成和知识库问答的可靠性。摘要给出的直接线索是：A retrieval architecture routes queries to native database, graph, and vector indexes instead of flattening all sources.
- [增强多模态模型理解图表和文档的能力](https://arxiv.org/abs/2606.00014) - 多模态模型，score 5。关注理由： 重点在于：强化多模态模型对图表、文档和视觉信息的理解。摘要给出的直接线索是：A vision-language benchmark measures chart, table, and document understanding in multimodal models.
- [让 Agent 更可靠地调用工具和复用技能](https://arxiv.org/abs/2606.00015) - Agent 与工具调用，score 5。关注理由： 重点在于：让 Agent 更可靠地调用工具和复用技能。摘要给出的直接线索是：A code intelligence benchmark tests agents that generate executable scripts for procedural 3D modeling.
- [跟进训练与后训练中的高分研究线索](https://arxiv.org/abs/2606.00018) - 训练与后训练，score 5。关注理由： 重点在于：提供一个值得进一步核验的 AI 研究方向。摘要给出的直接线索是：A training analysis uses LoRA adapters to estimate memorization capacity and decide when full fine-tuning is needed.
- [解释模型内部表征和行为归因](https://arxiv.org/abs/2606.00008) - 可解释性，score 4。关注理由： 重点在于：解释模型内部表征和行为归因。摘要给出的直接线索是：An interpretability method localizes representations involved in factual editing and model memory.
- [改进图像生成、视觉理解和可控渲染](https://arxiv.org/abs/2606.00010) - 视频生成，score 4。关注理由： 重点在于：改进图像生成、视觉理解或可控渲染。摘要给出的直接线索是：A video generation evaluation suite probes temporal consistency, motion realism, and causal order.
- [用新基准和评测方法暴露模型短板](https://arxiv.org/abs/2606.00016) - Agent 与工具调用，score 4。关注理由： 重点在于：用新基准或评测方法暴露模型短板。摘要给出的直接线索是：A data engineering workflow removes near duplicates and measures downstream benchmark contamination.
- [提升模型推理、规划和验证能力](https://arxiv.org/abs/2606.00006) - 机器人与具身智能，score 3。关注理由： 重点在于：改进模型推理、规划或验证过程。摘要给出的直接线索是：Embodied robot policies use memory, visual observations, and planning to improve manipulation and navigation.
- [让 Agent 更可靠地调用工具和复用技能](https://arxiv.org/abs/2606.00009) - Agent 与工具调用，score 2。关注理由： 重点在于：让 Agent 更可靠地调用工具和复用技能。摘要给出的直接线索是：A benchmark evaluates speech and audio agents that call tools, transcribe speech, and reason over sound.
- [降低推理成本并提升部署效率](https://arxiv.org/abs/2606.00011) - 系统与部署，score 2。关注理由： 重点在于：降低推理成本并提升部署效率。摘要给出的直接线索是：A deployment system improves throughput for quantized language models using adaptive batching and cache-aware scheduling.

## 今日关键词

agent, agents, alignment, api, attribution, benchmark, cache, chart, code, compression, curation, data, database, deployment

## 来源页链接

完整候选池、评分规则摘要和每篇 score breakdown 见 [来源透明页](/zh/daily/2026-06-07-self-evolving-agents-for-tool-use-skills-sources/)。

## 阅读边界
- 自动评分会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在来源页保留说明。
