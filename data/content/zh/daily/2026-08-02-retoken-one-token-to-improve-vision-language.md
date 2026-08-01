---
title: "提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力"
date: "2026-08-02"
target_date: "2026-07-31"
actual_date: "2026-07-30"
fallback_from: "2026-07-31"
lang: "zh"
slug: "2026-08-02-retoken-one-token-to-improve-vision-language"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "safety", "speech-audio", "training", "video-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "safety", "speech-audio", "training", "video-generation"]
sources_page: "/zh/daily/2026-08-02-retoken-one-token-to-improve-vision-language-sources/"
generated_at: "2026-08-01T22:07:59.615650+00:00"
page_type: "brief"
candidate_count: 469
featured_count: 6
mentions_count: 20
featured_paper_titles: ["ReToken: One Token to Improve Vision-Language Models for Visual Retrieval", "OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models", "Inducing language models to assert their own consciousness restores human beliefs and values", "SVR: Self-Verifying Refinement via Joint Verdict-Confidence Reinforcement Learning for Adaptive Test-Time Compute", "ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics Representations from a Video and Its Shadow", "HARGO: Heterogeneity-Aware Reward-Guided Optimization for RL Post-Training of LLMs on HPC Tasks"]
featured_paper_urls: ["https://arxiv.org/abs/2607.28627", "https://arxiv.org/abs/2607.28609", "https://arxiv.org/abs/2607.28607", "https://arxiv.org/abs/2607.28457", "https://arxiv.org/abs/2607.28362", "https://arxiv.org/abs/2607.28301"]
featured_paper_titles_zh: ["ReToken：One Token to Improve Vision-Language Models 面向 Visual Retrieval", "OSReward：Instituting Standardized 评测 面向 Cross-平台 Computer-Use Reward Models", "引入语言模型来维护自己的意识，恢复人类的信仰和价值观", "SVR ：通过联合判决-信心强化学习进行自适应测试时间计算的自我验证细化", "ShadowDancer：Teaching Video 世界模型 Any Action by Learning Unified Dynamics Representations 来自 a Video 与 Its Shadow", "HARGO：Heterogeneity-Aware Reward-Guided Optimization 面向 RL Post-Training of LLMs on HPC Tasks"]
---

# 提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>ReToken: One Token to Improve Vision-Language Models for Visual Retrieval (Yao Xiao, Reuben Tan, Zhen Zhu, Yuqun Wu, Jianfeng Gao, Derek Hoiem)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.28627">2607.28627</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.28627">PDF</a></p>

中文标题：ReToken：One Token to Improve Vision-Language Models 面向 Visual Retrieval

信号显示：长时间的视觉上下文给视觉语言模型带来了挑战：性能会随着干扰源数量的增加而下降，并且在GPU内存限制下，一次处理所有令牌在计算上是不可行的。关键词：retrieval、inference、benchmark、code。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models (Qiushi Sun, Kanzhi Cheng, Yian Wang, Bowen Yang, Hang Yan, Liheng Chen, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.28609">2607.28609</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.28609">PDF</a></p>

中文标题：OSReward：Instituting Standardized 评测 面向 Cross-平台 Computer-Use Reward Models

信号显示：使用计算机的代理（ CUA ）正在数字世界中迅速发展。关键词：agent、alignment、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Inducing language models to assert their own consciousness restores human beliefs and values (Junsol Kim, Winnie Street, Roberta Rocca, Diane M. Korngiebel, Adam Waytz, James Evans, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.28607">2607.28607</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.28607">PDF</a></p>

中文标题：引入语言模型来维护自己的意识，恢复人类的信仰和价值观

信号显示：调整大语言模型以防止他们将意识归因于自己，无意中改变了他们在其他实体中与人类信仰和价值观一起的思想表征。关键词：alignment、safety、fine-tuning、harmful。代码/数据可用性需查看原文确认。

### 4. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>SVR: Self-Verifying Refinement via Joint Verdict-Confidence Reinforcement Learning for Adaptive Test-Time Compute (Hongyu Chen, Liang Lin, Guangrun Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.28457">2607.28457</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.28457">PDF</a></p>

中文标题：SVR ：通过联合判决-信心强化学习进行自适应测试时间计算的自我验证细化

信号显示：缩放测试时间计算可以改进语言模型推理，但统一的预算浪费了简单输入的计算，而验证者引导的细化依赖于外部反馈。关键词：rag、inference、benchmark、reasoning。代码/数据可用性需查看原文确认。

### 5. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics Representations from a Video and Its Shadow (Jin Cao, Zian Meng, Kaipeng Zhang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.28362">2607.28362</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.28362">PDF</a></p>

中文标题：ShadowDancer：Teaching Video 世界模型 Any Action by Learning Unified Dynamics Representations 来自 a Video 与 Its Shadow

信号显示：我们展示了ShadowDancer ，这是一种对交互式视频世界模型进行任意动作、帧级控制的新方法。关键词：rag、code、fine-tuning、video。代码/数据可用性需查看原文确认。

### 6. 识别并缓解模型安全、越狱和对齐风险

<p class="paper-meta-line"><span>HARGO: Heterogeneity-Aware Reward-Guided Optimization for RL Post-Training of LLMs on HPC Tasks (Tiangang Li, Xiangbo Tian)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.28301">2607.28301</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.28301">PDF</a></p>

中文标题：HARGO：Heterogeneity-Aware Reward-Guided Optimization 面向 RL Post-Training of LLMs on HPC Tasks

信号显示：监督微调（ SFT ）可以为大语言模型（ LLM ）提供高性能计算（ HPC ）任务的领域知识，例如数据竞赛检测和基准问答。关键词：alignment、benchmark、fine-tuning、post-training。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Oracle-Budgeted Molecular Optimization with Short-Term Graph Memory](https://arxiv.org/abs/2607.28437)
中文标题：使用短期图形内存的Oracle预算分子优化
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Hand-Object Interaction in the Age of Large Foundation Models:Reconstruction, Generation, and Embodied Transfer](https://arxiv.org/abs/2607.28394)
中文标题：大型基础模型时代的手对象交互：重建、生成和具体化转移
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Structural Validation of LLM-Generated Microservice Decompositions Using Source-Code Dependencies](https://arxiv.org/abs/2607.28331)
中文标题：使用源代码依赖项对LLM生成的微服务分解进行结构验证
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Theia: Large-Scale Multimodal Captioning and Automated Validation of the Incidents1M Dataset for Data-Free Distillation](https://arxiv.org/abs/2607.28269)
中文标题：THEIA ：用于无数据蒸馏的大规模多模式字幕和自动验证Incidents1M数据集
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Understanding Is Done Early: A Depth Division of Labor in Large Language Models and Its Use for Unbounded-Context Memory](https://arxiv.org/abs/2607.28263)
中文标题：早期理解：大型语言模型的深度分工及其对无限上下文记忆的使用
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CDAE: Enhancing Perturbation Robustness in Pretrained Language Models with Contrastive Denoising](https://arxiv.org/abs/2607.28236)
中文标题：CDAE ：使用对比去噪增强预训练语言模型中的扰动鲁棒性
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [EMBL AI Librarian: Life-Sciences Knowledge Layer for AI Agents](https://arxiv.org/abs/2607.28229)
中文标题：EMBL AI Librarian：Life-Sciences Knowledge Layer 面向 AI Agents
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Security of World-Model-Based Embodied AI: A Lifecycle of Threats, Defenses, and Evaluation](https://arxiv.org/abs/2607.28226)
中文标题：Security of World-Model-Based Embodied AI：A Lifecycle of Threats，Defenses，与 评测
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [FaithEyes: Towards Faithful Tool Use via Multi-Agent Process-Image Verification](https://arxiv.org/abs/2607.28225)
中文标题：FAIthEyes ：通过多代理流程实现忠实工具使用-图像验证
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Scaling Vision-Language Models Is Not Enough to Mitigate Bias](https://arxiv.org/abs/2607.28211)
中文标题：扩展视觉语言模型不足以减轻偏见
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Old Tricks, New Models: How Simple Image Transformations Break Modern AI-based Content Moderation](https://arxiv.org/abs/2607.28187)
中文标题：老技巧，新模型：简单的图像转换如何破坏基于人工智能的现代内容审核
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [AgenticASR: Refining Speech Recognition in Real-World Scenarios via an Agentic Approach](https://arxiv.org/abs/2607.28175)
中文标题：AgenticASR ：通过Agentic方法在真实场景中改进语音识别
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Can Agents Deceive? Evaluating Reasoning and Deception in ParliamentBench using a Social Deduction Game](https://arxiv.org/abs/2607.28146)
中文标题：Can Agents Deceive? Evaluating Reasoning 与 Deception in ParliamentBench 使用 a Social Deduction Game
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [LM-GRASP: Instance-Specific Language Models for Combinatorial Construction via Online Imitation Learning](https://arxiv.org/abs/2607.28135)
中文标题：LM-GRASP ：通过在线模拟学习进行组合构造的实例特定语言模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ConMem: Contribution-Aware Memory for Long-Horizon Manufacturing Inspection Logs](https://arxiv.org/abs/2607.28126)
中文标题：ConMem：Contribution-Aware Memory 面向 Long-Horizon Manufacturing Inspection Logs
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Temporal Concentration from Rollout Errors: Implicit Preference Optimization for Text-to-Video Diffusion](https://arxiv.org/abs/2607.28058)
中文标题：Temporal Concentration 来自 Rollout Errors：Implicit Preference Optimization 面向 Text-to-Video Diffusion
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [VIG-RL: Learning to Search and Insert for Verified Image Grounding](https://arxiv.org/abs/2607.28055)
中文标题：VIG-RL：Learning to Search 与 Insert 面向 Verified Image 落地
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [RaDiVe: Robust 4D Radar Odometry with Distance-Bounded NDT and Velocity-Discrepancy Point Uncertainty](https://arxiv.org/abs/2607.28045)
中文标题：RaDiVe ：具有距离限制无损检测和速度差异点不确定性的强大4D雷达里程测量
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ClawTrack: Towards Trace-Level Evaluation and Improvement of Real-World Autonomous Agents](https://arxiv.org/abs/2607.28037)
中文标题：ClawTrack：Towards Trace-Level 评测 与 Improvement of Real-World Autonomous Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [MMLDSum-LLM: Multimodal Long-Document Summarization with Visual-Alignment and Keyword-Aware](https://arxiv.org/abs/2607.28006)
中文标题：MMLDSum-LLM ：使用视觉对齐和关键词感知的多模态长文档摘要
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
