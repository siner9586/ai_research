---
title: "让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险、提升代码生成、执行反馈和自动修复能力"
date: "2026-08-06"
target_date: "2026-08-04"
actual_date: "2026-08-04"
fallback_from: ""
lang: "zh"
slug: "2026-08-06-accelerating-dynamic-graph-clustering-on-gpu-architectures"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险、提升代码生成、执行反馈和自动修复能力。"
tags: ["agents", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "safety", "systems", "training", "video-generation", "vision-generation"]
topics: ["agents", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "safety", "systems", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-08-06-accelerating-dynamic-graph-clustering-on-gpu-architectures-sources/"
generated_at: "2026-08-05T22:19:35.579780+00:00"
page_type: "brief"
candidate_count: 503
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Accelerating Dynamic Graph Clustering on GPU Architectures with cuGraph", "How Closely Do LLM Reviews Align with Human Peer Review?", "JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion", "PRISM: Powerful Time Series to Image (TS2I) Representations for Multivariate Anomaly Detection", "SeqLLM: Augmenting LLMs with Behavioral-Sequence Modeling for High-Stakes Decisions at WeChat Pay", "ATLAS: Learning to Recommend Across Unseen Domains"]
featured_paper_urls: ["https://arxiv.org/abs/2608.03695", "https://arxiv.org/abs/2608.03659", "https://arxiv.org/abs/2608.03974", "https://arxiv.org/abs/2608.03926", "https://arxiv.org/abs/2608.03063", "https://arxiv.org/abs/2608.03899"]
featured_paper_titles_zh: ["使用cuGraph加速GPU架构上的动态图形聚类", "法学硕士评审与人类同行评审的紧密程度如何？", "JoyAI-Video-Edit ：使用自回归扩散的实时开放式视频编辑", "PRISM：Powerful Time Series to Image (TS2I) Representations 面向 Multivariate Anomaly Detection", "SeqLLM ：通过行为序列建模增强LLM ，以实现微信支付的高风险决策", "ATLAS ：学习跨看不见的领域推荐"]
---

# 让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险、提升代码生成、执行反馈和自动修复能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险、提升代码生成、执行反馈和自动修复能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Accelerating Dynamic Graph Clustering on GPU Architectures with cuGraph (Nelson Aloysio Reis de Almeida Passos, Emanuele Carlini, Salvatore Trani)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.03695">2608.03695</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.03695">PDF</a></p>

中文标题：使用cuGraph加速GPU架构上的动态图形聚类

信号显示：这项工作通过GPU加速的频谱聚类扩展和最初为静态图设计的基于模块化的算法来解决时间网络中的社区检测。关键词：serving、code、synthetic data、open-source。代码/数据可用性需查看原文确认。

### 2. 识别并缓解模型安全、越狱和对齐风险

<p class="paper-meta-line"><span>How Closely Do LLM Reviews Align with Human Peer Review? (Abraham Camelo-Guerrero, Jairo Diaz-Rodriguez)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.03659">2608.03659</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.03659">PDF</a></p>

中文标题：法学硕士评审与人类同行评审的紧密程度如何？

信号显示：大语言模型（ LLM ）越来越多地用于生成科学评论，但现有的评估很少检查不同的提供商是否在同一受控环境中与会议决策和人工审查优先事项保持一致。关键词：alignment、evaluation、eval、Benchmarks and Evaluation。代码/数据可用性需查看原文确认。

### 3. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion (Yicheng Xiao, Wenxun Dai, Xinran Qin, Lin Song, Maoquan Zhang, Hang Xu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.03974">2608.03974</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.03974">PDF</a></p>

中文标题：JoyAI-Video-Edit ：使用自回归扩散的实时开放式视频编辑

信号显示：实时视频编辑需要使用有限的计算资源进行低延迟因果生成，同时保持源保真度和长期时间一致性。关键词：inference、serving、latency、evaluation。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>PRISM: Powerful Time Series to Image (TS2I) Representations for Multivariate Anomaly Detection (Mateusz Smendowski, Kamil Faber, Piotr Nawrocki, Nathalie Japkowicz, Roberto Corizzo)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.03926">2608.03926</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.03926">PDF</a></p>

中文标题：PRISM：Powerful Time Series to Image (TS2I) Representations 面向 Multivariate Anomaly Detection

信号显示：时间序列异常检测（ TSAD ）是预测性维护、财务和云计算应用的基础，但性能仍然对表示选择敏感，尤其是在多变量设置中。关键词：workflow、rag、evaluation、code。代码/数据可用性需查看原文确认。

### 5. 评测视频生成的时间一致性和运动真实感

<p class="paper-meta-line"><span>SeqLLM: Augmenting LLMs with Behavioral-Sequence Modeling for High-Stakes Decisions at WeChat Pay (Guilin Li, Jiaxing Zhang, Matthias Hwai Yong Tan, Bo Wang, Weiran Huang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.03063">2608.03063</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.03063">PDF</a></p>

中文标题：SeqLLM ：通过行为序列建模增强LLM ，以实现微信支付的高风险决策

信号显示：大型支付平台的商家风险控制每天筛查数千万商家，其中误报损害合法商家，误报使有害活动未被发现。关键词：serving、alignment、benchmark、fine-tuning。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>ATLAS: Learning to Recommend Across Unseen Domains (Pervez Shaik, Prosenjit Biswas, Abhinav Thorat, Ravi Kolla, Niranjan Pedanekar)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.03899">2608.03899</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.03899">PDF</a></p>

中文标题：ATLAS ：学习跨看不见的领域推荐

信号显示：推荐系统仍然受域约束：在一个交互环境中训练的模型通常需要重新训练或目标域适应才能在新目录上运行。关键词：rag、alignment、code、knowledge。代码/数据可用性需查看原文确认。

## 其他值得关注
- [GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks](https://arxiv.org/abs/2608.03764)
中文标题：GDPevo ：评估代理对真实业务任务的自我进化
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous Workspaces](https://arxiv.org/abs/2608.03451)
中文标题：DataSpace：基准ing Data Agents 面向 Verifiable Analytics over Heterogeneous Workspaces
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [MultiCompose: Multi-Concept Personalized Composition with Per-Subject Attribute Binding](https://arxiv.org/abs/2608.03708)
中文标题：MultiCompose ：具有每个受试者属性绑定的多概念个性化组合
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [AI-Assisted Peer Review Across Research Communities: From Reviewer AI Policies to LLM Review Quality](https://arxiv.org/abs/2608.03581)
中文标题：AI-Assisted Peer Review Across Research Communities：来自 Reviewer AI Policies to LLM Review Quality
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Latent Reward Registers for Diffusion Preference Alignment](https://arxiv.org/abs/2608.03929)
中文标题：Latent Reward Registers 面向 Diffusion Preference Alignment
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Risky Business: Measuring The Faithfulness-Safety Tension](https://arxiv.org/abs/2608.03745)
中文标题：风险业务：衡量忠诚-安全紧张关系
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Shielding for Higher-Order Safety](https://arxiv.org/abs/2608.03662)
中文标题：高阶安全屏蔽
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Policy Fragmentation or Institutional Alignment? Institutional Governance of AI in Universities and Business Schools](https://arxiv.org/abs/2608.03584)
中文标题：Policy Fragmentation or Institutional Alignment? Institutional Governance of AI in Universities 与 Business Schools
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Can LLM design high-quality experiments? A Comprehensive and Systematic Benchmark on Autonomous Experimental Design](https://arxiv.org/abs/2608.03501)
中文标题：Can LLM design high-quality experiments? A Comprehensive 与 Systematic 基准 on Autonomous Experimental Design
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Solver-Aware Decompositions for Programming-by-Example: When Dividing Requires Knowing how to Conquer](https://arxiv.org/abs/2608.03461)
中文标题：通过示例编程的求解感知分解：当划分需要知道如何征服时
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Balancing Efficiency and Efficacy: Training-Free Attention-Guided Switching Between Explicit and Latent Thoughts for MLLMs](https://arxiv.org/abs/2608.03450)
中文标题：平衡效率和功效：培训-无需注意-在传销的明确和潜在思想之间引导切换
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Test-Time Scaling for Safe Text-Guided Image Generation via Intermediate Clean Estimates](https://arxiv.org/abs/2608.03284)
中文标题：通过中间清洁估算安全生成文本引导图像的测试时间缩放
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [TaskPress: Query-Agnostic KV Cache Compression via Task-Guided Pruning](https://arxiv.org/abs/2608.03276)
中文标题：TaskPress ：通过任务引导修剪进行与查询无关的KV缓存压缩
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CIGTSurv: Clinical Information Guided Tri-modal Survival Prediction with Local Prototype Association and Global Feature Alignment](https://arxiv.org/abs/2608.03247)
中文标题：CIGTSurv ：与当地原型协会和全球特征一致的临床信息引导的三峰生存预测
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Channel-wise Dynamic Knowledge Distillation via Adaptive Sample Generation for Action Recognition](https://arxiv.org/abs/2608.03100)
中文标题：通过自适应样本生成进行动作识别的渠道式动态知识蒸馏
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [CAPE-T2V: Captioner-Anchored Prompt Enhancement toward Two-Sided Conditioning Alignment in Text-to-Video Generation](https://arxiv.org/abs/2608.03046)
中文标题：CAPE-T2V：Captioner-Anchored Prompt Enhancement 面向 Two-Sided Conditioning Alignment in Text-to-Video Generation
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Clinically-Grounded Hierarchical Classification for Consistent Chest X-ray Interpretation](https://arxiv.org/abs/2608.03016)
中文标题：基于临床的分层分类以实现一致的胸部X射线解读
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [SparSEEty: Extracting Tokens from Sparsity-Exploiting LLM Serving Systems via Deterministic Side Channels](https://arxiv.org/abs/2608.02995)
中文标题：SparSEEty ：通过确定性侧通道从稀疏性利用LLM服务系统提取代币
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs](https://arxiv.org/abs/2608.04010)
中文标题：ParVL：Parallel Scaling 与 Expandable Compute Allocation 面向 Multimodal LLMs
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning](https://arxiv.org/abs/2608.04007)
中文标题：TurnSight：Turn-Level Hindsight Self-Distillation 面向 Tool-Integrated Reasoning
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
