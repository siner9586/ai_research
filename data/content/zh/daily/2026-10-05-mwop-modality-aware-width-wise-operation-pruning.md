---
title: "提升 RAG 检索和知识库问答可靠性、提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力"
date: "2026-10-05"
target_date: "2026-10-03"
actual_date: "2026-10-01"
fallback_from: "2026-10-03"
lang: "zh"
slug: "2026-10-05-mwop-modality-aware-width-wise-operation-pruning"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "systems", "training", "video-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-10-05-mwop-modality-aware-width-wise-operation-pruning-sources/"
generated_at: "2026-10-04T23:58:03.997121+00:00"
page_type: "brief"
candidate_count: 640
featured_count: 6
mentions_count: 20
featured_paper_titles: ["MWOP: Modality-aware Width-wise Operation Pruning for Efficient MLLMs", "AF-Muon: An AdamW-Free Muon Optimizer for Tied-Embedding Models", "PRISM: A Category-Theoretic Framework for Measuring and Refining Multimodal Analogies", "GPU-Initiated Communication: Dissecting Down to the Bone", "PACE: Provenance-Aware Capability Enforcement for Tool-Using LLM Agents", "HHR: Hierarchical Hash Retrieval for Efficient LLM Generation"]
featured_paper_urls: ["https://arxiv.org/abs/2610.01434", "https://arxiv.org/abs/2610.01395", "https://arxiv.org/abs/2610.01383", "https://arxiv.org/abs/2610.01380", "https://arxiv.org/abs/2610.01349", "https://arxiv.org/abs/2610.01230"]
featured_paper_titles_zh: ["MWOP：Modality-aware Width-wise Operation Pruning 面向 Efficient MLLMs", "AF-Muon：An AdamW-Free Muon Optimizer 面向 Tied-Embedding Models", "PRISM：A Category-Theoretic 框架 面向 Measuring 与 Refining Multimodal Analogies", "GPU启动的通信：解剖到骨头", "PACE：Provenance-Aware Capability Enforcement 面向 Tool-使用 LLM Agents", "HHR：Hierarchical Hash Retrieval 面向 Efficient LLM Generation"]
---

# 提升 RAG 检索和知识库问答可靠性、提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、提升代码生成、执行反馈和自动修复能力、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>MWOP: Modality-aware Width-wise Operation Pruning for Efficient MLLMs (Xudong Wang, Hao Wu, Haozhe Hu, Peiran Yin, Xinghao Chen, Yunpu Ma, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.01434">2610.01434</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.01434">PDF</a></p>

中文标题：MWOP：Modality-aware Width-wise Operation Pruning 面向 Efficient MLLMs

信号显示：多模态大语言模型（ MLLM ）在处理长视觉文本序列时会产生相当大的推理成本。关键词：rag、inference、compression、benchmark。代码/数据可用性需查看原文确认。

### 2. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>AF-Muon: An AdamW-Free Muon Optimizer for Tied-Embedding Models (Arash Lagzian, Paniz Halvachi, Junming Zhang, Zhouhan Lin, Dianbo Liu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.01395">2610.01395</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.01395">PDF</a></p>

中文标题：AF-Muon：An AdamW-Free Muon Optimizer 面向 Tied-Embedding Models

信号显示：Muon通过对矩阵参数应用谱范数最陡下降更新来改进大规模训练，但实用模型还包含不适合密集矩阵几何的参数块。关键词：benchmark、code、memory、image。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>PRISM: A Category-Theoretic Framework for Measuring and Refining Multimodal Analogies (Mirella Zeisler, Ojas Shirekar, Mircea Licǎ, Chirag Raman)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.01383">2610.01383</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.01383">PDF</a></p>

中文标题：PRISM：A Category-Theoretic 框架 面向 Measuring 与 Refining Multimodal Analogies

信号显示：类比推理涉及识别和保存跨领域的关系结构。关键词：serving、alignment、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 4. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>GPU-Initiated Communication: Dissecting Down to the Bone (Javid Baydamirli, Ismayil Ismayilov, Kaan Oktay, Didem Unat)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.01380">2610.01380</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.01380">PDF</a></p>

中文标题：GPU启动的通信：解剖到骨头

信号显示：GPU启动的通信允许GPU线程将RDMA操作直接发布到NIC。关键词：latency、code、memory、throughput。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>PACE: Provenance-Aware Capability Enforcement for Tool-Using LLM Agents (Fengpeng Li, Qizhou Wang, Yuke Hu, Kemou Li, Jun Liu, Haiwei Wu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.01349">2610.01349</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.01349">PDF</a></p>

中文标题：PACE：Provenance-Aware Capability Enforcement 面向 Tool-使用 LLM Agents

信号显示：使用工具的大语言模型（ LLM ）代理将生成的文本转化为真正的副作用，因此中毒的工具元数据、检索到的页面、内存和可重用技能可以引导下一次调用。关键词：agent、deployment、benchmark、memory。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>HHR: Hierarchical Hash Retrieval for Efficient LLM Generation (Lianjun Liu, Tiantian Zheng, You Huang, Weiqi Yan, Mingte Qiu, Huazhong Liu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2610.01230">2610.01230</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2610.01230">PDF</a></p>

中文标题：HHR：Hierarchical Hash Retrieval 面向 Efficient LLM Generation

信号显示：高效的长上下文推理对于大语言模型（ LLM ）至关重要，但它构成了严重的计算瓶颈。关键词：rag、retrieval、inference、serving。代码/数据可用性需查看原文确认。

## 其他值得关注
- [ITC-MoE: Importance-guided Token-aware Compression for MoE Diffusion Language Models](https://arxiv.org/abs/2610.01296)
中文标题：ITC-MoE：Importance-guided Token-aware Compression 面向 MoE Diffusion Language Models
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CineMR: Tool-Integrated Vision-Language Reasoning for Quantitative Cardiac MRI Assessment](https://arxiv.org/abs/2610.01166)
中文标题：CineMR：Tool-Integrated Vision-Language Reasoning 面向 Quantitative Cardiac MRI 评估
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [CortexBridge: Cortical Alignment of EEG Montages for Foundation Models](https://arxiv.org/abs/2610.01124)
中文标题：CortexBridge：Cortical Alignment of EEG Montages 面向 Foundation Models
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [AgSpec: Pushing the Limits of Retrieval-Based Speculative Decoding in Coding Agent Pipelines](https://arxiv.org/abs/2610.01108)
中文标题：AgSpec ：突破编码代理管道中基于检索的投机解码的极限
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [MVDG: Efficient Multi-view 3D Disambiguation on Unconstrained Real-World Images](https://arxiv.org/abs/2610.01098)
中文标题：MVDG ：在无约束的真实世界图像上高效消除多视图3D歧义
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MOMAT: Mixture of Multiple Atlases for Low-Power Jailbreak Defense of Quantized LLMs](https://arxiv.org/abs/2610.01058)
中文标题：MOMAT：Mixture of Multiple Atlases 面向 Low-Power Jailbreak Defense of Quantized LLMs
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Capturing In-Context Learning Dynamics with Task Operators](https://arxiv.org/abs/2610.01054)
中文标题：使用任务操作员捕捉上下文学习动态
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [FutureWorlds: Learning Robotic World Models from Alternative Futures](https://arxiv.org/abs/2610.01019)
中文标题：FutureWorlds：Learning Robotic 世界模型 来自 Alternative Futures
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [VASC: Value-Aware Sparse Attention with Cross-Layer Memory for Efficient 3D Reconstruction](https://arxiv.org/abs/2610.01013)
中文标题：VASC ：具有跨层内存的价值感知稀疏注意力，可实现高效的3D重建
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [HADRec: A Hierarchy-Aware Drug Recommendation Framework by Fusing Molecular Knowledge and Electronic Health Record](https://arxiv.org/abs/2610.00984)
中文标题：HADRec：A Hierarchy-Aware Drug Recommendation 框架 by Fusing Molecular Knowledge 与 Electronic Health Record
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Can AI Scientists Coordinate at Runtime?](https://arxiv.org/abs/2610.00980)
中文标题：人工智能科学家可以在运行时进行协调吗？
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Generalist Representation, Specialist Detection: TS-Router for Time-Series Anomaly Detection](https://arxiv.org/abs/2610.00978)
中文标题：通用表示、专家检测：用于时间序列异常检测的TS路由器
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack](https://arxiv.org/abs/2610.00973)
中文标题：概念驱动的领域适应：在大海捞针中寻找抽象之针
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Finding the Right Fit: Model-Harness Interactions across Agent Tasks](https://arxiv.org/abs/2610.00917)
中文标题：找到合适的选项：跨客服代表任务的模型-线束交互
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [DeBERTa-ConPara: Attack-Aware and Deployment-Realistic Detection of AI-Generated Text](https://arxiv.org/abs/2610.00883)
中文标题：DeBERTa-ConPara：Attack-Aware 与 Deployment-Realistic Detection of AI-Generated Text
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Kinematic MeanFlow: One-Step Action Generation Policy for Robotic Foundation Models](https://arxiv.org/abs/2610.00864)
中文标题：Kinematic MeanFlow：One-Step Action Generation Policy 面向 Robotic Foundation Models
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [AuraForge: Scaling Security Supervision for Training Coding Agents](https://arxiv.org/abs/2610.00850)
中文标题：AuraForge：Scaling Security Supervision 面向 Training Coding Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ROWBench: Do Video Models Render What the Program Specifies?](https://arxiv.org/abs/2610.02205)
中文标题：ROWBench ：视频模型是否渲染程序指定的内容？
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Trust the Direction, Search the Step: Zero-and-First-Order Methods for LLM Fine-Tuning](https://arxiv.org/abs/2610.02190)
中文标题：相信方向，搜索步骤： LLM微调的零和一阶方法
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Keyword Harnesses Fail Open: A Cheap Diagnostic Ladder for Tool-Use Claims in Small Language Models](https://arxiv.org/abs/2610.02142)
中文标题：关键词线束失效开放：小语言模型中工具使用索赔的廉价诊断阶梯
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
