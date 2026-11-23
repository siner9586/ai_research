---
title: "提升模型推理、规划和验证能力、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能"
date: "2026-11-24"
target_date: "2026-11-22"
actual_date: "2026-11-20"
fallback_from: "2026-11-22"
lang: "zh"
slug: "2026-11-24-robopro-a-perturbation-resilient-and-obstacle-aware"
summary: "今天主要跟进：提升模型推理、规划和验证能力、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "robotics", "safety", "training", "video-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "robotics", "safety", "training", "video-generation"]
sources_page: "/zh/daily/2026-11-24-robopro-a-perturbation-resilient-and-obstacle-aware-sources/"
generated_at: "2026-11-23T17:56:52.477870+00:00"
page_type: "brief"
candidate_count: 468
featured_count: 6
mentions_count: 20
featured_paper_titles: ["RoboPRO: A Perturbation-Resilient and Obstacle-Aware Benchmark for Robotic Manipulation", "Decision Models for Multilingual Emotion Classification: A Comparative Study Against LLMs and Encoders", "MetaRigor: From Agentic Automation to Verifiable End-to-End Meta-Analysis Through Scientific Decision Boundaries", "WaXup: Weight Averaging of Experts as Data Augmentation for Robust Introspection", "Towards Text-Mask Consistency in Medical Image Segmentation", "Budgeted Safety Verification for Streaming Video Generation"]
featured_paper_urls: ["https://arxiv.org/abs/2611.26971", "https://arxiv.org/abs/2611.27721", "https://arxiv.org/abs/2611.27713", "https://arxiv.org/abs/2611.27353", "https://arxiv.org/abs/2611.27050", "https://arxiv.org/abs/2611.27268"]
featured_paper_titles_zh: ["RoboPRO：A Perturbation-Resilient 与 Obstacle-Aware 基准 面向 Robotic Manipulation", "Decision Models 面向 Multilingual Emotion Classification：A Comparative Study Against LLMs 与 Encoders", "MetaRigor：来自 Agentic Automation to Verifiable End-to-End Meta-Analysis Through Scientific Decision Boundaries", "WaXup：Weight Averaging of Experts as Data Augmentation 面向 Robust Introspection", "Towards Text-Mask Consistency in Medical Image Segmentation", "Budgeted Safety Verification 面向 Streaming Video Generation"]
---

# 提升模型推理、规划和验证能力、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升模型推理、规划和验证能力、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>RoboPRO: A Perturbation-Resilient and Obstacle-Aware Benchmark for Robotic Manipulation (Zhiyuan Li, Charles Eret, Dingsheng Liu, Xuan Zhao, Joshua Choi, Yangzheng Wu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.26971">2611.26971</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.26971">PDF</a></p>

中文标题：RoboPRO：A Perturbation-Resilient 与 Obstacle-Aware 基准 面向 Robotic Manipulation

信号显示：在现实世界中进行物体操作，要求机器人策略对环境扰动具有鲁棒性，并且能够在杂乱的场景中进行安全规划。关键词：deployment、safety、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 2. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Decision Models for Multilingual Emotion Classification: A Comparative Study Against LLMs and Encoders (Alessandro Piccolo, Francesco De Nicolò, Francesco Manco, Eufemia Lella)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.27721">2611.27721</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.27721">PDF</a></p>

中文标题：Decision Models 面向 Multilingual Emotion Classification：A Comparative Study Against LLMs 与 Encoders

信号显示：决策模型接收一个带有封闭式答案列表的问题，并返回每个答案的概率，而不是自由文本。关键词：rag、latency、code、fine-tuning。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>MetaRigor: From Agentic Automation to Verifiable End-to-End Meta-Analysis Through Scientific Decision Boundaries (Yifeng Xie, Chenke Li, Yangshuo Miao, Jingyuan Zheng, Mingxuan Liu, Feiwei Qin, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.27713">2611.27713</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.27713">PDF</a></p>

中文标题：MetaRigor：来自 Agentic Automation to Verifiable End-to-End Meta-Analysis Through Scientific Decision Boundaries

信号显示：自动化荟萃分析不仅需要准确的数值提取，还需要在各个阶段（包括相关研究、比较、人群、结局、时间点和分析条件）始终如一地保持结果的一致性。关键词：agent、workflow、evaluation、agents。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>WaXup: Weight Averaging of Experts as Data Augmentation for Robust Introspection (Marc Boëlle, Lucas Dixon, Alexandre Ramé)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.27353">2611.27353</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.27353">PDF</a></p>

中文标题：WaXup：Weight Averaging of Experts as Data Augmentation 面向 Robust Introspection

信号显示：随着大语言模型的能力不断提升，传统的机械性可解释性方法难以跟上步伐。关键词：rag、alignment、benchmark、eval。代码/数据可用性需查看原文确认。

### 5. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Towards Text-Mask Consistency in Medical Image Segmentation (Jie Gui, Hang Tu, Wen Sha, Xiuquan Du)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.27050">2611.27050</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.27050">PDF</a></p>

中文标题：Towards Text-Mask Consistency in Medical Image Segmentation

信号显示：用于医学影像分割的视觉-语言模型通常会生成与所附文本相冲突的掩码，在多部位/多病灶描述的情况下尤其如此。关键词：alignment、code、multimodal、vision-language。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Budgeted Safety Verification for Streaming Video Generation (Yuxin Cao, Ziqi Ding, Jiayu Zhang, Xianglin Yang, Wei Song, Jin Song Dong)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.27268">2611.27268</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.27268">PDF</a></p>

中文标题：Budgeted Safety Verification 面向 Streaming Video Generation

信号显示：流式视频生成器会在生成每个片段时立即发布该片段，因此，等待完整片段生成后再做出安全决策，意味着在看到有害内容之后才做出决策。关键词：safety、code、guardrail、harmful。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Reliable Behavior Discovery via False Discovery Rate Control](https://arxiv.org/abs/2611.27104)
中文标题：Reliable Behavior Discovery 通过 False Discovery Rate Control
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Large Reported CHB-MIT Adaptation Gains Disappear with Pretrained Encoders and Matched Probes](https://arxiv.org/abs/2611.26929)
中文标题：Large Reported CHB-MIT Adaptation Gains Disappear with Pretrained Encoders 与 Matched Probes
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Non-penetrating World Models](https://arxiv.org/abs/2611.27963)
中文标题：Non-penetrating 世界模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Who Grades the Agent? Privilege Separation for Coding-Agent Benchmarks](https://arxiv.org/abs/2611.27860)
中文标题：Who Grades the Agent? Privilege Separation 面向 Coding-Agent 基准s
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [On the Limits of Observability for Evaluating Coverage in Machine Unlearning](https://arxiv.org/abs/2611.27543)
中文标题：On the Limits of Observability 面向 Evaluating Coverage in Machine Unlearning
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Learning When to Ask: Advisor-Aware Post-Training for SLM Agents](https://arxiv.org/abs/2611.27443)
中文标题：Learning When to Ask：Advisor-Aware Post-Training 面向 SLM Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SIR-Agent: Skill-Augmented Image Restoration Agent with Recursive Self-Improvement](https://arxiv.org/abs/2611.27285)
中文标题：SIR-Agent：Skill-Augmented Image Restoration Agent 结合 Recursive Self-Improvement
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Trailblazer-F: Speculative Action-Flow Inference for Autonomous Driving](https://arxiv.org/abs/2611.27226)
中文标题：Trailblazer-F：Speculative Action-Flow Inference 面向 Autonomous Driving
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [DepthMSA: Combinatorial Training and Budget-Aware Depth Allocation for Multimodal Sentiment Analysis](https://arxiv.org/abs/2611.27198)
中文标题：DepthMSA：Combinatorial Training 与 Budget-Aware Depth Allocation 面向 Multimodal Sentiment Analysis
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [FM4SAR-Bench 1.0: Towards A Fair Benchmark for Evaluating Foundation Models for SAR Image Interpretation](https://arxiv.org/abs/2611.27158)
中文标题：FM4SAR-Bench 1.0：Towards A Fair 基准 面向 Evaluating Foundation Models 面向 SAR Image Interpretation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Topology Hub Optimal Transport: Eliminating Long Context Dilution at Flash Speed](https://arxiv.org/abs/2611.27951)
中文标题：Topology Hub Optimal Transport：Eliminating Long Context Dilution at Flash Speed
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [OpenAHBU: Open-sourced Automatic Human Behaviour Understanding Toolkit Through Facial Behaviour Analysis](https://arxiv.org/abs/2611.27862)
中文标题：OpenAHBU：Open-sourced Automatic Human Behaviour Understanding Toolkit Through Facial Behaviour Analysis
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ENC-QA: A Diagnostic Benchmark for Vision-Language Models on Electronic Navigational Charts](https://arxiv.org/abs/2611.27858)
中文标题：ENC-QA：A Diagnostic 基准 面向 Vision-Language Models on Electronic Navigational Charts
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Refrain: Learning Multi-Shot Consistency from Inconsistent References for A$^2$O Video Generation](https://arxiv.org/abs/2611.27806)
中文标题：Refrain：Learning Multi-Shot Consistency 来自 Inconsistent References 面向 A$^2$O Video Generation
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [ChildAI-Gov: An Evidence-Linked AI System for Assessing EdTech Policies Against Children's Digital Rights](https://arxiv.org/abs/2611.27799)
中文标题：ChildAI-Gov：An Evidence-Linked AI System 面向 Assessing EdTech Policies Against Children's Digital Rights
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Neural Defend ARCAS 290M: A Robust Foundation Model for AI-Generated Audio Detection](https://arxiv.org/abs/2611.27784)
中文标题：Neural Defend ARCAS 290M：A Robust Foundation Model 面向 AI-Generated Audio Detection
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [SUPERVISE: A Unified Framework for Standardized and Reproducible Superpixel Evaluation](https://arxiv.org/abs/2611.27753)
中文标题：SUPERVISE：A Unified 框架 面向 Standardized 与 Reproducible Superpixel 评测
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [RoSci: Exploring Robustness in Science VLMs](https://arxiv.org/abs/2611.27750)
中文标题：RoSci：Exploring Robustness in Science VLMs
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [AutoOntologyBench: A Task-Grounded Benchmark for Agentic Knowledge Engineering](https://arxiv.org/abs/2611.27734)
中文标题：AutoOntologyBench：A Task-Grounded 基准 面向 Agentic Knowledge Engineering
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CanopyFormer: Attention-Guided SegFormer for Explainable Forest Cover Segmentation](https://arxiv.org/abs/2611.27674)
中文标题：CanopyFormer：Attention-Guided SegFormer 面向 可解释 Forest Cover Segmentation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
