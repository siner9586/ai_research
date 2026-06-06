---
title: "让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力"
date: "2026-06-06"
target_date: "2026-06-05"
actual_date: "2026-06-04"
fallback_from: "2026-06-05"
lang: "zh"
slug: "2026-06-06-self-evolving-agents-for-tool-use-skills"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力。"
tags: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "robotics", "safety", "systems", "training", "video-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "robotics", "safety", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-06-06-self-evolving-agents-for-tool-use-skills-sources/"
generated_at: "2026-06-06T00:18:38.152142+00:00"
page_type: "brief"
candidate_count: 18
featured_count: 6
mentions_count: 12
---

# 让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力。建议先看每篇的原文链接、摘要、评测设置和代码/数据是否可用，再决定是否深入复现。

## 重点论文：题目、看点与核验线索

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Self Evolving Agents for Tool Use Skills (Alice Chen, Bob Smith)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00001">2606.00001</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00001">PDF</a></p>

让 Agent 更可靠地调用工具和复用技能。摘要显示：Agents learn reusable tool use skills through iterative self improvement, unit tests, execution feedback, and evaluation. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 2. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Multimodal Safety Evaluation for Vision Language Models (Eva Green)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00004">2606.00004</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00004">PDF</a></p>

增强多模态模型理解图表和文档的能力。摘要显示：A safety evaluation suite measures multimodal models across risky visual prompts, jailbreak attempts, and alignment failures. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Efficient Long Context Inference with Cache Compression (Carol Li)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00002">2606.00002</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00002">PDF</a></p>

提升模型推理、规划和验证能力。摘要显示：A systems method reduces memory and latency during long context model inference while preserving code reasoning accuracy. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>RAG Evaluation under Noisy Retrieval (Dan Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00003">2606.00003</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00003">PDF</a></p>

提升 RAG 检索和知识库问答可靠性。摘要显示：A benchmark studies retrieval augmented generation reliability under noisy evidence, missing citations, and adversarial documents. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Code Model Repair with Execution Feedback (Frank Moore)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00005">2606.00005</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00005">PDF</a></p>

提升代码生成、执行反馈和自动修复能力。摘要显示：Code models improve patch generation through execution feedback loops, repository tests, and API-aware repair. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 6. 改进训练数据筛选、合成和去重流程

<p class="paper-meta-line"><span>Synthetic Data Curation for Post Training (Henry Liu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00007">2606.00007</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00007">PDF</a></p>

改进训练数据筛选、合成和去重流程。摘要显示：A data pipeline selects synthetic instruction data for fine-tuning and post-training with quality filters. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

## 其他值得关注
- [Preference Optimization for Safer Tool Agents](https://arxiv.org/abs/2606.00012)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [Red Teaming Open Source LLM Guardrails](https://arxiv.org/abs/2606.00017)：关注模型安全、护栏路由、风险分类或治理评测，适合跟进安全评测与治理工具链。
- [Database Native Retrieval for Enterprise RAG](https://arxiv.org/abs/2606.00013)：关注检索、知识库问答与证据可靠性，适合跟进 RAG 评测和企业知识系统。
- [Chart Understanding for Vision Language Models](https://arxiv.org/abs/2606.00014)：关注多模态模型中的新任务、数据或系统线索，适合快速判断是否值得阅读全文。
- [Agentic 3D Modeling through Code Execution](https://arxiv.org/abs/2606.00015)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [Low Rank Adapters as Model Memory Probes](https://arxiv.org/abs/2606.00018)：关注训练与后训练中的新任务、数据或系统线索，适合快速判断是否值得阅读全文。
- [Mechanistic Attribution for Factual Editing](https://arxiv.org/abs/2606.00008)：关注可解释性中的新任务、数据或系统线索，适合快速判断是否值得阅读全文。
- [Video Diffusion Models Need Temporal Tests](https://arxiv.org/abs/2606.00010)：关注视频生成中的新任务、数据或系统线索，适合快速判断是否值得阅读全文。
- [Training Data Deduplication for Foundation Models](https://arxiv.org/abs/2606.00016)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [Robotics Policies with Memory Grounded Planning](https://arxiv.org/abs/2606.00006)：关注机器人与具身智能中的新任务、数据或系统线索，适合快速判断是否值得阅读全文。
- [Open Speech Agent Benchmark](https://arxiv.org/abs/2606.00009)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [Serving Quantized Models with Adaptive Batching](https://arxiv.org/abs/2606.00011)：关注推理成本、延迟、吞吐和部署约束，适合跟进系统优化。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
