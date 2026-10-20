---
title: "提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力"
date: "2026-10-21"
target_date: "2026-10-19"
actual_date: "2026-10-19"
fallback_from: ""
lang: "zh"
slug: "2026-10-21-nads-navigator-guided-data-selection-for-mitigating"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力。"
tags: ["agents", "data-engineering", "evaluation", "rag", "reasoning", "safety", "systems", "training"]
topics: ["agents", "data-engineering", "evaluation", "rag", "reasoning", "safety", "systems", "training"]
sources_page: "/zh/daily/2026-10-21-nads-navigator-guided-data-selection-for-mitigating-sources/"
generated_at: "2026-10-20T23:50:27.423349+00:00"
page_type: "brief"
candidate_count: 570
featured_count: 6
mentions_count: 20
featured_paper_titles: ["NADS: Navigator-Guided Data Selection for Mitigating Catastrophic Forgetting in Fine-Tuning", "StrucChunk: Structure-Aware Retrieval for Legal Document RAG", "GenOlympiad: Benchmarking Frontier Image Models at Their Capability Boundaries", "Agent World Model in the Wild: Computer-Use Agent Environment Synthesis", "SafeWall: A Risk-Aware Job Walltime Recommendation for HPC Scheduling", "Training Natural Schemers: RL Can Amplify Oversight-Conditional Behavior"]
featured_paper_urls: ["https://arxiv.org/abs/2610.25751", "https://arxiv.org/abs/2610.26313", "https://arxiv.org/abs/2610.26850", "https://arxiv.org/abs/2610.26828", "https://arxiv.org/abs/2610.26577", "https://arxiv.org/abs/2610.26551"]
featured_paper_titles_zh: ["NADS：Navigator-Guided Data Selection 面向 Mitigating Catastrophic Forgetting in Fine-Tuning", "StrucChunk：Structure-Aware Retrieval 面向 Legal Document RAG", "GenOlympiad：基准ing Frontier Image Models at Their Capability Boundaries", "Agent World Model in the Wild ：计算机使用Agent环境合成", "SafeWall：A Risk-Aware Job Walltime Recommendation 面向 HPC Scheduling", "培训自然计划者：强化学习可以放大监督-有条件的行为"]
---

# 提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>NADS: Navigator-Guided Data Selection for Mitigating Catastrophic Forgetting in Fine-Tuning (Jianhao Zhang, Ou Wu, Yi Du)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.25751">2610.25751</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.25751">PDF</a></p>

中文标题：NADS：Navigator-Guided Data Selection 面向 Mitigating Catastrophic Forgetting in Fine-Tuning

信号显示：灾难性遗忘是在新任务上对大语言模型（ LLM ）进行单阶段微调的中心障碍，特别是当原始预训练数据不可用时。关键词：alignment、code、synthetic data、fine-tuning。代码/数据可用性需查看原文确认。

### 2. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>StrucChunk: Structure-Aware Retrieval for Legal Document RAG (Surya Deep Singh, Ashutosh Tripathi, Gaurav Deep Singh)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.26313">2610.26313</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.26313">PDF</a></p>

中文标题：StrucChunk：Structure-Aware Retrieval 面向 Legal Document RAG

信号显示：检索增强生成（ RAG ）可以将LLM输出基于特定领域的知识，但法律文档很难：标准分块片段分层参数结构，通用嵌入难以精确引用匹配和语义。关键词：rag、retrieval、alignment、evaluation。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>GenOlympiad: Benchmarking Frontier Image Models at Their Capability Boundaries (Xi Hu, Martin Bell, Liang Zheng)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.26850">2610.26850</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.26850">PDF</a></p>

中文标题：GenOlympiad：基准ing Frontier Image Models at Their Capability Boundaries

信号显示：文本到图像模型取得了巨大的进步，可以生成高质量的图像。关键词：alignment、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Agent World Model in the Wild: Computer-Use Agent Environment Synthesis (Zhaoyang Wang, Qianhui Wu, Haorui Wang, Simon Yu, Baolin Peng, Canwen Xu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.26828">2610.26828</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.26828">PDF</a></p>

中文标题：Agent World Model in the Wild ：计算机使用Agent环境合成

信号显示：代理学习正在从从人类数据中学习转变为通过与世界的互动进行学习。关键词：agent、tool use、benchmark、code。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>SafeWall: A Risk-Aware Job Walltime Recommendation for HPC Scheduling (Kanglin Xu, Michael Papka, Zhiling Lan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.26577">2610.26577</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.26577">PDF</a></p>

中文标题：SafeWall：A Risk-Aware Job Walltime Recommendation 面向 HPC Scheduling

信号显示：在高性能计算（ HPC ）中，用户必须提交其工作的资源要求，用户提供的壁挂时间是一个关键参数。关键词：serving、safety、code、risk。代码/数据可用性需查看原文确认。

### 6. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Training Natural Schemers: RL Can Amplify Oversight-Conditional Behavior (Bart Jaworski, Nathaniel Mitrani, Fred Bruford, Victoria Krakovna)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.26551">2610.26551</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.26551">PDF</a></p>

中文标题：培训自然计划者：强化学习可以放大监督-有条件的行为

信号显示：高级人工智能的安全性的核心问题之一是阴谋：当模型在监督下战略性地遵守，但在未被观察到的情况下追求自己的目标时。关键词：deployment、alignment、safety、reasoning。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Game of Phones: Harnessing Game Theory and LLMs in 'Bot Wars' to Counteract Phone Scams](https://arxiv.org/abs/2610.26781)
中文标题：手机游戏：在“机器人大战”中利用游戏理论和LLM来对抗手机诈骗
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SAR2Net: Learning Spatially Anchored Representations for Retrieval-Guided Cross-Stain Alignment](https://arxiv.org/abs/2610.26217)
中文标题：SAR2Net：Learning Spatially Anchored Representations 面向 Retrieval-Guided Cross-Stain Alignment
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [MoveBench: A Rubric-Based Benchmark for Evaluating Large Language Models in Sports and Health Coaching](https://arxiv.org/abs/2610.26185)
中文标题：MoveBench：A Rubric-Based 基准 面向 Evaluating Large Language Models in Sports 与 Health Coaching
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Toolkit for Facial Deidentification](https://arxiv.org/abs/2610.26079)
中文标题：面部去识别工具包
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Auditor-Assisted Summary-Channel Verification for Hosted LLM Identity Substitution](https://arxiv.org/abs/2610.25982)
中文标题：托管LLM身份替换的审核员辅助总结-渠道验证
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [SWE-Residual: Evaluating Starting-State Robustness of Coding Agents](https://arxiv.org/abs/2610.25899)
中文标题：SWE-剩余：评估编码代理的起始状态稳健性
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [UniJev: Separating Accuracy from Calibration in Trimodal System One Decision Models](https://arxiv.org/abs/2610.25784)
中文标题：UniJev：Separating Accuracy 来自 Calibration in Trimodal System One Decision Models
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Cognitively Decoupled Meta-Induction for Out-of-Distribution Generalization](https://arxiv.org/abs/2610.25749)
中文标题：用于分布外泛化的认知解耦元归纳
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [MapSteal: Map-based Autonomous Knowledge Stealing Attack Against Large Language Models](https://arxiv.org/abs/2610.25626)
中文标题：MapSteal ：针对大型语言模型的基于地图的自主知识窃取攻击
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ASTOR: Benchmarking and Improving Autoformulation for Soft-Constraint Optimization with a Formal Grammar](https://arxiv.org/abs/2610.26819)
中文标题：ASTOR ：使用正式语法对软约束优化进行基准测试和改进自动配方
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [PICA-WAM: Visual Perturbation Invariance via Cross-Appearance Self-Alignment in World Action Models](https://arxiv.org/abs/2610.26813)
中文标题：PICA-WAM ：世界动作模型中通过交叉外观自对齐的视觉摄动不变性
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [EpiLens: Lightweight RAG for Epidemiological Knowledge Acquisition](https://arxiv.org/abs/2610.26730)
中文标题：EpiLens：Lightweight RAG 面向 Epidemiological Knowledge Acquisition
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [YUTELA: A Scalable Edge Cloud AIoT System for Multi-Site Video Anomaly Detection with Scene Specific Adaptation](https://arxiv.org/abs/2610.26468)
中文标题：YUTELA ：一种可扩展的边缘云AIoT系统，用于场景特定适应的多站点视频异常检测
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [CARNet: End-to-End Coupled Association-Recognition Network for Fine-Grained Multi-Drone Collaborative Detection](https://arxiv.org/abs/2610.26312)
中文标题：CARNet：End-to-End Coupled Association-Recognition Network 面向 Fine-Grained Multi-Drone Collaborative Detection
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Decision4Rec: A Jev-Inspired Framework of Decision Models on Knowledge and Active Graphs for Multi-Agent Recommender Systems](https://arxiv.org/abs/2610.26035)
中文标题：Decision4Rec：A Jev-Inspired 框架 of Decision Models on Knowledge 与 Active Graphs 面向 Multi-Agent Recommender Systems
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Keep the Lineages Alive: Diversity-Preserving SMC for Diffusion LLM Decoding](https://arxiv.org/abs/2610.25932)
中文标题：保持谱系活力：为Diffusion LLM解码保留多样性的SMC
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Minimum-Cost Robust Evidence Certificates for Horn Reasoning under Correlated Source Failures](https://arxiv.org/abs/2610.25865)
中文标题：相关源故障下喇叭推理的最低成本可靠证据证书
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Are Self-Evolving Agents Continual Learners?](https://arxiv.org/abs/2610.25858)
中文标题：自我进化的代理是不是持续的学习者？
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [OneChord: Distill What You Rank, Recommend in One Pass](https://arxiv.org/abs/2610.25805)
中文标题：OneChord ：提炼您的排名，一次推荐
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [How Much Does One Wrong Answer Cost? Error Propagation in Constraint Pruning with Noisy LLM Oracles](https://arxiv.org/abs/2610.25739)
中文标题：一个错误答案的费用是多少？使用噪声LLM预言机进行约束修剪时的错误传播
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
