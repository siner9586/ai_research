---
title: "让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力"
date: "2026-09-16"
target_date: "2026-09-14"
actual_date: "2026-09-14"
fallback_from: ""
lang: "zh"
slug: "2026-09-16-safe-meta-reinforcement-learning-via-information-space"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "systems", "training", "video-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-09-16-safe-meta-reinforcement-learning-via-information-space-sources/"
generated_at: "2026-09-15T23:31:50.558746+00:00"
page_type: "brief"
candidate_count: 436
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Safe Meta-Reinforcement Learning via Information Space Reachability", "The Troy Moment of AI: Why SomeWill Cheat and SomeWill Follow?", "SkillLift: Learning Dense Rubrics from Sparse Oracles for Efficient Skill Evolution", "CWM: Controllable White-Box Meta-Prompting for Adaptive Retrieval-Augmented Generation and Reasoning Ability", "Disentangling Representation Evolution in Transformers through Directional Decomposition", "Personalizing Personal Health Interfaces: Co-Design with Generative AI"]
featured_paper_urls: ["https://arxiv.org/abs/2609.15915", "https://arxiv.org/abs/2609.15494", "https://arxiv.org/abs/2609.15396", "https://arxiv.org/abs/2609.15234", "https://arxiv.org/abs/2609.15975", "https://arxiv.org/abs/2609.15046"]
featured_paper_titles_zh: ["通过信息空间可达性实现安全元强化学习", "Troy Moment of AI：Why SomeWill Cheat 与 SomeWill Follow?", "SkillLift：Learning Dense Rubrics 来自 Sparse Oracles 面向 Efficient Skill Evolution", "CWM：Controllable White-Box Meta-Prompting 面向 Adaptive Retrieval-Augmented Generation 与 Reasoning Ability", "通过方向分解解开变压器中的表示演化", "个性化个人健康界面：与生成式人工智能共同设计"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Safe Meta-Reinforcement Learning via Information Space Reachability (Zeyang Li, Sunbochen Tang, Navid Azizan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.15915">2609.15915</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.15915">PDF</a></p>

中文标题：通过信息空间可达性实现安全元强化学习

信号显示：元强化学习（ meta-RL ）使客服代表能够在经验有限的情况下适应看不见的任务。关键词：agent、rag、safety、benchmark。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>The Troy Moment of AI: Why SomeWill Cheat and SomeWill Follow? (Ivy Zhang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.15494">2609.15494</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.15494">PDF</a></p>

中文标题：Troy Moment of AI：Why SomeWill Cheat 与 SomeWill Follow?

信号显示：最近对2026年7月OpenAI--Hugging Face事件的调查引发了两个关于任务失败情况下客服代表行为的问题：当分配的任务变得不可能时，客服代表是否会停止或升级，以及是否可以观察到其他客服代表的行为改变。关键词：agent、serving、benchmark、code。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>SkillLift: Learning Dense Rubrics from Sparse Oracles for Efficient Skill Evolution (Haoxiang Kang, Ming Wen)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.15396">2609.15396</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.15396">PDF</a></p>

中文标题：SkillLift：Learning Dense Rubrics 来自 Sparse Oracles 面向 Efficient Skill Evolution

信号显示：基于LLM的客服代表越来越依赖于持续的技能，即可重复使用的程序提示，以便在没有权重更新的情况下进行调整。关键词：agent、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>CWM: Controllable White-Box Meta-Prompting for Adaptive Retrieval-Augmented Generation and Reasoning Ability (Keuntae Kim, Eunhye Jeong, Yong Suk Choi)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.15234">2609.15234</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.15234">PDF</a></p>

中文标题：CWM：Controllable White-Box Meta-Prompting 面向 Adaptive Retrieval-Augmented Generation 与 Reasoning Ability

信号显示：最近，大语言模型（ LLM ）因其强大的语言理解和产生能力而备受关注，表现出令人印象深刻的推理能力以及有效利用外部知识。关键词：rag、retrieval、benchmark、code。代码/数据可用性需查看原文确认。

### 5. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Disentangling Representation Evolution in Transformers through Directional Decomposition (Shwai He, Haichao Zhang, Shen Yan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.15975">2609.15975</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.15975">PDF</a></p>

中文标题：通过方向分解解开变压器中的表示演化

信号显示：变换器表示通过学习的加性变换进化，这些变换要么保留其当前方向，要么重定向它。关键词：rag、serving、compression、code。代码/数据可用性需查看原文确认。

### 6. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Personalizing Personal Health Interfaces: Co-Design with Generative AI (Karthik S. Bhat, Vidhi Shah, Vedika Agnihotri, Dong Whi Yoo, Koustuv Saha)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.15046">2609.15046</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.15046">PDF</a></p>

中文标题：个性化个人健康界面：与生成式人工智能共同设计

信号显示：个人健康界面通过标准化的仪表板呈现健康数据，这些仪表板很少适合人们如何解释或采取行动。关键词：serving、latency、safety、systems。代码/数据可用性需查看原文确认。

## 其他值得关注
- [OpenAI4S: Code as Action, Science as Sessions](https://arxiv.org/abs/2609.15096)
中文标题：OpenAI4S ：代码即行动，科学即会议
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Route Me If You Can: A Benchmark for Query Reformulation Selection](https://arxiv.org/abs/2609.14885)
中文标题：如果可以，请发送给我：查询重构选择的基准
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Vulnerability Localization Benchmark: Measuring Agentic Security Analysis at Repository Scale](https://arxiv.org/abs/2609.15939)
中文标题：漏洞本地化基准：在存储库规模上衡量代理安全分析
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Look Before You Leap: Factual Decoding with Internal Attribution Signals](https://arxiv.org/abs/2609.15745)
中文标题：跳跃前看：使用内部归因信号进行事实解码
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](https://arxiv.org/abs/2609.15983)
中文标题：Stellar Colosseum：A Many-Agent Harness 面向 Long-Horizon Research in Mathematics 与 Theoretical Computer Science
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Learning Multimodal One-step Flow Policy via Value-weighted Optimal Transport](https://arxiv.org/abs/2609.15883)
中文标题：通过价值加权最优运输学习多式联运一步法流程策略
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Can a Neural Encoding Model Replicate an fMRI Visualization Study?](https://arxiv.org/abs/2609.15685)
中文标题：神经编码模型可以复制fMRI可视化研究吗？
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SAM3D-Part: Interactive Part Selection and Generation from 3D Objects](https://arxiv.org/abs/2609.15639)
中文标题：SAM3D部分： 3D对象的交互式零件选择和生成
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [VideoScout: Learning Agentic Active Exploration with Adaptive Reasoning Pacing for Long Video Understanding](https://arxiv.org/abs/2609.15606)
中文标题：VideoScout ：通过适应性推理节奏学习代理人主动探索，实现长视频理解
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Accelerating the Solving of Many Tiny General Linear Systems on GPUs: Application to Constitutive Laws](https://arxiv.org/abs/2609.15217)
中文标题：加速求解GPU上的许多微小通用线性系统：在构成法中的应用
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Pick Your Poison: Learning to Select Poison Sets for Stronger LLM Backdoor Attacks](https://arxiv.org/abs/2609.15029)
中文标题：选择你的毒药：学习为更强大的LLM后门攻击选择毒药组合
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ActGuard: Pre-execution Action Auditing against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2609.14987)
中文标题：ACTGuard ：针对LLM代理间接提示注入的执行前行动审核
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Online Language Adaptive Sampling for Better Distributed Cross-lingual Gains](https://arxiv.org/abs/2609.14969)
中文标题：在线语言自适应采样，实现更好的分布式跨语言增益
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection](https://arxiv.org/abs/2609.15989)
中文标题：腐败的计划，干净的痕迹：通过计划注入规避思想链监控
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Inoculation Midtraining with Learned Neologisms](https://arxiv.org/abs/2609.15886)
中文标题：学习新词的接种中级培训
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [CiteGuard-RAG: A Validation-Centered AI System for Evidence-Grounded Question Answering](https://arxiv.org/abs/2609.15830)
中文标题：CiteGuard-RAG：A Validation-Centered AI System 面向 Evidence-Grounded Question Answering
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Atria Dawn: The Dawn of Agentic Superintelligence](https://arxiv.org/abs/2609.15818)
中文标题：Atria Dawn：The Dawn of Agentic Superintelligence
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control](https://arxiv.org/abs/2609.15803)
中文标题：将授权委托给未对齐的代理商：煤炭对齐和安全控制
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [KnowBench: Effort Reduction as a Unified, Deployment-Grounded Benchmark for Clinical AI](https://arxiv.org/abs/2609.15794)
中文标题：KnowBench：Effort Reduction as a Unified，Deployment-Grounded 基准 面向 Clinical AI
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [EvoOntology: A Self-Evolving Ontology Layer for Data Agents](https://arxiv.org/abs/2609.15779)
中文标题：EvoOntology：A Self-Evolving Ontology Layer 面向 Data Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
