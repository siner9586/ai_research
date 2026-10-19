---
title: "让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性"
date: "2026-10-20"
target_date: "2026-10-18"
actual_date: "2026-10-16"
fallback_from: "2026-10-18"
lang: "zh"
slug: "2026-10-20-catchup-depth-aware-re-admission-of-visual"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "code", "evaluation", "interpretability", "multimodal", "rag", "reasoning", "safety", "training"]
topics: ["agents", "code", "evaluation", "interpretability", "multimodal", "rag", "reasoning", "safety", "training"]
sources_page: "/zh/daily/2026-10-20-catchup-depth-aware-re-admission-of-visual-sources/"
generated_at: "2026-10-19T16:21:00.905220+00:00"
page_type: "brief"
candidate_count: 471
featured_count: 6
mentions_count: 20
featured_paper_titles: ["CatchUp: Depth-Aware Re-Admission of Visual Tokens for Efficient Large Vision-Language Models", "MLOps-Bench: Benchmarking AI Agents on Production ML Engineering in Real Repositories", "Self-Reflective Chain-of-Thought (SRCoT): Evidence-Based Text Generation via a Closed-Loop Retrieve--Reflect--Revise Pipeline on Edge LLMs", "NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models", "ECHO: Replacing the Compliance Proxy with Response Harmfulness in Optimization-Based Jailbreak Attack", "OwlSight: A Panoramic Monitor for Chain-of-Thought Reasoning"]
featured_paper_urls: ["https://arxiv.org/abs/2610.23324", "https://arxiv.org/abs/2610.23506", "https://arxiv.org/abs/2610.23311", "https://arxiv.org/abs/2610.23271", "https://arxiv.org/abs/2610.23030", "https://arxiv.org/abs/2610.23670"]
featured_paper_titles_zh: ["CatchUp：Depth-Aware Re-Admission of Visual Tokens 面向 Efficient Large Vision-Language Models", "MLOps-Bench：基准ing AI Agents on Production ML Engineering in Real Repositories", "自反式思维链（ SRCoT ） ：通过闭环检索基于证据的文本生成--反射--边缘LLM上的修订管道", "NestedVLA：Learning to Consolidate 与 Generate Skills 面向 视觉-语言-动作模型", "ECHO ：在基于优化的越狱攻击中用响应有害性替换合规代理", "OwlSight：A Panoramic Monitor 面向 Chain-of-Thought Reasoning"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>CatchUp: Depth-Aware Re-Admission of Visual Tokens for Efficient Large Vision-Language Models (Eunju Park, Uiwon Hwang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.23324">2610.23324</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.23324">PDF</a></p>

中文标题：CatchUp：Depth-Aware Re-Admission of Visual Tokens 面向 Efficient Large Vision-Language Models

信号显示：大型视觉语言模型（ LVLM ）在解码器层重复处理数百个视觉令牌，导致大量计算和内存成本。关键词：rag、inference、latency、benchmark。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>MLOps-Bench: Benchmarking AI Agents on Production ML Engineering in Real Repositories (Quoc Co Tran, Hitesh Laxmichand Patel, Diwakar Mahajan, Kshitij Bakliwal, Avi Sil, Katrin Kirchhoff)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.23506">2610.23506</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.23506">PDF</a></p>

中文标题：MLOps-Bench：基准ing AI Agents on Production ML Engineering in Real Repositories

信号显示：人们越来越期望人工智能代理在生产中修改和维护机器学习系统，但现有的基准主要评估竞争式机器学习实验或通用存储库问题解决方案。关键词：agent、serving、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Self-Reflective Chain-of-Thought (SRCoT): Evidence-Based Text Generation via a Closed-Loop Retrieve--Reflect--Revise Pipeline on Edge LLMs (Fabian Broszio, Michael Hoffmann, Adrian Paschke)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.23311">2610.23311</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.23311">PDF</a></p>

中文标题：自反式思维链（ SRCoT ） ：通过闭环检索基于证据的文本生成--反射--边缘LLM上的修订管道

信号显示：大语言模型（ LLM ）可以生成缺乏源支持或与当地运营约束冲突的流畅输出。关键词：rag、retrieval、safety、memory。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models (Guodong Du, Wanyu Lin)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.23271">2610.23271</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.23271">PDF</a></p>

中文标题：NestedVLA：Learning to Consolidate 与 Generate Skills 面向 视觉-语言-动作模型

信号显示：视觉--语言--行动（ VLA ）模型承诺通才机器人代理，但巩固跨异构任务和环境学习的技能仍然很困难：训练数据跨平台分散，联合多任务训练受到影响。关键词：agent、rag、benchmark、code。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>ECHO: Replacing the Compliance Proxy with Response Harmfulness in Optimization-Based Jailbreak Attack (Yuanwei Wu, Lingdong Huang, Yunlong Mao, Kanye Ye Wang, Jingyu Hua, Sheng Zhong)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.23030">2610.23030</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.23030">PDF</a></p>

中文标题：ECHO ：在基于优化的越狱攻击中用响应有害性替换合规代理

信号显示：尽管进行了广泛的安全调整，但大语言模型仍然容易受到越狱攻击。关键词：alignment、safety、evaluation、code。代码/数据可用性需查看原文确认。

### 6. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>OwlSight: A Panoramic Monitor for Chain-of-Thought Reasoning (Lewen Yan, Yanxu Zhu, Jie Zhang, Jing Shao)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.23670">2610.23670</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.23670">PDF</a></p>

中文标题：OwlSight：A Panoramic Monitor 面向 Chain-of-Thought Reasoning

信号显示：思想链（ CoT ）监测为监督人工智能系统提供了可操作的证据，有可能实现早期检测和干预。关键词：compression、safety、benchmark、reasoning。代码/数据可用性需查看原文确认。

## 其他值得关注
- [FederatedBytes: Tokenizer-Free, Byte-Level Small Language Models for Efficient Multimodal Federated Learning](https://arxiv.org/abs/2610.22906)
中文标题：FederatedBytes：Tokenizer-Free，Byte-Level Small Language Models 面向 Efficient Multimodal Federated Learning
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [GeoReason: Bridging Logical Reasoning and Spatial Fidelity in Remote Sensing Segmentation](https://arxiv.org/abs/2610.23416)
中文标题：GeoReason：Bridging Logical Reasoning 与 Spatial Fidelity in Remote Sensing Segmentation
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Who Pays for Efficient Inference? Confidence-Based Small-to-Large LLM Routing Across Tasks and Languages](https://arxiv.org/abs/2610.23249)
中文标题：谁为高效推理付出代价？跨任务和语言的基于信心的小型到大型LLM路由
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Agentic In-Context Learning: What Algorithms Can Transformers Learn in Closed-Loop Interaction?](https://arxiv.org/abs/2610.23051)
中文标题：代理上下文学习：变形金刚可以在闭环交互中学习哪些算法？
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval](https://arxiv.org/abs/2610.22959)
中文标题：SAFE-Mem ：具有精细权限和治理感知检索的安全代理内存
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Identify, Classify, Act: Per-Instruction Controlled Compliance for LLMs over External Data](https://arxiv.org/abs/2610.22874)
中文标题：识别、分类、行动：针对LLM对外部数据的指令控制合规性
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [From Trajectories to Differentiated Skills: Cognitive Differentiation for Self-Improving Agents](https://arxiv.org/abs/2610.23599)
中文标题：从轨迹到差异化技能：自我完善代理人的认知差异化
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SkillBrowser: Selective Skill Exposure for Scalable Skill-Using Agents](https://arxiv.org/abs/2610.23554)
中文标题：SkillBrowser：Selective Skill Exposure 面向 可扩展 Skill-使用 Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Interpreting SSL Representations for Spoof Detection: a WavLM Study](https://arxiv.org/abs/2610.23526)
中文标题：Interpreting SSL Representations 面向 Spoof Detection：a WavLM Study
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems](https://arxiv.org/abs/2610.23372)
中文标题：超越成功率：视觉-语言-动作系统中记忆的介入评估
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Beyond Marginal Influence: Interaction-Aware Memory Selection for LLM Agents](https://arxiv.org/abs/2610.23266)
中文标题：超越边际影响： LLM客服代表的交互感知记忆选择
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [MLLM Frame Subset Ensembling for Audio-Visual Video QA and MLLM-based Reranking for Ad-hoc Video Search in TRECVID 2025](https://arxiv.org/abs/2610.23214)
中文标题：MLLM Frame Subset Ensembling 面向 Audio-Visual Video QA 与 M基于 LLM 的 Reranking 面向 Ad-hoc Video Search in TRECVID 2025
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Domain-specific language alignment of multimodal embeddings towards explainable predictions](https://arxiv.org/abs/2610.23110)
中文标题：针对特定领域的多模态嵌入与可解释的预测进行语言对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Rethinking GRPO for Large Reasoning Model Safety Alignment](https://arxiv.org/abs/2610.23085)
中文标题：Rethinking GRPO 面向 Large Reasoning Model Safety Alignment
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [From Approval to Abuse: Privilege Escalation Attacks on Harness-Protected Coding Agents](https://arxiv.org/abs/2610.22987)
中文标题：从批准到滥用：针对受线束保护的编码代理的特权提升攻击
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [UniField++: A Unified Agentic Framework with Loop Reasoning for MRI Field-Strength Enhancement](https://arxiv.org/abs/2610.22982)
中文标题：UniField + + ：具有循环推理的统一代理框架，用于MRI场强增强
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Conformal Policy Selection: When to Deploy AI Decisions for Targeted Intervention](https://arxiv.org/abs/2610.22930)
中文标题：Conformal Policy Selection：When to Deploy AI Decisions 面向 Targeted Intervention
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [DICL-Qwen3VL: Decoupled Confidence Calibration for Interpretable Workwear Detection](https://arxiv.org/abs/2610.22929)
中文标题：DICL-Qwen3VL：Decoupled Confidence Calibration 面向 Interpretable Workwear Detection
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Behavioral Couplings: From Formation to Behavioral Emergence in Language Models](https://arxiv.org/abs/2610.23847)
中文标题：行为耦合：从语言模型的形成到行为出现
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Waiting Buys Exactly Two Moments: Endogenous Identification in Prediction-Driven Allocation](https://arxiv.org/abs/2610.23830)
中文标题：等待恰恰购买了两个时刻：预测驱动分配中的内源性识别
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
