---
title: "提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性"
date: "2026-08-22"
target_date: "2026-08-20"
actual_date: "2026-08-20"
fallback_from: ""
lang: "zh"
slug: "2026-08-22-learning-how-to-forget-fine-tuning-for"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "safety", "systems", "training", "video-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "safety", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-08-22-learning-how-to-forget-fine-tuning-for-sources/"
generated_at: "2026-08-21T21:35:55.600735+00:00"
page_type: "brief"
candidate_count: 291
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Learning how to Forget: Fine-tuning for Long-Context Sparse Attention", "Projecting BrowseComp-Plus onto ClimbMix: Toward More Realistic Corpora for Agentic Search", "Natural Language Code Retrieval for 1C:Enterprise: An Open Benchmark and Efficient Bi-Encoder", "One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows", "MOSAIC: Modality-agnostic Spectral Alignment for Federated Image-level Weakly Supervised Tumor Segmentation under Client-specific Missing Modalities", "Electronic Navigational Chart Change Classification"]
featured_paper_urls: ["https://arxiv.org/abs/2608.19920", "https://arxiv.org/abs/2608.20317", "https://arxiv.org/abs/2608.19957", "https://arxiv.org/abs/2608.19741", "https://arxiv.org/abs/2608.19788", "https://arxiv.org/abs/2608.20218"]
featured_paper_titles_zh: ["学习如何忘记：长上下文稀疏注意力的微调", "Projecting BrowseComp-Plus onto ClimbMix：面向 More Realistic Corpora 面向 Agentic Search", "1C的自然语言代码检索：企业：开放的基准和高效的双编码器", "One Success Isn't Reliability：Thinkingbox，a Sandbox 与 基准 面向 Agents in Stateful Business Workflows", "MOSAIC：Modality-agnostic Spectral Alignment 面向 Federated Image-level Weakly Supervised Tumor Segmentation under Client-specific Missing Modalities", "电子导航图变更分类"]
---

# 提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Learning how to Forget: Fine-tuning for Long-Context Sparse Attention (Matthias Seeger, Zeyu Zhang, Vihang Patil, Konstantinos Benidis, Sebastian Schelter)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.19920">2608.19920</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.19920">PDF</a></p>

中文标题：学习如何忘记：长上下文稀疏注意力的微调

信号显示：以前的许多工作都是通过稀疏的关注来解决键值（ KV ）缓存选择和压缩问题，以便在没有过多硬件预算的情况下为变压器语言模型实现长上下文推理。关键词：inference、compression、code、fine-tuning。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Projecting BrowseComp-Plus onto ClimbMix: Toward More Realistic Corpora for Agentic Search (Sahel Sharifymoghaddam, Lingwei Gu, Yijun Ge, Jimmy Lin)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.20317">2608.20317</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.20317">PDF</a></p>

中文标题：Projecting BrowseComp-Plus onto ClimbMix：面向 More Realistic Corpora 面向 Agentic Search

信号显示：BrowseComp-Plus基准测试通过用固定语料库替换不透明的Web搜索来解开代理搜索的评估，以便可以将代理的角色与检索器的角色分开。关键词：agent、retrieval、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Natural Language Code Retrieval for 1C:Enterprise: An Open Benchmark and Efficient Bi-Encoder (Konstantin Chesnokov, Chingiz Mingazov)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.19957">2608.19957</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.19957">PDF</a></p>

中文标题：1C的自然语言代码检索：企业：开放的基准和高效的双编码器

信号显示：自然语言代码检索是计算机科学中一项快速发展的任务。关键词：rag、retrieval、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>One Success Isn&#x27;t Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows (Zhuochun Li, Youngmin Ko, Ali Keramati, Nicola Ferri, Susana Palmaz Lopez Pelaez, Liang-Chun Tsai, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.19741">2608.19741</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.19741">PDF</a></p>

中文标题：One Success Isn't Reliability：Thinkingbox，a Sandbox 与 基准 面向 Agents in Stateful Business Workflows

信号显示：最近的代理基准测试越来越多地在可执行环境中进行评估，从代码修复到Web导航、应用程序API和函数调用。关键词：agent、workflow、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 5. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>MOSAIC: Modality-agnostic Spectral Alignment for Federated Image-level Weakly Supervised Tumor Segmentation under Client-specific Missing Modalities (Tarun Kumar Garg, Vaanathi Sundaresan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.19788">2608.19788</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.19788">PDF</a></p>

中文标题：MOSAIC：Modality-agnostic Spectral Alignment 面向 Federated Image-level Weakly Supervised Tumor Segmentation under Client-specific Missing Modalities

信号显示：临床环境中值得信赖的多模式融合需要处理跨机构的不完整和异构模式子集，其中隐私限制禁止集中式数据共享。关键词：alignment、benchmark、code、multimodal。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Electronic Navigational Chart Change Classification (Jacob Arndt, Abhishek Potnis, Alexandre Sorokine)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.20218">2608.20218</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.20218">PDF</a></p>

中文标题：电子导航图变更分类

信号显示：电子导航图（ ENC ）是海上导航系统中使用的地理空间矢量数据集，表示水文和导航信息，如深度、导航辅助、交通方案和危险。关键词：workflow、rag、safety、code。代码/数据可用性需查看原文确认。

## 其他值得关注
- [G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs](https://arxiv.org/abs/2608.19964)
中文标题：G-MARK ：通过知识图谱进行合作驾驶的基础多Agent推理
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [From Noise to Signal: Improving Security Log Anomaly Detection Using LLMs with Endpoint-Specific Logs](https://arxiv.org/abs/2608.19938)
中文标题：从噪音到信号：使用具有端点特定日志的LLM改进安全日志异常检测
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Repo0: Design-Driven Zero-to-All Code Generation](https://arxiv.org/abs/2608.19854)
中文标题：Repo0 ：设计驱动的零到全部代码生成
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving](https://arxiv.org/abs/2608.19758)
中文标题：FlashPrefill V2：Block-Sparse Prefill Attention 面向 Long-Context LLM Serving
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [From Retrieved Context to Runtime Control: Adaptive Compression for Edge-based RAG](https://arxiv.org/abs/2608.19535)
中文标题：从检索的上下文到运行时控制：基于边缘的RAG的自适应压缩
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving](https://arxiv.org/abs/2608.20129)
中文标题：LLM自动驾驶常识推理能力的多Agent编排
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [OenoBench: A Wine-Domain Benchmark for Knowledge-Grounded Evaluation of Large Language Models](https://arxiv.org/abs/2608.20106)
中文标题：OenoBench：A Wine-Domain 基准 面向 Knowledge-Grounded 评测 of Large Language Models
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [On the Applicability of Safety Nets: A Safety-By-Design Solution for Certifying Neural Networks](https://arxiv.org/abs/2608.20053)
中文标题：论安全网的适用性：神经网络认证的安全设计解决方案
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [From Street View Imagery to Street Quality Indicators: Vision Language Inference for the Suburban 15-minute City](https://arxiv.org/abs/2608.20026)
中文标题：从街景图像到街道质量指标：郊区15分钟城市的视觉语言推断
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Stopping and Routing LLM Judge Panels](https://arxiv.org/abs/2608.19802)
中文标题：停止和路由LLM法官小组
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Truncate Bad, Upweight Good: BoN-Style Distillation via Rank-Based Classification](https://arxiv.org/abs/2608.19748)
中文标题：截断不良，增重货物：通过基于等级的分类进行BoN型蒸馏
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Escaping the Quicksand: A Call to Arms](https://arxiv.org/abs/2608.19674)
中文标题：逃离流沙：武器召唤
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [FleetSieve: Decision-Critical Profiling for SLO-Aware LLM Fleet Configuration](https://arxiv.org/abs/2608.19659)
中文标题：FleetSieve：Decision-Critical Profiling 面向 SLO-Aware LLM Fleet Configuration
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [ConceptGuard: Benchmarking Context-Sensitive Unlearning in Large Language Models](https://arxiv.org/abs/2608.20338)
中文标题：ConceptGuard：基准ing Context-Sensitive Unlearning in Large Language Models
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement](https://arxiv.org/abs/2608.20318)
中文标题：AI4AI-Bench：基准ing LLM Agents in Algorithmic Design 面向 Recursive Self-Improvement
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization](https://arxiv.org/abs/2608.20281)
中文标题：注入、对齐、恢复：无检索文档知识内化的分阶段后期培训
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Rule-Compliant Visual Spatial Planning for Multimodal Large Language Models](https://arxiv.org/abs/2608.20237)
中文标题：多模态大型语言模型的规则兼容视觉空间规划
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [RoMAN-Flow: Taming Autoregressive Normalizing Flows for Offline Reinforcement Learning in Robotic Manipulation](https://arxiv.org/abs/2608.20208)
中文标题：RoMAN-Flow：Taming Autoregressive Normalizing Flows 面向 Offline Reinforcement Learning in Robotic Manipulation
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [The Third Restructuring of Software Form: From the Three-Tier Architecture to Storage, Models, and Agents](https://arxiv.org/abs/2608.20201)
中文标题：第三次软件形态重构：从三层架构到存储、模型、代理
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ID-VTG: Image-Disambiguated Video Temporal Grounding](https://arxiv.org/abs/2608.20127)
中文标题：ID-VTG：Image-Disambiguated Video Temporal 落地
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
