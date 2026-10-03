---
title: "提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力、评测视频生成的时间一致性和运动真实感"
date: "2026-10-04"
target_date: "2026-10-02"
actual_date: "2026-10-01"
fallback_from: "2026-10-02"
lang: "zh"
slug: "2026-10-04-omni-embed-mini-binding-modalities-without-forgetting"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力、评测视频生成的时间一致性和运动真实感。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "training", "video-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "training", "video-generation"]
sources_page: "/zh/daily/2026-10-04-omni-embed-mini-binding-modalities-without-forgetting-sources/"
generated_at: "2026-10-03T23:47:41.661633+00:00"
page_type: "brief"
candidate_count: 640
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation", "Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic Scenes", "Scalable, Transferable Meta-network for Data Selection Requires a Different Loss (and Why the Obvious Choice is Problematic)", "Homomorphic Advantage Operator: Stabilizing Reinforcement Learning Under Fully Homomorphic Encryption Constraints", "Causal Memory Policy: Making Memory Utility Identifiable by Intervening on Retrieval", "Mem++: Non-Destructive Memory for Long-Term Organizational LLM Agents"]
featured_paper_urls: ["https://arxiv.org/abs/2610.02148", "https://arxiv.org/abs/2610.02117", "https://arxiv.org/abs/2610.02092", "https://arxiv.org/abs/2610.02074", "https://arxiv.org/abs/2610.02070", "https://arxiv.org/abs/2610.02002"]
featured_paper_titles_zh: ["Omni-Embed-Mini ：通过密集蒸馏不遗忘的结合方式", "Where-OPD ：合成场景下MLLM的空间引导随机自蒸馏", "可扩展，Transferable Meta-network 面向 Data Selection Requires a Different Loss (与 Why the Obvious Choice is Problematic)", "同态优势算子：全同态加密约束下的稳定强化学习", "因果内存策略：通过介入检索来识别内存实用程序", "Mem++：Non-Destructive Memory 面向 Long-Term Organizational LLM Agents"]
---

# 提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力、评测视频生成的时间一致性和运动真实感

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力、评测视频生成的时间一致性和运动真实感。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation (Mohammed Irfan Kurpath, Jaseel Muhammad Kaithakkodan, Sahal Shaji Mullappilly, Ivan Laptev, Hisham Cholakkal)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.02148">2610.02148</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.02148">PDF</a></p>

中文标题：Omni-Embed-Mini ：通过密集蒸馏不遗忘的结合方式

信号显示：将文本嵌入模型扩展到新模态通常会降低文本检索质量，现有的全模态嵌入器通过数十亿个参数进行补偿。关键词：rag、retrieval、alignment、evaluation。代码/数据可用性需查看原文确认。

### 2. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic Scenes (Sophia Sirko-Galouchenko, Monika Wysoczanska, Andrei Bursuc, Nicolas Thome, Spyros Gidaris)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.02117">2610.02117</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.02117">PDF</a></p>

中文标题：Where-OPD ：合成场景下MLLM的空间引导随机自蒸馏

信号显示：政策自我蒸馏最近已经成为一种改进语言模型推理的有效方法，通过监督学生使用接收特权信息的冻结或EMA版本的自己来改进语言模型推理。关键词：rag、benchmark、multimodal、post-training。代码/数据可用性需查看原文确认。

### 3. 评测视频生成的时间一致性和运动真实感

<p class="paper-meta-line"><span>Scalable, Transferable Meta-network for Data Selection Requires a Different Loss (and Why the Obvious Choice is Problematic) (Zilin Du, Bowen Yang, Boyang Albert Li)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.02092">2610.02092</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.02092">PDF</a></p>

中文标题：可扩展，Transferable Meta-network 面向 Data Selection Requires a Different Loss (与 Why the Obvious Choice is Problematic)

信号显示：数据选择对于在大规模和异构语料库上训练大语言模型至关重要。关键词：safety、data、dataset、data-engineering。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Homomorphic Advantage Operator: Stabilizing Reinforcement Learning Under Fully Homomorphic Encryption Constraints (Abid Mohamed Nadhir, Ahmad Al Hanbali, Beggas Mounir)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.02074">2610.02074</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.02074">PDF</a></p>

中文标题：同态优势算子：全同态加密约束下的稳定强化学习

信号显示：保护隐私的机器学习在云端为具有机密数据的智能系统带来了巨大的部署挑战。关键词：agent、serving、deployment、benchmark。代码/数据可用性需查看原文确认。

### 5. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Causal Memory Policy: Making Memory Utility Identifiable by Intervening on Retrieval (Arman Behnam, Binghui Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.02070">2610.02070</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.02070">PDF</a></p>

中文标题：因果内存策略：通过介入检索来识别内存实用程序

信号显示：记忆增强的大语言模型必须决定保留哪些记忆，而最近的系统通过估计每个记忆对任务性能的影响来决定保留哪些记忆。关键词：retrieval、serving、code、memory。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Mem++: Non-Destructive Memory for Long-Term Organizational LLM Agents (Ahmad Yehia, Aly O. Abdelkareem, Islam Ahmed, Hesham Omran, Khaled Alashmouny, Christian Claudel, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.02002">2610.02002</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.02002">PDF</a></p>

中文标题：Mem++：Non-Destructive Memory 面向 Long-Term Organizational LLM Agents

信号显示：大语言模型（ LLM ）代理现在参与组织工作，许多作者在数月内记录跨文档的决策。关键词：agent、rag、evaluation、benchmark。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Controllable Multi-label Video Safety Detection via Adaptive Tversky Policy Optimization](https://arxiv.org/abs/2610.02019)
中文标题：通过自适应Tversky策略优化实现可控多标签视频安全检测
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [FastCI: Efficient GPU-Intensive CI for LLM Training Frameworks](https://arxiv.org/abs/2610.01967)
中文标题：FastCI ： LLM培训框架的高效GPU密集型CI
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [A Hybrid Approach to Malware Detection: Integrating Few-Shot Model-Agnostic Meta-Learning with Autoencoders](https://arxiv.org/abs/2610.01949)
中文标题：恶意软件检测的混合方法：将与模型无关的少量拍摄元学习与自动编码器集成
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Anti-Persona: Disrupting Unauthorized Identity Binding and Recognition in Personalized Vision--Language Models](https://arxiv.org/abs/2610.01944)
中文标题：反人格：在个性化视觉中破坏未经授权的身份绑定和识别--语言模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Mapping the RAG Landscape: A Four Axis Taxonomy of Efficiency, Defense, Interactivity, and Reasoning](https://arxiv.org/abs/2610.01936)
中文标题：Mapping the RAG Landscape：A Four Axis Taxonomy of Efficiency，Defense，Interactivity，与 Reasoning
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Cross-Lingual Alignment for Decoder-Only Models using MoE Routers](https://arxiv.org/abs/2610.01921)
中文标题：Cross-Lingual Alignment 面向 Decoder-Only Models 使用 MoE Routers
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Memory-Guided B-Roll Generation from User Video Collections](https://arxiv.org/abs/2610.01884)
中文标题：Memory-Guided B-Roll Generation 来自 User Video Collections
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [From Pixels to Policy: A Multi-Agent System for Intervention and Geo-Spatial Decision Support](https://arxiv.org/abs/2610.01870)
中文标题：来自 Pixels to Policy：A Multi-Agent System 面向 Intervention 与 Geo-Spatial Decision Support
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [AVSD-Scenes: A Dataset for Audio-Visual Description of Urban Scenes](https://arxiv.org/abs/2610.01861)
中文标题：AVSD-Scenes：A Dataset 面向 Audio-Visual Description of Urban Scenes
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Token Communication-Assisted Collaborative Embodied Artificial Intelligence: Concepts, Framework, and Opportunities](https://arxiv.org/abs/2610.01826)
中文标题：代币通信辅助协作式人工智能：概念、框架和机遇
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [A Safe Prototype Is Not a Safety Direction: Reference Dependence and Prompt Confounds in Response-Safety Embeddings](https://arxiv.org/abs/2610.01801)
中文标题：安全原型不是安全方向：响应-安全嵌入中的参考依赖性和快速混淆
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [VideoEvolve: Evolving Agent Harnesses for Video Temporal Grounding](https://arxiv.org/abs/2610.01766)
中文标题：VideoEvolve：Evolving Agent Harnesses 面向 Video Temporal 落地
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [FFBL-Coop: Association-Decoupled Cooperative 3D Multi-Object Tracking](https://arxiv.org/abs/2610.01750)
中文标题：FFBL-Coop ：关联解耦协作3D多对象跟踪
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Function-Structured Reinforcement Learning with Executable Verifiers for Mathematical Reasoning](https://arxiv.org/abs/2610.01729)
中文标题：使用可执行验证器进行数学推理的功能结构强化学习
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Do MLLM Judges Judge the Edit? Auditing Bias in Image Editing Evaluation with Verified Quality Preservation](https://arxiv.org/abs/2610.01670)
中文标题：传销法官会评判编辑吗？使用经过验证的质量保护来审核图像编辑评估中的偏差
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [PAGER: Partial-to-global Alignment via Geometric and Relational Distillation](https://arxiv.org/abs/2610.01589)
中文标题：寻呼机：通过几何和关系蒸馏的部分到全局对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Evaluating Physical Consistency and Plausibility in Generative Scenario Models for Autonomous Driving](https://arxiv.org/abs/2610.01581)
中文标题：评估自动驾驶生成场景模型中的物理一致性和合理性
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [False Floors: LLM Safety Routing Evaluations Break Under Distribution Shift](https://arxiv.org/abs/2610.01535)
中文标题：错误楼层： LLM安全路由评估在分配班次下中断
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [OpenMTB-Audit: Exposing Over-Refusal and Clinical Expert Perspectives in LLM-Based Molecular Tumor Board Safety Evaluation](https://arxiv.org/abs/2610.01497)
中文标题：OpenMTB-Audit：Exposing Over-Refusal 与 Clinical Expert Perspectives in 基于 LLM 的 Molecular Tumor Board Safety 评测
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [No Model Required: Text Entropy Rate Filtering Mitigates Iterative Fine-Tuning Collapse](https://arxiv.org/abs/2610.01493)
中文标题：无需模型：文本熵率过滤可缓解迭代微调崩溃
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
