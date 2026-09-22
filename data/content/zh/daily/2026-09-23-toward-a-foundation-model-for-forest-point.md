---
title: "提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-09-23"
target_date: "2026-09-21"
actual_date: "2026-09-21"
fallback_from: ""
lang: "zh"
slug: "2026-09-23-toward-a-foundation-model-for-forest-point"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "data-engineering", "evaluation", "interpretability", "multimodal", "robotics", "safety", "systems", "training", "video-generation"]
topics: ["agents", "data-engineering", "evaluation", "interpretability", "multimodal", "robotics", "safety", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-09-23-toward-a-foundation-model-for-forest-point-sources/"
generated_at: "2026-09-22T23:36:16.612537+00:00"
page_type: "brief"
candidate_count: 432
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Toward a foundation model for forest point clouds", "RRSI: Regularized Recursive Self-Improvement of Agent Harnesses", "DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security", "MedRSI: Recursive Self-Improvement for Medical Agents via Clinically Aligned Self-Evolution", "0.5\\%>100\\%: Bidirectional Reciprocal Learning for Referring Image Segmentation", "High-Dimensional Online Change Point Detection with Adaptive Thresholding and Interpretability"]
featured_paper_urls: ["https://arxiv.org/abs/2609.24787", "https://arxiv.org/abs/2609.24972", "https://arxiv.org/abs/2609.24662", "https://arxiv.org/abs/2609.24838", "https://arxiv.org/abs/2609.24510", "https://arxiv.org/abs/2609.24278"]
featured_paper_titles_zh: ["面向森林点云的基础模型", "RRSI ：药剂线束的规则化递归自我改善", "DUMA-Bench ：评估LLM Agent安全性的双控多Agent基准", "MedRSI ：通过临床一致性自我进化对医疗人员进行递归自我改善", "0.5\\ % > 100\\ % ：引用图像分割的双向相互学习", "具有自适应阈值和可解释性的高维在线变更点检测"]
---

# 提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Toward a foundation model for forest point clouds (Yuanwen Yue, Stefano Puliti, Damien Robert, Atakan Topaloğlu, Binbin Xiang, Maciej Wielgosz, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.24787">2609.24787</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.24787">PDF</a></p>

中文标题：面向森林点云的基础模型

信号显示：森林库存越来越依赖于人工智能（ AI ）模型从大规模3D点云中获取森林属性。关键词：benchmark、code、eval、evaluation。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>RRSI: Regularized Recursive Self-Improvement of Agent Harnesses (Peng Xia, Rujun Han, Zifeng Wang, Yanfei Chen, Yufan Zhang, Yoonho Lee, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.24972">2609.24972</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.24972">PDF</a></p>

中文标题：RRSI ：药剂线束的规则化递归自我改善

信号显示：LLM代理的能力在很大程度上通过其利用来放大，即围绕冷冻骨干模型的提示、控制流、工具、内存和上下文管理。关键词：agent、rag、benchmark、code。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security (Ivan Aleksandrov, German Kochnev, Sabrina Sadiekh, Yaroslav Rogoza)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.24662">2609.24662</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.24662">PDF</a></p>

中文标题：DUMA-Bench ：评估LLM Agent安全性的双控多Agent基准

信号显示：基于LLM的代理越来越多地在与用户、工具和外部系统交互的环境中运行。关键词：agent、rag、deployment、evaluation。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>MedRSI: Recursive Self-Improvement for Medical Agents via Clinically Aligned Self-Evolution (Junde Wu, Jiayuan Zhu, Minghao Hu, Fenglin Liu, Jiazhen Pan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.24838">2609.24838</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.24838">PDF</a></p>

中文标题：MedRSI ：通过临床一致性自我进化对医疗人员进行递归自我改善

信号显示：医疗代理商越来越多地将一般推理模型与专门的临床工具相结合，但他们的能力在很大程度上仍然取决于临床医生和工程师在部署前的设计。关键词：agent、deployment、safety、benchmark。代码/数据可用性需查看原文确认。

### 5. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>0.5\%&gt;100\%: Bidirectional Reciprocal Learning for Referring Image Segmentation (Xiaoqiang Lu, Licheng Jiao, Lingling Li, Yuting Yang, Long Sun, Wenping Ma, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.24510">2609.24510</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.24510">PDF</a></p>

中文标题：0.5\ % > 100\ % ：引用图像分割的双向相互学习

信号显示：视觉基础模型(VFM)的最新进展在各种单模态视觉任务中显示出非凡的能力。关键词：alignment、benchmark、code、vision-language。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>High-Dimensional Online Change Point Detection with Adaptive Thresholding and Interpretability (Sven Jacob, Bardh Prenkaj, Weijia Shao, Gjergji Kasneci)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.24278">2609.24278</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.24278">PDF</a></p>

中文标题：具有自适应阈值和可解释性的高维在线变更点检测

信号显示：变更点检测（ CPD ）识别连续数据的突然和重大变化，应用于人类活动识别、金融市场、网络安全、制造和自主系统。关键词：rag、deployment、code、interpretability。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Incentive Noise and Structural Prior Infusion for Multi-modal Object Re-Identification](https://arxiv.org/abs/2609.24539)
中文标题：用于多模式物体重新识别的激励噪声和结构事先输注
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [When Evidence Conflicts: Reliability-aware Meta-review Generation](https://arxiv.org/abs/2609.24028)
中文标题：当证据发生冲突时：具有可靠性感知的元审核生成
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Who Pays for the KV Cache? Attributing Shared AI Inference Spend Across Kubernetes and LLM Provider Bills](https://arxiv.org/abs/2609.24991)
中文标题：谁为KV缓存付费？在Kubernetes和LLM提供商账单中归因共享AI推断支出
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Rare Event Estimation via Iterative Unalignment](https://arxiv.org/abs/2609.24969)
中文标题：通过迭代不对齐的罕见事件估计
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [PrismGPT: Proxy-Guided Learning for Region-Aware Photo Editing with Self-Synthesized Reasoning](https://arxiv.org/abs/2609.24768)
中文标题：PrismGPT ：基于自合成推理的区域感知照片编辑代理引导式学习
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [D-JEPA: A Decision-Aligned Latent World Model](https://arxiv.org/abs/2609.24749)
中文标题：D-JEPA ：与决策相一致的潜在世界模型
关注理由：涉及机器人与具身智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [AlignMorph: Tuning-Free Diffusion Image Morphing via Explicit Semantic Transport](https://arxiv.org/abs/2609.24330)
中文标题：AlignMorph ：通过显式语义传输实现无调整扩散图像变形
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [A$^2$Safe: Counterfactual Evidence-Aligned Adaptive Agent Collaboration for Safe and Effective Visual Question Answering](https://arxiv.org/abs/2609.24098)
中文标题：A$^2$Safe：Counterfactual Evidence-Aligned Adaptive Agent Collaboration 面向 Safe 与 Effective Visual Question Answering
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [ACLArena: Agent Continue Learning in Multi-stage Post-training](https://arxiv.org/abs/2609.23989)
中文标题：ACLArena ：客服代表在多阶段培训后继续学习
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [LEAP-NBV: Lightweight Edge Active-Perception for Foundation-Model Next-Best-View Planning](https://arxiv.org/abs/2609.23974)
中文标题：LEAP-NBV：Lightweight Edge Active-Perception 面向 Foundation-Model Next-Best-View Planning
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [SPHQuant: Efficient extreme low bit weight quantization for Vision-Language Models](https://arxiv.org/abs/2609.24875)
中文标题：SPHQuant：Efficient extreme low bit weight quantization 面向 Vision-Language Models
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [When Quantization Preserves Accuracy but Not Evidence: Explanation-Aware Post-Training Quantization for Medical LLMs](https://arxiv.org/abs/2609.24799)
中文标题：当量化保持准确性但没有证据时：医疗LLM的解释感知训练后量化
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [GraphSVR: q-Space--Aware Graph-Based Slice-to-Volume Registration for Diffusion MRI](https://arxiv.org/abs/2609.24732)
中文标题：GraphSVR：q-Space--Aware Graph-Based Slice-to-Volume Registration 面向 Diffusion MRI
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [ReSTI: A Source-Grounded Audit and Repair of STI-Bench](https://arxiv.org/abs/2609.24727)
中文标题：ReSTI：A Source-Grounded Audit 与 Repair of STI-Bench
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Think Like a World Model, Act Like a VLA: Distilling World-Model Representations into Compact Robot Policies](https://arxiv.org/abs/2609.24682)
中文标题：像世界模型一样思考，像VLA一样行动：将世界模型表征提炼成紧凑型机器人政策
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Augmented Hypothesis Testing with Persona-Based LLM Simulations](https://arxiv.org/abs/2609.24629)
中文标题：使用基于角色的LLM模拟进行增强假设测试
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [FedMust: Semi-supervised Multi-task Student-Teacher Federated Learning for Multi-organ CT Segmentation](https://arxiv.org/abs/2609.24627)
中文标题：FedMust：Semi-supervised Multi-task Student-Teacher Federated Learning 面向 Multi-organ CT Segmentation
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Learning tactile perception from high-bandwidth single-point sensing](https://arxiv.org/abs/2609.24621)
中文标题：从高带宽单点感知中学习触觉感知
关注理由：涉及机器人与具身智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Taking a Second Look: Correcting Sea Ice Forecasts with Sparse Observations](https://arxiv.org/abs/2609.24591)
中文标题：重新审视：用稀疏观测修正海冰预报
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [HyperCLIP++: Fine-tuning CLIP forOpen-vocabulary Semantic Segmentation in Hyperbolic Space](https://arxiv.org/abs/2609.24564)
中文标题：HyperCLIP + + ：双曲空间中开放词汇语义分割的微调剪辑
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
