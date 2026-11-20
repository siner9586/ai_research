---
title: "提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性"
date: "2026-11-21"
target_date: "2026-11-19"
actual_date: "2026-11-19"
fallback_from: ""
lang: "zh"
slug: "2026-11-21-beyond-alignment-whitening-geometry-profile-synthesis-and"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "data-engineering", "evaluation", "multimodal", "rag", "robotics", "safety", "systems", "training", "video-generation"]
topics: ["agents", "data-engineering", "evaluation", "multimodal", "rag", "robotics", "safety", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-11-21-beyond-alignment-whitening-geometry-profile-synthesis-and-sources/"
generated_at: "2026-11-20T16:46:50.998448+00:00"
page_type: "brief"
candidate_count: 586
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Beyond Alignment: Whitening Geometry, Profile Synthesis, and Heterogeneous Ensembles for Cross-Environment WiFi Action Recognition", "Seer: Guiding Small Deep-Research Agents with Shared Decision Models", "Rubric Semantics or Numerical Priors? Auditing Scale-Direction Bias in LLM Judges", "Active Feature Acquisition by Distilling an Oracle Teacher", "TuringPAI: A Foundation for On-Device Physical AI", "LocoMuJoCo: A Comprehensive Imitation Learning Benchmark for Whole-Body Control"]
featured_paper_urls: ["https://arxiv.org/abs/2611.25831", "https://arxiv.org/abs/2611.26423", "https://arxiv.org/abs/2611.25588", "https://arxiv.org/abs/2611.26598", "https://arxiv.org/abs/2611.25474", "https://arxiv.org/abs/2611.26293"]
featured_paper_titles_zh: ["Beyond Alignment：Whitening Geometry，Profile Synthesis，与 Heterogeneous Ensembles 面向 Cross-Environment WiFi Action Recognition", "Seer：使用共享决策模型指导小型深度研究代理", "评分细则语义还是数值先验？审核大语言模型评判者的量表方向性偏见", "通过蒸馏 Oracle 教师进行主动特征采集", "TuringPAI：A Foundation 面向 On-Device Physical AI", "LocoMuJoCo：A Comprehensive Imitation Learning 基准 面向 Whole-Body Control"]
---

# 提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Beyond Alignment: Whitening Geometry, Profile Synthesis, and Heterogeneous Ensembles for Cross-Environment WiFi Action Recognition (Lei Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.25831">2611.25831</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.25831">PDF</a></p>

中文标题：Beyond Alignment：Whitening Geometry，Profile Synthesis，与 Heterogeneous Ensembles 面向 Cross-Environment WiFi Action Recognition

信号显示：跨环境部署是实用型 WiFi 感知的核心障碍：在训练环境中达到 0.89+ 的 top-1 管道，在仅使用 K-shot 标签的留一域交叉验证 (LODO) 评估中降至 0.408。关键词：deployment、alignment、evaluation、code。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Seer: Guiding Small Deep-Research Agents with Shared Decision Models (Yuhao Zhou, Yang Zhou, Yuanxi Li, Jindi Lv, Dan Si, Qing Ye, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.26423">2611.26423</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.26423">PDF</a></p>

中文标题：Seer：使用共享决策模型指导小型深度研究代理

信号显示：深度研究代理反复决定要搜索、阅读和核实的内容，通常使用大型云托管语言模型来提出行动建议。关键词：agent、rag、inference、evaluation。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Rubric Semantics or Numerical Priors? Auditing Scale-Direction Bias in LLM Judges (Chanwoo Kim, Doyun Kim, Minsoo Song, Sihyeon Lee, Chanjun Park)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.25588">2611.25588</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.25588">PDF</a></p>

中文标题：评分细则语义还是数值先验？审核大语言模型评判者的量表方向性偏见

信号显示：最近的基准评估越来越依赖于将大语言模型（LLM）作为自动评判工具。关键词：rag、alignment、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 4. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Active Feature Acquisition by Distilling an Oracle Teacher (Yang Meng, Zixin Ding, Robert L. Grossman, Yuxin Chen)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.26598">2611.26598</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.26598">PDF</a></p>

中文标题：通过蒸馏 Oracle 教师进行主动特征采集

信号显示：获取实例的每个特征通常成本高昂：一项测量可能需要付出金钱、时间或隐私成本。关键词：deployment、benchmark、multimodal、training。代码/数据可用性需查看原文确认。

### 5. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>TuringPAI: A Foundation for On-Device Physical AI (Qiman Wu, Hanlin Chen, Yuhua Wei, Mingyuan Wang, Shaman Tang, Minghao Li, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.25474">2611.25474</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.25474">PDF</a></p>

中文标题：TuringPAI：A Foundation 面向 On-Device Physical AI

信号显示：物理 AI 需要能够理解空间关系和动态环境的模型，并在有限的机载计算能力下将观察结果转化为行动。关键词：rag、evaluation、multimodal、vision-language。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>LocoMuJoCo: A Comprehensive Imitation Learning Benchmark for Whole-Body Control (Firas Al-Hafez, Davide Tateo, Oleg Kaidanov, Aditya Bhatt, Artur Zelik, Zhengyi Luo, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.26293">2611.26293</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.26293">PDF</a></p>

中文标题：LocoMuJoCo：A Comprehensive Imitation Learning 基准 面向 Whole-Body Control

信号显示：LocoMuJoCo 是一个开源基准，用于全身控制的模仿学习 (IL) 和强化学习 (RL)。关键词：deployment、benchmark、open-source、data。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Parameter-Efficient Adaptation of Self-supervised Vision Backbones Survives Distribution Shift in Radar Micro-Doppler HAR](https://arxiv.org/abs/2611.25874)
中文标题：自监督视觉主干的参数高效适配在雷达微多普勒HAR中经受住了分布偏移的考验
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [AdaptReg: Skip-level FiLM Adapter for Task-Specific Adaptation of a Frozen Registration Foundation Model](https://arxiv.org/abs/2611.25761)
中文标题：AdaptReg：Skip-level FiLM Adapter 面向 Task-Specific Adaptation of a Frozen Registration Foundation Model
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents](https://arxiv.org/abs/2611.25583)
中文标题：DriftGuard：通过因果归因实现对大语言模型（LLM）代理的在线记忆漂移检测
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control](https://arxiv.org/abs/2611.26613)
中文标题：AgentRoboCritic：了解前沿智能体在直接机器人控制方面的能力
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Asuka-FM: A System-Architectural Co-Design Framework for Efficient Text-to-Image Pretraining on Consumer Hardware](https://arxiv.org/abs/2611.26437)
中文标题：Asuka-FM：A System-Architectural Co-Design 框架 面向 Efficient Text-to-Image Pretraining on Consumer Hardware
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Mamba Flow Matching Neural Processes: Linear-Time Inference for Irregularly Observed Spatial Fields](https://arxiv.org/abs/2611.26355)
中文标题：Mamba 流匹配神经过程：对不规则观测空间场的线性时间推理
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency](https://arxiv.org/abs/2611.26040)
中文标题：Streaming-AAA：Streaming AAA Game Video Generation at High Resolution，High Frame Rate，与 Low Latency
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Safe Subgame Resolving in Multiplayer Games](https://arxiv.org/abs/2611.25981)
中文标题：多人游戏中安全的子博弈求解
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Disentangling Monitor Hardware Artifacts and Smoothing Lag for Shift-Robust Intraoperative EEG and Hemodynamic Risk Calibration](https://arxiv.org/abs/2611.25765)
中文标题：分离监测硬件伪影并平滑延迟，以实现对术中EEG和血流动力学风险的稳健校准
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Trajectory-Calibrated Merging of Embodied Policies](https://arxiv.org/abs/2611.25575)
中文标题：基于轨迹校准的具身策略融合
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [DRVEXO-4B-Unified: Design and Evaluation of a Modular Speech-Vision System](https://arxiv.org/abs/2611.25521)
中文标题：DRVEXO-4B-Unified：Design 与 评测 of a Modular Speech-Vision System
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [CANDOR: Contrastive Self-Denoising Rewards for Label-Free Text-to-Image Post-Training](https://arxiv.org/abs/2611.25457)
中文标题：CANDOR：Contrastive Self-Denoising Rewards 面向 Label-Free Text-to-Image Post-Training
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Probing the "Conscious" Mind: Selective Access and Global Workspace in Vision-Language Models](https://arxiv.org/abs/2611.26590)
中文标题：探究“有意识”的心智：视觉-语言模型中的选择性访问和全局工作空间
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Text-Aware, Vision-Blind: How Multimodal Image Editing Systems Handle Unsafe Inputs](https://arxiv.org/abs/2611.26569)
中文标题：文本感知、视觉盲区：多模态图像编辑系统如何处理不安全输入
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Learning to Defer under Expert Drift](https://arxiv.org/abs/2611.26440)
中文标题：在专家漂移下学会推迟
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2611.26438)
中文标题：面向视觉-语言-行动模型的风险受控测试时自适应
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning](https://arxiv.org/abs/2611.26380)
中文标题：EgoCaptioner：Towards Comprehensive 与 Fine-Grained Egocentric Video Captioning
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Beam Model Technical Report](https://arxiv.org/abs/2611.26358)
中文标题：梁模型技术报告
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [DeepQuest: From Knowledge Gaps to Scientific Discovery in Alzheimer's Disease](https://arxiv.org/abs/2611.26343)
中文标题：DeepQuest：来自 Knowledge Gaps to Scientific Discovery in Alzheimer's Disease
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Scalable fault vulnerability analysis for ReRAM-based process-in-memory CNN accelerators](https://arxiv.org/abs/2611.26307)
中文标题：可扩展 fault vulnerability analysis 面向 ReRAM-based process-in-memory CNN accelerators
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
