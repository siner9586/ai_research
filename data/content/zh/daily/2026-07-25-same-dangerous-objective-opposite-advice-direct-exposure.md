---
title: "让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升代码生成、执行反馈和自动修复能力"
date: "2026-07-25"
target_date: "2026-07-23"
actual_date: "2026-07-23"
fallback_from: ""
lang: "zh"
slug: "2026-07-25-same-dangerous-objective-opposite-advice-direct-exposure"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "safety", "systems", "training", "vision-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "safety", "systems", "training", "vision-generation"]
sources_page: "/zh/daily/2026-07-25-same-dangerous-objective-opposite-advice-direct-exposure-sources/"
generated_at: "2026-07-24T22:16:39.849117+00:00"
page_type: "brief"
candidate_count: 321
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Same Dangerous Objective, Opposite Advice: Direct Exposure versus Multi-Agent Mediation", "Future Rendering $\\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window", "Multimodal Pretraining for Generalizable EEG Representation Learning", "Inference-Time Scaling of Diffusion Models via Progressive Seed Pruning", "When Are Reasoning-Based Guardrails Not Efficient? ResponseGuard: A Fast Vision-Language Guard for Real-Time Moderation", "Declarative Problem Solving in UAM Strategic Deconfliction"]
featured_paper_urls: ["https://arxiv.org/abs/2607.21518", "https://arxiv.org/abs/2607.21471", "https://arxiv.org/abs/2607.21384", "https://arxiv.org/abs/2607.21591", "https://arxiv.org/abs/2607.21401", "https://arxiv.org/abs/2607.21197"]
featured_paper_titles_zh: ["相同的危险目标，相反的建议：直接接触与多代理调解", "未来渲染$\\ neq $未来曲面：观测窗口之外的动态曲面重建的基准和数据集", "Multimodal Pretraining 面向 Generalizable EEG Representation Learning", "通过渐进种子修剪的扩散模型的推理时间缩放", "When Are Reasoning-Based Guardrails Not Efficient? ResponseGuard：A Fast Vision-Language Guard 面向 Real-Time Moderation", "UAM战略消除冲突中的陈述性问题解决"]
---

# 让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升代码生成、执行反馈和自动修复能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Same Dangerous Objective, Opposite Advice: Direct Exposure versus Multi-Agent Mediation (Linjun Li)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.21518">2607.21518</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.21518">PDF</a></p>

中文标题：相同的危险目标，相反的建议：直接接触与多代理调解

信号显示：当直接显示危险目标时，即使是当前的高性能LLM也比其他代理人转换和传递其方向时看起来更安全。关键词：agent、workflow、serving、safety。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window (Yukun Shi, Minglun Gong)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.21471">2607.21471</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.21471">PDF</a></p>

中文标题：未来渲染$\ neq $未来曲面：观测窗口之外的动态曲面重建的基准和数据集

信号显示：动态场景重建几乎总是在观察到的时间窗口内进行评估，但AR叠加、机器人交互和预期规划等部署设置需要未来的表面：几何体有时超出捕获的几何体。关键词：deployment、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 3. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Multimodal Pretraining for Generalizable EEG Representation Learning (Targol Bakhtiarvand, Jugal Kalita, Adham Atyabi)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.21384">2607.21384</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.21384">PDF</a></p>

中文标题：Multimodal Pretraining 面向 Generalizable EEG Representation Learning

信号显示：用于癫痫的脑电图（ EEG ）模型通常仅限于特定的数据集和任务。关键词：alignment、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Inference-Time Scaling of Diffusion Models via Progressive Seed Pruning (Rogerio Guimaraes, Pietro Perona)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.21591">2607.21591</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.21591">PDF</a></p>

中文标题：通过渐进种子修剪的扩散模型的推理时间缩放

信号显示：扩散和流量匹配模型主导了条件图像生成，但这些模型的推理时间缩放远远低于自回归语言模型。关键词：inference、alignment、evaluation、code。代码/数据可用性需查看原文确认。

### 5. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>When Are Reasoning-Based Guardrails Not Efficient? ResponseGuard: A Fast Vision-Language Guard for Real-Time Moderation (Dongbin Na)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.21401">2607.21401</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.21401">PDF</a></p>

中文标题：When Are Reasoning-Based Guardrails Not Efficient? ResponseGuard：A Fast Vision-Language Guard 面向 Real-Time Moderation

信号显示：视觉语言AI助手将其答案作为生成的令牌流返回。关键词：safety、benchmark、code、multimodal。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Declarative Problem Solving in UAM Strategic Deconfliction (Gioacchino Sterlicchio, Angelo Oddi, Riccardo Rasconi, Francesca Alessandra Lisi)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.21197">2607.21197</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.21197">PDF</a></p>

中文标题：UAM战略消除冲突中的陈述性问题解决

信号显示：对城市空中交通（ UAM ）日益增长的需求给空域管理带来了重大挑战，特别是在人口稠密的大都市地区。关键词：benchmark、memory、program、execution。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks](https://arxiv.org/abs/2607.21482)
中文标题：无云代理编码：评估纵向数据准备任务的开放权重大型语言模型
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [DINOde: Continuous Vision-Text Alignment for Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2607.21371)
中文标题：DINOde：Continuous Vision-Text Alignment 面向 Open-Vocabulary Semantic Segmentation
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction](https://arxiv.org/abs/2607.20911)
中文标题：Tencent WorkBuddy Bench：A Multi-Domain Coding-Agent 基准 with Contamination-Resistant Task Construction
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Sidewalk Moments: Are Richer Representations Always More Human-Aligned? Evidence from City-Walk Videos](https://arxiv.org/abs/2607.20903)
中文标题：人行道时刻：更丰富的代表性是否总是更人性化？城市漫步视频中的证据
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [HGeo-TopoMap: Boosting Topological Mapping with Hierarchical Geometric Priors](https://arxiv.org/abs/2607.21281)
中文标题：HGeo-TopoMap ：使用分层几何先验增强拓扑映射
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [V-DEAL: Diagnosing Video Safety De-Calibration as an Understanding-Refusal Coupling Failure](https://arxiv.org/abs/2607.21151)
中文标题：V-DEAL ：将视频安全反校准诊断为理解-拒绝耦合故障
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Faster IndexTTS-2: Accelerating and Streaming Autoregressive Zero-Shot Text-to-Speech Synthesis on GPUs](https://arxiv.org/abs/2607.21042)
中文标题：Faster IndexTTS-2：Accelerating 与 Streaming Autoregressive Zero-Shot Text-to-Speech Synthesis on GPUs
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Boosting Robustness for All-Weather Self-Supervised Depth Estimation in Autonomous Driving](https://arxiv.org/abs/2607.21526)
中文标题：提高自动驾驶中全天候自我监督深度估计的鲁棒性
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Toward Generalizable Cognitive Impairment Detection with Speech-Based Multimodal Large Language Models](https://arxiv.org/abs/2607.21496)
中文标题：使用基于语音的多模态大型语言模型进行可推广的认知障碍检测
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Toward Continuous Assurance for the Democratization of AI Agent Creation in Industry](https://arxiv.org/abs/2607.21495)
中文标题：面向产业AI智能体创造民主化的持续保障
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Euclid-MCP: A Model Context Protocol Server for Deterministic Logical Reasoning via Prolog](https://arxiv.org/abs/2607.21412)
中文标题：Euclid-MCP ：通过Prolog进行确定性逻辑推理的模型上下文协议服务器
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Phonetic forced alignment for low-resource language varieties: Model training and evaluation on Chengdu Mandarin](https://arxiv.org/abs/2607.21332)
中文标题：低资源语言品种的语音强制对齐：成都普通话的模型训练和评估
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [SlerpFlow: Spherical Trajectory Correction for Rectified Flow Inversion](https://arxiv.org/abs/2607.21326)
中文标题：SlerpFlow：Spherical Trajectory Correction 面向 Rectified Flow Inversion
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for Pre-Trained LLMs](https://arxiv.org/abs/2607.21291)
中文标题：自适应深度稀疏框架：预训练LLM的相似性驱动资源分配
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Detectors Learn the Wrong Thing: Shortcut-Resistant Adversarial Training Against Physically Realizable Attacks](https://arxiv.org/abs/2607.21243)
中文标题：探测器学习错误的东西：针对物理可实现攻击的抗捷径对抗性训练
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders](https://arxiv.org/abs/2607.21217)
中文标题：ICAE-Bench ：评估编码代理作为交互式项目构建商
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Safety-oriented sidewalk and road segmentation for smartphone-based assistive navigation](https://arxiv.org/abs/2607.21137)
中文标题：以安全为导向的人行道和道路分段，用于基于智能手机的辅助导航
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [C-PTQ: Fisher-weighted Channel-wise Sensitivity for Post-training Quantization of MLLMs](https://arxiv.org/abs/2607.21076)
中文标题：C-PTQ：Fisher-weighted Channel-wise Sensitivity 面向 Post-training Quantization of MLLMs
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Spectral Transformation for Layer-wise Global Rank Discovery in Federated LoRA for Vision Transformers](https://arxiv.org/abs/2607.21074)
中文标题：Spectral Transformation 面向 Layer-wise Global Rank Discovery in Federated LoRA 面向 Vision Transformers
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [From Evaluation to Optimisation: Hierarchy-Aware Training Signals for CWE Prediction in Python](https://arxiv.org/abs/2607.21069)
中文标题：来自 评测 to Optimisation：Hierarchy-Aware Training Signals 面向 CWE Prediction in Python
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
