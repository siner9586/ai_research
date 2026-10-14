---
title: "提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-10-15"
target_date: "2026-10-13"
actual_date: "2026-10-13"
fallback_from: ""
lang: "zh"
slug: "2026-10-15-who-improves-the-robot-toward-physical-recursive"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力。"
tags: ["agents", "code", "data-engineering", "evaluation", "reasoning", "speech-audio", "systems", "training"]
topics: ["agents", "code", "data-engineering", "evaluation", "reasoning", "speech-audio", "systems", "training"]
sources_page: "/zh/daily/2026-10-15-who-improves-the-robot-toward-physical-recursive-sources/"
generated_at: "2026-10-14T23:54:57.343552+00:00"
page_type: "brief"
candidate_count: 660
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Who Improves the Robot? Toward Physical Recursive Self-Improvement", "Agent-Reflex: Teaching Language Agents to Act Reflectively", "WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions", "Does self-distillation improve reasoning?", "Self-Evolving Agent Harness", "CryoTracer: A Synthetic-to-Real System for Filament Instance Tracing in Cryo-EM"]
featured_paper_urls: ["https://arxiv.org/abs/2610.18842", "https://arxiv.org/abs/2610.17953", "https://arxiv.org/abs/2610.18826", "https://arxiv.org/abs/2610.18613", "https://arxiv.org/abs/2610.18813", "https://arxiv.org/abs/2610.18696"]
featured_paper_titles_zh: ["谁在改进机器人？走向物理递归自我提升", "Agent-Reflex ：教语言学会反思", "WorldOracle：基准ing Action-Conditioned 世界模型 against Real-World Executions", "自馏能否改善推理能力？", "自我进化的Agent线束", "CryoTracer：A Synthetic-to-Real System 面向 Filament Instance Tracing in Cryo-EM"]
---

# 提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、提升代码生成、执行反馈和自动修复能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Who Improves the Robot? Toward Physical Recursive Self-Improvement (Hai Zhou, Fan Yang, Zeyi Chen, Lejun Zhang, Chenyang Fu, Jianping Li, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.18842">2610.18842</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.18842">PDF</a></p>

中文标题：谁在改进机器人？走向物理递归自我提升

信号显示：机器人在执行任务时越来越自主，但它们的改进仍然主要由人类驱动。关键词：serving、safety、benchmark、search。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Agent-Reflex: Teaching Language Agents to Act Reflectively (Guanting Dong, Xinyu Yang, Jiajie Jin, Yuyang Hu, Xiaoshuai Song, Yifei Chen, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.17953">2610.17953</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.17953">PDF</a></p>

中文标题：Agent-Reflex ：教语言学会反思

信号显示：大语言模型已经从单圈聊天机器人演变为能够进行长距离推理的交互式代理。关键词：agent、deployment、benchmark、code。代码/数据可用性需查看原文确认。

### 3. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions (Haoyi Duan, Liliang Chen, Nan Wang, Yang Zhang, Yuhang Lu, Xiaotong Chen, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.18826">2610.18826</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.18826">PDF</a></p>

中文标题：WorldOracle：基准ing Action-Conditioned 世界模型 against Real-World Executions

信号显示：我们推出了WorldOracle ，这是一个专门用于根据配对的真实世界执行来评估动作条件世界模型（ ACWM ）的基准。关键词：alignment、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Does self-distillation improve reasoning? (Jason Ken Adhinarta, Raina Wu, Ashutosh Sharma, Avinash Balakrishnan, Rameswar Panda, Polina Golland, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.18613">2610.18613</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.18613">PDF</a></p>

中文标题：自馏能否改善推理能力？

信号显示：自蒸馏是一种新兴的方法，它训练模型在受特权信息（如正确答案或环境反馈）制约时模仿自己的预测。关键词：tool use、rag、alignment、evaluation。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Self-Evolving Agent Harness (Chuyang Wei, Haoxiang Guan, Minghang Zhu, Kexin Zhou, Jiyan He, Xiren Zhou, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.18813">2610.18813</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.18813">PDF</a></p>

中文标题：自我进化的Agent线束

信号显示：利用自我进化修改客服代表的软件支架，包括提示、内存、工作流程和可执行组件，同时保持模型权重固定。关键词：agent、workflow、deployment、safety。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>CryoTracer: A Synthetic-to-Real System for Filament Instance Tracing in Cryo-EM (Radosław Kuczbański, Wojciech Kozłowski, Mateusz Grzesiuk, Konrad Karanowski, Lukas Frey, Andrzej Rzepiela, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.18696">2610.18696</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.18696">PDF</a></p>

中文标题：CryoTracer：A Synthetic-to-Real System 面向 Filament Instance Tracing in Cryo-EM

信号显示：在低温电子显微镜中，粒子拾取通常被公式化为物体检测问题，其中单个粒子由边界框表示，这是球形粒子的自然表示，但对于可以延伸到。关键词：serving、evaluation、code、fine-tuning。代码/数据可用性需查看原文确认。

## 其他值得关注
- [When and How Order-Flow Interventions Work After Dealers Adapt](https://arxiv.org/abs/2610.18158)
中文标题：经销商适应后何时以及如何进行订单流程干预
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SYNPRED: A Synergistic Approach to Multimodal Learning for Clinical Prediction](https://arxiv.org/abs/2610.18110)
中文标题：SYNPRED：A Synergistic Approach to Multimodal Learning 面向 Clinical Prediction
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution](https://arxiv.org/abs/2610.17816)
中文标题：赋能边缘代理： LLM代理执行中边缘云协作的系统分析
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [LatentRiskBench: Measuring State-Dependent Risks in Enterprise Agents](https://arxiv.org/abs/2610.17685)
中文标题：LatentRiskBench ：衡量企业代理中的状态相关风险
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ATTUNE: Agentic Throughput Tuning for LLM Training](https://arxiv.org/abs/2610.17528)
中文标题：ATTUNE：Agentic Throughput Tuning 面向 LLM Training
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2610.18683)
中文标题：ProAS：A Progress-Aware Advantage Shaping 框架 面向 Multi-Turn Agentic Reinforcement Learning
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Nudge the Judge: Uncovering Program Decision Hijacking in Real-World Jev Applications](https://arxiv.org/abs/2610.18612)
中文标题：Nudge the Judge ：揭露现实JEV应用程序中的计划决策劫持
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Rethinking Projector Training in Multimodal LLMs](https://arxiv.org/abs/2610.18598)
中文标题：重新思考多模态LLM中的投影仪培训
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents](https://arxiv.org/abs/2610.18457)
中文标题：KAIROS ： LLM代理系统边界的交易安全执行
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Privacy-Preserving GNN Inference on Financial Transaction Graphs via Homomorphic Encryption](https://arxiv.org/abs/2610.18054)
中文标题：通过同态加密对金融交易图进行隐私保护的GNN推断
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Web Scale on a Budget: Tail-Aware Retrieval Evaluation](https://arxiv.org/abs/2610.17986)
中文标题：经济实惠的网络规模：尾部感知检索评估
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [AlignPred: Error-Controlled KV Cache Compression via Alignment and Predictive Coding](https://arxiv.org/abs/2610.17970)
中文标题：AlignPred ：通过对齐和预测编码进行错误控制的KV缓存压缩
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [HaloBlock: Faster and Better Decoding for Diffusion Large Language Models](https://arxiv.org/abs/2610.17948)
中文标题：HaloBlock：Faster 与 Better Decoding 面向 Diffusion Large Language Models
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [SSEmb: Training a Generalizable Speech Retrieval Model Using Only Automatic Speech Recognition Data](https://arxiv.org/abs/2610.17813)
中文标题：SSEmb：Training a Generalizable Speech Retrieval Model 使用 Only Automatic Speech Recognition Data
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Beyond the End-Effector: Learning Whole-Arm Contact Manipulation from Human Demonstrations](https://arxiv.org/abs/2610.17802)
中文标题：超越终端执行器：从人类演示中学习全臂接触操纵
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Representation Geometry and Inductive Biases in Quantum Classifiers across Classical Visual Benchmarks](https://arxiv.org/abs/2610.17722)
中文标题：跨经典视觉基准的量子分类器中的表示几何和归纳偏差
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Facts Don't Speak Louder than Words: The Behavioral Essence of Long-CoT Distillation](https://arxiv.org/abs/2610.17607)
中文标题：事实不胜言辞：长时间物联网蒸馏的行为本质
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [RAN-JEPA: An Action-Conditioned World Model for Energy-efficient Mobile Network Control](https://arxiv.org/abs/2610.17584)
中文标题：RAN-JEPA：An Action-Conditioned World Model 面向 Energy-efficient Mobile Network Control
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Chasing Label Shifters: A Change-Aware Framework for Dynamic Graph Node Classification](https://arxiv.org/abs/2610.17582)
中文标题：追逐标签移位器：动态图形节点分类的变化感知框架
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Towards Green AI: Evaluating Energy Efficiency for Quantized LLM Inference](https://arxiv.org/abs/2610.17531)
中文标题：迈向绿色AI ：评估量化LLM推断的能源效率
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
