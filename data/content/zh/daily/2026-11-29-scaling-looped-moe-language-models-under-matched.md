---
title: "提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能"
date: "2026-11-29"
target_date: "2026-11-27"
actual_date: "2026-11-25"
fallback_from: "2026-11-27"
lang: "zh"
slug: "2026-11-29-scaling-looped-moe-language-models-under-matched"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "evaluation", "multimodal", "robotics", "systems", "training", "video-generation"]
topics: ["agents", "evaluation", "multimodal", "robotics", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-11-29-scaling-looped-moe-language-models-under-matched-sources/"
generated_at: "2026-11-28T16:05:24.206556+00:00"
page_type: "brief"
candidate_count: 612
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Scaling Looped MoE Language Models under Matched Budgets: Information Flow and Parameter Allocation", "Navigent: A Geometry-Grounded Agentic Framework for Vision Language Navigation", "Variation-aware Temporal Correspondence for Self-Supervised Video Representation Learning", "MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance", "Admoab-DETR: Resolution-Tiered Fusion for Infrared-Visible Object Detection with Missing Modalities", "Understanding Diffusion Acceleration: Methods, Trade-Offs, and Open Questions"]
featured_paper_urls: ["https://arxiv.org/abs/2611.34276", "https://arxiv.org/abs/2611.34249", "https://arxiv.org/abs/2611.34220", "https://arxiv.org/abs/2611.34188", "https://arxiv.org/abs/2611.34163", "https://arxiv.org/abs/2611.34056"]
featured_paper_titles_zh: ["Scaling Looped MoE Language Models under Matched Budgets：Information Flow 与 Parameter Allocation", "Navigent：A Geometry-Grounded Agentic 框架 面向 Vision Language Navigation", "用于自监督视频表征学习的变异感知时序对应", "MINE：通过互信息和嵌入向量方差实现无需训练的间接提示注入防御", "Admoab-DETR：用于存在缺失模态的红外-可见光物体检测的分辨率分层融合", "Understanding Diffusion Acceleration：Methods，Trade-Offs，与 Open Questions"]
---

# 提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Scaling Looped MoE Language Models under Matched Budgets: Information Flow and Parameter Allocation (Shipeng Bai, Jiayu Qin, Hong Liu, Xili Wang, Jianchao Tan, Jiacheng Li, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.34276">2611.34276</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.34276">PDF</a></p>

中文标题：Scaling Looped MoE Language Models under Matched Budgets：Information Flow 与 Parameter Allocation

信号显示：循环式变压器将计算深度与参数数量解耦，先前的研究已表明，随着计算量的增加，性能有望得到提升。关键词：rag、serving、benchmark、code。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Navigent: A Geometry-Grounded Agentic Framework for Vision Language Navigation (Xinyu Zhou, Weiren Cai, Yitong Chen, Shenghai Yuan, Zihang Mu, Boyu Ma, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.34249">2611.34249</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.34249">PDF</a></p>

中文标题：Navigent：A Geometry-Grounded Agentic 框架 面向 Vision Language Navigation

信号显示：采用通用多模态大语言模型（MLLM）的视觉-语言导航（VLN）为特定任务的导航策略提供了一种灵活的替代方案，但可靠的远期执行仍然具有挑战性。关键词：agent、code、multimodal、memory。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Variation-aware Temporal Correspondence for Self-Supervised Video Representation Learning (Yang Liu, Qianqian Xu, Peisong Wen, Siran Dai, Qingming Huang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.34220">2611.34220</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.34220">PDF</a></p>

中文标题：用于自监督视频表征学习的变异感知时序对应

信号显示：通过利用大规模的未标记视频数据，自监督视频表征学习取得了显著进展。关键词：rag、alignment、benchmark、video。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance (Truong Phan, Ngoc-Quan Pham, Dat Quoc Nguyen)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.34188">2611.34188</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.34188">PDF</a></p>

中文标题：MINE：通过互信息和嵌入向量方差实现无需训练的间接提示注入防御

信号显示：针对检索增强生成（RAG）中间接提示注入的现有防御措施本质上是反应性的：提示工程方法通常会被注入的指令所覆盖，而监督式检测器必须针对每次新攻击进行重新训练。关键词：agent、rag、retrieval、inference。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Admoab-DETR: Resolution-Tiered Fusion for Infrared-Visible Object Detection with Missing Modalities (Wenchao Li, Haoran Jia, Shuyuan Wen, Keyan Chen)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.34163">2611.34163</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.34163">PDF</a></p>

中文标题：Admoab-DETR：用于存在缺失模态的红外-可见光物体检测的分辨率分层融合

信号显示：红外图像和可见光图像为全天候目标检测提供了互补的线索，但现实世界中的传感器掉线会导致一个数据流不可用，并使配对输入检测器的性能下降。关键词：inference、latency、benchmark、code。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Understanding Diffusion Acceleration: Methods, Trade-Offs, and Open Questions (Xiaofeng Mao, Fu-yun Wang, Le Zhuo, Zhengkai Jiang, Shaohao Rui, Weijie Ma)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.34056">2611.34056</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.34056">PDF</a></p>

中文标题：Understanding Diffusion Acceleration：Methods，Trade-Offs，与 Open Questions

信号显示：扩散和基于流的生成模型支持高质量的图像、音频和视频合成。关键词：inference、latency、compression、alignment。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Agentic-Level Adversarial Purification: Revisiting Diffusion Purifiers on Native-Resolution Agentic Inputs](https://arxiv.org/abs/2611.34181)
中文标题：代理级别对抗净化：重新审视原生分辨率代理输入的扩散净化器
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Lost in the Grid: Where Multimodal LLMs Fail Between Seeing and Planning](https://arxiv.org/abs/2611.34152)
中文标题：迷失在网格中：多模态大语言模型在“观察”与“规划”之间失灵的原因
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Out of Sight, Not Out of Clues: Can Video LLMs Guess from Partial Evidence?](https://arxiv.org/abs/2611.34126)
中文标题：虽未尽收眼底，却仍有蛛丝马迹：视频大语言模型能否从部分证据中推断出答案？
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Reliable User Simulation in Complex Multi-Step Workflows](https://arxiv.org/abs/2611.34044)
中文标题：在复杂的多步工作流程中进行可靠的用户模拟
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [MoSk: A Unified Motion-Skeleton Foundation Model for Human Motion Understanding and Generation](https://arxiv.org/abs/2611.34022)
中文标题：MoSk：A Unified Motion-Skeleton Foundation Model 面向 Human Motion Understanding 与 Generation
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [geo-eval-harness: An Evaluation Harness for Geospatial Foundation Models](https://arxiv.org/abs/2611.33990)
中文标题：geo-eval-harness：An 评测 Harness 面向 Geospatial Foundation Models
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [BayesPath: Reliability-Aware Bayesian Reasoning for Whole-Slide Pathology Agents](https://arxiv.org/abs/2611.33935)
中文标题：BayesPath：Reliability-Aware Bayesian Reasoning 面向 Whole-Slide Pathology Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures](https://arxiv.org/abs/2611.33925)
中文标题：超越“快乐路径”：从模拟故障中泛化机器人世界模型
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Event-WAM: Learning to Act with Event-Derived Futures](https://arxiv.org/abs/2611.33917)
中文标题：事件-WAM：学会根据事件衍生未来采取行动
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [EATS: Scaling Tool-Use Experience for Medical Reasoning Agents](https://arxiv.org/abs/2611.33897)
中文标题：EATS：Scaling Tool-Use Experience 面向 Medical Reasoning Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Privacy-Aware Adaptive Client Selection for Federated Retrieval-Augmented Generation](https://arxiv.org/abs/2611.33890)
中文标题：面向联邦检索增强生成的隐私感知型自适应客户端选择
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [FORK: Co-Evolving Safe Disclosure and Decision Skills Against Attackers Who Read Every Refusal](https://arxiv.org/abs/2611.33879)
中文标题：分叉：针对阅读每次拒绝的攻击者，共同发展安全披露和决策技能
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [DriftWAM: Faster World-Action Models via Action-Aware Video Drifting](https://arxiv.org/abs/2611.33797)
中文标题：DriftWAM：通过动作感知视频漂移实现更快的世界-动作模型
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Multimodal Safety Evaluation of Vision-Language Models in Japanese](https://arxiv.org/abs/2611.33789)
中文标题：日语视觉-语言模型的多模态安全评估
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [GlassGround: GUI Grounding Beyond Native Screenshots with Egocentric Wearable Vision](https://arxiv.org/abs/2611.33760)
中文标题：GlassGround：通过以自我为中心的穿戴式视觉，将 GUI 截屏提升至超越原生截屏的水平
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [VAPOR: Improving Multimodal Reasoning with Sparse Visual Updates](https://arxiv.org/abs/2611.33751)
中文标题：VAPOR：通过稀疏视觉更新改进多模态推理
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [NORMCRAFT: Cultural Norm Generation for Context-Aware Language Model Alignment](https://arxiv.org/abs/2611.33726)
中文标题：NORMCRAFT：Cultural Norm Generation 面向 Context-Aware Language Model Alignment
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [EVA: Evidence-seeking Visual Agent for Hallucination-Resistant Multimodal Reasoning](https://arxiv.org/abs/2611.33706)
中文标题：EVA：Evidence-seeking Visual Agent 面向 抗幻觉 Multimodal Reasoning
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [MOVR-SAR: A Multi-resolution SAR Registration Dataset under Orbit-crossing and View-variant Imaging Differences](https://arxiv.org/abs/2611.33673)
中文标题：MOVR-SAR：A Multi-resolution SAR Registration Dataset under Orbit-crossing 与 View-variant Imaging Differences
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [The Detour Is the Danger: Preserving Security During LLM Agent Recovery](https://arxiv.org/abs/2611.33605)
中文标题：绕行就是危险：在 LLM 代理恢复过程中保障安全
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
