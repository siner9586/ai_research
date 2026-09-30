---
title: "让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险、提升模型推理、规划和验证能力"
date: "2026-10-01"
target_date: "2026-09-29"
actual_date: "2026-09-29"
fallback_from: ""
lang: "zh"
slug: "2026-10-01-automark-enabling-autoresearch-to-discover-better-llm"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险、提升模型推理、规划和验证能力。"
tags: ["code", "data-engineering", "evaluation", "reasoning", "safety", "systems", "training", "video-generation"]
topics: ["code", "data-engineering", "evaluation", "reasoning", "safety", "systems", "training", "video-generation"]
sources_page: "/zh/daily/2026-10-01-automark-enabling-autoresearch-to-discover-better-llm-sources/"
generated_at: "2026-09-30T16:24:25.611149+00:00"
page_type: "brief"
candidate_count: 905
featured_count: 6
mentions_count: 20
featured_paper_titles: ["AutoMark: Enabling Autoresearch to Discover Better LLM Watermarks", "Safer Content or Firmer Refusals? A Hybrid Perturbation Defense for Alignment under Harmful Fine-tuning", "Distilling What Matters: Confidence-Aware Selective Distillation for Large Language Models", "Mixture of Self-Improving Branches For Agent Harness Optimization", "ReCaVSR: One-Step Streaming Diffusion Video Super-Resolution with Recycled Latents and Learned Cache Routing", "End-to-End Self-Supervised RGB-T Tracking without Modality Misleading"]
featured_paper_urls: ["https://arxiv.org/abs/2609.37310", "https://arxiv.org/abs/2609.36862", "https://arxiv.org/abs/2609.36734", "https://arxiv.org/abs/2609.37834", "https://arxiv.org/abs/2609.37831", "https://arxiv.org/abs/2609.37162"]
featured_paper_titles_zh: ["AutoMark ：启用自动搜索以发现更好的LLM水印", "更安全的内容还是更坚定的拒绝？有害微调下对准的混合扰动防御", "重要的蒸馏：大型语言模型的信心感知选择性蒸馏", "用于Agent线束优化的自我改进分支的混合物", "ReCaVSR：One-Step Streaming Diffusion Video Super-Resolution with Recycled Latents 与 Learned Cache Routing", "无误导模态的端到端自我监督RGB-T跟踪"]
---

# 让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、识别并缓解模型安全、越狱和对齐风险、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>AutoMark: Enabling Autoresearch to Discover Better LLM Watermarks (Thibaud Gloaguen, Robin Staab, Martin Vechev)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.37310">2609.37310</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.37310">PDF</a></p>

中文标题：AutoMark ：启用自动搜索以发现更好的LLM水印

信号显示：随着LLM水印被商业化部署，现在法规要求，提高其可靠性和有效性已变得至关重要。关键词：agent、evaluation、code、eval。代码/数据可用性需查看原文确认。

### 2. 识别并缓解模型安全、越狱和对齐风险

<p class="paper-meta-line"><span>Safer Content or Firmer Refusals? A Hybrid Perturbation Defense for Alignment under Harmful Fine-tuning (Muhammad Zeeshan Akram, Mufid Kamel Marican, Anvesh Reddy Yenugu, Ali Zain Kaimkhani, Minghong Fang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.36862">2609.36862</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.36862">PDF</a></p>

中文标题：更安全的内容还是更坚定的拒绝？有害微调下对准的混合扰动防御

信号显示：微调即服务允许用户根据自己的数据调整安全对齐的语言模型，但它也会产生有害的微调攻击面：少量有害数据混合到其他良性微调集中可能会降低模型的对齐方式。关键词：alignment、safety、evaluation、fine-tuning。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Distilling What Matters: Confidence-Aware Selective Distillation for Large Language Models (Ayan Sengupta, Vaibhav Seth, Tanmoy Chakraborty)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.36734">2609.36734</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.36734">PDF</a></p>

中文标题：重要的蒸馏：大型语言模型的信心感知选择性蒸馏

信号显示：知识蒸馏（ KD ）训练小容量学生模型，通过匹配输出分布来模仿大容量教师模型，隐式假设教师是可靠的预言机。关键词：rag、alignment、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Mixture of Self-Improving Branches For Agent Harness Optimization (Haoyu Dong, Yuhang Zhou, Zihao Lin, Yifan Wu, Bo Peng, Mingyi Wang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.37834">2609.37834</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.37834">PDF</a></p>

中文标题：用于Agent线束优化的自我改进分支的混合物

信号显示：线束优化为递归自我改进（ RSI ）提供了实用设置，其中代理生成的修改通过执行反馈通知后续更改。关键词：agent、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>ReCaVSR: One-Step Streaming Diffusion Video Super-Resolution with Recycled Latents and Learned Cache Routing (Xijun Wang, Xin Li, Suhang Yao, Zirui Lang, Bingchen Li, Zhibo Chen)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.37831">2609.37831</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.37831">PDF</a></p>

中文标题：ReCaVSR：One-Step Streaming Diffusion Video Super-Resolution with Recycled Latents 与 Learned Cache Routing

信号显示：基于实时扩散的视频超分辨率（ VSR ）对在线流媒体的需求很高，但严格的延迟要求往往会影响生成保真度。关键词：inference、latency、benchmark、code。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>End-to-End Self-Supervised RGB-T Tracking without Modality Misleading (Shenglan Li, Rui Yao, Kunyang Sun, Hong Jia, Yong Zhou, Javen Qinfeng Shi, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.37162">2609.37162</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.37162">PDF</a></p>

中文标题：无误导模态的端到端自我监督RGB-T跟踪

信号显示：RGB-T物体跟踪利用可见光和热红外模式的互补特性，在不利条件下提高鲁棒性。关键词：rag、inference、alignment、benchmark。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Retrieve, Reproduce, Reveal: Dissecting Retrieval-Augmented Software Vulnerability Detection](https://arxiv.org/abs/2609.37669)
中文标题：检索、再现、揭示：解剖检索-增强软件漏洞检测
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CypherTurn: A Multi-Turn Benchmark for Conversational Text-to-Cypher Evaluation and the Autonomy Divergence](https://arxiv.org/abs/2609.36987)
中文标题：CypherTurn ：会话文本到密码评估和自主性发散的多回合基准
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [AdaptArena: Evaluating Test-Time Personalization of Web Agents](https://arxiv.org/abs/2609.36488)
中文标题：AdaptArena ：评估Web代理的测试时间个性化
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Losing the name before the box: measuring and repairing what narrow fine-tuning costs a detector outside its deployment vocabulary](https://arxiv.org/abs/2609.36426)
中文标题：丢掉盒子之前的名字：测量和修复部署词汇之外的探测器所花费的狭窄微调
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [RelayVSR: Large-Small Model Collaboration for Efficient Real-World Video Super-Resolution](https://arxiv.org/abs/2609.37850)
中文标题：RelayVSR：Large-Small Model Collaboration 面向 Efficient Real-World Video Super-Resolution
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Cross-Entropy Guided Routing in Mixture-of-Experts Large Language Models](https://arxiv.org/abs/2609.37751)
中文标题：混合专家大型语言模型中的交叉熵引导路由
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [LEMON-ZEST: Evolution-Informed Tokenization for Efficient Protein Language Modeling](https://arxiv.org/abs/2609.37675)
中文标题：LEMON-ZEST：Evolution-Informed Tokenization 面向 Efficient Protein Language Modeling
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [LLM unbranding: Erasing Commercial Identity while Preserving Generic Utility](https://arxiv.org/abs/2609.37127)
中文标题：法学硕士无品牌：在保留通用效用的同时抹去商业身份
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Embedded Bi-Temporal Building Damage Assessment for On-Board Data Reduction](https://arxiv.org/abs/2609.37013)
中文标题：用于减少车载数据的嵌入式双时间建筑物损坏评估
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [PrecogUI: Proactive GUI Agents via Pre-cognitive Simulation and Experience Retrieval](https://arxiv.org/abs/2609.36923)
中文标题：PrecogUI ：通过预认知模拟和经验检索的主动GUI代理
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SafeVantage: Vantage-Aware Memory for Reliable Embodied Decisions](https://arxiv.org/abs/2609.36906)
中文标题：SafeVantage：Vantage-Aware Memory 面向 Reliable Embodied Decisions
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Architecture Alignment With Sparse Priors in Tabular Foundation Models](https://arxiv.org/abs/2609.36883)
中文标题：表格基础模型中稀疏先验的架构对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [RESCUE: Repairing Language Model Errors to Sparse Circuits via Reinforcement Learning](https://arxiv.org/abs/2609.36813)
中文标题：RESCUE ：通过强化学习将语言模型错误修复到稀疏电路
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Where Root Cause Analysis Fails: A Retrieval-Reranking Decomposition](https://arxiv.org/abs/2609.36686)
中文标题：根本原因分析失败的地方：检索排序分解
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [VLM4Cluster: Benchmarking Deep Clustering In the Era of Vision-Language Pre-training](https://arxiv.org/abs/2609.36648)
中文标题：VLM4Cluster ：视觉语言预训练时代的深度聚类基准测试
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning](https://arxiv.org/abs/2609.36588)
中文标题：通过强化微调合作的多Agent视觉-语言-行动模型
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ThinkingGuard: Decoding Implicit Hazards via Step-by-Step Risk Attribution in Multimodal Large Language Models](https://arxiv.org/abs/2609.36562)
中文标题：ThinkingGuard ：通过多模式大型语言模型中的分步风险归因来解码隐含危害
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [RA-CFGCache: From Branch-Level Criteria to Guided-Risk Control under Classifier-Free Guidance](https://arxiv.org/abs/2609.36433)
中文标题：RA-CFGCache：来自 Branch-Level Criteria to Guided-Risk Control under Classifier-Free Guidance
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning](https://arxiv.org/abs/2609.38147)
中文标题：思考前思考：通过元推理扩展代理推理
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [CLeaR: A Unified Framework for Resolving the Leakage-Degradation Dilemma in Style Transfer](https://arxiv.org/abs/2609.38136)
中文标题：CLeaR ：解决风格转换中泄漏降解困境的统一框架
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
