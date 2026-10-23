---
title: "让 Agent 更可靠地调用工具和复用技能"
date: "2026-10-24"
target_date: "2026-10-22"
actual_date: "2026-10-22"
fallback_from: ""
lang: "zh"
slug: "2026-10-24-conservative-meta-agent-search-architecture-adaptation-under"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "evaluation", "multimodal", "rag", "systems", "training", "video-generation", "vision-generation"]
topics: ["agents", "evaluation", "multimodal", "rag", "systems", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-10-24-conservative-meta-agent-search-architecture-adaptation-under-sources/"
generated_at: "2026-10-23T23:51:22.921357+00:00"
page_type: "brief"
candidate_count: 494
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Conservative Meta-Agent Search: Architecture Adaptation under Non-Stationarity", "AgentTriage: Replayable Security Diagnosis Across Heterogeneous Agent Runtimes", "nnInteractive Agent: General-Purpose AI Agents as 3D Image Annotators", "Amplifying Latency and Cost of LLM Inference via Rowhammer Attack", "Pos4CHD: A Positive-Free Mask-Guided Counterfactual Synthesis Framework for Fetal Congenital Heart Defect Analysis", "ColaBench: Evaluating Memory-Guided Knowledge Acquisition in Personal Agents"]
featured_paper_urls: ["https://arxiv.org/abs/2610.31436", "https://arxiv.org/abs/2610.30738", "https://arxiv.org/abs/2610.31080", "https://arxiv.org/abs/2610.30798", "https://arxiv.org/abs/2610.31139", "https://arxiv.org/abs/2610.30989"]
featured_paper_titles_zh: ["保守的元代理搜索：非平稳性下的架构适应", "AgentTriage ：跨异构Agent运行时的可重播安全诊断", "nnInteraCTive Agent ：作为3D图像注释器的通用AI Agent", "通过Rowhammer攻击放大LLM推理的延迟和成本", "Pos4CHD：A Positive-Free Mask-Guided Counterfactual Synthesis 框架 面向 Fetal Congenital Heart Defect Analysis", "ColaBench ：评估个人代理的记忆导向知识获取"]
---

# 让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Conservative Meta-Agent Search: Architecture Adaptation under Non-Stationarity (Ali Atiah Alzahrani)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.31436">2610.31436</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.31436">PDF</a></p>

中文标题：保守的元代理搜索：非平稳性下的架构适应

信号显示：自动代理系统设计通常在具有即时标量奖励的静态任务套件上进行评估。关键词：agent、inference、deployment、benchmark。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>AgentTriage: Replayable Security Diagnosis Across Heterogeneous Agent Runtimes (Jie Ying, Xutao Zhang, Ningyuan Chen, Mengce Zheng, Jun Li, Zhongjie Zhu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.30738">2610.30738</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.30738">PDF</a></p>

中文标题：AgentTriage ：跨异构Agent运行时的可重播安全诊断

信号显示：当工具使用代理编写文件、执行代码或发送数据时，其最终响应无法解释由此产生的安全事件，异构运行时通过不兼容的接口暴露相关证据。关键词：agent、rag、code、open-source。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>nnInteractive Agent: General-Purpose AI Agents as 3D Image Annotators (Fabian Isensee, Constantin Ulrich Harsy, Maximilian Rokuss, Benjamin Hamm, Philipp Vollmuth, Klaus H. Maier-Hein)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.31080">2610.31080</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.31080">PDF</a></p>

中文标题：nnInteraCTive Agent ：作为3D图像注释器的通用AI Agent

信号显示：交互式3D分割模型（如nnInteractive ）将一些空间提示（点、涂鸦、框）转换为精确的体积遮罩，但人仍在进行注释工作：查找每个结构，放置提示，检查结果并纠正。关键词：agent、benchmark、code、open-source。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Amplifying Latency and Cost of LLM Inference via Rowhammer Attack (Mrityunjay Shukla, Shubham Roy, Biswabandan Panda)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.30798">2610.30798</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.30798">PDF</a></p>

中文标题：通过Rowhammer攻击放大LLM推理的延迟和成本

信号显示：大语言模型（ LLM ）使用由Triton等实时（ JIT ）编译框架生成的优化GPU内核来实现高推理效率。关键词：inference、serving、deployment、latency。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Pos4CHD: A Positive-Free Mask-Guided Counterfactual Synthesis Framework for Fetal Congenital Heart Defect Analysis (Wenjie Xuan, Yapeng Li, Hang Su, Chen Cheng, Juhua Liu, Sheng Zhao, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.31139">2610.31139</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.31139">PDF</a></p>

中文标题：Pos4CHD：A Positive-Free Mask-Guided Counterfactual Synthesis 框架 面向 Fetal Congenital Heart Defect Analysis

信号显示：阳性病例的稀缺性仍然是开发胎儿先天性心脏缺陷（ CHD ）自动诊断系统的主要瓶颈，特别是对于罕见的亚型。关键词：alignment、evaluation、code、image generation。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>ColaBench: Evaluating Memory-Guided Knowledge Acquisition in Personal Agents (Wenjie Zhang, Zhichao Shi, Xuhui Jiang, Xiaojun Wu, Cehao Yang, Chengjin Xu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.30989">2610.30989</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.30989">PDF</a></p>

中文标题：ColaBench ：评估个人代理的记忆导向知识获取

信号显示：个人客服代表需要借鉴长期互动历史记录，以检索和应用适合用户当前请求的外部知识。关键词：agent、rag、retrieval、evaluation。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Governance-State Corruption in Long-Term Memory for LLM Agents: A Cross-Model Stress Test](https://arxiv.org/abs/2610.30698)
中文标题：LLM代理长期记忆中的治理-国家腐败：跨模型压力测试
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [KinoUAV: A Benchmark for Safe and Stable UAV Vision-Language Navigation with Kinodynamic Modeling](https://arxiv.org/abs/2610.30609)
中文标题：KinoUAV ：基于运动动力学建模的安全稳定无人机视觉语言导航基准
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Mitigating Saliency Collapse: Robust Saliency-Aware Long-Text Image-Text Alignment](https://arxiv.org/abs/2610.31005)
中文标题：缓解显着性崩溃：强大的显着性感知长文本图像-文本对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Diagnostic Loss: Asymmetric Supervision for Radiology Report Generation](https://arxiv.org/abs/2610.30980)
中文标题：诊断损失：放射学报告生成的不对称监督
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Ground-Truth-First Benchmarking of Reinforcement Learning via Converse Optimality: From Smooth, Fully Observed Systems to Non-Smooth or Partially Observed Tasks](https://arxiv.org/abs/2610.30954)
中文标题：通过反向最优性对强化学习进行基准测试：从平滑、完全观察的系统到非平滑或部分观察的任务
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [RetiJev: Fast and Source-Grounded Ophthalmic Decision Models](https://arxiv.org/abs/2610.30947)
中文标题：RetiJev：Fast 与 Source-Grounded Ophthalmic Decision Models
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [TESSA: A Governance-Oriented Custom GPT for SME Guidance under the EU AI Act: Design, Implementation, and Evaluation](https://arxiv.org/abs/2610.30822)
中文标题：TESSA：A Governance-Oriented Custom GPT 面向 SME Guidance under the EU AI Act：Design，Implementation，与 评测
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [GIFT: Gradient Informed Filtering for Distillation Augmented Reasoning RL](https://arxiv.org/abs/2610.30796)
中文标题：GIFT：Gradient Informed Filtering 面向 Distillation Augmented Reasoning RL
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [One-shot federated unsupervised domain adaptation with Smoothed Knowledge Distillation and teacher refinement](https://arxiv.org/abs/2610.30646)
中文标题：通过平滑知识蒸馏和教师精炼进行一次性联合无监督域适应
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Future of Time Series Anomaly Detection: From Historical Review to Unified Outlook](https://arxiv.org/abs/2610.30628)
中文标题：时间序列异常检测的未来：从历史回顾到统一展望
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core](https://arxiv.org/abs/2610.30557)
中文标题：自主投资的受控自我进化：具有不变核心的多代理LLM系统
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [WorldForge V2: Eliciting Camera-Trajectory Alignment in Video Diffusion Models](https://arxiv.org/abs/2610.31640)
中文标题：WorldForge V2 ：在视频扩散模型中引发相机轨迹对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [On the Token Collapse Phenomenon in Textual Graph Soft Prompting](https://arxiv.org/abs/2610.31572)
中文标题：论文本图形软提示中的令牌崩溃现象
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [LACToS: Local Anomaly Detection via Conditional Typicality of Superpixels](https://arxiv.org/abs/2610.31538)
中文标题：LACToS ：通过超像素的条件典型性进行本地异常检测
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Evaluating the Applicability of LLM Inference Optimizations on Apple Silicon](https://arxiv.org/abs/2610.31479)
中文标题：评估LLM推理优化在Apple Silicon上的适用性
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MoG-VLM: Efficient Video Anomaly Detection through Motion-Guided Vision-Language Models](https://arxiv.org/abs/2610.31478)
中文标题：MoG-VLM ：通过运动引导视觉语言模型进行高效视频异常检测
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [From Structured Records to Patient Narratives: Preserving Clinical Alignment in LLM-Generated Health Summaries](https://arxiv.org/abs/2610.31467)
中文标题：从结构化记录到患者叙述：在LLM生成的健康总结中保持临床一致性
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Drift Says When, Budget Says How Much: Rate-Controlled KV Re-selection for Long-Form Multimodal Generation](https://arxiv.org/abs/2610.31433)
中文标题：漂移表示何时，预算表示多少：长式多式联运发电的速率控制KV重新选择
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SurveyGraph: Generating Academic Surveys via Methods-Entity Knowledge Graphs](https://arxiv.org/abs/2610.31317)
中文标题：SurveyGraph ：通过方法-实体知识图生成学术调查
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Lightweight Frame Compensation for Real-Time Polyp Segmentation under Frame Skipping](https://arxiv.org/abs/2610.31228)
中文标题：Lightweight Frame Compensation 面向 Real-Time Polyp Segmentation under Frame Skipping
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
