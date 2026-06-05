---
title: "让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险"
date: "2026-06-01"
target_date: "2026-06-01"
actual_date: "2026-06-01"
fallback_from: ""
lang: "zh"
slug: "2026-06-01-cosmos-3-omnimodal-world-models-for-physical"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险。"
tags: ["agents", "evaluation", "multimodal", "rag", "speech-audio", "systems", "training"]
topics: ["agents", "evaluation", "multimodal", "rag", "speech-audio", "systems", "training"]
sources_page: "/zh/daily/2026-06-01-cosmos-3-omnimodal-world-models-for-physical-sources/"
generated_at: "2026-06-05T16:22:25.748313+00:00"
page_type: "brief"
candidate_count: 273
featured_count: 5
mentions_count: 15
---

# 让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险。建议先看每篇的原文链接、摘要、评测设置和代码/数据是否可用，再决定是否深入复现。

## 重点论文：题目、看点与核验线索

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Cosmos 3: Omnimodal World Models for Physical AI (Aditi, Niket Agarwal, Arslan Ali, Jon Allen, Martin Antolini, Adeline Aubame, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.02800">2606.02800</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.02800">PDF</a></p>

让 Agent 更可靠地调用工具和复用技能。摘要显示：We introduce Cosmos 3, a family of omnimodal world models designed to jointly process and generate language, image, video, audio, and action sequences within a unified mixture-of-transformers architecture. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Thinking Past the Answer: Evaluating Harmful Overthinking in Large Reasoning Models (Simone Caldarella, Davide Talon, Rahaf Aljundi, Elisa Ricci, Massimiliano Mancini)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.02835">2606.02835</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.02835">PDF</a></p>

让 Agent 更可靠地调用工具和复用技能。摘要显示：Large Reasoning Models (LRMs) improve performance by generating explicit intermediate reasoning traces through increased test-time compute, yet the assumption that longer reasoning is consistently beneficial remains under-examined. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 3. 识别并缓解模型安全、越狱和对齐风险

<p class="paper-meta-line"><span>Breaking the Information Silo: Semantic Personas for Cross-Domain Recommendation (Jonathan Mayo, Moshe Unger, Konstantin Bauman)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.01783">2606.01783</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.01783">PDF</a></p>

识别并缓解模型安全、越狱和对齐风险。摘要显示：Digital platforms increasingly operate as isolated information silos, limiting their ability to construct comprehensive user representations across domains. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>KForge: LLM-Driven Cross-Platform Kernel Generation for AI Accelerators (Taras Sereda, Burak Bartan, Ankita Nayak, Tom St. John, Natalie Serrino, Zain Asgar)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.02963">2606.02963</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.02963">PDF</a></p>

让 Agent 更可靠地调用工具和复用技能。摘要显示：Production inference increasingly targets a heterogeneous mix of accelerators. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>EntangleCodec: A Unified Discrete Audio Tokenizer via Semantic-Acoustic Entanglement (Hui Li, Yangfan Gao, Junlin Shang, Changhao Jiang, Tao Gui, Qi Zhang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.02739">2606.02739</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.02739">PDF</a></p>

提升代码生成、执行反馈和自动修复能力。摘要显示：Audio tokenizers serve as the discrete interface between continuous audio and Audio Language Models (ALMs), but existing tokenizers often struggle to support both understanding and generation. 重点核验：任务设置是否真实，是否有代码或数据，评测是否覆盖复杂场景，结论是否能迁移到实际系统。

## 其他值得关注
- [Large AI Models in Dental Healthcare: From General-Purpose Systems to Domain-Specific Foundation Models](https://arxiv.org/abs/2606.02914)：关注任务设置、指标和失效案例，适合补充模型评测与回归测试。
- [GloResNet: A lightweight 3D CNN with global topological features for preterm brain injury prediction](https://arxiv.org/abs/2606.02498)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [MASER: Modality-Adaptive Specialist Routing for Embodied 3D Spatial Intelligence](https://arxiv.org/abs/2606.02463)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [AgentRedBench: Dynamic Redteaming and Integration-Aware Defense for LLM Agents over SaaS Integrations](https://arxiv.org/abs/2606.02240)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [OpenWebRL: Demystifying Online Multi-turn Reinforcement Learning for Visual Web Agents](https://arxiv.org/abs/2606.02031)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [What Benchmarks Don't Measure: The Case for Evaluating Abstention Competence in Autonomous Agents](https://arxiv.org/abs/2606.02965)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [ATLAS: A Large-Scale Evaluation Benchmark for Adversarial LiDAR Perception](https://arxiv.org/abs/2606.02924)：关注检索、知识库问答与证据可靠性，适合跟进 RAG 评测和企业知识系统。
- [Tiny Collaborative Inference for Occlusion-Robust Object Detection](https://arxiv.org/abs/2606.02894)：关注检索、知识库问答与证据可靠性，适合跟进 RAG 评测和企业知识系统。
- [Do Transformers Need Three Projections? Systematic Study of QKV Variants](https://arxiv.org/abs/2606.04032)：关注推理成本、延迟、吞吐和部署约束，适合跟进系统优化。
- [Pathway-Structured Privileged Distillation for Deployable Computational Pathology](https://arxiv.org/abs/2606.02877)：关注检索、知识库问答与证据可靠性，适合跟进 RAG 评测和企业知识系统。
- [RRISE: Robust Radius Inference via a Surrogate Estimator](https://arxiv.org/abs/2606.02876)：关注任务设置、指标和失效案例，适合补充模型评测与回归测试。
- [Toward a Modular Architecture for Embedded AI Agent Systems at the Edge](https://arxiv.org/abs/2606.02862)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [Which Defense Closes Which Threat? Attributing OWASP-LLM-Top-10 Coverage and Its Brittleness Under Paraphrasing](https://arxiv.org/abs/2606.02822)：关注检索、知识库问答与证据可靠性，适合跟进 RAG 评测和企业知识系统。
- [Traj-Evolve: A Self-Evolving Multi-Agent System for Patient Trajectory Modeling in Lung Cancer Early Detection](https://arxiv.org/abs/2606.02812)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。
- [Acceptance-Test-Driven Evaluation Protocols for Business-Centric LLM Systems](https://arxiv.org/abs/2606.02755)：关注工具调用、执行反馈和可复用能力，适合跟进 Agent 工作流和工程可靠性。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
