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

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Self Evolving Agents for Tool Use Skills (Alice Chen, Bob Smith)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00001">2606.00001</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00001">PDF</a></p>

核心：这篇论文主要解决 Agent 在工具调用中如何沉淀、复用并自我改进技能的问题；方法上通过迭代式自我改进、单元测试、执行反馈和能力评测来组织工具使用训练流程，实现更可靠的可复用工具技能；主要论点是标题和摘要显示该工作关注把执行反馈转化为可迁移的工具调用能力，适用边界仍需结合具体任务与系统环境判断。关键词：Agent、tool use、execution feedback、unit tests。代码/数据可用性需查看原文确认。

### 2. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Multimodal Safety Evaluation for Vision Language Models (Eva Green)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00004">2606.00004</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00004">PDF</a></p>

核心：这篇论文主要解决视觉语言模型在复杂视觉任务中如何被系统评估的问题；方法上通过多模态评测套件组织图像、文本和风险提示的交叉测试，实现对模型图表、文档与视觉证据理解能力的压力检验；主要论点是摘要显示该工作把多模态理解能力和风险识别放在同一评测框架中观察，结论是否可迁移到真实产品场景仍需阅读全文确认。关键词：multimodal、evaluation、vision language models、alignment。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Efficient Long Context Inference with Cache Compression (Carol Li)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00002">2606.00002</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00002">PDF</a></p>

核心：这篇论文主要解决长上下文推理中的显存占用、延迟和代码推理稳定性之间的权衡问题；方法上通过缓存压缩和长上下文推理系统优化来减少内存与延迟开销，实现更高效的部署与推理流程；主要论点是摘要显示该方法试图在压缩推理成本的同时保持代码推理准确性，但不同模型规模、上下文长度和硬件条件下的边界需要继续核对。关键词：long context、cache compression、inference、code reasoning。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>RAG Evaluation under Noisy Retrieval (Dan Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00003">2606.00003</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00003">PDF</a></p>

核心：这篇论文主要解决 RAG 系统在噪声证据、缺失引用和干扰文档影响下如何保持问答可靠性的问题；方法上通过围绕噪声检索构造基准和失效案例来观察证据质量变化，实现对检索增强生成流程的鲁棒性评估；主要论点是摘要显示该工作把可靠性问题拆解为证据、引用和文档干扰等可检验环节，适合补充企业知识库问答的回归测试。关键词：RAG、retrieval、noisy evidence、citations。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Code Model Repair with Execution Feedback (Frank Moore)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00005">2606.00005</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00005">PDF</a></p>

核心：这篇论文主要解决代码模型在补丁生成和自动修复中如何利用真实执行反馈的问题；方法上通过执行反馈循环、仓库测试和 API 感知修复线索来约束补丁生成，实现更贴近工程环境的代码修复流程；主要论点是摘要显示执行结果和测试信号可帮助模型改进修复质量，但结论能否覆盖大型仓库、复杂依赖和多语言场景仍需确认。关键词：code repair、execution feedback、repository tests、API-aware repair。代码/数据可用性需查看原文确认。

### 6. 改进训练数据筛选、合成和去重流程

<p class="paper-meta-line"><span>Synthetic Data Curation for Post Training (Henry Liu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00007">2606.00007</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00007">PDF</a></p>

核心：这篇论文主要解决后训练阶段如何从合成指令数据中筛选更高质量样本的问题；方法上通过数据流水线、质量过滤和合成数据整理机制来组织微调与后训练材料，实现更可控的数据策展流程；主要论点是摘要显示数据质量过滤会影响后训练效果，但具体过滤规则、评测任务和泛化边界需要结合全文与实验细节判断。关键词：synthetic data、curation、post-training、quality filters。代码/数据可用性需查看原文确认。

## 其他值得关注
- [2606.00012](https://arxiv.org/abs/2606.00012)：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [2606.00017](https://arxiv.org/abs/2606.00017)：涉及模型风险治理、分类和评测流程，可作为安全评测与治理工具链的补充线索。
- [2606.00013](https://arxiv.org/abs/2606.00013)：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [2606.00014](https://arxiv.org/abs/2606.00014)：涉及多模态模型中的任务、数据或系统线索，可作为后续跟进清单的一部分。
- [2606.00015](https://arxiv.org/abs/2606.00015)：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [2606.00018](https://arxiv.org/abs/2606.00018)：涉及训练与后训练中的表征观察线索，可作为模型记忆和适配器分析的补充材料。
- [2606.00008](https://arxiv.org/abs/2606.00008)：涉及内部表征和事实编辑归因，可补充可解释性与模型编辑方向。
- [2606.00010](https://arxiv.org/abs/2606.00010)：涉及视频生成的时间一致性和运动真实感，可补充生成模型评测方向。
- [2606.00016](https://arxiv.org/abs/2606.00016)：涉及训练数据去重和基础模型数据治理，可补充数据工程方向。
- [2606.00006](https://arxiv.org/abs/2606.00006)：涉及机器人策略、记忆和规划，可补充具身智能任务线索。
- [2606.00009](https://arxiv.org/abs/2606.00009)：涉及语音 Agent 和基准任务，可补充语音/音频评测方向。
- [2606.00011](https://arxiv.org/abs/2606.00011)：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
