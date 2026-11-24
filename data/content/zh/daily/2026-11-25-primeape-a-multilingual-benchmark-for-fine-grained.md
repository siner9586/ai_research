---
title: "提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能"
date: "2026-11-25"
target_date: "2026-11-23"
actual_date: "2026-11-23"
fallback_from: ""
lang: "zh"
slug: "2026-11-25-primeape-a-multilingual-benchmark-for-fine-grained"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "robotics", "training"]
topics: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "robotics", "training"]
sources_page: "/zh/daily/2026-11-25-primeape-a-multilingual-benchmark-for-fine-grained-sources/"
generated_at: "2026-11-24T17:33:13.858375+00:00"
page_type: "brief"
candidate_count: 606
featured_count: 6
mentions_count: 20
featured_paper_titles: ["PRIMEAPE: A Multilingual Benchmark for Fine-Grained Meta-Evaluation of Judge Models", "FATCAT: Fault Injection Attacks Targeting Chip-level Alignment", "Parsing Visual Latents for Multimodal Spatial Reasoning", "Spatial-Zero: Self-Evolving Spatial Reasoning in Vision-Language Models from Zero Data", "AXE: AlpaSim E2E Closed Loop Challenge Technical Report", "STMemoLLM: A Spatial-Temporal Memory-Augmented LLM for Robust Traffic Forecasting"]
featured_paper_urls: ["https://arxiv.org/abs/2611.30925", "https://arxiv.org/abs/2611.31129", "https://arxiv.org/abs/2611.31021", "https://arxiv.org/abs/2611.30424", "https://arxiv.org/abs/2611.30511", "https://arxiv.org/abs/2611.30148"]
featured_paper_titles_zh: ["PRIMEAPE：A Multilingual 基准 面向 Fine-Grained Meta-评测 of Judge Models", "FATCAT：针对芯片级对齐的故障注入攻击", "解析多模态空间推理的视觉潜在特征", "Spatial-Zero：Self-Evolving Spatial Reasoning in Vision-Language Models 来自 Zero Data", "AXE：AlpaSim E2E 闭环挑战技术报告", "STMemoLLM：A Spatial-Temporal Memory-Augmented LLM 面向 Robust Traffic Forecasting"]
---

# 提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>PRIMEAPE: A Multilingual Benchmark for Fine-Grained Meta-Evaluation of Judge Models (Vladislav Mikhailov, Sarfraz Ahmad, Momina Ahsan, Zoia Butenko, Vladimir Dobrovolskii, Preslav Nakov, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.30925">2611.30925</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.30925">PDF</a></p>

中文标题：PRIMEAPE：A Multilingual 基准 面向 Fine-Grained Meta-评测 of Judge Models

信号显示：大语言模型日益成为其他模型的评判者，影响着基准排名和模型开发。关键词：alignment、safety、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 2. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>FATCAT: Fault Injection Attacks Targeting Chip-level Alignment (Peter Horvath, Ilia Shumailov, Zhuoran Liu, Lukasz Chmielewski, Lejla Batina)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.31129">2611.31129</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.31129">PDF</a></p>

中文标题：FATCAT：针对芯片级对齐的故障注入攻击

信号显示：在现代基础模型中，模型对齐是拒绝恶意提示的主要安全和保障机制；然而，现有的对抗性评估隐含地假设了底层硬件的完整性。关键词：rag、serving、alignment、safety。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Parsing Visual Latents for Multimodal Spatial Reasoning (Zhuoying Yang, Yichen Guo, Kathy Jia, Zichang Su, Ayesha Kashif, Nange Hai, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.31021">2611.31021</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.31021">PDF</a></p>

中文标题：解析多模态空间推理的视觉潜在特征

信号显示：跨多个视角的空间推理需要根据 2D 观察结果推断物体与摄像头之间的 3D 关系，这取决于跨视角对应关系和场景几何形状，而视觉-语言模型 (VLM) 无法可靠地提取这些信息。关键词：rag、code、multimodal、vision-language。代码/数据可用性需查看原文确认。

### 4. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Spatial-Zero: Self-Evolving Spatial Reasoning in Vision-Language Models from Zero Data (Yutong Li, Haoyu Zhao, Daoguo Dong, Ziyi Ye, Yugang Jiang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.30424">2611.30424</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.30424">PDF</a></p>

中文标题：Spatial-Zero：Self-Evolving Spatial Reasoning in Vision-Language Models 来自 Zero Data

信号显示：空间推理需要视觉-语言模型（VLM）来理解度量距离、三维关系和视点相关的几何形状。关键词：rag、benchmark、code、vision-language。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>AXE: AlpaSim E2E Closed Loop Challenge Technical Report (Joonhee Lim, Seonmyeong Lee, Sihwan Hwang, Hanbin Jang, Hiwon Shin, Dogun Kim, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.30511">2611.30511</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.30511">PDF</a></p>

中文标题：AXE：AlpaSim E2E 闭环挑战技术报告

信号显示：本报告介绍了为 Physical AI 自动驾驶赛道开发端到端 (E2E) 自动驾驶模型的完整流程。关键词：rag、safety、data、dataset。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>STMemoLLM: A Spatial-Temporal Memory-Augmented LLM for Robust Traffic Forecasting (Jian Zhou, Binqing Wu, Zongjiang Shang, Wanghui Qiu, Dongliang Cui, Chenxi Jin, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.30148">2611.30148</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.30148">PDF</a></p>

中文标题：STMemoLLM：A Spatial-Temporal Memory-Augmented LLM 面向 Robust Traffic Forecasting

信号显示：交通预测对于智能交通系统至关重要。关键词：compression、alignment、code、memory。代码/数据可用性需查看原文确认。

## 其他值得关注
- [FiRE: Fine-grained Ranking Evaluation for Machine Translation](https://arxiv.org/abs/2611.30168)
中文标题：FiRE：Fine-grained Ranking 评测 面向 Machine Translation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Thermal-Guided Low-Light UAV Image Enhancement: A Reliability-Aware Guidance Network and a Unified Benchmark](https://arxiv.org/abs/2611.30114)
中文标题：热成像引导的低光照无人机图像增强：一种可靠性感知引导网络和统一基准
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [FlexGaze: Weakly Supervised Gaze Estimation at Scale](https://arxiv.org/abs/2611.30012)
中文标题：FlexGaze：Weakly Supervised Gaze Estimation 的大规模方法
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Seeking in Space: Benchmarking Purposeful Active Exploration of Vision-Language Models for Spatial Reasoning](https://arxiv.org/abs/2611.31215)
中文标题：在空间中寻找：对视觉-语言模型进行有目的的主动探索，以实现空间推理的基准测试
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [SPROUT: Predicting Objective-Grounded Prompt Utility for Efficient Text-to-Image Preference Tuning](https://arxiv.org/abs/2611.31163)
中文标题：SPROUT：Predicting Objective-Grounded Prompt Utility 面向 Efficient Text-to-Image Preference Tuning
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Reinforcing Diffusion Models by Instantaneous Trajectory Distribution Matching](https://arxiv.org/abs/2611.30986)
中文标题：通过瞬时轨迹分布匹配强化扩散模型
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Learning Dense Head-Object Contact Estimation with Synthetic Data](https://arxiv.org/abs/2611.30751)
中文标题：使用合成数据学习密集型头部-物体接触估算
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Transport-Safe Evaluation of LLM Agents: Trajectory-Dependent Judge Error and Anytime-Valid Auditing](https://arxiv.org/abs/2611.30742)
中文标题：LLM 代理的传输安全评估：轨迹依赖性判断误差和随时有效的审计
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Optimistic Online Learning for Coding Agents with Aggregate Feedback](https://arxiv.org/abs/2611.30405)
中文标题：基于聚合反馈的编码智能体乐观在线学习
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [RigidAnchor: Cross-View Geo-Localization for UAV via Iterative Planar Rigid Alignment](https://arxiv.org/abs/2611.30278)
中文标题：RigidAnchor：通过迭代平面刚性对齐实现无人机跨视图地理定位
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Visual-RFT++: Extending Visual Reinforcement Fine-Tuning to Multimodal Tool Use](https://arxiv.org/abs/2611.30193)
中文标题：Visual-RFT++：将视觉强化微调扩展至多模态工具使用
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Quantizing in the Loop: Drift-Aware Ultra-Low-Bit Vision-Language-Action Models](https://arxiv.org/abs/2611.30178)
中文标题：环路量化：漂移感知超低比特视觉-语言-动作模型
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [MotionServe: Efficient Multi-Robot Serving by Exploiting Robot Execution Slack](https://arxiv.org/abs/2611.30083)
中文标题：MotionServe：利用机器人执行松弛实现高效的多机器人服务
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [One Size Doesn't Fit All: Input Adaptive Class Activation Mapping for Improved Visual Explanations](https://arxiv.org/abs/2611.29993)
中文标题：并非一刀切：输入自适应类激活映射，以改进视觉解释
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Self-Supervised Dataset Distillation via Mutual Information Maximization](https://arxiv.org/abs/2611.31225)
中文标题：通过互信息最大化实现自监督数据集蒸馏
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [UMAMI: A Multimodal Benchmark Dataset for Evidence-Grounded Dietary Decisions](https://arxiv.org/abs/2611.31068)
中文标题：UMAMI：A Multimodal 基准 Dataset 面向 Evidence-Grounded Dietary Decisions
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Demographic Encoding is Not Exposure: Fairness and Privacy in Chest X-ray Foundation Models](https://arxiv.org/abs/2611.31014)
中文标题：人口统计学编码并非暴露：胸部 X 射线基础模型中的公平性和隐私性
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [CART: Clustering-based Analysis of Recurring narratives for Taxonomy construction](https://arxiv.org/abs/2611.30993)
中文标题：CART：Clustering-based Analysis of Recurring narratives 面向 Taxonomy construction
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [MedUIGym: Evaluating and Training GUI Agents for Clinical Workflows](https://arxiv.org/abs/2611.30983)
中文标题：MedUIGym：Evaluating 与 Training GUI Agents 面向 Clinical Workflows
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Prediction-Powered Regression via Calibration: Beyond the Supervised Minimax Benchmark](https://arxiv.org/abs/2611.30976)
中文标题：通过校准实现的预测驱动回归：超越有监督的极小极大基准
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
