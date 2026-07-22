---
title: "让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力"
date: "2026-07-23"
target_date: "2026-07-21"
actual_date: "2026-07-21"
fallback_from: ""
lang: "zh"
slug: "2026-07-23-coderescue-budget-calibrated-recovery-routing-for-coding"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "reasoning", "safety", "training", "vision-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "reasoning", "safety", "training", "vision-generation"]
sources_page: "/zh/daily/2026-07-23-coderescue-budget-calibrated-recovery-routing-for-coding-sources/"
generated_at: "2026-07-22T22:15:17.787706+00:00"
page_type: "brief"
candidate_count: 305
featured_count: 6
mentions_count: 20
featured_paper_titles: ["CodeRescue: Budget-Calibrated Recovery Routing for Coding Agents", "Point Ladder Tuning: Parameter-Efficient Hierarchical Adaptation for 3D Point Cloud Understanding", "Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents", "CASE: Causal Alignment and Structural Enforcement for Improving Chain-of-Thought Faithfulness", "Wave2Body: Rethinking mmWave Human Pose Estimation as Radar-to-Body Token Translation", "The safety failures we are not instrumenting: a perspective on hidden safety-critical challenges in modern AI systems"]
featured_paper_urls: ["https://arxiv.org/abs/2607.19338", "https://arxiv.org/abs/2607.19171", "https://arxiv.org/abs/2607.18826", "https://arxiv.org/abs/2607.18820", "https://arxiv.org/abs/2607.18875", "https://arxiv.org/abs/2607.19292"]
featured_paper_titles_zh: ["CodeRescue：Budget-Calibrated Recovery Routing 面向 Coding Agents", "点阶梯调整：用于三维点云理解的高参数分层自适应", "跨代理活动归因：跨LLM代理链接异步攻击", "案例：提高思想链忠诚度的因果对齐和结构执行", "Wave2Body ：将毫米波人体姿态估计重新思考为雷达到人体令牌转换", "我们没有计量的安全故障：对现代人工智能系统中隐藏的安全关键挑战的看法"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>CodeRescue: Budget-Calibrated Recovery Routing for Coding Agents (Qijia He, Jiayi Cheng, Chenqian Le, Rui Wang, Xunmei Liu, Yixian Chen, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.19338">2607.19338</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.19338">PDF</a></p>

中文标题：CodeRescue：Budget-Calibrated Recovery Routing 面向 Coding Agents

信号显示：编码代理越来越多地在可执行环境中运行，在这种环境中，失败的尝试会产生可操作的反馈，而不仅仅是错误的答案。关键词：agent、deployment、benchmark、code。代码/数据可用性需查看原文确认。

### 2. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Point Ladder Tuning: Parameter-Efficient Hierarchical Adaptation for 3D Point Cloud Understanding (Junlin Chang, Longhao Zou, Rui Li)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.19171">2607.19171</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.19171">PDF</a></p>

中文标题：点阶梯调整：用于三维点云理解的高参数分层自适应

信号显示：微调预训练的点云骨干通常会更新所有参数，从而导致大量计算和内存开销。关键词：rag、code、fine-tuning、memory。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents (SangJin Park, Myungsub Choi, Jineok Kim, Minseung Kang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.18826">2607.18826</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.18826">PDF</a></p>

中文标题：跨代理活动归因：跨LLM代理链接异步攻击

信号显示：LLM代理防御通常每次评估一个会话。关键词：agent、rag、deployment、evaluation。代码/数据可用性需查看原文确认。

### 4. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>CASE: Causal Alignment and Structural Enforcement for Improving Chain-of-Thought Faithfulness (Ziming Wang, Yinghua Yao, Changwu Huang, Ke Tang, Xin Yao)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.18820">2607.18820</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.18820">PDF</a></p>

中文标题：案例：提高思想链忠诚度的因果对齐和结构执行

信号显示：思维链（ CoT ）推理被广泛用于提高大语言模型（ LLM ）的性能和可解释性，但生成的推理可能无法忠实地支持最终答案。关键词：rag、inference、alignment、benchmark。代码/数据可用性需查看原文确认。

### 5. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Wave2Body: Rethinking mmWave Human Pose Estimation as Radar-to-Body Token Translation (Bo Liang, Chen Gong, Wei Gao, Chenren Xu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.18875">2607.18875</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.18875">PDF</a></p>

中文标题：Wave2Body ：将毫米波人体姿态估计重新思考为雷达到人体令牌转换

信号显示：毫米波（ mmWave ）雷达可实现隐私友好的人体感应，但其稀疏的点云是对视图相关电磁反射的物理测量，仅间接表征人体关节。关键词：rag、inference、alignment、code。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>The safety failures we are not instrumenting: a perspective on hidden safety-critical challenges in modern AI systems (Gjergji Kasneci, Enkelejda Kasneci)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.19292">2607.19292</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.19292">PDF</a></p>

中文标题：我们没有计量的安全故障：对现代人工智能系统中隐藏的安全关键挑战的看法

信号显示：当前的人工智能安全话语仍然不成比例地关注可见的故障，包括明显的危害、戏剧性的滥用和假设的灾难性场景。关键词：workflow、retrieval、deployment、safety。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Cognitive Dual-Process Planning for Autonomous Driving with Structured Scene Knowledge and Verifiable Reasoning-Action Consistency](https://arxiv.org/abs/2607.19194)
中文标题：具有结构化场景知识和可验证推理-行动一致性的自动驾驶认知双流程规划
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Delineate Anything v2: A Global Foundation Model for Field Delineation](https://arxiv.org/abs/2607.19069)
中文标题：描绘任何内容v2 ：现场描绘的全球基础模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Beyond Noisy Signals: Dual-Level Denoising for Multi-modal Sequential Recommendation](https://arxiv.org/abs/2607.18786)
中文标题：超越噪声信号：针对多模态顺序推荐的双级去噪
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [No Training, Better Flights: Test-Time Scaled VLMs for UAV Navigation](https://arxiv.org/abs/2607.19288)
中文标题：无需培训，更好的飞行：用于无人机导航的测试时间缩放VLM
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Inference-Time Steering for Cross-Lingual Factual Consistency in LLMs](https://arxiv.org/abs/2607.19243)
中文标题：LLM中跨语言事实一致性的推理时间指导
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://arxiv.org/abs/2607.19191)
中文标题：ABot-World-0 ：在单个桌面GPU上推出无限互动世界
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://arxiv.org/abs/2607.19064)
中文标题：Mage-Flow：An Efficient Native-Resolution Foundation Model 面向 Image Generation 与 Editing
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [CoGoal3D: Collaborative 3D Object Detection with 3D-Aware Fusion and Refinement](https://arxiv.org/abs/2607.19036)
中文标题：CoGoal3D ：具有3D感知融合和细化的协作3D对象检测
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Measuring Reward-Seeking via Contrastive Belief Updates](https://arxiv.org/abs/2607.18966)
中文标题：通过对比信念更新来衡量奖励寻求
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [From a Multilingual Streaming ASR Backbone to Kenyan-Language Systems: Data-Centric Adaptation of Nemotron 3.5 for Kikuyu, Dholuo, and Kalenjin](https://arxiv.org/abs/2607.18912)
中文标题：来自 a Multilingual Streaming ASR Backbone to Kenyan-Language Systems：Data-Centric Adaptation of Nemotron 3.5 面向 Kikuyu，Dholuo，与 Kalenjin
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Spaghetti Architect: A Contamination-Resistant, By-Construction-Labelled, Multi-Language Code Dataset Generator](https://arxiv.org/abs/2607.18642)
中文标题：Spaghetti ArchiteCT ：一种抗污染、附带施工标签的多语言代码数据集生成器
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [BRIDGE: Bottleneck-Aware Regulator-Set Inference and Diagnosis for Cooperative Gene Regulatory Recovery](https://arxiv.org/abs/2607.18602)
中文标题：BRIDGE：Bottleneck-Aware Regulator-Set Inference 与 Diagnosis 面向 Cooperative Gene Regulatory Recovery
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ExpertVerse: A General-Purpose Benchmark for Expert-Level Reasoning in Knowledge-Intensive Visual Synthesis](https://arxiv.org/abs/2607.19341)
中文标题：ExpertVerse：A General-Purpose 基准 面向 Expert-Level Reasoning in Knowledge-Intensive Visual Synthesis
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [OmniReasoner: Thinking with Long Audio-Video via Native Tool Use](https://arxiv.org/abs/2607.19339)
中文标题：OmniReasoner ：通过原生工具使用长音频视频进行思考
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Agents in the Wild: Where Research Meets Deployment](https://arxiv.org/abs/2607.19336)
中文标题：野外特工：研究与部署相遇的地方
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Two-Level Meta-Rubrics for Evaluating Open-Ended Generation: GAMUT, a Benchmark for Factual Completeness](https://arxiv.org/abs/2607.19322)
中文标题：Two-Level Meta-Rubrics 面向 Evaluating Open-Ended Generation：GAMUT，a 基准 面向 Factual Completeness
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D](https://arxiv.org/abs/2607.19321)
中文标题：ResearchArena：Evaluating Sabotage 与 Monitoring in Automated AI R&D
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [CircuitKIT : Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability](https://arxiv.org/abs/2607.19317)
中文标题：CircuitKIT：Circuit Discovery，评测，与 Application Toolkit 面向 Mechanistic Interpretability
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Beyond Score Prediction: LLM-Based Essay Scoring and Feedback Generation via Reinforcement Learning with Rubric Rewards](https://arxiv.org/abs/2607.19219)
中文标题：超越分数预测：基于法学硕士的论文评分和通过强化学习与评分细则表奖励生成反馈
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](https://arxiv.org/abs/2607.19190)
中文标题：Agentic Real2Sim ：使用视觉语言代理进行基于物理的世界建模
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
