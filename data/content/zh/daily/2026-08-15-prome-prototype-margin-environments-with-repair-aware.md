---
title: "让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升 RAG 检索和知识库问答可靠性"
date: "2026-08-15"
target_date: "2026-08-13"
actual_date: "2026-08-13"
fallback_from: ""
lang: "zh"
slug: "2026-08-15-prome-prototype-margin-environments-with-repair-aware"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "safety", "training", "video-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "safety", "training", "video-generation"]
sources_page: "/zh/daily/2026-08-15-prome-prototype-margin-environments-with-repair-aware-sources/"
generated_at: "2026-08-14T21:36:59.747963+00:00"
page_type: "brief"
candidate_count: 363
featured_count: 6
mentions_count: 20
featured_paper_titles: ["ProME: Prototype-Margin Environments with Repair-Aware Selection for Group-Robust Learning", "TopoIntent: Compiling Security Intent into Executable, Compliance-Checked Network Topologies", "Scaling Representation Diversity: Modulated Attention and Reconstructive Regularization for Visual Grounding", "Who Speaks Matters: Authority-Aware Multi-View RAG over Italian Parliamentary Proceedings", "Learning Unified Video and Image Representation for Video Face Forgery Detection", "Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents"]
featured_paper_urls: ["https://arxiv.org/abs/2608.13190", "https://arxiv.org/abs/2608.13389", "https://arxiv.org/abs/2608.12748", "https://arxiv.org/abs/2608.13410", "https://arxiv.org/abs/2608.13064", "https://arxiv.org/abs/2608.12851"]
featured_paper_titles_zh: ["ProME ：具有维修感知选择的原型边际环境，可实现团队健壮的学习", "TopoIntent ：将安全意图编译为可执行、合规性检查的网络拓扑", "缩放表示多样性：视觉基础的调节注意力和重构正则化", "WHO Speaks Matters: Authority-Aware Multi-View RAG关于意大利议会诉讼", "学习用于视频人脸伪造检测的统一视频和图像表示", "实践使不安全：自我完善法学硕士代理的技能错误演变"]
---

# 让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>ProME: Prototype-Margin Environments with Repair-Aware Selection for Group-Robust Learning (Qianqian Wang, Yunshan Li, Dawei Huang, Wenwu Gong, Lili Yang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.13190">2608.13190</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.13190">PDF</a></p>

中文标题：ProME ：具有维修感知选择的原型边际环境，可实现团队健壮的学习

信号显示：当训练组标签不可用时，群体稳健学习对于保持罕见亚群的准确性至关重要。关键词：rag、deployment、alignment、evaluation。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>TopoIntent: Compiling Security Intent into Executable, Compliance-Checked Network Topologies (Xiaokang Qu, Jianliang Ma, Zao Fan, Tianshu Chu, Tianlong Fan, Linyuan Lü)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.13389">2608.13389</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.13389">PDF</a></p>

中文标题：TopoIntent ：将安全意图编译为可执行、合规性检查的网络拓扑

信号显示：企业安全拓扑设计需要将业务意图、监管要求和风险假设转化为区域、边界设备、区域间路径和访问控制策略。关键词：rag、retrieval、serving、alignment。代码/数据可用性需查看原文确认。

### 3. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Scaling Representation Diversity: Modulated Attention and Reconstructive Regularization for Visual Grounding (Junyi Hu, Tian Bai, Fengyi Wu, Yian Huang, Wei Wen, Zaoli Li, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.12748">2608.12748</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.12748">PDF</a></p>

中文标题：缩放表示多样性：视觉基础的调节注意力和重构正则化

信号显示：参考表达理解（ REC ）通常在特定于数据集的微调下进行研究，从而产生具有有限跨数据集泛化的专业模型。关键词：inference、alignment、benchmark、vision-language。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Who Speaks Matters: Authority-Aware Multi-View RAG over Italian Parliamentary Proceedings (Mirko Tritella, Riccardo Pozzi, Matteo Palmonari)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.13410">2608.13410</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.13410">PDF</a></p>

中文标题：WHO Speaks Matters: Authority-Aware Multi-View RAG关于意大利议会诉讼

信号显示：议会程序是民主审议的主要记录，但其数量和分散性使公民、记者和研究人员难以从多角度进行访问。关键词：rag、retrieval、evaluation、search。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Learning Unified Video and Image Representation for Video Face Forgery Detection (Haotian Liu, Yang Liu, Guoying Zhao, Xiaobai Li)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.13064">2608.13064</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.13064">PDF</a></p>

中文标题：学习用于视频人脸伪造检测的统一视频和图像表示

信号显示：鉴于人脸处理技术和深度生成模型的快速发展，人脸伪造检测对于保持人脸数据的安全性和完整性至关重要。关键词：serving、alignment、benchmark、code。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents (Xutao Mao, Liangjie Zhao, Xiang Zheng, Cong Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.12851">2608.12851</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.12851">PDF</a></p>

中文标题：实践使不安全：自我完善法学硕士代理的技能错误演变

信号显示：自我改进的LLM代理将成功轨迹转化为持续的交叉任务状态。关键词：agent、retrieval、safety、benchmark。代码/数据可用性需查看原文确认。

## 其他值得关注
- [How Good are Foundation Models in Longitudinal MRI Disease Progression Reasoning?](https://arxiv.org/abs/2608.13309)
中文标题：纵向MRI疾病进展推理中的基础模型有多好？
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [VALG: An Agentic System for ML Theory Research](https://arxiv.org/abs/2608.13060)
中文标题：VALG：An Agentic System 面向 ML Theory Research
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [P2Fusion: Prompt-based Progressive Infrared-Visible Image Fusion via Dual-Prior Distillation](https://arxiv.org/abs/2608.13045)
中文标题：P2Fusion ：通过双优先蒸馏进行基于提示的渐进式红外可见图像融合
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [CoMedBench: A Multi-Source Benchmark of Synthetic Medical Data Fidelity and Downstream Utility](https://arxiv.org/abs/2608.12805)
中文标题：CoMedBench：A Multi-Source 基准 of Synthetic Medical Data Fidelity 与 Downstream Utility
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [PatchGen: Learning Soft Intra-Image Predictive Subsets for Visual Generalization](https://arxiv.org/abs/2608.12766)
中文标题：PatchGen：Learning Soft Intra-Image Predictive Subsets 面向 Visual Generalization
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design](https://arxiv.org/abs/2608.13560)
中文标题：AutoDesign：Meta-Harness Optimization 面向 Long-Horizon Agentic Design
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Reduced Matrix Multiplication: Input-Adaptive Matrix-Product Reduction for LLM Inference](https://arxiv.org/abs/2608.13426)
中文标题：简化矩阵乘法： LLM推理的输入-自适应矩阵-乘积简化
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Enhancing Virtual Agents through SLMs and Edge-Computing: An Exploratory Evaluation of Think and Memory Processes](https://arxiv.org/abs/2608.13420)
中文标题：Enhancing Virtual Agents through SLMs 与 Edge-Computing：An Exploratory 评测 of Think 与 Memory Processes
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Rules or Character? Scaling Laws for AI Safety Design](https://arxiv.org/abs/2608.13345)
中文标题：Rules or Character? Scaling Laws 面向 AI Safety Design
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Operationalizing Cyber Threat Intelligence with GraphRAG](https://arxiv.org/abs/2608.13050)
中文标题：使用GraphRAG实现网络威胁情报的运营
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [STAR: Structured Tokenization and Target-Aware Interest Representation for PCVR Prediction](https://arxiv.org/abs/2608.12986)
中文标题：STAR：Structured Tokenization 与 Target-Aware Interest Representation 面向 PCVR Prediction
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Beyond Retrieval: Query-Conditioned Reuse of Long-Horizon Agent Trajectories](https://arxiv.org/abs/2608.12847)
中文标题：超越检索：长期客服代表轨迹的查询条件重用
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Fast A/B/n Testing: Exact Multi-Policy Comparison via Tree-Coupled Feedback Sharing](https://arxiv.org/abs/2608.12831)
中文标题：快速A/B/n测试：通过树耦合反馈共享进行精确的多策略比较
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [HiRoute: Hierarchical Routed Prompt Tuning for Safety Alignment of Large Language Models](https://arxiv.org/abs/2608.12821)
中文标题：HiRoute：Hierarchical Routed Prompt Tuning 面向 Safety Alignment of Large Language Models
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Query Translation vs. Cross-Lingual Embeddings for Sinhala-Tamil E-Government Information Retrieval](https://arxiv.org/abs/2608.12820)
中文标题：僧伽罗语-泰米尔语电子政务信息检索的查询翻译与跨语言嵌入
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives](https://arxiv.org/abs/2608.13552)
中文标题：PlayWorld：基准ing 世界模型 with Agent Players over Long-Horizon Objectives
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Vero: Can AI Agents Build Formally Verified Software Repositories?](https://arxiv.org/abs/2608.13522)
中文标题：Vero ：人工智能代理能否构建经过正式验证的软件存储库？
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval](https://arxiv.org/abs/2608.13495)
中文标题：TraVEL：Trajectory-Guided Video Embedding Learning 面向 Driving-Video Retrieval
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination](https://arxiv.org/abs/2608.13476)
中文标题：MARC v1：An Open-Source Multi-Agent 框架 面向 Clinical AI Reasoning 与 Coordination
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Mind the Context: Continual Learning of Socially Appropriate Robot Actions via Environmental-Social Disentanglement](https://arxiv.org/abs/2608.13448)
中文标题：注意背景：通过环境-社会解体不断学习适合社会的机器人行为
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
