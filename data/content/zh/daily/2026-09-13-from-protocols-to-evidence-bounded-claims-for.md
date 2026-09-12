---
title: "提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能"
date: "2026-09-13"
target_date: "2026-09-11"
actual_date: "2026-09-10"
fallback_from: "2026-09-11"
lang: "zh"
slug: "2026-09-13-from-protocols-to-evidence-bounded-claims-for"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "speech-audio", "systems", "training", "video-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "speech-audio", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-09-13-from-protocols-to-evidence-bounded-claims-for-sources/"
generated_at: "2026-09-12T23:17:17.021146+00:00"
page_type: "brief"
candidate_count: 100
featured_count: 6
mentions_count: 20
featured_paper_titles: ["From Protocols to Evidence: Bounded Claims for AI in Service of the Common Good", "SIRF: A Spec-Internalized Risk Foundation Model for Industrial Content Risk Control", "Building py-kvcache: A Performance Characterization of External KV Caching for vLLM with NVMe SSDs", "Autonomy, Social Norms, and Alignment: Towards a Developmental Framework for Autonomous Artificial Agents", "SpecGuard: Inference-Time Backdoor Detection For Free", "Dynamic language model representations for multi-objective reaction optimisation"]
featured_paper_urls: ["https://arxiv.org/abs/2609.11910", "https://arxiv.org/abs/2609.11752", "https://arxiv.org/abs/2609.11744", "https://arxiv.org/abs/2609.11660", "https://arxiv.org/abs/2609.11799", "https://arxiv.org/abs/2609.11790"]
featured_paper_titles_zh: ["从协议到证据：为公共利益服务的人工智能的有限主张", "SIRF：A Spec-Internalized Risk Foundation Model 面向 Industrial Content Risk Control", "构建py-kvcache ： NVMe SSD用于vLLM的外部KV缓存的性能表征", "自主性、社会规范和一致性：走向自主人工智能的发展框架", "SpecGuard：Inference-Time Backdoor Detection 面向 Free", "多目标反应优化的动态语言模型表示"]
---

# 提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>From Protocols to Evidence: Bounded Claims for AI in Service of the Common Good (Nitesh V. Chawla, Paulo Benanti)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.11910">2609.11910</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.11910">PDF</a></p>

中文标题：从协议到证据：为公共利益服务的人工智能的有限主张

信号显示：人工智能不仅会造成治理问题。关键词：deployment、safety、evaluation、eval。代码/数据可用性需查看原文确认。

### 2. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>SIRF: A Spec-Internalized Risk Foundation Model for Industrial Content Risk Control (Suwan Wu, Yumeng Lin, Pengcheng Yuan, Xiaolong Jiang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.11752">2609.11752</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.11752">PDF</a></p>

中文标题：SIRF：A Spec-Internalized Risk Foundation Model 面向 Industrial Content Risk Control

信号显示：对于工业内容风险控制，真正的部署约束不是平均精度，而是在高精度和二级延迟下可以自动处理多少风险。关键词：rag、deployment、latency、training。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Building py-kvcache: A Performance Characterization of External KV Caching for vLLM with NVMe SSDs (Joseph Kanichai, Tiziano De Matteis, Animesh Trivedi)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.11744">2609.11744</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.11744">PDF</a></p>

中文标题：构建py-kvcache ： NVMe SSD用于vLLM的外部KV缓存的性能表征

信号显示：前缀缓存可以通过重用先前计算的键值（ KV ）状态来减少长上下文LLM请求的第一个令牌（ TTFT ）时间，但对于短前缀或快速GPU ，重新计算可以比从外部缓存加载更快。关键词：rag、benchmark、memory、search。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Autonomy, Social Norms, and Alignment: Towards a Developmental Framework for Autonomous Artificial Agents (Marica Notte, Ludovica Marinucci, Vieri Giuliano Santucci)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.11660">2609.11660</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.11660">PDF</a></p>

中文标题：自主性、社会规范和一致性：走向自主人工智能的发展框架

信号显示：近年来，由于能够泛化的大规模模型和复杂输出的生成，人工智能取得了非凡的进步。关键词：agent、rag、alignment、agents。代码/数据可用性需查看原文确认。

### 5. 降低推理成本并提升部署效率

<p class="paper-meta-line"><span>SpecGuard: Inference-Time Backdoor Detection For Free (Rui Wen, Ahmed Salem, Andrew Paverd, Mark Russinovich, Zheng Li)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.11799">2609.11799</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.11799">PDF</a></p>

中文标题：SpecGuard：Inference-Time Backdoor Detection 面向 Free

信号显示：大语言模型通常是从第三方微调、共享或下载的，因此部署的模型可能携带一个隐藏的后门，该后门通常在良性输入上运行，但在出现秘密触发器时切换到攻击者控制的行为。关键词：inference、serving、deployment、latency。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Dynamic language model representations for multi-objective reaction optimisation (Joshua W. Sin, David Ming Segura, Bojana Ranković, Siu Lun Chau, Marius D. R. Lutz, Andrea Anelli, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.11790">2609.11790</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.11790">PDF</a></p>

中文标题：多目标反应优化的动态语言模型表示

信号显示：优化收率、选择性和安全性等多个目标的化学反应是化学合成的核心，而模型驱动的方法在很大程度上取决于反应组分的表示方式。关键词：safety、code、coding、Code Intelligence。代码/数据可用性需查看原文确认。

## 其他值得关注
- [SenseNova-U1.5: Towards Native Unified Visual Intelligence](https://arxiv.org/abs/2609.11929)
中文标题：SenseNova-U1.5 ：迈向本地统一视觉智能
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Artificial Id: Drive and Persistent Alignment in Agentic AI](https://arxiv.org/abs/2609.11911)
中文标题：Artificial Id：Drive 与 Persistent Alignment in Agentic AI
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [MindTopo: Can Foundation Models Reason in Topological Space?](https://arxiv.org/abs/2609.11900)
中文标题：MindTopo ：基础模型可以在拓扑空间中进行推理吗？
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [AdamX: Cosine similarity meets gradient descent](https://arxiv.org/abs/2609.11867)
中文标题：AdamX ：余弦相似性与梯度下降
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [RetroThinker: Enabling Retrospective Thinking in Speech LLMs](https://arxiv.org/abs/2609.11864)
中文标题：RetroThinker ：在言语法学硕士中实现回顾性思维
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Explainability Assistant: A Conversational XAI Interface for Interpreting Energy Consumption Models](https://arxiv.org/abs/2609.11860)
中文标题：Explainability Assistant：A Conversational XAI Interface 面向 Interpreting Energy Consumption Models
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Model-Aware Schedules Improve Generation via Fiberwise Optimal Transport](https://arxiv.org/abs/2609.11842)
中文标题：模型感知调度通过光纤优化传输改进生成
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [MotionQ: Operator-Conditioned Motion Quotients for Cross-Observation WiFi Gesture Recognition](https://arxiv.org/abs/2609.11818)
中文标题：MotionQ：Operator-Conditioned Motion Quotients 面向 Cross-Observation WiFi Gesture Recognition
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Generative Late-Interaction Embeddings For Visual Document Retrieval](https://arxiv.org/abs/2609.11808)
中文标题：用于可视化文档检索的生成式后期交互嵌入
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Predicting Privacy Leakage from Weight Spectral Density](https://arxiv.org/abs/2609.11780)
中文标题：根据权重谱密度预测隐私泄露
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Component-Aware Differential Privacy for Federated Multilingual Speech-LLMs](https://arxiv.org/abs/2609.11762)
中文标题：联合多语言语音LLM的组件感知差分隐私
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Continuous-Time Acoustic Modelling with Neural Controlled Differential Equations](https://arxiv.org/abs/2609.11725)
中文标题：神经控制微分方程连续时间声学建模
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [The Eloquence submission for Task 2 of the Interspeech 2026 MLC-SLM challenge](https://arxiv.org/abs/2609.11724)
中文标题：Interspeech 2026 MLC-SLM挑战任务2的口才提交
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Negative Self-Distillation: Learning to Reason by Avoiding Flaws](https://arxiv.org/abs/2609.11699)
中文标题：消极的自我蒸馏：通过避免缺陷来学习推理
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization](https://arxiv.org/abs/2609.11682)
中文标题：COBRA-Skills：Contextual Bandit-Guided Evolution 面向 Agent Skill Optimization
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Your Retriever Already Knows: Distribution-Shape QPP for RAG Retrieval Sufficiency](https://arxiv.org/abs/2609.11646)
中文标题：Your Retriever Already Knows：Distribution-Shape QPP 面向 RAG Retrieval Sufficiency
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [MAPLE: Memory-Augmented Planning with Language and Evolution](https://arxiv.org/abs/2609.11636)
中文标题：MAPLE ：使用语言和进化进行记忆增强计划
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Can Edge-Deployable Vision-Language Models Identify Species?](https://arxiv.org/abs/2609.11916)
中文标题：边缘可部署视觉语言模型可以识别物种吗？
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [TART: A Modular Tool for Technique-Aware Audio-to-Tablature Guitar Transcription](https://arxiv.org/abs/2609.11904)
中文标题：TART：A Modular Tool 面向 Technique-Aware Audio-to-Tablature Guitar Transcription
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Caption-once, Frames-on-Demand: Visual-Need Routing for Budget-Aware Agentic Long Video Understanding](https://arxiv.org/abs/2609.11899)
中文标题：一次性字幕，按需帧：视觉需求路由，以实现预算感知代理长视频理解
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
