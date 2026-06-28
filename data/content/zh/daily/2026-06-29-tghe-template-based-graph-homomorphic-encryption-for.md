---
title: "提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能"
date: "2026-06-29"
target_date: "2026-06-27"
actual_date: "2026-06-25"
fallback_from: "2026-06-27"
lang: "zh"
slug: "2026-06-29-tghe-template-based-graph-homomorphic-encryption-for"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "rag", "reasoning", "speech-audio", "systems", "training", "video-generation", "vision-generation"]
topics: ["agents", "code", "evaluation", "rag", "reasoning", "speech-audio", "systems", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-06-29-tghe-template-based-graph-homomorphic-encryption-for-sources/"
generated_at: "2026-06-28T22:13:23.340335+00:00"
page_type: "brief"
candidate_count: 386
featured_count: 6
mentions_count: 20
featured_paper_titles: ["TGHE: Template-based Graph Homomorphic Encryption for Privacy-Preserving GNN Inference in Edge-Cloud Systems", "LAMP: Lane-Aligned Motion Primitives for Feasible Trajectory Prediction", "Autoformalization of Agent Instructions into Policy-as-Code", "LayersReg: A Layer-by-Layer Progressive Regressor for Reliable Intraoperative 3D/2D Registration", "SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference", "IDEA: Insensitive to Dynamics Mismatch via Effect Alignment for Sim-to-Real Transfer in Multi-Agent Control"]
featured_paper_urls: ["https://arxiv.org/abs/2606.26664", "https://arxiv.org/abs/2606.26661", "https://arxiv.org/abs/2606.26649", "https://arxiv.org/abs/2606.26647", "https://arxiv.org/abs/2606.26587", "https://arxiv.org/abs/2606.26575"]
featured_paper_titles_zh: ["TGHE：Template-based Graph Homomorphic Encryption 面向 隐私保护 GNN Inference in Edge-Cloud Systems", "LAMP：Lane-Aligned Motion Primitives 面向 Feasible Trajectory Prediction", "将代理说明自动格式化为策略即代码", "LayersReg：A Layer-by-Layer Progressive Regressor 面向 Reliable Intraoperative 3D/2D Registration", "SharQ：Bridging Activation Sparsity 与 FP4 Quantization 面向 LLM Inference", "创意：在多Agent控制中，通过Sim-to-Real传输的效果对动态不匹配不敏感"]
---

# 提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>TGHE: Template-based Graph Homomorphic Encryption for Privacy-Preserving GNN Inference in Edge-Cloud Systems (Ngoc Bao Anh Le, Thai T. Vu, John Le, Heath Cooper, Jun Shen)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.26664">2606.26664</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.26664">PDF</a></p>

中文标题：TGHE：Template-based Graph Homomorphic Encryption 面向 隐私保护 GNN Inference in Edge-Cloud Systems

信号显示：现有的基于同态加密（ HE ）的GNN系统采用以图为中心的范式，将每次查询的成本与全局图大小相结合，将评估限制在最多约2万个节点，并使其与动态的大规模财务图不兼容。关键词：rag、inference、serving、evaluation。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>LAMP: Lane-Aligned Motion Primitives for Feasible Trajectory Prediction (Sangjin Han, Hoseong Jung, Jeongtae Her, Changhyun Choi, H. Jin Kim)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.26661">2606.26661</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.26661">PDF</a></p>

中文标题：LAMP：Lane-Aligned Motion Primitives 面向 Feasible Trajectory Prediction

信号显示：运动预测对于自动驾驶系统在复杂的驾驶场景中实现安全决策和规划至关重要。关键词：serving、safety、code、multimodal。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Autoformalization of Agent Instructions into Policy-as-Code (Adam Mondl, Matthew Maisel, John H. Brock)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.26649">2606.26649</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.26649">PDF</a></p>

中文标题：将代理说明自动格式化为策略即代码

信号显示：高风险领域的代理安全需要正式的政策执行，但大多数现有方法要么依赖于没有正式保证的概率护栏（微调的分类器，基于提示的转向） ，要么依赖于手工编码的符号执行。关键词：agent、safety、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>LayersReg: A Layer-by-Layer Progressive Regressor for Reliable Intraoperative 3D/2D Registration (Xiyuan Wang, Zhenchao Wang, Xinran Chen, Junkai Liu, Chuan Chen, Feng Yin)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.26647">2606.26647</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.26647">PDF</a></p>

中文标题：LayersReg：A Layer-by-Layer Progressive Regressor 面向 Reliable Intraoperative 3D/2D Registration

信号显示：3D/2D配准是手术导航的基石技术。关键词：retrieval、alignment、multimodal、memory。代码/数据可用性需查看原文确认。

### 5. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference (Haoqian Meng, Yilun Luo, Yafei Zhao, Wenyuan Liu, Huaqing Zheng, Xindian Ma, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.26587">2606.26587</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.26587">PDF</a></p>

中文标题：SharQ：Bridging Activation Sparsity 与 FP4 Quantization 面向 LLM Inference

信号显示：现代加速器越来越多地支持低位浮点格式和半结构化稀疏性，但将它们组合用于LLM激活压缩仍然具有挑战性：激活包含主导FP4中块规模的输入相关异常值。关键词：inference、serving、latency、compression。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>IDEA: Insensitive to Dynamics Mismatch via Effect Alignment for Sim-to-Real Transfer in Multi-Agent Control (Chenlong Liu, Zhuohui Zhang, Xinyan Chen, Zhipeng Wang, Bin Cheng, Bin He)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.26575">2606.26575</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.26575">PDF</a></p>

中文标题：创意：在多Agent控制中，通过Sim-to-Real传输的效果对动态不匹配不敏感

信号显示：对于传统的基于规则和基于模型的方法，复杂的多智能体控制任务仍然具有挑战性，这促使采用基于学习的方法。关键词：agent、rag、deployment、alignment。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents](https://arxiv.org/abs/2606.26627)
中文标题：了解太多的代理：以数据为中心的LLM代理隐私调查
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Can Large Language Models Reliably Code Qualitative Humanitarian Data? A Benchmark Study Against Human Expert Adjudication](https://arxiv.org/abs/2606.26541)
中文标题：大型语言模型能否可靠地编码定性人道主义数据？针对人类专家裁决的基准研究
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [NeuraDock Visual Cognitive Load Agent Tutorial: A Quality-Gated Open-Source EEG Workflow for Alpha Dynamics and Real-Time Applications](https://arxiv.org/abs/2606.26518)
中文标题：NeuraDock Visual Cognitive Load Agent Tutorial：A Quality-Gated Open-Source EEG Workflow 面向 Alpha Dynamics 与 Real-Time Applications
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Speaking Numbers to LLMs: Multi-Wavelet Number Embeddings for Time Series Forecasting](https://arxiv.org/abs/2606.26487)
中文标题：向LLM讲述数字：用于时间序列预测的多小波数嵌入
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents](https://arxiv.org/abs/2606.26479)
中文标题：对LLM药剂中针对快速注射的带外防御进行自适应评估
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Don't Settle at the Mode! Mitigating Diversity Collapse in Pretrained Flow Models via Feature Self-Guidance](https://arxiv.org/abs/2606.27371)
中文标题：不要沉溺于这种模式！通过特征自导缓解预训练流程模型中的多样性崩溃
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems](https://arxiv.org/abs/2606.27243)
中文标题：NOVA：A Verification-Aware Agent Harness 面向 Architecture Evolution in Industrial Recommender Systems
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement](https://arxiv.org/abs/2606.27226)
中文标题：Ask，Don't Judge：Binary Questions 面向 Interpretable LLM 评测 与 Self-Improvement
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Learning to Fold: prizewinning solution at LeHome Challenge 2026 (1st place online, 2nd offline)](https://arxiv.org/abs/2606.27163)
中文标题：Learning to Fold ： LeHome Challenge 2026的获奖解决方案（线上第一，线下第二）
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Mostly Automatic Translation of Language Interpreters from C to Safe Rust](https://arxiv.org/abs/2606.27122)
中文标题：Mostly Automatic Translation of Language Interpreters 来自 C to Safe Rust
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [TMP: Tree-structured Mixed-policy Pruning for Large-scale Image Generation and Editing](https://arxiv.org/abs/2606.27089)
中文标题：TMP：Tree-structured Mixed-policy Pruning 面向 Large-scale Image Generation 与 Editing
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP](https://arxiv.org/abs/2606.27027)
中文标题：ShareLock ：针对MCP的隐形多工具阈值中毒攻击
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive Morphological Alignment](https://arxiv.org/abs/2606.27019)
中文标题：MinGram ：具有高压缩和竞争性形态对齐的极简主义Unigram标记器
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Adaptive Utility driven Resource Orchestration for Resilient AI (AURORA-AI)](https://arxiv.org/abs/2606.27005)
中文标题：Adaptive Utility driven Resource Orchestration 面向 Resilient AI (AURORA-AI)
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Where Do Models Find Happiness? Emotion Vectors in Open-Source LLMs](https://arxiv.org/abs/2606.26987)
中文标题：模特儿在哪里找到快乐？开源LLM中的情感向量
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [In-Context Model Predictive Generation: Open-Vocabulary Motion Synthesis from Language Models to Physics](https://arxiv.org/abs/2606.26981)
中文标题：语境模型预测生成：从语言模型到物理学的开放式词汇运动合成
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring](https://arxiv.org/abs/2606.26979)
中文标题：代码代理需要多少静态结构？确定性锚定研究
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [RedVox: Safety and Fairness Gaps in Speech Models Across Languages](https://arxiv.org/abs/2606.26968)
中文标题：RedVox：Safety 与 Fairness Gaps in Speech Models Across Languages
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Learning to Recover Task Experts from a Multi-Task Merged Model](https://arxiv.org/abs/2606.26902)
中文标题：学习从多任务合并模型中恢复任务专家
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SamaVaani: Auditing and Debiasing Multilingual Clinical ASR for Indian Languages](https://arxiv.org/abs/2606.26901)
中文标题：SamaVaani：Auditing 与 Debiasing Multilingual Clinical ASR 面向 Indian Languages
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
