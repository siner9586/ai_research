---
title: "改进图像生成、视觉理解和可控渲染、提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性"
date: "2026-10-14"
target_date: "2026-10-12"
actual_date: "2026-10-09"
fallback_from: "2026-10-12"
lang: "zh"
slug: "2026-10-14-x-avdd-cross-attentive-audio-visual-dataset"
summary: "今天主要跟进：改进图像生成、视觉理解和可控渲染、提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性。"
tags: ["agents", "data-engineering", "evaluation", "rag", "training", "video-generation"]
topics: ["agents", "data-engineering", "evaluation", "rag", "training", "video-generation"]
sources_page: "/zh/daily/2026-10-14-x-avdd-cross-attentive-audio-visual-dataset-sources/"
generated_at: "2026-10-13T16:50:15.300733+00:00"
page_type: "brief"
candidate_count: 532
featured_count: 6
mentions_count: 20
featured_paper_titles: ["X-AVDD: Cross-Attentive Audio-Visual Dataset Distillation", "Not All Dimensions Are Equal: Outlier-Aware Attention Linearization with Grouped Quadratic Kernels", "TabReliBench: Evaluating Tabular Foundation Models Beyond Predictive Accuracy", "APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces", "RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation", "ELMA: Benchmarking Anaphoric Compositions for Long-Term Text-to-Motion Generation"]
featured_paper_urls: ["https://arxiv.org/abs/2610.13687", "https://arxiv.org/abs/2610.13674", "https://arxiv.org/abs/2610.13654", "https://arxiv.org/abs/2610.13623", "https://arxiv.org/abs/2610.13578", "https://arxiv.org/abs/2610.13549"]
featured_paper_titles_zh: ["X-AVDD ：交叉注意视听数据集蒸馏", "并非所有维度都相等：使用分组二次核进行离群感知注意线性化", "TabReliBench ：评估超越预测准确性的表格基础模型", "APEX-Harm ：评估代理在共享专业工作场所的安全性", "RARA：Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment 面向 Robotic Manipulation", "ELMA：基准ing Anaphoric Compositions 面向 Long-Term Text-to-Motion Generation"]
---

# 改进图像生成、视觉理解和可控渲染、提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：改进图像生成、视觉理解和可控渲染、提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 改进图像生成、视觉理解和可控渲染

<p class="paper-meta-line"><span>X-AVDD: Cross-Attentive Audio-Visual Dataset Distillation (Saumyaranjan Mohanty, Aravind Reddy, Konda Reddy Mopuri)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.13687">2610.13687</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.13687">PDF</a></p>

中文标题：X-AVDD ：交叉注意视听数据集蒸馏

信号显示：视听数据集提取旨在从大型配对视听数据集合成小数据集，同时几乎保留了神经网络的训练实用程序。关键词：serving、alignment、synthetic data、memory。代码/数据可用性需查看原文确认。

### 2. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Not All Dimensions Are Equal: Outlier-Aware Attention Linearization with Grouped Quadratic Kernels (Weiqi Sun, Qianyue Wu, Wenjia Wang, Tianyang Hu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.13674">2610.13674</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.13674">PDF</a></p>

中文标题：并非所有维度都相等：使用分组二次核进行离群感知注意线性化

信号显示：线性化softmax注意力为高效的变压器推理提供了一条途径，但保留预先训练的注意力仍然具有挑战性。关键词：inference、serving、evaluation、code。代码/数据可用性需查看原文确认。

### 3. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>TabReliBench: Evaluating Tabular Foundation Models Beyond Predictive Accuracy (Tianqi Zhao, Jia Guo, Yan Shuo Tan, Qiong Zhang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.13654">2610.13654</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.13654">PDF</a></p>

中文标题：TabReliBench ：评估超越预测准确性的表格基础模型

信号显示：表格基础模型（ TFM ）因其强大的预测性能而越来越受欢迎。关键词：rag、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces (Ziyi Yang, Adel Bibi, Guohao Li, Bernard Ghanem, Carlos Hinojosa)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.13623">2610.13623</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.13623">PDF</a></p>

中文标题：APEX-Harm ：评估代理在共享专业工作场所的安全性

信号显示：专业代理越来越多地通过命令行界面和多个工具在包含文件、消息和业务应用程序的共享工作区上工作。关键词：agent、rag、safety、benchmark。代码/数据可用性需查看原文确认。

### 5. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation (Xuhui Kang, Sung-Wook Lee, Yan Zhuang, Tianle Zhong, Yen-Ling Kuo)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.13578">2610.13578</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.13578">PDF</a></p>

中文标题：RARA：Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment 面向 Robotic Manipulation

信号显示：预先训练的机器人策略，如视觉-语言-行动（ VLA ）模型，为通才机器人操纵提供了坚实的基础，但仅通过少数演示就使它们适应新任务仍然具有挑战性。关键词：rag、retrieval、serving、alignment。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>ELMA: Benchmarking Anaphoric Compositions for Long-Term Text-to-Motion Generation (Shun Kato, Dixin Yang, Kotaro Amaya, Yuiga Wada, Kazumi Fukuda, Takashi Shibuya, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.13549">2610.13549</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.13549">PDF</a></p>

中文标题：ELMA：基准ing Anaphoric Compositions 面向 Long-Term Text-to-Motion Generation

信号显示：文本引导的长期人体运动生成对于持续运行数字头像等应用至关重要。关键词：rag、alignment、benchmark、data。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics](https://arxiv.org/abs/2610.13522)
中文标题：超越成功的机器人演示：从人机交互和失败动态建模中学习
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Proactive Agentic Orchestration](https://arxiv.org/abs/2610.13485)
中文标题：主动代理编排
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Rollout-Time Intervention: Unlocking Agentic Reinforcement Learning Beyond Policy Limits](https://arxiv.org/abs/2610.13438)
中文标题：推出时间干预：超越政策限制解锁客服强化学习
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [PPG-Bench: A Unified Benchmark for PPG Foundation Models](https://arxiv.org/abs/2610.13435)
中文标题：PPG-Bench：A Unified 基准 面向 PPG Foundation Models
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [ManeuverFlow: Maneuver Hypothesis Generation with Future Evidence for Trajectory Evaluation and Refinement in End-to-End Autonomous Driving](https://arxiv.org/abs/2610.13409)
中文标题：ManeuverFlow ：基于未来证据的机动假设生成，用于端到端自动驾驶中的轨迹评估和优化
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Towards the Roof of the World: NLP Progress in Tibetan Languages](https://arxiv.org/abs/2610.13398)
中文标题：迈向世界屋脊：藏语NLP进展
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Test-Time Memory Construction](https://arxiv.org/abs/2610.13348)
中文标题：测试时内存构造
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents](https://arxiv.org/abs/2610.13335)
中文标题：AgentTune：A Unified Training Lifecycle 面向 Tool-使用 LLM Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Masked Diffusion Language Agents for Tool-Integrated Chemical Reasoning](https://arxiv.org/abs/2610.13330)
中文标题：Masked Diffusion Language Agents 面向 Tool-Integrated Chemical Reasoning
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [CoVA: Composing VAE Representations for Generative Learning](https://arxiv.org/abs/2610.13322)
中文标题：CoVA：Composing VAE Representations 面向 Generative Learning
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [PAGE: Parts-Aware Guidance for Co-Speech Gesture Portrait Video Generation](https://arxiv.org/abs/2610.13301)
中文标题：页面：共语手势肖像视频生成的零件感知指南
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ConClick: Element-Wise Contrastive Learning Improves GUI Grounding](https://arxiv.org/abs/2610.13268)
中文标题：ConClick：Element-Wise Contrastive Learning Improves GUI 落地
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents](https://arxiv.org/abs/2610.13267)
中文标题：遗忘并不总是坏事：中毒LLM代理的神经激发记忆修复机制
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [CAST: Credit Alignment for Cross-Tokenizer On-Policy Distillation](https://arxiv.org/abs/2610.13257)
中文标题：CAST：Credit Alignment 面向 Cross-Tokenizer On-Policy Distillation
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [FPD-Drive: Future Policy Distillation for End-to-End Autonomous Driving](https://arxiv.org/abs/2610.13232)
中文标题：FPD-Drive：Future Policy Distillation 面向 End-to-End Autonomous Driving
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Multi-Modal Graph Neural Network-Inspired Vessel Identification and Tracking for UAV-Based Maritime Surveillance](https://arxiv.org/abs/2610.13220)
中文标题：用于无人机海上监视的多模态图神经网络启发式船舶识别和跟踪
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [SharP: Soft and Hard Prompt-Guided Augmentation with LLM for Low Resource Fake News Detection](https://arxiv.org/abs/2610.13207)
中文标题：SharP ： LLM的软硬提示引导增强，用于低资源假新闻检测
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Fix the Match, Not the Solver: STITCH -- a Self-Supervised Compatibility Measure for Eroded Visual Puzzles](https://arxiv.org/abs/2610.13176)
中文标题：Fix the Match，Not the Solver：STITCH -- a Self-Supervised Compatibility Measure 面向 Eroded Visual Puzzles
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SOAR: Source-Aware Reinforcement Learning with Precise Credit Assignment for Search Agents](https://arxiv.org/abs/2610.13157)
中文标题：SOAR ：源感知强化学习，为搜索代理提供精确的学分分配
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [From Glance to Focus: Mitigating Recognition Laziness in MLLMs for Fine-Grained Recognition](https://arxiv.org/abs/2610.13154)
中文标题：从一瞥到专注：缓解传销中的识别懒惰，实现细粒度识别
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
