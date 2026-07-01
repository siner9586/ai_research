---
title: "增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-07-02"
target_date: "2026-06-30"
actual_date: "2026-06-30"
fallback_from: ""
lang: "zh"
slug: "2026-07-02-unicoder-unified-visual-to-code-generation-via"
summary: "今天主要跟进：增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "interpretability", "multimodal", "rag", "robotics", "safety", "systems", "training", "video-generation", "vision-generation"]
topics: ["agents", "code", "evaluation", "interpretability", "multimodal", "rag", "robotics", "safety", "systems", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-07-02-unicoder-unified-visual-to-code-generation-via-sources/"
generated_at: "2026-07-01T22:39:32.271182+00:00"
page_type: "brief"
candidate_count: 453
featured_count: 6
mentions_count: 20
featured_paper_titles: ["UniCoder: Unified Visual-to-Code Generation via Symbolic Rewards and Reference-Guided Code Optimization", "Technical Report of RoboSpatial Challenge at CVPR 2026: Selective Reasoning Activation and Reference-Frame Disambiguation for Embodied Spatial Reasoning", "HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents", "SkillSpotter: Pose-Aware Multi-View Skilled Action Detection and Grading in Ego-Exo Videos", "CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation", "OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation"]
featured_paper_urls: ["https://arxiv.org/abs/2606.31732", "https://arxiv.org/abs/2606.31645", "https://arxiv.org/abs/2606.31179", "https://arxiv.org/abs/2606.31127", "https://arxiv.org/abs/2606.32012", "https://arxiv.org/abs/2606.31993"]
featured_paper_titles_zh: ["UniCoder：Unified Visual-to-Code Generation via Symbolic Rewards 与 Reference-Guided Code Optimization", "Technical Report of RoboSpatial Challenge at CVPR 2026：Selective Reasoning Activation 与 Reference-Frame Disambiguation 面向 Embodied Spatial Reasoning", "HealthAgentBench：A Unified 基准 Suite of Realistic Agentic Healthcare Environments 面向 Challenging Frontier AI Agents", "SkillSpotter：Pose-Aware Multi-View Skilled Action Detection 与 Grading in Ego-Exo Videos", "CoMet：Context 与 Multiplicity Decomposition 面向 Multimodal Uncertainty Estimation", "OopsieVerse：A Safety 基准 with Damage-Aware Simulation 面向 Robot Manipulation"]
---

# 增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：增强多模态模型理解图表和文档的能力、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>UniCoder: Unified Visual-to-Code Generation via Symbolic Rewards and Reference-Guided Code Optimization (Yaozhi Zheng, Yilei Jiang, Manyuan Zhang, Yuxuan Wan, Kaituo Feng, Tianshuo Peng, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.31732">2606.31732</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.31732">PDF</a></p>

中文标题：UniCoder：Unified Visual-to-Code Generation via Symbolic Rewards 与 Reference-Guided Code Optimization

信号显示：Visual-to-Code generation, which transforms scientific plots, vector graphics, and webpages into executable scripts, demands a level of pixel-precise alignment that standard Multimodal 大语言模型 (MLLMs) fail to achieve through Supervised Fine-Tunin。关键词：alignment、benchmark、code、multimodal。代码/数据可用性需查看原文确认。

### 2. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Technical Report of RoboSpatial Challenge at CVPR 2026: Selective Reasoning Activation and Reference-Frame Disambiguation for Embodied Spatial Reasoning (Yuxiang Xie, Qi Lv, Jianming Xing, Zijian Hong, Xiang Deng, Weili Guan, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.31645">2606.31645</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.31645">PDF</a></p>

中文标题：Technical Report of RoboSpatial Challenge at CVPR 2026：Selective Reasoning Activation 与 Reference-Frame Disambiguation 面向 Embodied Spatial Reasoning

信号显示：该研究围绕题名与摘要所揭示的问题展开，具体信号需结合原文进一步核验：Vision-language models achieve strong general perception but often struggle with the spatial reasoning required for embodied tasks。关键词：inference、code、vision-language、fine-tuning。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents (Qianchu Liu, Sheng Zhang, Guanghui Qin, Jeya Maria Jose Valanarasu, Maximilian Rokuss, Mingyu Lu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.31179">2606.31179</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.31179">PDF</a></p>

中文标题：HealthAgentBench：A Unified 基准 Suite of Realistic Agentic Healthcare Environments 面向 Challenging Frontier AI Agents

信号显示：该研究围绕题名与摘要所揭示的问题展开，具体信号需结合原文进一步核验：As AI agents become increasingly capable of complex, long-horizon reasoning, rigorous and holistic evaluation is essential for measuring progress toward real-world healthcare applications。关键词：agent、workflow、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>SkillSpotter: Pose-Aware Multi-View Skilled Action Detection and Grading in Ego-Exo Videos (Björn Braun, Christian Holz)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.31127">2606.31127</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.31127">PDF</a></p>

中文标题：SkillSpotter：Pose-Aware Multi-View Skilled Action Detection 与 Grading in Ego-Exo Videos

信号显示：该研究围绕题名与摘要所揭示的问题展开，具体信号需结合原文进一步核验：To enable personalized, real-time coaching using Augmented Reality glasses or fixed camera setups in domains such as sports, cooking, or music, a system must understand not just what a person does, but how well they execute an activity。关键词：rag、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 5. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation (Sanghyuk Chun, William Yang, Amaya Dharmasiri, Olga Russakovsky)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.32012">2606.32012</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.32012">PDF</a></p>

中文标题：CoMet：Context 与 Multiplicity Decomposition 面向 Multimodal Uncertainty Estimation

信号显示：该研究围绕题名与摘要所揭示的问题展开，具体信号需结合原文进一步核验：Uncertainty estimation has been a long-standing challenge in AI models; it amounts to "knowing what you don't know," and metacognition is notoriously difficult even for humans (cf。关键词：benchmark、code、multimodal、visual。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation (Arnav Balaji, Arpit Bahety, Sriniket Ambatipudi, Daniel Lam, Junhong Xu, Roberto Martín-Martín)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.31993">2606.31993</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.31993">PDF</a></p>

中文标题：OopsieVerse：A Safety 基准 with Damage-Aware Simulation 面向 Robot Manipulation

信号显示：该研究围绕题名与摘要所揭示的问题展开，具体信号需结合原文进一步核验：While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings。关键词：safety、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

## 其他值得关注
- [MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied Environments](https://arxiv.org/abs/2606.31966)
中文标题：MECoBench：A Systematic Study of Multimodal Agent Collaboration in Embodied Environments
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Evo-PI: Aligning Medical Reasoning via Evolving Principle-Guided Supervision](https://arxiv.org/abs/2606.31800)
中文标题：Evo-PI：Aligning Medical Reasoning 通过 Evolving Principle-Guided Supervision
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [FedXDS: Leveraging Model Attribution Methods to counteract Data Heterogeneity in Federated Learning](https://arxiv.org/abs/2606.31742)
中文标题：FedXDS：Leveraging Model Attribution Methods to counteract Data Heterogeneity in Federated Learning
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks](https://arxiv.org/abs/2606.31700)
中文标题：Diffusing Blame：Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Preserve the Hard, Regenerate the Rest: Uncertainty-Guided Synthetic Training Data Augmentation with Diffusion Models](https://arxiv.org/abs/2606.31603)
中文标题：Preserve the Hard，Regenerate the Rest：Uncertainty-Guided Synthetic Training Data Augmentation 结合 Diffusion Models
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [CSTrader: A Testbed for Language-Grounded Trading in a Community-Driven Virtual Asset Market](https://arxiv.org/abs/2606.31461)
中文标题：CSTrader：A Testbed 面向 Language-Grounded Trading in a Community-Driven Virtual Asset Market
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Distilling Temporal Coherence into 2D Networks for Transrectal Ultrasound Prostate Video Segmentation](https://arxiv.org/abs/2606.31198)
中文标题：Distilling Temporal Coherence into 2D Networks 面向 Transrectal Ultrasound Prostate Video Segmentation
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Fleet: Few Shots Lead Effective AI-generated Image Detection](https://arxiv.org/abs/2606.31082)
中文标题：Fleet：Few Shots Lead Effective AI-generated Image Detection
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [ADAPT: Attention Dynamics Alignment with Preference Tuning for Faithful MLLMs](https://arxiv.org/abs/2606.31054)
中文标题：ADAPT：Attention Dynamics Alignment with Preference Tuning 面向 Faithful MLLMs
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Certified Speculative Execution for Untrusted AI Agents](https://arxiv.org/abs/2606.31023)
中文标题：Certified Speculative Execution 面向 Untrusted AI Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [GEAR: Guided End-to-End AutoRegression for Image Synthesis](https://arxiv.org/abs/2606.32039)
中文标题：GEAR：Guided End-to-End AutoRegression 面向 Image Synthesis
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Harnessing Textual Refusal Directions for Multimodal Safety](https://arxiv.org/abs/2606.31876)
中文标题：Harnessing Textual Refusal Directions 面向 Multimodal Safety
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [AeroVerse-SatAgent: UAV-Satellite Collaborative Spatial Reasoning Inspired by the Dual Visual Pathway Theory of Cognitive Neuroscience](https://arxiv.org/abs/2606.31467)
中文标题：AeroVerse-SatAgent：UAV-Satellite Collaborative Spatial Reasoning Inspired by the Dual Visual Pathway Theory of Cognitive Neuroscience
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Transformers as Bayesian In-Context Experimenters: Smoothness-Adaptive Efficient ATE Estimation](https://arxiv.org/abs/2606.31184)
中文标题：Transformers as Bayesian In-Context Experimenters：Smoothness-Adaptive Efficient ATE Estimation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Beyond Single Character: Evaluating MLLMs for Sentence-Level Oracle Bone Inscription Understanding](https://arxiv.org/abs/2606.31169)
中文标题：Beyond Single Character：Evaluating MLLMs 面向 Sentence-Level Oracle Bone Inscription Understanding
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [An Empirical Study of Security Calibration in Large Language Models for Code](https://arxiv.org/abs/2606.31159)
中文标题：一种Empirical Study of Security Calibration in Large Language Models 面向 Code
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [PPT-Eval: A Benchmark for Computer-Use Agents on PowerPoint Tasks](https://arxiv.org/abs/2606.31154)
中文标题：PPT-Eval：A 基准 面向 Computer-Use Agents on PowerPoint Tasks
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [A Modular Vision-Language-Action Robotics Framework for Indoor Environments](https://arxiv.org/abs/2606.31144)
中文标题：一种Modular Vision-Language-Action Robotics 框架 面向 Indoor Environments
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Cross-Space Distillation: Teaching One-Step Students with Modern Diffusion Teachers](https://arxiv.org/abs/2606.32020)
中文标题：Cross-Space Distillation：Teaching One-Step Students 结合 Modern Diffusion Teachers
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [FedLAB: Traceable Semantic Codebooks for Federated Multimodal Graph Foundation Learning](https://arxiv.org/abs/2606.32016)
中文标题：FedLAB：Traceable Semantic Codebooks 面向 Federated Multimodal Graph Foundation Learning
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
