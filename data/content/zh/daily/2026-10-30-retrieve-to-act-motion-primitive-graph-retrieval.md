---
title: "提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险"
date: "2026-10-30"
target_date: "2026-10-28"
actual_date: "2026-10-27"
fallback_from: "2026-10-28"
lang: "zh"
slug: "2026-10-30-retrieve-to-act-motion-primitive-graph-retrieval"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "safety", "systems", "training", "video-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "safety", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-10-30-retrieve-to-act-motion-primitive-graph-retrieval-sources/"
generated_at: "2026-10-29T16:53:00.765450+00:00"
page_type: "brief"
candidate_count: 521
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution", "Does Your Generalist Skill Optimizer Really Incentivize Agentic Tasks? Rethinking Skill Optimization via Bipartite Attribution", "FastBEVFusion: Simple Multi-Modal Fusion for 3D Object Detection at 50 FPS", "GCSR-OCC: Geometry Calibration and Semantic Routing for Open-Vocabulary Occupancy Prediction", "Learning to Look Beyond Screens: Transferable Visual Observation from GUI Grounding", "Tessera: Structure-Completed Evidence Units for Web Retrieval-Augmented Generation"]
featured_paper_urls: ["https://arxiv.org/abs/2610.37215", "https://arxiv.org/abs/2610.37201", "https://arxiv.org/abs/2610.37153", "https://arxiv.org/abs/2610.37149", "https://arxiv.org/abs/2610.37093", "https://arxiv.org/abs/2610.37080"]
featured_paper_titles_zh: ["Retrieve to Act：Motion Primitive Graph Retrieval 面向 Robust VLA Execution", "您的多面手技能优化器是否真的激励了代理任务？通过双方归因重新思考技能优化", "FastBEVFusion：Simple Multi-Modal Fusion 面向 3D Object Detection at 50 FPS", "GCSR-OCC：Geometry Calibration 与 Semantic Routing 面向 Open-Vocabulary Occupancy Prediction", "Learning to Look Beyond Screens：Transferable Visual Observation 来自 GUI 落地", "Tessera：Structure-Completed Evidence Units 面向 Web Retrieval-Augmented Generation"]
---

# 提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution (Pham Tri Quang, Bao-Ngoc Dao, Minh Duc Nguyen, Duc-Duy Nguyen, Hung T. Ho, Linh Dang Le, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.37215">2610.37215</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.37215">PDF</a></p>

中文标题：Retrieve to Act：Motion Primitive Graph Retrieval 面向 Robust VLA Execution

信号显示：视觉-语言-行动（ VLA ）策略表现出显着的语义泛化，但在执行期间仍然非常容易受到分布外（ OOD ）视觉变化的影响。关键词：rag、retrieval、inference、serving。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Does Your Generalist Skill Optimizer Really Incentivize Agentic Tasks? Rethinking Skill Optimization via Bipartite Attribution (Jiawei Zhou, Bo Peng, Yuxuan Huang, Ming Zhang, Youbang Sun, Xiang Wang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.37201">2610.37201</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.37201">PDF</a></p>

中文标题：您的多面手技能优化器是否真的激励了代理任务？通过双方归因重新思考技能优化

信号显示：技能优化器通过重写其技能（其上下文中的自然语言过程）并保留在一个小开发集上提高成功的编辑来使代理适应长时间任务，例如修复终端环境。关键词：agent、rag、benchmark、code。代码/数据可用性需查看原文确认。

### 3. 识别并缓解模型安全、越狱和对齐风险

<p class="paper-meta-line"><span>FastBEVFusion: Simple Multi-Modal Fusion for 3D Object Detection at 50 FPS (Tom Sanitz, Emre Gülsoylu, Simone Frintrop, Christian Wilms)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.37153">2610.37153</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.37153">PDF</a></p>

中文标题：FastBEVFusion：Simple Multi-Modal Fusion 面向 3D Object Detection at 50 FPS

信号显示：基于LiDAR和摄像头数据的可靠实时3D物体检测对于自动驾驶的安全至关重要，系统必须以最小的延迟准确感知周围环境。关键词：deployment、latency、safety、data。代码/数据可用性需查看原文确认。

### 4. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>GCSR-OCC: Geometry Calibration and Semantic Routing for Open-Vocabulary Occupancy Prediction (Bohua Wang, Congyang Zhao, Tianxiong Lv, Chenxu Zhao, He Zheng, Hangqi Fan, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.37149">2610.37149</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.37149">PDF</a></p>

中文标题：GCSR-OCC：Geometry Calibration 与 Semantic Routing 面向 Open-Vocabulary Occupancy Prediction

信号显示：开放式词汇表3D占用预测表示统一体素网格中的场景几何和语义，实现超出预定义类别的识别。关键词：serving、latency、alignment、code。代码/数据可用性需查看原文确认。

### 5. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Learning to Look Beyond Screens: Transferable Visual Observation from GUI Grounding (Ruilin Yao, Xinyu Qiu, Tianyu Zou, Yi Rong, Shengwu Xiong, Shuheng Shen, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.37093">2610.37093</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.37093">PDF</a></p>

中文标题：Learning to Look Beyond Screens：Transferable Visual Observation 来自 GUI 落地

信号显示：视觉感知正在从被动识别演变为主动的、以任务为导向的观察。关键词：inference、code、multimodal、vision-language。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Tessera: Structure-Completed Evidence Units for Web Retrieval-Augmented Generation (Peichun Hua, He Sun, Zirui Zhuang, Qi Qi, Yiming Qiu, Shinan Liu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.37080">2610.37080</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.37080">PDF</a></p>

中文标题：Tessera：Structure-Completed Evidence Units 面向 Web Retrieval-Augmented Generation

信号显示：Web检索增强生成（ RAG ）将页面拆分为固定大小的文本块，或者在最近的可视化管道中，屏幕截图图块，检索到的项目同时作为索引、排名和阅读的单位。关键词：agent、rag、retrieval、benchmark。代码/数据可用性需查看原文确认。

## 其他值得关注
- [SplatScout: Query-Driven Part-Level Referring Segmentation in Gaussian Scenes](https://arxiv.org/abs/2610.37098)
中文标题：SplatScout ：高斯场景中的查询驱动部分级引用分割
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [V-LUMEN: Visual Lookup Memory for Embedding Scaling in Vision-Language Models](https://arxiv.org/abs/2610.37019)
中文标题：V-LUMEN：Visual Lookup Memory 面向 Embedding Scaling in Vision-Language Models
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Proactive Memory for Event-Driven LLM Agents](https://arxiv.org/abs/2610.36967)
中文标题：事件驱动型LLM客服代表的主动内存
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [When Diffusion Recommenders Stop Sampling: Preserving Generative Diversity](https://arxiv.org/abs/2610.36954)
中文标题：当扩散推荐者停止采样时：保护生成多样性
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Algorithmic Monoculture in Machine Learning-based Site-Specific Fertilizer Recommendation](https://arxiv.org/abs/2610.36941)
中文标题：基于机器学习的场地特异性肥料推荐中的算法单一培养
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Vision-Language Agents Can Learn in Their Own Latent Worlds](https://arxiv.org/abs/2610.36925)
中文标题：视觉语言经纪人可以在自己的潜在世界中学习
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG](https://arxiv.org/abs/2610.36915)
中文标题：我们是否需要LLM来了解源冲突的原因？ RAG中知识冲突打字的决策模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents](https://arxiv.org/abs/2610.36877)
中文标题：GUI-JEPA：Candidate-Conditioned JEPA Latents as a Fast Action Policy 面向 Mobile GUI Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [uTHCD-C: A Corruption-Robustness Benchmark for Tamil Handwritten Character Recognition](https://arxiv.org/abs/2610.36850)
中文标题：uTHCD-C：A Corruption-Robustness 基准 面向 Tamil Handwritten Character Recognition
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Latent Visual Contrastive Reasoning with Multi-Branch Exploration](https://arxiv.org/abs/2610.36809)
中文标题：多分支探索的潜在视觉对比推理
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Making Self-Driving Laboratories Auditable:A Unified Framework for Hybrid Actions,Measurements, and Safe Execution](https://arxiv.org/abs/2610.36761)
中文标题：使自动驾驶实验室可审计：混合行动、测量和安全执行的统一框架
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Efficient Remote Sensing Image-Text Retrieval via Interaction-Free Recall and Text-Guided Reranking](https://arxiv.org/abs/2610.36756)
中文标题：通过无交互召回和文本引导排序进行高效的遥感图像文本检索
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Nonlinear Direct Feedback Alignment for Scalable Backpropagation-Free Training](https://arxiv.org/abs/2610.36718)
中文标题：用于可扩展的无反向传播训练的非线性直接反馈对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Conservative Dueling Bandits: Preference Learning under Baseline Constraints](https://arxiv.org/abs/2610.36708)
中文标题：保守决斗强盗：基线约束下的偏好学习
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Haste Makes Waste? Towards Safe Few-Step Text-to-Image Models](https://arxiv.org/abs/2610.36665)
中文标题：匆忙造成浪费？朝着安全的几步文字转图像模型迈进
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SAGE: Semantic-Augmented Geometric Experts for Point Cloud Registration](https://arxiv.org/abs/2610.36658)
中文标题：SAGE：Semantic-Augmented Geometric Experts 面向 Point Cloud Registration
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [TACO-Graph: Automated Construction of Text-Atributed Graphs](https://arxiv.org/abs/2610.36650)
中文标题：TACO-Graph ：文本属性图的自动构建
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Deep Bayesian Approaches for Interpretable Nonlinear Structural System Identification](https://arxiv.org/abs/2610.36633)
中文标题：可解释非线性结构系统辨识的深贝叶斯方法
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MM-Net: A Multimodal Multi-Task Network for Sleep Staging and Sleep Apnea Assessment After Ischemic Stroke](https://arxiv.org/abs/2610.36583)
中文标题：MM-Net：A Multimodal Multi-Task Network 面向 Sleep Staging 与 Sleep Apnea 评估 After Ischemic Stroke
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [ADTGuard: Adaptive Depth-Time Safeguard for Streaming Inference in Large Language Models](https://arxiv.org/abs/2610.36574)
中文标题：ADTGuard：Adaptive Depth-Time Safeguard 面向 Streaming Inference in Large Language Models
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
