---
title: "让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力、提升 RAG 检索和知识库问答可靠性"
date: "2026-09-20"
target_date: "2026-09-18"
actual_date: "2026-09-17"
fallback_from: "2026-09-18"
lang: "zh"
slug: "2026-09-20-chronicle-cut-point-replay-for-regression-testing"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "robotics", "systems", "training", "video-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "robotics", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-09-20-chronicle-cut-point-replay-for-regression-testing-sources/"
generated_at: "2026-09-19T22:57:58.435632+00:00"
page_type: "brief"
candidate_count: 468
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Chronicle: Cut-Point Replay for Regression Testing of LLM Agents", "Reasoning Quality Matters: Combating Reasoning Collapse in LLM-based Embedding Learning", "SCGFM-ART: Amortized Relational Transport for Structure-Centric Graph Foundation Models", "Stress-testing Alignment Midtraining", "QoS-Aware Federated Learning for Multimodal In-Cabin Interaction in Smart Vehicles", "Marginal utility, matrix factorization, and the Key-Value (KV) cache: a unified information-economic framework for sovereign geo-mining inference"]
featured_paper_urls: ["https://arxiv.org/abs/2609.20625", "https://arxiv.org/abs/2609.20563", "https://arxiv.org/abs/2609.20419", "https://arxiv.org/abs/2609.20412", "https://arxiv.org/abs/2609.20123", "https://arxiv.org/abs/2609.20068"]
featured_paper_titles_zh: ["Chronicle：Cut-Point Replay 面向 Regression Testing of LLM Agents", "推理质量很重要：在基于LLM的嵌入式学习中对抗推理崩溃", "SCGFM-ART：Amortized Relational Transport 面向 Structure-Centric Graph Foundation Models", "压力测试对中训练", "QoS-Aware Federated Learning 面向 Multimodal In-Cabin Interaction in Smart Vehicles", "边际效用、矩阵分解和关键值（ KV ）缓存：主权地理采矿推断的统一信息经济框架"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Chronicle: Cut-Point Replay for Regression Testing of LLM Agents (Tisha Chawla, Susheem Koul)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.20625">2609.20625</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.20625">PDF</a></p>

中文标题：Chronicle：Cut-Point Replay 面向 Regression Testing of LLM Agents

信号显示：大语言模型响应是不确定的，因此LLM代理的故障很难重现：故障取决于不可按位重现的推理、读取变化状态的工具以及重新运行很少重复的多步轨迹。关键词：agent、inference、benchmark、code。代码/数据可用性需查看原文确认。

### 2. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Reasoning Quality Matters: Combating Reasoning Collapse in LLM-based Embedding Learning (Zihan Gong, Xiaohan Ye, Jiangchao Yao, Jinsong Lan, Xiaoyong Zhu, Xu Chen)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.20563">2609.20563</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.20563">PDF</a></p>

中文标题：推理质量很重要：在基于LLM的嵌入式学习中对抗推理崩溃

信号显示：大语言模型（ LLM ）最近显示出产生上下文丰富的文本嵌入以供检索的强大潜力。关键词：rag、retrieval、serving、alignment。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>SCGFM-ART: Amortized Relational Transport for Structure-Centric Graph Foundation Models (Xiaodong He, Xincheng Wang, Zhao Kang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.20419">2609.20419</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.20419">PDF</a></p>

中文标题：SCGFM-ART：Amortized Relational Transport 面向 Structure-Centric Graph Foundation Models

信号显示：图基础模型（ GFM ）旨在学习跨越严重异构图域的可转移表示。关键词：rag、inference、alignment、benchmark。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Stress-testing Alignment Midtraining (Sid Baines, Jonathan Bostock, Maria Angelica Martinez, Andrew Draganov, David Africa, Daniel Tan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.20412">2609.20412</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.20412">PDF</a></p>

中文标题：压力测试对中训练

信号显示：在通过训练后技术对齐前沿模型时，不可能直接演示我们希望模型在所有可能的部署环境中展现的所有行为；我们的模型必须在训练后分布之外进行推广。关键词：rag、deployment、alignment、post-training。代码/数据可用性需查看原文确认。

### 5. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>QoS-Aware Federated Learning for Multimodal In-Cabin Interaction in Smart Vehicles (Baran Can Gül, Mert Nakıp, Nasser Jazdi, Michael Weyrich)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.20123">2609.20123</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.20123">PDF</a></p>

中文标题：QoS-Aware Federated Learning 面向 Multimodal In-Cabin Interaction in Smart Vehicles

信号显示：现代智能车辆利用从高带宽视觉系统到低速生理监视器的多模态传感器，提供个性化的舱内服务。关键词：rag、deployment、latency、safety。代码/数据可用性需查看原文确认。

### 6. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Marginal utility, matrix factorization, and the Key-Value (KV) cache: a unified information-economic framework for sovereign geo-mining inference (Caroline Gans Combe)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.20068">2609.20068</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.20068">PDF</a></p>

中文标题：边际效用、矩阵分解和关键值（ KV ）缓存：主权地理采矿推断的统一信息经济框架

信号显示：本文建立了边际效用的经济概念与两种机器学习构造之间的理论桥梁，即矩阵分解和变压器语言模型的关键值缓存。关键词：inference、latency、compression、benchmark。代码/数据可用性需查看原文确认。

## 其他值得关注
- [PointEvent: Rethinking Event-based Tiny Object Detection via Serialized Motion Evidence Accumulation](https://arxiv.org/abs/2609.20066)
中文标题：PointEvent ：通过序列化运动证据累积重新思考基于事件的微小物体检测
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [The Missing Complement: State-Conditioned Minimal Sufficient Evidence for Coding Agents](https://arxiv.org/abs/2609.20050)
中文标题：缺失的补充：编码代理的状态条件最小足够证据
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [GRF-Recon: Global Ray-Field Optimization for Long-Sequence Feed-forward Reconstruction](https://arxiv.org/abs/2609.20012)
中文标题：GRF-Recon：Global Ray-Field Optimization 面向 Long-Sequence Feed-forward Reconstruction
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Benchmarking LLM Compliance with China AI Generated Content Regulations](https://arxiv.org/abs/2609.19989)
中文标题：对标LLM是否符合中国AI生成内容法规
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [From "Who Is This User?" to "What Does This Purchase Mean?": A Deployed Pipeline for Semantic User Profiling at Bank Scale](https://arxiv.org/abs/2609.19928)
中文标题：从“此用户是谁？”到“此购买意味着什么？":银行规模的语义用户分析部署管道
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ClashBench: Conflicts Leading Agents to Seize and Harm](https://arxiv.org/abs/2609.19892)
中文标题：ClashBench：Conflicts Leading Agents to Seize 与 Harm
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Beyond Flattened Tokens: Structure-Preserving EEG Decoding with Reusable TriDim Blocks](https://arxiv.org/abs/2609.19842)
中文标题：超越扁平化令牌：使用可重复使用的TriDim块进行结构保留脑电图解码
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Absence is Presence: Understanding Visual Scene Negative Events Under Safety Cognitive Constraint](https://arxiv.org/abs/2609.19812)
中文标题：缺勤就是在场：了解安全认知约束下的视觉场景负面事件
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Learn Before You Judge: Progressive Knowledge-to-Decision Alignment for Explainable Hateful Meme Detection](https://arxiv.org/abs/2609.19778)
中文标题：判断前学习：可解释的仇恨模因检测的渐进式知识与决策一致性
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Benchmarking MLLMs via Cognitive Expected Scene Graph for Safety-Critical Visual Negation Understanding](https://arxiv.org/abs/2609.19767)
中文标题：通过认知预期场景图对安全关键视觉否定理解的MLLM进行基准测试
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Federated Learning Framework for Privacy-Preserving Kidney Stone Detection](https://arxiv.org/abs/2609.19740)
中文标题：保护隐私的肾结石检测联合学习框架
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Opinion Dynamics-based Coalition Formation for Federated Learning in Heterogeneous IoT Systems](https://arxiv.org/abs/2609.19695)
中文标题：异构物联网系统中联合学习的基于动态的联盟形成
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [From Intent to Action: Benchmarking LLM Safety in Vehicle Voice Command Authorization](https://arxiv.org/abs/2609.19630)
中文标题：从意图到行动：在车辆语音指令授权中对标LLM安全
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [TacSushi: Tactile-Grounded World-Action Modeling for Dexterous Sushi Manipulation](https://arxiv.org/abs/2609.19613)
中文标题：TacSushi：Tactile-Grounded World-Action Modeling 面向 Dexterous Sushi Manipulation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [FootprintRAG: Visual Analytics for Evidence Context Refinement in RAG-based Scientific Literature Exploration](https://arxiv.org/abs/2609.19601)
中文标题：FootprintRAG：Visual Analytics 面向 Evidence Context Refinement in RAG-based Scientific Literature Exploration
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Form Over Content In Gradient-Based Data Attribution Methods](https://arxiv.org/abs/2609.19589)
中文标题：基于梯度的数据归因方法中的表单内容
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [AMB3R-SLAM: Kilometer-scale SLAM with Hierarchical Backend](https://arxiv.org/abs/2609.19518)
中文标题：AMB3R-SLAM ：带分层后端的千米级SLAM
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [NS3Learn: Transferring 5G NR Mode-2 Reception Realism from ns-3 to the Veins/SUMO Stack for Connected-Vehicle Safety Assessment](https://arxiv.org/abs/2609.20578)
中文标题：NS3Learn ：将5G NR模式-2接收真实感从ns-3转移到静脉/SUMO堆栈以进行联网车辆安全评估
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Accelerating Visual Policy Learning with Sampling-Based Model Predictive Control](https://arxiv.org/abs/2609.20575)
中文标题：使用基于抽样的模型预测控制加速可视化策略学习
关注理由：涉及机器人与具身智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Model-based Bootstrap for Offline Policy Evaluation in Tabular Reinforcement Learning](https://arxiv.org/abs/2609.20389)
中文标题：表格强化学习中离线策略评估的基于模型的引导
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
