---
title: "提升 RAG 检索和知识库问答可靠性、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-09-27"
target_date: "2026-09-25"
actual_date: "2026-09-24"
fallback_from: "2026-09-25"
lang: "zh"
slug: "2026-09-27-beyond-average-safety-chance-constrained-llm-fine"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "reasoning", "safety", "systems", "training"]
topics: ["agents", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "reasoning", "safety", "systems", "training"]
sources_page: "/zh/daily/2026-09-27-beyond-average-safety-chance-constrained-llm-fine-sources/"
generated_at: "2026-09-26T23:34:04.055615+00:00"
page_type: "brief"
candidate_count: 497
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Beyond Average Safety: Chance-Constrained LLM Fine-tuning", "ENDOPROMPT: Victim-Side Pseudo-References for Utility Degradation", "PUBG Ally: A Conversational Embodied Agent as an AI Teammate", "Hallucination Neurons and Where to Find Them: An Investigation into the existence of Hallucination Neurons", "TopU-LBVS: A Realistic Multi Target Benchmark for Ligand Based Virtual Screening", "C3M: Cross-Session Multimodal Memory Maintenance for Long-Horizon Tasks"]
featured_paper_urls: ["https://arxiv.org/abs/2609.29960", "https://arxiv.org/abs/2609.29948", "https://arxiv.org/abs/2609.29837", "https://arxiv.org/abs/2609.29781", "https://arxiv.org/abs/2609.29740", "https://arxiv.org/abs/2609.29735"]
featured_paper_titles_zh: ["超越平均安全性：机会受限的LLM微调", "ENDOPROMPT：Victim-Side Pseudo-References 面向 Utility Degradation", "PUBG盟友：作为AI队友的对话式体验代理", "幻觉神经元以及在哪里找到它们：对幻觉神经元存在的调查", "TopU-LBVS：A Realistic Multi Target 基准 面向 Ligand Based Virtual Screening", "C3M ：用于长时间任务的跨会话多模态内存维护"]
---

# 提升 RAG 检索和知识库问答可靠性、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Beyond Average Safety: Chance-Constrained LLM Fine-tuning (Taha Entesari, Mahyar Fazlyab)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.29960">2609.29960</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.29960">PDF</a></p>

中文标题：超越平均安全性：机会受限的LLM微调

信号显示：在新目标上微调大语言模型可以提高有用性、指导跟踪或特定领域的表现，但也可能导致安全关键提示的回归。关键词：rag、serving、safety、fine-tuning。代码/数据可用性需查看原文确认。

### 2. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>ENDOPROMPT: Victim-Side Pseudo-References for Utility Degradation (Qingyu Wu, Zeyu Feng, Yongda Yu, Yuzhe Luo, Hua Cheng)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.29948">2609.29948</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.29948">PDF</a></p>

中文标题：ENDOPROMPT：Victim-Side Pseudo-References 面向 Utility Degradation

信号显示：及时注射可以降低良性任务性能，而不会引发有害内容。关键词：deployment、benchmark、code、search。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>PUBG Ally: A Conversational Embodied Agent as an AI Teammate (Beomsoo Kim, Byeongju Kim, Dohyun Kim, Dongwon Kim, Eunchong Kim, Hongmin Kim, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.29837">2609.29837</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.29837">PDF</a></p>

中文标题：PUBG盟友：作为AI队友的对话式体验代理

信号显示：我们推出了《绝地求生》盟友，这是《绝地求生：战场》的具体代理，可以推理、自主行动，并作为语音支持的队友与玩家一起玩耍。关键词：agent、tool use、latency、compression。代码/数据可用性需查看原文确认。

### 4. 识别并缓解模型安全、越狱和对齐风险

<p class="paper-meta-line"><span>Hallucination Neurons and Where to Find Them: An Investigation into the existence of Hallucination Neurons (Huseyin Cavus, Sebin Sabu, Joshua Spear, Jaskaran Singh Kawatra, Pavithra Rajendran)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.29781">2609.29781</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.29781">PDF</a></p>

中文标题：幻觉神经元以及在哪里找到它们：对幻觉神经元存在的调查

信号显示：大语言模型（ LLM ）的可解释机器学习越来越依赖于稀疏探测方法，该方法识别声称检测并因果影响行为（如事实回忆、安全对齐和幻觉）的小型神经元集合。关键词：alignment、safety、evaluation、open-source。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>TopU-LBVS: A Realistic Multi Target Benchmark for Ligand Based Virtual Screening (Surbhi Kumar, Yuhe Zhou, Varun Shiralkar, Niu Huang, Baris Coskunuzer)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.29740">2609.29740</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.29740">PDF</a></p>

中文标题：TopU-LBVS：A Realistic Multi Target 基准 面向 Ligand Based Virtual Screening

信号显示：基于配体的虚拟筛查（ LBVS ）是早期药物发现中的实用首选工具，但现有基准可能会通过随机阴性、易诱饵、有限的目标覆盖和非标准化评估方案来高估性能。关键词：rag、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 6. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>C3M: Cross-Session Multimodal Memory Maintenance for Long-Horizon Tasks (Xueshu Chen, Yan Wang, Zihao Xue, Jiefu Li, Zhenfang Liu, Jayden Chen, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.29735">2609.29735</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.29735">PDF</a></p>

中文标题：C3M ：用于长时间任务的跨会话多模态内存维护

信号显示：长期任务需要在有限的、查询盲记忆预算下保留并稍后恢复跨会话证据。关键词：serving、compression、code、multimodal。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Dense Coverage, Sparse Refinement: Byte-Constrained Cooperative Perception](https://arxiv.org/abs/2609.29456)
中文标题：密集覆盖，稀疏细化：字节约束协作感知
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [A Systematic Multi-Domain Evaluation of Document Retrievers](https://arxiv.org/abs/2609.29455)
中文标题：文档检索器的系统化多域评估
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Demystifying Agent Skills for Smart Contract Auditing: Design, Effectiveness, Behavioral Impact](https://arxiv.org/abs/2609.29454)
中文标题：Demystifying Agent Skills 面向 Smart Contract Auditing：Design，Effectiveness，Behavioral Impact
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [An auditable conditional-strategy framework for open-ended decision-making in complex lung cancer](https://arxiv.org/abs/2609.29381)
中文标题：复杂肺癌开放式决策的可审计条件-战略框架
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Learning a Flow to Self-Supervised Representations](https://arxiv.org/abs/2609.29350)
中文标题：学习自我监督表示流程
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [SkinAgent AI: A Safety-Grounded Multimodal Agentic Framework for Non-Diagnostic Skincare Support](https://arxiv.org/abs/2609.29341)
中文标题：SkinAgent AI：A Safety-Grounded Multimodal Agentic 框架 面向 Non-Diagnostic Skincare Support
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [AEGIS: Audio Endogenous Guarding via Internal Signals Against Large Audio-Language Model Jailbreaks](https://arxiv.org/abs/2609.29287)
中文标题：AEGIS ：通过内部信号进行音频内生防护，防止大型音频语言模型越狱
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [From Text Decisions to Pixels: An Study of Jev-Style Visual Choice Model](https://arxiv.org/abs/2609.29283)
中文标题：来自 Text Decisions to Pixels：An Study of Jev-Style Visual Choice Model
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [ComplexSync: High-Fidelity and Real-Time Lip Sync in Complex Scenarios](https://arxiv.org/abs/2609.29225)
中文标题：ComplexSync：High-Fidelity 与 Real-Time Lip Sync in Complex Scenarios
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [IndicBankBench: Evaluating Safety and Reliability of Language Model Assistants in Indian Retail Banking](https://arxiv.org/abs/2609.29167)
中文标题：IndicBankBench：Evaluating Safety 与 Reliability of Language Model Assistants in Indian Retail Banking
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Med-AR: Autoregressive Vision-Language Pretraining for Long-Tailed Chest X-Ray Classification and Uncertainty-Aware Evaluation](https://arxiv.org/abs/2609.29156)
中文标题：Med-AR：Autoregressive Vision-Language Pretraining 面向 Long-Tailed Chest X-Ray Classification 与 Uncertainty-Aware 评测
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Scope Before You Persist: Preventing Cross-Family Interference in Agent Memory](https://arxiv.org/abs/2609.29144)
中文标题：坚持之前的范围：防止座席记忆中的跨家族干扰
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [FoCal: Frequency-Oriented Cross-Modal Interaction and Spectral Calibration for Aerial Visible-Infrared Object Detection](https://arxiv.org/abs/2609.29125)
中文标题：FoCal：Frequency-Oriented Cross-Modal Interaction 与 Spectral Calibration 面向 Aerial Visible-Infrared Object Detection
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [TRACE: Interactive Bi-Directional Tracing of Monochrome Cables Amid Clutter](https://arxiv.org/abs/2609.29103)
中文标题：TRACE ：杂乱中单色电缆的交互式双向跟踪
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ELF-REG: Scaling Continuous Diffusion Language Models to Reasoning Tasks](https://arxiv.org/abs/2609.29102)
中文标题：ELF-REG ：将连续扩散语言模型扩展到推理任务
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [RGBD20K: A Large-Scale Benchmark for RGB-D Semantic Segmentation](https://arxiv.org/abs/2609.29028)
中文标题：RGBD20K：A Large-Scale 基准 面向 RGB-D Semantic Segmentation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Polite but Misaligned: Evaluating LLM Politeness Judgments Against Human Pragmatic Norms](https://arxiv.org/abs/2609.29001)
中文标题：礼貌但不一致：根据人类务实规范评估法学硕士的礼貌判断
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Calibrated Decision Models for Autonomous Penetration-Testing Harnesses: JEV and Laya as System One Decision Layers for LLM-Driven Pentest Agents](https://arxiv.org/abs/2609.28940)
中文标题：Calibrated Decision Models 面向 Autonomous Penetration-Testing Harnesses：JEV 与 Laya as System One Decision Layers 面向 LLM-Driven Pentest Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [LLM Agents Can Easily Tamper With Their Own Traces](https://arxiv.org/abs/2609.30266)
中文标题：法学硕士经纪人可以轻松篡改自己的痕迹
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Smartphone-Based Method for Automated Speed Enforcement](https://arxiv.org/abs/2609.30107)
中文标题：基于智能手机的自动速度执行方法
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
