---
title: "提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性"
date: "2026-06-27"
target_date: "2026-06-25"
actual_date: "2026-06-25"
fallback_from: ""
lang: "zh"
slug: "2026-06-27-from-hallucination-to-grounding-diagnosing-visual-spatial"
summary: "今天主要跟进：提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "rag", "reasoning", "systems", "training", "video-generation"]
topics: ["agents", "code", "evaluation", "rag", "reasoning", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-06-27-from-hallucination-to-grounding-diagnosing-visual-spatial-sources/"
generated_at: "2026-06-26T22:22:39.331002+00:00"
page_type: "brief"
candidate_count: 386
featured_count: 6
mentions_count: 20
featured_paper_titles: ["From Hallucination to Grounding: Diagnosing Visual Spatial Intelligence via CRISP", "Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform", "Retrieval-Warmed Energy-Based Reasoning: A Five-Arm Ablation Methodology for Diffusion-as-Inference on Structured Reasoning Tasks", "Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings", "Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation", "\\textsc{DiARC}: Distinguishing Positive and Negative Samples Helps Improving ARC-like Reasoning Ability of Large Language Models"]
featured_paper_urls: ["https://arxiv.org/abs/2606.26535", "https://arxiv.org/abs/2606.26590", "https://arxiv.org/abs/2606.26476", "https://arxiv.org/abs/2606.27287", "https://arxiv.org/abs/2606.26686", "https://arxiv.org/abs/2606.26530"]
featured_paper_titles_zh: ["从幻觉到接地：通过CRISP诊断视觉空间智能", "Empirical Software Engineering TerraProbe：A Layered-Oracle 框架 面向 Detecting Deceptive Fixes in LLM-Assisted Terraform", "Retrieval-Warmed Energy-Based Reasoning：A Five-Arm Ablation Methodology 面向 Diffusion-as-Inference on Structured Reasoning Tasks", "大型语言模型自动简历筛选中的快速注射：单次和多次注射设置", "Do Safety Guardrails Need to Reason? LeanGuard：A Fast 与 Light Approach 面向 Robust Moderation", "\\textsc{DiARC}：Distinguishing Positive 与 Negative Samples Helps Improving ARC-like Reasoning Ability of Large Language Models"]
---

# 提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>From Hallucination to Grounding: Diagnosing Visual Spatial Intelligence via CRISP (Zhixing Li, Yinan Yu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.26535">2606.26535</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.26535">PDF</a></p>

中文标题：从幻觉到接地：通过CRISP诊断视觉空间智能

信号显示：当前的VLM评估通常将语言先验与真正的空间推理混为一谈。关键词：rag、alignment、evaluation、code。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Empirical Software Engineering TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform (Manar Alsaid, Chimdumebi Nebolisa, Faris Abbas)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.26590">2606.26590</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.26590">PDF</a></p>

中文标题：Empirical Software Engineering TerraProbe：A Layered-Oracle 框架 面向 Detecting Deceptive Fixes in LLM-Assisted Terraform

信号显示：Terraform基础架构即代码中的安全配置错误是云部署中日益增长的风险，大语言模型越来越多地被用作自动修复代理。关键词：agent、deployment、evaluation、code。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Retrieval-Warmed Energy-Based Reasoning: A Five-Arm Ablation Methodology for Diffusion-as-Inference on Structured Reasoning Tasks (Libo Sun, Po-Wei Harn, Zewei Zhang, Peixiong He, Xiao Qin)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.26476">2606.26476</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.26476">PDF</a></p>

中文标题：Retrieval-Warmed Energy-Based Reasoning：A Five-Arm Ablation Methodology 面向 Diffusion-as-Inference on Structured Reasoning Tasks

信号显示：热启动的扩散采样器加速迭代推断，但很少清楚流水线的哪一部分承载增益。关键词：rag、retrieval、inference、alignment。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings (Preet Baxi, Jiannan Xu, Jane Yi Jiang, Stefanus Jasin)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.27287">2606.27287</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.27287">PDF</a></p>

中文标题：大型语言模型自动简历筛选中的快速注射：单次和多次注射设置

信号显示：大语言模型（ LLM ）越来越多地用于筛选求职者并对其进行排名，从而激励求职者战略性地操纵算法招聘系统。关键词：rag、evaluation、code、api。代码/数据可用性需查看原文确认。

### 5. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation (Dongbin Na)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.26686">2606.26686</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.26686">PDF</a></p>

中文标题：Do Safety Guardrails Need to Reason? LeanGuard：A Fast 与 Light Approach 面向 Robust Moderation

信号显示：为了筛选提示或回复，最近的护栏方法在发布判决之前生成思维链（ CoT ）。关键词：rag、inference、safety、benchmark。代码/数据可用性需查看原文确认。

### 6. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>\textsc{DiARC}: Distinguishing Positive and Negative Samples Helps Improving ARC-like Reasoning Ability of Large Language Models (Yuxuan Yang, Feiyang Li, Yile Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.26530">2606.26530</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.26530">PDF</a></p>

中文标题：\textsc{DiARC}：Distinguishing Positive 与 Negative Samples Helps Improving ARC-like Reasoning Ability of Large Language Models

信号显示：抽象和推理语料库(ARC; ~\ citealp {chollet2019measure})包含的任务需要从有限的网格样本中总结模式并预测输出网格。关键词：alignment、benchmark、code、fine-tuning。代码/数据可用性需查看原文确认。

## 其他值得关注
- [FlameVQA: A Physically-Grounded UAV Wildfire VQA Benchmark with Radiometric Thermal Supervision](https://arxiv.org/abs/2606.27128)
中文标题：FlameVQA ：具有辐射热监控的物理接地无人机野火VQA基准
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Unison: Benchmarking Unified Multimodal Models via Synergistic Understanding and Generation](https://arxiv.org/abs/2606.26984)
中文标题：UNISON ：通过协同理解和生成对统一多模式模型进行基准测试
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Geometric Gradient Rectification for Safe Open-Set Semi-Supervised Learning](https://arxiv.org/abs/2606.26973)
中文标题：用于安全开放式半监督学习的几何梯度校正
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems](https://arxiv.org/abs/2606.26859)
中文标题：AgentX ：走向工业推荐系统的代理驱动自我迭代
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [LCAi: Life Cycle Assessment with big data fusion and retrieval-augmented generation-assisted interpretation](https://arxiv.org/abs/2606.26857)
中文标题：LCAI ：使用大数据融合和检索增强生成辅助解释的生命周期评估
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP](https://arxiv.org/abs/2606.26794)
中文标题：ReasonCLIP-58M：Visually Grounded Commonsense Reasoning Supervision 面向 CLIP
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Adversarial Diffusion Across Modalities: A Fusion Survey of Attacks, Defenses, and Evaluation for Text, Vision, and Vision-Language Models](https://arxiv.org/abs/2606.26566)
中文标题：Adversarial Diffusion Across Modalities：A Fusion Survey of Attacks，Defenses，与 评测 面向 Text，Vision，与 Vision-Language Models
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [OctoSense: Self-Supervised Learning for Multimodal Robot Perception](https://arxiv.org/abs/2606.27317)
中文标题：OctoSense：Self-Supervised Learning 面向 Multimodal Robot Perception
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Automating Potential-based Reward Shaping with Vision Language Model Guidance](https://arxiv.org/abs/2606.27180)
中文标题：通过视觉语言模型指导实现基于潜力的奖励塑造自动化
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Cascaded Multi-Granularity Pruning for On-Device LLM Inference in Industrial IoT](https://arxiv.org/abs/2606.26861)
中文标题：工业物联网中用于设备上LLM推理的级联多粒度修剪
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [The Capability Frontier: Benchmarks Miss 82% of Model Performance](https://arxiv.org/abs/2606.26836)
中文标题：能力前沿：基准错过了82%的模型性能
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.26790)
中文标题：OPID：On-Policy Skill Distillation 面向 Agentic Reinforcement Learning
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Dual-Prior Guided Null-Space Learning with Mixture-of-Splines for Arbitrary Medical Slice Super-Resolution](https://arxiv.org/abs/2606.26716)
中文标题：用于任意医学切片超分辨率的混合样条双前导空空间学习
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation](https://arxiv.org/abs/2606.26712)
中文标题：MLFFM-SegDiff：A Multi-Level Feature Fusion Diffusion Model 面向 Skin Lesion Segmentation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Autoregressive Boltzmann Generators](https://arxiv.org/abs/2606.27361)
中文标题：自回归玻尔兹曼发生器
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning](https://arxiv.org/abs/2606.27330)
中文标题：通过自主体验探索和任务规划的后见之明体验利用来增强GUI代理的能力
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [See & Sniff: Learning Visuo-Olfactory Representations](https://arxiv.org/abs/2606.27307)
中文标题：观看和嗅探：学习视觉嗅觉表征
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [How Surprising Is Historical Italian to Language Models? Tokenization Tax, Comprehension Tax, and a Simple Mitigation](https://arxiv.org/abs/2606.27275)
中文标题：历史意大利语对语言模型有多令人惊讶？代币化税、理解税和简单的减免
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223)
中文标题：SatSplatDiff：Geometry-preserving generative refinement 面向 high-fidelity satellite Gaussian Splatting
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes](https://arxiv.org/abs/2606.27210)
中文标题：用真实意图铺平道路：意图感知培训改善了各种培训制度下的法学硕士安全分类
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
