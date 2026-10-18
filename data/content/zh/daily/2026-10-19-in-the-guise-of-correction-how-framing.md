---
title: "提升代码生成、执行反馈和自动修复能力、增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-10-19"
target_date: "2026-10-17"
actual_date: "2026-10-15"
fallback_from: "2026-10-17"
lang: "zh"
slug: "2026-10-19-in-the-guise-of-correction-how-framing"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "robotics", "safety", "systems", "training"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "robotics", "safety", "systems", "training"]
sources_page: "/zh/daily/2026-10-19-in-the-guise-of-correction-how-framing-sources/"
generated_at: "2026-10-18T23:05:13.746318+00:00"
page_type: "brief"
candidate_count: 611
featured_count: 6
mentions_count: 20
featured_paper_titles: ["In the Guise of Correction: How Framing and Cultural Adaptation Erode LLM Safety on Real-World Criminal Cases", "FusionAudit: Pathway-Conditioned Robustness Auditing for Native Multimodal Models", "Data World: Scaling Data Environments from Scratch", "A Decision-Aware Evaluation Protocol for Uncertainty in Medical Image Segmentation", "AVALON: Zero-Shot Indoor Navigation with Human-Seeded Topological Memory", "Poison Valleys: Diagnosing Path-Dependent Failure in LLM Code Repair"]
featured_paper_urls: ["https://arxiv.org/abs/2610.21789", "https://arxiv.org/abs/2610.21667", "https://arxiv.org/abs/2610.21656", "https://arxiv.org/abs/2610.21616", "https://arxiv.org/abs/2610.21586", "https://arxiv.org/abs/2610.21514"]
featured_paper_titles_zh: ["在更正的幌子下：框架和文化适应如何在现实世界的刑事案件中侵蚀法学硕士的安全", "FusionAudit：Pathway-Conditioned Robustness Auditing 面向 Native Multimodal Models", "数据世界：从头开始扩展数据环境", "一种医学图像分割不确定性的决策评估方法", "AVALON ：带有人工种子拓扑记忆的零拍室内导航", "Poison Valleys ：诊断LLM代码修复中的路径依赖性故障"]
---

# 提升代码生成、执行反馈和自动修复能力、增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>In the Guise of Correction: How Framing and Cultural Adaptation Erode LLM Safety on Real-World Criminal Cases (Mohsinul Kabir, Md. Tariquzzaman, Karam S. R. Elradie, Polydoros Giannouris, Yuechen Jiang, Shaoxiong Ji, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.21789">2610.21789</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.21789">PDF</a></p>

中文标题：在更正的幌子下：框架和文化适应如何在现实世界的刑事案件中侵蚀法学硕士的安全

信号显示：现有的安全基准在很大程度上依赖于具有松散分类法的合成提示，对严重犯罪类别几乎没有提供重点分析。关键词：alignment、safety、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 2. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>FusionAudit: Pathway-Conditioned Robustness Auditing for Native Multimodal Models (Jiaming Zhang, Zherui Li, Siqi Guo, Junhao Dong, Kun Wang, Wei Yang Bryan Lim)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.21667">2610.21667</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.21667">PDF</a></p>

中文标题：FusionAudit：Pathway-Conditioned Robustness Auditing 面向 Native Multimodal Models

信号显示：随着视觉语言模型（ VLM ）从冻结编码器管道过渡到原生多模态架构，视觉通道越来越多地充当感知输入和渲染文本的载体，与用户提示竞争。关键词：evaluation、benchmark、code、multimodal。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Data World: Scaling Data Environments from Scratch (Zhanli Li, Zeyuan Xu, Chaoxu Pang, Zeyuan Liu, Anyang Ji, Te Sun, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.21656">2610.21656</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.21656">PDF</a></p>

中文标题：数据世界：从头开始扩展数据环境

信号显示：数据代理使用代码处理异构文件并获得分析见解。关键词：agent、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>A Decision-Aware Evaluation Protocol for Uncertainty in Medical Image Segmentation (Saket Maganti, Shreyank N Gowda)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.21616">2610.21616</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.21616">PDF</a></p>

中文标题：一种医学图像分割不确定性的决策评估方法

信号显示：医学分割不确定性通常通过校准误差或像素级误差检测分数进行评估，但这些指标并未显示不确定性是否改善下游审核决策。关键词：rag、inference、evaluation、code。代码/数据可用性需查看原文确认。

### 5. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>AVALON: Zero-Shot Indoor Navigation with Human-Seeded Topological Memory (Jing Xia, Changyan Li, Yuduo Wang, Guiyin Tian, Bo Wang, Yifan Liao, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.21586">2610.21586</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.21586">PDF</a></p>

中文标题：AVALON ：带有人工种子拓扑记忆的零拍室内导航

信号显示：室内服务机器人经常进入未映射的建筑物，其布局和任务约束已经为用户所熟悉。关键词：rag、deployment、alignment、memory。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Poison Valleys: Diagnosing Path-Dependent Failure in LLM Code Repair (Veljko Skarich)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.21514">2610.21514</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.21514">PDF</a></p>

中文标题：Poison Valleys ：诊断LLM代码修复中的路径依赖性故障

信号显示：当代码修复代理失败时，最终测试显示修补程序是错误的，但不是之前的承诺导致的，也不是软件义务失败。关键词：agent、code、software、repair。代码/数据可用性需查看原文确认。

## 其他值得关注
- [MYOPIA: Understanding the Limits of Tree-Based Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.21573)
中文标题：近视：了解视觉语言模型中基于树的推理的局限性
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [From Perception to Prediction and Intervention: Benchmarking Proactive Video Assistants in Real-Life Scenarios](https://arxiv.org/abs/2610.21568)
中文标题：从感知到预测和干预：对现实场景中的主动视频助理进行基准测试
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Reinforcement Learning-driven Diffusion Models: Language, Vision, and Beyond](https://arxiv.org/abs/2610.21539)
中文标题：Reinforcement Learning-driven Diffusion Models：Language，Vision，与 Beyond
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [OPRD: On-Policy Reminder Distillation for Long-Horizon Coding Agents](https://arxiv.org/abs/2610.21496)
中文标题：OPRD：On-Policy Reminder Distillation 面向 Long-Horizon Coding Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Fault Detection and Bit-Error Rate Diagnostics in Optical Wireless Links Using Edge-AI](https://arxiv.org/abs/2610.21402)
中文标题：Fault Detection 与 Bit-Error Rate Diagnostics in Optical Wireless Links 使用 Edge-AI
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Quantum Versus Classical Machine Learning for Neuropsychiatric Disorders: A Feature-Matched Multi-Cohort Evaluation](https://arxiv.org/abs/2610.21344)
中文标题：神经精神疾病的量子与经典机器学习：特征匹配的多队列评估
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [DocPilot: Interactive Agent Orchestration and Training for Long Visual Document Understanding](https://arxiv.org/abs/2610.21327)
中文标题：DocPilot：Interactive Agent Orchestration 与 Training 面向 Long Visual Document Understanding
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Spectrum Is Not Enough: A Random-Matrix Account of Data-Free Preconditioning for Differentially Private Learning](https://arxiv.org/abs/2610.21312)
中文标题：频谱是不够的：差异私有学习的无数据预处理的随机矩阵帐户
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Combining LLM and Dynamic Analysis for Universal Testing of Static Application Security Testing Tools](https://arxiv.org/abs/2610.21309)
中文标题：将LLM和动态分析相结合，用于静态应用程序安全测试工具的通用测试
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models](https://arxiv.org/abs/2610.21306)
中文标题：VLA-$Δ$：Learning Physical State Transition 面向 视觉-语言-动作模型
关注理由：涉及数据工程中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Bias Control and Injection for Multi-Agent Aggregation](https://arxiv.org/abs/2610.21290)
中文标题：多Agent聚合的偏差控制和注入
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Diviner: Agentic RCA with Human-Governed Adaptation for Large-Scale Infrastructure](https://arxiv.org/abs/2610.21281)
中文标题：占卜师：针对大规模基础设施进行人为管理适应的代理RCA
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Fractional Power-of-Two Quantization for Efficient and Effective Multiplier-Free LLM Inference](https://arxiv.org/abs/2610.21257)
中文标题：有效和无乘数LLM推理的分数幂量化
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [CLIS-MPPI: Closed-Loop Model Predictive Path Integral Control With Initial-State Sampling Under Execution Delay](https://arxiv.org/abs/2610.21239)
中文标题：CLIS-MPPI ：执行延迟下具有初始状态采样的闭环模型预测路径积分控制
关注理由：涉及机器人与具身智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [RecSoup: Efficient Model Merging Approach for Controllable Multi-Objective Recommendation](https://arxiv.org/abs/2610.21220)
中文标题：RecSoup：Efficient Model Merging Approach 面向 Controllable Multi-Objective Recommendation
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [FedSumUp: User-Auditable Privacy-Aware Representation Sharing for Resource-Constrained Federated Intelligence](https://arxiv.org/abs/2610.21194)
中文标题：FedSumUp：User-Auditable Privacy-Aware Representation Sharing 面向 Resource-Constrained Federated Intelligence
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [GRADS: Graph-Regulated Agentic Data Synthesis with Controllable Difficulty](https://arxiv.org/abs/2610.21167)
中文标题：GRADS ：具有可控难度的图形调节代理数据合成
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Stop Training Against Soft Users: Mentalized Adversarial Self-Play for Proactive Dialogue](https://arxiv.org/abs/2610.21156)
中文标题：停止针对软用户的培训：积极对话的心理化对抗性自我游戏
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation](https://arxiv.org/abs/2610.21135)
中文标题：更强大的评委看不到更多： LLM评估中的部署-完整性盲目性
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Noise-Space Reward Alignment for Few-Step Generative Models](https://arxiv.org/abs/2610.21125)
中文标题：几步生成模型的噪声空间奖励对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
