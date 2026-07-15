---
title: "让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力"
date: "2026-07-16"
target_date: "2026-07-14"
actual_date: "2026-07-14"
fallback_from: ""
lang: "zh"
slug: "2026-07-16-can-llms-write-reliable-rubrics-a-meta"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力。"
tags: ["agents", "evaluation", "interpretability", "multimodal", "rag", "systems", "training", "video-generation", "vision-generation"]
topics: ["agents", "evaluation", "interpretability", "multimodal", "rag", "systems", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-07-16-can-llms-write-reliable-rubrics-a-meta-sources/"
generated_at: "2026-07-15T22:11:50.796755+00:00"
page_type: "brief"
candidate_count: 307
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Can LLMs Write Reliable Rubrics? A Meta-Evaluation for Experiment Reproduction", "Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference", "Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?", "Label-Decoupled Style Augmentation for Domain Generalization in Multi-Label Remote Sensing Scene Classification", "Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution", "LARAD: Layout-Aware Road Anomaly Detection via Spatial-Logic Reasoning"]
featured_paper_urls: ["https://arxiv.org/abs/2607.12835", "https://arxiv.org/abs/2607.12659", "https://arxiv.org/abs/2607.12787", "https://arxiv.org/abs/2607.12704", "https://arxiv.org/abs/2607.13034", "https://arxiv.org/abs/2607.12858"]
featured_paper_titles_zh: ["LLM可以撰写可靠的评分细则表吗？实验重现的元评估", "Jetson-PI ：通过Foresight-Aligned异步推理实现机载实时机器人控制", "我们真的需要大于1B参数的多模态情感语言模型吗？", "多标签遥感场景分类中域泛化的标签解耦样式增强", "Do AI Agents Know When a Task Is Simple? 面向 Complexity-Aware Reasoning 与 Execution", "LARAD ：通过空间逻辑推理进行布局感知道路异常检测"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Can LLMs Write Reliable Rubrics? A Meta-Evaluation for Experiment Reproduction (Hanhua Hong, Yizhi Li, Jiaoyan Chen, Luu Gia Huy, Sophia Ananiadou, Jung-jae Kim, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.12835">2607.12835</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.12835">PDF</a></p>

中文标题：LLM可以撰写可靠的评分细则表吗？实验重现的元评估

信号显示：基于评分的评估是评估基于LLM的研究代理的开放式产出的一种有前途的方法，特别是在纸张复制中，纸张与存储库的直接比较容易产生幻觉。关键词：agent、alignment、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 2. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference (Zebin Yang, Qi Wang, Yunhe Wang, Xiurui Guo, Bo Yu, Shaoshan Liu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.12659">2607.12659</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.12659">PDF</a></p>

中文标题：Jetson-PI ：通过Foresight-Aligned异步推理实现机载实时机器人控制

信号显示：视觉-语言-行动（ VLA ）模型在多样化的具体任务中取得了令人印象深刻的性能。关键词：rag、inference、deployment、latency。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters? (Kaiwen Zheng, Junchen Fu, Wenhao Deng, Hu Han, Joemon M. Jose, Xuri Ge)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.12787">2607.12787</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.12787">PDF</a></p>

中文标题：我们真的需要大于1B参数的多模态情感语言模型吗？

信号显示：多模态大语言模型（ MLLM ）的最新进展显著提高了多模态情感识别（ MER ）的性能，并通过联合建模视频、音频和语言等实现了可解释的描述生成。关键词：inference、deployment、alignment、benchmark。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Label-Decoupled Style Augmentation for Domain Generalization in Multi-Label Remote Sensing Scene Classification (Alaa Almouradi, Erchan Aptoula)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.12704">2607.12704</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.12704">PDF</a></p>

中文标题：多标签遥感场景分类中域泛化的标签解耦样式增强

信号显示：多标签分类为每个空中场景分配多个同时出现的标签，但部署的模型通常会遇到不同于其训练的数据分布。关键词：rag、inference、benchmark、code。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution (Junjie Yin, Xinyu Feng)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.13034">2607.13034</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.13034">PDF</a></p>

中文标题：Do AI Agents Know When a Task Is Simple? 面向 Complexity-Aware Reasoning 与 Execution

信号显示：大语言模型（ LLM ）代理越来越多地自动化多步骤工程和信息学工作流程，但他们很少询问任务实际需要多少工作量。关键词：agent、workflow、retrieval、benchmark。代码/数据可用性需查看原文确认。

### 6. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>LARAD: Layout-Aware Road Anomaly Detection via Spatial-Logic Reasoning (Shiyi Mu, Xujie Chen, Shugong Xu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.12858">2607.12858</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.12858">PDF</a></p>

中文标题：LARAD ：通过空间逻辑推理进行布局感知道路异常检测

信号显示：准确的开放世界障碍物检测对于自动驾驶至关重要。关键词：inference、latency、training、rl。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227)
中文标题：重新思考智能体线束演进的评估
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Decouple and Reason: Anatomically Guided Two-Stage Voxel-Level Grounding of Free-Text Findings in 3D Chest CT](https://arxiv.org/abs/2607.12602)
中文标题：解耦和原因：三维胸部CT中自由文本发现的解剖学引导两阶段体素水平接地
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Lightweight Multi-Scale Anomaly Detection for Resource-Constrained Edge Devices](https://arxiv.org/abs/2607.12599)
中文标题：资源受限边缘设备的轻量级多尺度异常检测
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [StratMamba: Strategic and Reactive Stream Partitioning for Path-Efficient LiDAR-Based Obstacle Avoidance](https://arxiv.org/abs/2607.12370)
中文标题：StratMamba：Strategic 与 Reactive Stream Partitioning 面向 Path-Efficient LiDAR-Based Obstacle Avoidance
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale](https://arxiv.org/abs/2607.13028)
中文标题：TerraZero：Procedural Driving Simulation 面向 Zero-Demonstration Self-Play 的大规模方法
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [PalmClaw: A Native On-Device Agent Framework for Mobile Phones](https://arxiv.org/abs/2607.13027)
中文标题：PalmClaw：A Native On-Device Agent 框架 面向 Mobile Phones
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [DermDepth: Toward Monocular Metric Scale 3D Reconstruction Models for Dermatology](https://arxiv.org/abs/2607.13010)
中文标题：DermDepth：面向 Monocular Metric Scale 3D Reconstruction Models 面向 Dermatology
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [ViHoRec: A Quality-Controlled Vietnamese Hotel Recommendation Dataset and Cold-Start Benchmark](https://arxiv.org/abs/2607.12946)
中文标题：ViHoRec：A Quality-Controlled Vietnamese Hotel Recommendation Dataset 与 Cold-Start 基准
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Open-KNEAD: Knowledge-grounded Nutrition Estimation via Agentic Decomposition](https://arxiv.org/abs/2607.12911)
中文标题：Open-KNEAD ：通过代理分解进行基于知识的营养估算
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [UniMedSeg: Unified In-Context Learning for Multi-Paradigm 2D/3D Medical Image Segmentation](https://arxiv.org/abs/2607.12896)
中文标题：UniMedSeg：Unified In-Context Learning 面向 Multi-Paradigm 2D/3D Medical Image Segmentation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Inhibited Self-Attention: Sharpening Focus in Vision Transformers](https://arxiv.org/abs/2607.12881)
中文标题：抑制自我注意力：在视觉变压器中锐化焦点
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Verifier-Based Reinforcement Fine-Tuning of Reasoning Models for Thermal Energy Storage Control](https://arxiv.org/abs/2607.12856)
中文标题：基于验证器的热能存储控制推理模型的强化微调
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Breaking Déjà Vu: Independent Auditing of Visual Place Recognition through Vision-Language Reasoning](https://arxiv.org/abs/2607.12818)
中文标题：突破似曾相识：通过视觉语言推理对视觉场所识别进行独立审计
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Silent Alarm: A J-Space Protocol for Comparing Danger Recognition Across Models and Quantization Levels](https://arxiv.org/abs/2607.12792)
中文标题：无声警报：用于比较模型和量化级别的危险识别的J空间协议
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents](https://arxiv.org/abs/2607.12790)
中文标题：谁给评分员评分？自我完善的LLM专员的共同进化评估指标和技能
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [CoRe: A Comprehensive Framework for Cross-Image Comparative Reasoning in Vision-Language Models](https://arxiv.org/abs/2607.12786)
中文标题：CoRe：A Comprehensive 框架 面向 Cross-Image Comparative Reasoning in Vision-Language Models
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Directional Constraints for Efficient Exploration in Safe Reinforcement Learning](https://arxiv.org/abs/2607.12784)
中文标题：安全强化学习中有效探索的方向性约束
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Constraint-Aware Aggregation for Federated Reinforcement Learning in Microgrid Energy Coordination](https://arxiv.org/abs/2607.12763)
中文标题：微电网能源协调中用于联合强化学习的约束感知聚合
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [RFMSR: Residual Flow Matching for Image Super-Resolution](https://arxiv.org/abs/2607.12753)
中文标题：RFMSR：Residual Flow Matching 面向 Image Super-Resolution
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Epistemic Stance Flexibility Probing: Measuring Prompt-Conditioned Register Shift in Large Language Models](https://arxiv.org/abs/2607.12739)
中文标题：认知姿态灵活性探测：测量大型语言模型中的提示条件寄存器偏移
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
