---
title: "让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险、提升 RAG 检索和知识库问答可靠性"
date: "2026-09-24"
target_date: "2026-09-22"
actual_date: "2026-09-22"
fallback_from: ""
lang: "zh"
slug: "2026-09-24-swe-serve-benchmarking-agentic-engineering-for-production"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "evaluation", "multimodal", "robotics", "training", "video-generation", "vision-generation"]
topics: ["agents", "evaluation", "multimodal", "robotics", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-09-24-swe-serve-benchmarking-agentic-engineering-for-production-sources/"
generated_at: "2026-09-23T23:39:05.986078+00:00"
page_type: "brief"
candidate_count: 414
featured_count: 6
mentions_count: 20
featured_paper_titles: ["SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving", "Calibration as a First-Class Criterion in LLM Evaluation", "IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models", "TriWorldBench: A Tri-View Consistency Perspective on Embodied World Models", "Governed AI-Agent Coordination for Dementia Care: Architecture, Safety Contracts, and Evidence-Derived Workflow Verification", "A Data-Interventional Framework for Auditing Privacy and Fairness in Generative Medical Imaging"]
featured_paper_urls: ["https://arxiv.org/abs/2609.26777", "https://arxiv.org/abs/2609.26489", "https://arxiv.org/abs/2609.25562", "https://arxiv.org/abs/2609.26314", "https://arxiv.org/abs/2609.25956", "https://arxiv.org/abs/2609.26623"]
featured_paper_titles_zh: ["SWE-Serve：基准ing Agentic Engineering 面向 Production Inference Serving", "校准作为LLM评估的一流标准", "IndustrialVLA-Bench：A Traceable Multi-Axis 评测 of Open Robot Policy Models", "TriWorldBench：A Tri-View Consistency Perspective on Embodied 世界模型", "Governed AI-Agent Coordination 面向 Dementia Care：Architecture，Safety Contracts，与 Evidence-Derived Workflow Verification", "用于审核生成性医学成像中的隐私和公平性的数据介入框架"]
---

# 让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving (Jennifer Williams, Dave Farris, Jeff Farris, Jiantao Jiao)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.26777">2609.26777</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.26777">PDF</a></p>

中文标题：SWE-Serve：基准ing Agentic Engineering 面向 Production Inference Serving

信号显示：我们引入SWE-Serve ，这是评估生产推理工程任务代理的基准。关键词：agent、rag、inference、serving。代码/数据可用性需查看原文确认。

### 2. 识别并缓解模型安全、越狱和对齐风险

<p class="paper-meta-line"><span>Calibration as a First-Class Criterion in LLM Evaluation (Mario Sanz-Guerrero, Katharina von der Wense)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.26489">2609.26489</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.26489">PDF</a></p>

中文标题：校准作为LLM评估的一流标准

信号显示：语言模型的校准-表达或隐式置信度和经验正确性之间的对齐-是NLP中一个经过充分研究的子领域。关键词：deployment、alignment、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models (Yiqi Wang, Zhifeng Rao, Jiaqi Zhang, Xiaoyang Li, Zhangkai Wu, Yiqun Duan, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.25562">2609.25562</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.25562">PDF</a></p>

中文标题：IndustrialVLA-Bench：A Traceable Multi-Axis 评测 of Open Robot Policy Models

信号显示：开放式机器人政策越来越遵循两种范式：视觉-语言-行动模型（ VLA ）直接将观察和指令映射到行动，而世界-行动模型（ WAM ）将学习到的视频或世界动态纳入政策学习或行动生成。关键词：rag、inference、deployment、latency。代码/数据可用性需查看原文确认。

### 4. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>TriWorldBench: A Tri-View Consistency Perspective on Embodied World Models (Xuanyi Liu, Haofeng Wang, Ruiqi Li, Danni Yu, Rui Wan, Ruixu Zhang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.26314">2609.26314</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.26314">PDF</a></p>

中文标题：TriWorldBench：A Tri-View Consistency Perspective on Embodied 世界模型

信号显示：具体化的世界模型预测机器人行动的结果，以支持学习和规划。关键词：alignment、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Governed AI-Agent Coordination for Dementia Care: Architecture, Safety Contracts, and Evidence-Derived Workflow Verification (Francesca Medda, Hui Gong)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.25956">2609.25956</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.25956">PDF</a></p>

中文标题：Governed AI-Agent Coordination 面向 Dementia Care：Architecture，Safety Contracts，与 Evidence-Derived Workflow Verification

信号显示：痴呆症护理越来越多地涉及连接的传感器、药物设备、电子记录和辅助技术。关键词：agent、workflow、serving、safety。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>A Data-Interventional Framework for Auditing Privacy and Fairness in Generative Medical Imaging (Mischa Dombrowski, Bernhard Kainz)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.26623">2609.26623</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.26623">PDF</a></p>

中文标题：用于审核生成性医学成像中的隐私和公平性的数据介入框架

信号显示：基于扩散的合成数据生成为共享医学成像数据提供了一条有希望的途径，而无需发布敏感的患者记录。关键词：retrieval、code、synthetic data、frame。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Testing-Driven Reliability Audit of Trajectory-Based Early Outcome Prediction for LLM Agents: Target-Specific Calibration Transfer Persists Within a Single Benchmark](https://arxiv.org/abs/2609.25647)
中文标题：LLM代理基于轨迹的早期结果预测的测试驱动可靠性审计：目标特定校准转移持续存在于单个基准中
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem](https://arxiv.org/abs/2609.26761)
中文标题：A2M ： MCP生态系统中的跟踪优化Agent劫持
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [EquivSVA: A Formally Verified Dataset of Behavioral Assertions Across Equivalent RTL Implementations](https://arxiv.org/abs/2609.26751)
中文标题：EquivSVA ：经过正式验证的等效RTL实施的行为断言数据集
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Metrics Failure in LLM-Based Code Vulnerability Repair: An Empirical Study and a Change-Aware Screen](https://arxiv.org/abs/2609.26749)
中文标题：基于LLM的代码漏洞修复中的指标失败：实证研究和变更感知屏幕
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Beyond End-Task Success: How to Audit Visual Experience Retrieval in Robotics](https://arxiv.org/abs/2609.26567)
中文标题：超越最终任务的成功：如何审核机器人中的视觉体验检索
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation](https://arxiv.org/abs/2609.26313)
中文标题：SafeLoop：Risk-Aware Rollback 面向 Vision-Language-Action Manipulation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Certified Against Which Oracle? Execution Labels Set the Reported Risk of Conformal Abstention for Text-to-SQL](https://arxiv.org/abs/2609.25938)
中文标题：针对哪个Oracle认证？执行标签设置Text-to-SQL的Conformal Abstention报告风险
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Shallow to Deep: Aligning Token Pruning with Stage-wise Roles in LVLMs](https://arxiv.org/abs/2609.25635)
中文标题：从浅到深：将令牌修剪与LVLM中的阶段性角色对齐
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery](https://arxiv.org/abs/2609.25558)
中文标题：HABILIS Brain 0：Geometry-Change Supervision 面向 Vision-Language-Action 与 Residual Flow Recovery
关注理由：涉及机器人与具身智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [The Sirens' Song: When Proximal Background Context Overshadows Distant Evidence](https://arxiv.org/abs/2609.26718)
中文标题：The Sirens' Song：When Proximal Background Context Overshadows Distant Evidence
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Optimal Sequential Annotations for Off-Policy Evaluation](https://arxiv.org/abs/2609.26707)
中文标题：非政策评估的最佳顺序注释
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [GTR: Gated Token Recurrence for Efficient Dense Prediction](https://arxiv.org/abs/2609.26590)
中文标题：GTR：Gated Token Recurrence 面向 Efficient Dense Prediction
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Combining Hierarchical Cognitive Process with Process Supervision for Interpretable Scene Safety Understanding](https://arxiv.org/abs/2609.26399)
中文标题：将分层认知过程与过程监督相结合，以实现可解释的场景安全理解
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [KwaiMind Technical Report](https://arxiv.org/abs/2609.26375)
中文标题：KwAIMind技术报告
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [PACT: From Credit Assignment to Critic Alignment](https://arxiv.org/abs/2609.26355)
中文标题：PACT：来自 Credit Assignment to Critic Alignment
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Towards Systematic Qualification of Vision-Language Models for Automotive Perception Systems](https://arxiv.org/abs/2609.25945)
中文标题：面向汽车感知系统视觉语言模型的系统化认证
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [When Does Execution Provenance Help Agent Memory Retrieval?](https://arxiv.org/abs/2609.25913)
中文标题：Execution Provenance何时帮助代理检索内存？
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Risk-Aware Online Conformal State Probing](https://arxiv.org/abs/2609.25889)
中文标题：风险意识在线适形状态探测
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [LoRango: It Takes Two LoRAs to Unlock Hidden Behaviors in Diffusion Models](https://arxiv.org/abs/2609.25884)
中文标题：LoRango ：需要两个LoRA才能解锁扩散模型中的隐藏行为
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [AgenticSizing: A Large Language Model-based Multi-Agent Framework for Analog Circuit Sizing](https://arxiv.org/abs/2609.25873)
中文标题：AgenticSizing：A Large Language Model-based Multi-Agent 框架 面向 Analog Circuit Sizing
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
