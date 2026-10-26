---
title: "提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力"
date: "2026-10-27"
target_date: "2026-10-25"
actual_date: "2026-10-23"
fallback_from: "2026-10-25"
lang: "zh"
slug: "2026-10-27-personalquery-benchmark-evaluating-retrieval-robustness-to-personalized"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力。"
tags: ["agents", "evaluation", "multimodal", "rag", "reasoning", "systems", "training", "video-generation"]
topics: ["agents", "evaluation", "multimodal", "rag", "reasoning", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-10-27-personalquery-benchmark-evaluating-retrieval-robustness-to-personalized-sources/"
generated_at: "2026-10-26T16:45:11.133736+00:00"
page_type: "brief"
candidate_count: 427
featured_count: 6
mentions_count: 20
featured_paper_titles: ["PersonalQuery-Benchmark:Evaluating Retrieval Robustness to Personalized User Expression Differences", "TGR-EvoDAG: A DAG-based Multi-Agent Code Evolution Framework for Generative Recommendation on Tencent", "RxnExBench: Benchmarking Vision-Language Models for Structured Chemical Reaction Extraction from Scientific Literature", "Flownomaly: Single-Step Conditional-Mean Recovery for Few-Shot Anomaly Detection", "Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery", "On the Identifiability of Hybrid Deep Generative Models: Meta-Learning as a Solution"]
featured_paper_urls: ["https://arxiv.org/abs/2610.32164", "https://arxiv.org/abs/2610.32326", "https://arxiv.org/abs/2610.32221", "https://arxiv.org/abs/2610.32964", "https://arxiv.org/abs/2610.32866", "https://arxiv.org/abs/2610.32748"]
featured_paper_titles_zh: ["PersonalQuery-基准：Evaluating Retrieval Robustness to Personalized User Expression Differences", "TGR-EvoDAG：A DAG-based Multi-Agent Code Evolution 框架 面向 Generative Recommendation on Tencent", "RxnExBench：基准ing Vision-Language Models 面向 Structured Chemical Reaction 抽取 来自 Scientific Literature", "Flownomaly：Single-Step Conditional-Mean Recovery 面向 Few-Shot Anomaly Detection", "使用TopKLoRA进行可解释的稀疏微调，实现忠实的电路发现", "论混合深度生成模型的可识别性：元学习作为一种解决方案"]
---

# 提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>PersonalQuery-Benchmark:Evaluating Retrieval Robustness to Personalized User Expression Differences (Wenyu Liang, Hongzhi Yin, Tongtong Wu, Fan Liu, Kexin Dai, Weiqing Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.32164">2610.32164</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.32164">PDF</a></p>

中文标题：PersonalQuery-基准：Evaluating Retrieval Robustness to Personalized User Expression Differences

信号显示：现有的个性化信息检索方法主要通过用户偏好和查询意图来模拟用户需求的差异，而很少关注不同用户表达相同检索时出现的个性化表达差异。关键词：retrieval、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>TGR-EvoDAG: A DAG-based Multi-Agent Code Evolution Framework for Generative Recommendation on Tencent (Junlin He, Junzhang Zhu, Yudong Li, Yihong Tang, Xuefeng Jiang, Wei Ma, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.32326">2610.32326</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.32326">PDF</a></p>

中文标题：TGR-EvoDAG：A DAG-based Multi-Agent Code Evolution 框架 面向 Generative Recommendation on Tencent

信号显示：大语言模型(LLM)代理已启用算法发现的自动代码演化。关键词：agent、deployment、alignment、evaluation。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>RxnExBench: Benchmarking Vision-Language Models for Structured Chemical Reaction Extraction from Scientific Literature (Jiaxing Sun, Junyuan Gao, Ruikang Zhang, Hao Zheng, Lingli Ge, Xiao An, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.32221">2610.32221</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.32221">PDF</a></p>

中文标题：RxnExBench：基准ing Vision-Language Models 面向 Structured Chemical Reaction 抽取 来自 Scientific Literature

信号显示：筛选表和底物范围是合成化学文献中广泛使用的信息密集型数字，但从中自动提取结构化反应数据仍然具有挑战性。关键词：evaluation、benchmark、code、multimodal。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Flownomaly: Single-Step Conditional-Mean Recovery for Few-Shot Anomaly Detection (Bernardo Perrone Ribeiro, Erkut Akdag, Egor Bondarev)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.32964">2610.32964</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.32964">PDF</a></p>

中文标题：Flownomaly：Single-Step Conditional-Mean Recovery 面向 Few-Shot Anomaly Detection

信号显示：少量工业异常检测仅需要从少数无缺陷图像中对特定类别的正态性进行建模。关键词：inference、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery (Marek Masiak, Andrzej Szablewski, Nicola Cancedda, Constantin Venhoff)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.32866">2610.32866</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.32866">PDF</a></p>

中文标题：使用TopKLoRA进行可解释的稀疏微调，实现忠实的电路发现

信号显示：当数据包括中毒示例时，对来源未知的数据集进行微调可以在训练模型中创建后门。关键词：agent、safety、code、fine-tuning。代码/数据可用性需查看原文确认。

### 6. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>On the Identifiability of Hybrid Deep Generative Models: Meta-Learning as a Solution (Yubo Ye, Maryam Toloubidokhti, Sumeet Vadhavkar, Xiajun Jiang, Huafeng Liu, Linwei Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.32748">2610.32748</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.32748">PDF</a></p>

中文标题：论混合深度生成模型的可识别性：元学习作为一种解决方案

信号显示：在深度学习中利用基于物理的归纳偏差的兴趣导致了混合深度生成模型（ hybrid-DGMs ）的最新发展，该模型将已知的基于物理的数学表达式集成到神经生成模型中。关键词：rag、benchmark、code、math。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Can LLM Annotators Match Human Consistency? Benchmarking Human Agreement and Optimizing Multi-Agent with Contrastive Knowledge](https://arxiv.org/abs/2610.32415)
中文标题：Can LLM Annotators Match Human Consistency? 基准ing Human Agreement 与 Optimizing Multi-Agent with Contrastive Knowledge
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Guided Zero-Shot Anomaly Explanation for Anonymized Crowd Video Monitoring: Context, Categorization, and Spatial Localization](https://arxiv.org/abs/2610.32073)
中文标题：匿名人群视频监控的引导式零拍摄异常解释：上下文、分类和空间定位
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Concept Acupuncturist: An Efficient and Precise Concept Erasure Method for Diffusion Models via Sparse Autoencoders](https://arxiv.org/abs/2610.32059)
中文标题：概念针灸师：通过稀疏自动编码器实现扩散模型的高效精确概念擦除方法
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents](https://arxiv.org/abs/2610.32752)
中文标题：ActionRAG：Evidence-Refining Graph Diffusion 面向 Long-Term Memory in LLM Agents
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [InferSlice: A Reference Architecture for SLO-driven LLM Inference over a Telco Wide-Area Network](https://arxiv.org/abs/2610.32638)
中文标题：InferSlice：A Reference Architecture 面向 SLO-driven LLM Inference over a Telco Wide-Area Network
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance](https://arxiv.org/abs/2610.32555)
中文标题：在现实MCP故障下调用LLM代理的工具：规模不购买容错
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Efficient Zero-Shot Video Anomaly Detection via Signal-Aware Adaptive Fusion (SAAF)](https://arxiv.org/abs/2610.32486)
中文标题：通过信号感知自适应融合（ SAAF ）进行有效的零拍摄视频异常检测
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [An Error Budget for Shuffled Multimodal Windows in the 3rd WEAR Challenge: Stacking, Count Constraints and Seam Matching](https://arxiv.org/abs/2610.32398)
中文标题：第3次磨损挑战中洗牌多式联运窗口的错误预算：堆叠、计数约束和接缝匹配
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [DynaSlots: Slot-Centric 3D Dynamics Pretraining for Robot Manipulation](https://arxiv.org/abs/2610.32330)
中文标题：DynaSlots：Slot-Centric 3D Dynamics Pretraining 面向 Robot Manipulation
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Organizing Temporal Evidence in Hyperbolic Space for Video Moment Retrieval](https://arxiv.org/abs/2610.32317)
中文标题：在双曲空间中组织时间证据进行视频矩检索
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Correct but Unselectable: The Hidden Interface Tax in Multi-Candidate Reasoning](https://arxiv.org/abs/2610.32235)
中文标题：正确但不可选：多候选人推理中的隐性界面税
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [The LLENS Platform for On-Premises Large Language Model Agents in a Japanese University Hospital: Development and Evaluation Study](https://arxiv.org/abs/2610.32151)
中文标题：LLENS 平台 面向 On-Premises Large Language Model Agents in a Japanese University Hospital：Development 与 评测 Study
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms](https://arxiv.org/abs/2610.32971)
中文标题：RobustRLlib：A Unified Library 与 基准 面向 Robust Reinforcement Learning Algorithms
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Closing the Modality Gap via Simplex-Constrained Representations](https://arxiv.org/abs/2610.32890)
中文标题：通过单纯形约束表示缩小模态差距
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [When Human Corrections Travel: Safety in Federated VLA Adaptation](https://arxiv.org/abs/2610.32888)
中文标题：人体矫正旅行时：联邦VLA适应中的安全
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [SPOOK: Sparse Pixel Optimization for Off-Manifold Knowledge in Vision Encoders](https://arxiv.org/abs/2610.32835)
中文标题：SPOOK：Sparse Pixel Optimization 面向 Off-Manifold Knowledge in Vision Encoders
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Cross-Architectural Feature Fusion for Coronary Artery Stenosis Detection in X-ray Angiography](https://arxiv.org/abs/2610.32730)
中文标题：X线血管造影中冠状动脉狭窄检测的跨建筑特征融合
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Are Textual Residuals Truly Complementary? Learning Visual Complements under Semantic Superposition for Visible-Infrared Person Re-Identification](https://arxiv.org/abs/2610.32709)
中文标题：文本残差真的是互补的吗？可见红外人物再识别语义叠加下的学习视觉补充
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SP-Guide: Enhancing Aerial Vision-Language Navigation with Spatial Priors](https://arxiv.org/abs/2610.32697)
中文标题：SP-Guide ：与空间先验者一起增强空中视觉语言导航
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [DriveOSS: Dataset and Benchmark for 3D Anomaly Segmentation and Open-set Semantic Segmentation in Autonomous Driving](https://arxiv.org/abs/2610.32612)
中文标题：DriveOSS：Dataset 与 基准 面向 3D Anomaly Segmentation 与 Open-set Semantic Segmentation in Autonomous Driving
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
