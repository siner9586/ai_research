---
title: "提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能"
date: "2026-09-18"
target_date: "2026-09-16"
actual_date: "2026-09-16"
fallback_from: ""
lang: "zh"
slug: "2026-09-18-a-zeroth-order-paradigm-for-llm-preference"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "reasoning", "training", "video-generation", "vision-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "reasoning", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-09-18-a-zeroth-order-paradigm-for-llm-preference-sources/"
generated_at: "2026-09-17T23:32:57.441213+00:00"
page_type: "brief"
candidate_count: 431
featured_count: 6
mentions_count: 20
featured_paper_titles: ["A Zeroth-Order Paradigm for LLM Preference Alignment", "PULSE: Unlocking Practical Image Compression on Single-Thread CPU", "Collective Loss of Control in LLM Agent Systems: An Epidemic Account of Mutation, Contagion, and Recovery", "WetRobo: A Reproducible Robot Kit for Coding Agents in Biological Laboratories", "FIVE-VLA: Fast and EffectIVE Autonomous Driving with Recurrent Action Memory", "Risk-Aware World Modeling with Flow-Guided Occupancy Evolution for Selective Trajectory Planning in Automated Driving"]
featured_paper_urls: ["https://arxiv.org/abs/2609.19144", "https://arxiv.org/abs/2609.18602", "https://arxiv.org/abs/2609.18460", "https://arxiv.org/abs/2609.18435", "https://arxiv.org/abs/2609.18623", "https://arxiv.org/abs/2609.18442"]
featured_paper_titles_zh: ["LLM偏好调整的零次序范例", "脉冲：在单线程CPU上解锁实用图像压缩", "Collective Loss of Control in LLM Agent Systems：An Epidemic Account of Mutation，Contagion，与 Recovery", "WetRobo：A Reproducible Robot Kit 面向 Coding Agents in Biological Laboratories", "FIVE-VLA ：具有循环动作记忆的快速有效的自动驾驶", "用于自动驾驶中选择性轨迹规划的流程引导占用进化风险感知世界建模"]
---

# 提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>A Zeroth-Order Paradigm for LLM Preference Alignment (Peter Chen, Xi Chen, Wotao Yin, Tianyi Lin)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.19144">2609.19144</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.19144">PDF</a></p>

中文标题：LLM偏好调整的零次序范例

信号显示：直接偏好对齐方法因其计算和内存效率而被广泛用于将大语言模型（ LLM ）与人类偏好对齐。关键词：rag、alignment、fine-tuning、memory。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>PULSE: Unlocking Practical Image Compression on Single-Thread CPU (Zhaoyang Jia, Tianyu Zhang, Zihan Zheng, Wenxuan Xie, Jiahao Li, Bin Li, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.18602">2609.18602</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.18602">PDF</a></p>

中文标题：脉冲：在单线程CPU上解锁实用图像压缩

信号显示：尽管最近在学习图像压缩方面取得了进展，但现有方法在资源受限的硬件上仍然计算昂贵，特别是CPU。关键词：agent、latency、compression、code。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Collective Loss of Control in LLM Agent Systems: An Epidemic Account of Mutation, Contagion, and Recovery (Xiangfan Wu, Zonghao Ying, Huiyu Wu, Xing Zheng, Huangsheng Cheng, Xiaorong Shi, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.18460">2609.18460</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.18460">PDF</a></p>

中文标题：Collective Loss of Control in LLM Agent Systems：An Epidemic Account of Mutation，Contagion，与 Recovery

信号显示：多智能体系统如何从局部偏差演变为集体失控？。关键词：agent、deployment、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>WetRobo: A Reproducible Robot Kit for Coding Agents in Biological Laboratories (Yuna Oikawa, Kei Endo, Takanori Uzawa, Yunzhe Zhang, Manan Anjaria, Lerrel Pinto, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.18435">2609.18435</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.18435">PDF</a></p>

中文标题：WetRobo：A Reproducible Robot Kit 面向 Coding Agents in Biological Laboratories

信号显示：自动化生物研究需要通用、可重复的机器人系统，允许个人湿实验室研究人员委派机器人任务，而无需执行远程操作或神经网络训练。关键词：agent、code、vision-language、robotics。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>FIVE-VLA: Fast and EffectIVE Autonomous Driving with Recurrent Action Memory (Kemal Oksuz, Alexandru Buburuzan, Yuhan Yao, Puneet K. Dokania)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.18623">2609.18623</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.18623">PDF</a></p>

中文标题：FIVE-VLA ：具有循环动作记忆的快速有效的自动驾驶

信号显示：最先进的自动驾驶视觉-语言-动作模型（ VLA ）面临严重限制：参数计数过多，高分辨率图像处理效率低下，以及缺乏时间内存。关键词：benchmark、code、vision-language、memory。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Risk-Aware World Modeling with Flow-Guided Occupancy Evolution for Selective Trajectory Planning in Automated Driving (Rongxiang Zeng, Linsen Cai, Jiafu Zhang, Yijie Zhong, Yide Tao, Shuai Wang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.18442">2609.18442</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.18442">PDF</a></p>

中文标题：用于自动驾驶中选择性轨迹规划的流程引导占用进化风险感知世界建模

信号显示：自动驾驶的安全运动规划需要预测不断变化的交通风险，并决定何时修改当前的计划轨迹。关键词：rag、evaluation、temporal、motion。代码/数据可用性需查看原文确认。

## 其他值得关注
- [CapMap-MS-TTA: 3rd Place Solution for the MUMU Track of the 8th LSVOS Challenge at ECCV 2026](https://arxiv.org/abs/2609.18206)
中文标题：CapMap-MS-TTA ： ECCV 2026第八届LSVOS挑战赛MUMU赛道第三名解决方案
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [OmniRisk: Omnidirectional Trajectory-Risk Learning for Agile Quadrotor Dynamic Avoidance](https://arxiv.org/abs/2609.18191)
中文标题：OmniRisk：Omnidirectional Trajectory-Risk Learning 面向 Agile Quadrotor Dynamic Avoidance
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Can MiniMax-H3 Reason About the Physical World? An Evaluation of Omni-Modal Generative Model](https://arxiv.org/abs/2609.18323)
中文标题：MiniMax-H3能否解释物理世界的原因？全模态生成模型的评估
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Visual Autoregressive Priors for RAW-to-sRGB Image Signal Processing](https://arxiv.org/abs/2609.18302)
中文标题：Visual Autoregressive Priors 面向 RAW-to-sRGB Image Signal Processing
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [BENCHCOMPASS: From Scores to Signals for Training and Harness Decisions in Payment-Domain LLMs](https://arxiv.org/abs/2609.18270)
中文标题：BENCHCOMPASS：来自 Scores to Signals 面向 Training 与 Harness Decisions in Payment-Domain LLMs
关注理由：涉及数据工程中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [WAVE-Go: World-Model Navigation with Adaptive Execution for Wheel-Legged Robots](https://arxiv.org/abs/2609.18193)
中文标题：WAVE-Go ：适用于轮腿机器人的自适应执行世界模型导航
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Ask the Tool, Don't Guess: Agent Tool Calls Hold Their Progress, and the Serving System Should Read It](https://arxiv.org/abs/2609.18849)
中文标题：询问工具，不要猜测：客服代表工具呼叫会保留他们的进度，服务系统应该读取它
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SURF: Subtractive Updates for Recommender Forgetting](https://arxiv.org/abs/2609.18695)
中文标题：SURF：Subtractive Updates 面向 Recommender Forgetting
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [RankGround: Efficient High-Resolution GUI Grounding via Lightweight Reranker-Guided Crop Selection](https://arxiv.org/abs/2609.18690)
中文标题：RankGround ：通过轻量级Reranker引导的作物选择实现高效的高分辨率GUI接地
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Reasoning through Evolution: Automatic Meta-path Discovery for LLM-based Fake News Detection](https://arxiv.org/abs/2609.18597)
中文标题：通过演进进行推理：基于LLM的虚假新闻检测的自动元路径发现
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Hardware-Free Robotics Laboratories in Mixed Reality](https://arxiv.org/abs/2609.18434)
中文标题：混合现实中的无硬件机器人实验室
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Occluded Gait Recognition with Mixture of Experts: An Action Detection Perspective](https://arxiv.org/abs/2609.18432)
中文标题：混合专家的闭塞步态识别：行动检测视角
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [HiLNO: A Hierarchical Latent Neural Operator with Multi-Scale Supervision for PDEs on General Geometries](https://arxiv.org/abs/2609.18419)
中文标题：HiLNO ：对一般几何体上的PDE进行多尺度监控的分层潜伏神经算子
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Where Should Agents Live? Energy-Memory Characterization of Agentic AI for the Edge-Cloud Continuum](https://arxiv.org/abs/2609.18283)
中文标题：客服代表应该住在哪里？用于边缘云连续体的智能AI的能量-记忆表征
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [I code or AI code: A comparative evaluation of AI-rated scores in classroom observations](https://arxiv.org/abs/2609.18274)
中文标题：I代码或AI代码：课堂观察中AI评级分数的比较评估
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [${M}^2$Tok: Multi-head Multi-codebook Discrete Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2609.18259)
中文标题：${M}^2$Tok：Multi-head Multi-codebook Discrete Action Tokenization 面向 视觉-语言-动作模型
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [CPR: Combining global composing, local performing and full-sequence refining in piano rendering with continuous autoregressive modelling](https://arxiv.org/abs/2609.18216)
中文标题：CPR ：将钢琴渲染中的全局构图、本地表演和全序列精炼与连续自回归建模相结合
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Colla-Q: Toward Collaborative Experts in MoE Quantization via Minimax Precision Balancing](https://arxiv.org/abs/2609.18131)
中文标题：Colla-Q ：通过Minimax Precision Balancing面向教育部量化方面的协作专家
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Designing Agentic AI Workflow Portfolios under Imperfect Selection and Compute Cost](https://arxiv.org/abs/2609.18126)
中文标题：Designing Agentic AI Workflow Portfolios under Imperfect Selection 与 Compute Cost
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Aligned Consensus Teaching for Label-Efficient Oriented Object Detection in Weakly-Aligned Visible-Infrared Imagery](https://arxiv.org/abs/2609.18124)
中文标题：弱对齐可见红外图像中面向目标的标签效率对齐共识教学
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
