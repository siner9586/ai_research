---
title: "让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力"
date: "2026-09-11"
target_date: "2026-09-09"
actual_date: "2026-09-09"
fallback_from: ""
lang: "zh"
slug: "2026-09-11-agentaudit-an-open-extensible-framework-for-full"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力。"
tags: ["agents", "code", "data-engineering", "evaluation", "rag", "safety", "systems", "training"]
topics: ["agents", "code", "data-engineering", "evaluation", "rag", "safety", "systems", "training"]
sources_page: "/zh/daily/2026-09-11-agentaudit-an-open-extensible-framework-for-full-sources/"
generated_at: "2026-09-10T23:07:37.041768+00:00"
page_type: "brief"
candidate_count: 354
featured_count: 6
mentions_count: 20
featured_paper_titles: ["AgentAudit: An Open, Extensible Framework for Full-Lifecycle Trust Evaluation of AI Agents", "Cross-Species Animal Re-Identification with Semantic Consistency Learning", "MOONWALK: Mediating Operations with Intent-Evidence-Action Alignment Across Junior-Supervisor Review Workflows in Animation/VFX Pre-Production", "When Fusion Fails: Corruption-Aware Rebalanced Fusion for Multi-Modal Medical Image Segmentation", "What Makes Adversarial Examples Transfer Across Deepfake Detectors?", "Arbitrary Cipher Attacks Against Large Language Models Do Not Require Fine-Tuning"]
featured_paper_urls: ["https://arxiv.org/abs/2609.09875", "https://arxiv.org/abs/2609.09705", "https://arxiv.org/abs/2609.10385", "https://arxiv.org/abs/2609.10261", "https://arxiv.org/abs/2609.10002", "https://arxiv.org/abs/2609.09553"]
featured_paper_titles_zh: ["AgentAudit：An Open，Extensible 框架 面向 Full-Lifecycle Trust 评测 of AI Agents", "跨物种动物再识别与语义一致性学习", "月球漫步：通过动画/视觉特效预制作中的初级主管审核工作流程，通过意图-证据-行动对齐来调解操作", "融合失败时：用于多模态医学图像分割的腐败感知重新平衡融合", "是什么让对抗性示例跨Deepfake检测器传输？", "针对大型语言模型的任意密码攻击不需要微调"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>AgentAudit: An Open, Extensible Framework for Full-Lifecycle Trust Evaluation of AI Agents (Shrey Nag, Sachita, Abhishek Kumar Singh, Lipi Goel, Rajeshwar Singh Janwar)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.09875">2609.09875</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.09875">PDF</a></p>

中文标题：AgentAudit：An Open，Extensible 框架 面向 Full-Lifecycle Trust 评测 of AI Agents

信号显示：现有的评估框架大多只评估AI Agent的一部分，如任务完成（ AgentBench ）或安全鲁棒性（ AgentDojo ， ASB ） ，而不是规划、工具选择、工具执行、内存和推理的完整管道。关键词：agent、alignment、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 2. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Cross-Species Animal Re-Identification with Semantic Consistency Learning (Shuoyi Chen, Yuejia Li, Mang Ye)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.09705">2609.09705</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.09705">PDF</a></p>

中文标题：跨物种动物再识别与语义一致性学习

信号显示：可普遍化的动物再识别（ ReID ）旨在识别具有不同形态和生态环境的物种中的个体动物。关键词：rag、serving、evaluation、code。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>MOONWALK: Mediating Operations with Intent-Evidence-Action Alignment Across Junior-Supervisor Review Workflows in Animation/VFX Pre-Production (Shih-Yu Lai, Wen-Fan Wang, Sai Ling, Shaune Jan, Bing-Yu Chen, Xiang Anthony Chen)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.10385">2609.10385</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.10385">PDF</a></p>

中文标题：月球漫步：通过动画/视觉特效预制作中的初级主管审核工作流程，通过意图-证据-行动对齐来调解操作

信号显示：动画和视觉特效预制作评审要求团队将松散指定的创意意图（简报、不断发展的规范、异构引用和口头决定）翻译成初级艺术家可以执行的修订，而无需反复澄清。关键词：workflow、alignment、evaluation、code。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>When Fusion Fails: Corruption-Aware Rebalanced Fusion for Multi-Modal Medical Image Segmentation (Yuchen Pei, Xiaoyu Hu, Yixiong Zou, Dingwen Hu, Hui Chu, Yutao Ma, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.10261">2609.10261</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.10261">PDF</a></p>

中文标题：融合失败时：用于多模态医学图像分割的腐败感知重新平衡融合

信号显示：多模态医学图像分割利用了互补的诊断信息，但当空间对齐的输入质量不同时，融合可能会低于单模态基线。关键词：rag、inference、alignment、code。代码/数据可用性需查看原文确认。

### 5. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>What Makes Adversarial Examples Transfer Across Deepfake Detectors? (Rafael M. Mamede, Pedro C. Neto, Ana F. Sequeira)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.10002">2609.10002</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.10002">PDF</a></p>

中文标题：是什么让对抗性示例跨Deepfake检测器传输？

信号显示：Deepfake检测器仍然容易受到基于传输的黑盒攻击，其中对抗性示例在源代理模型上生成并传输到攻击者未知的目标模型。关键词：rag、evaluation、code、training。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Arbitrary Cipher Attacks Against Large Language Models Do Not Require Fine-Tuning (Thomas Rivasseau)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2609.09553">2609.09553</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2609.09553">PDF</a></p>

中文标题：针对大型语言模型的任意密码攻击不需要微调

信号显示：大语言模型的安全和安保研究主要关注检测和预防越狱攻击：绕过对抗性用户从模型中获取不必要或有害的输出。关键词：alignment、safety、fine-tuning、jailbreak。代码/数据可用性需查看原文确认。

## 其他值得关注
- [3rd Place Solution to Human Motion Challenges in Real-World and Clinical Settings (MoCha) @ECCV2026: Language-Aligned Motion Representations for Domain-Generalizable UPDRS-Gait Severity Estimation](https://arxiv.org/abs/2609.10187)
中文标题：3rd Place Solution to Human Motion Challenges in Real-World 与 Clinical Settings (MoCha) @ECCV2026：Language-Aligned Motion Representations 面向 Domain-Generalizable UPDRS-Gait Severity Estimation
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [EEGBind: Detecting Source-Level Interictal Epileptiform Discharges via EEG-Centric Multimodal Binding](https://arxiv.org/abs/2609.09728)
中文标题：EEGBind ：通过以EEG为中心的多峰结合检测发作间期癫痫样放电
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [PELM: Power Efficient On-Device LLM Inference with Speculative Decoding and Dynamic Voltage Frequency Scaling](https://arxiv.org/abs/2609.09662)
中文标题：PELM ：采用推测解码和动态电压频率缩放的节能型器件上LLM推理
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Watermarks Without Verification: AI Text Watermarking After the EU AI Act](https://arxiv.org/abs/2609.09604)
中文标题：未经验证的水印：欧盟AI法案后的AI文本水印
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ProbPlug: A Plugin Uncertainty Network for Reliable Confidence in LLM Binary Classification](https://arxiv.org/abs/2609.10122)
中文标题：ProbPlug：A Plugin Uncertainty Network 面向 Reliable Confidence in LLM Binary Classification
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [When Does Defendant Statement Matter? A Study of Bias and Persuasion in LLM-Simulated Jurors](https://arxiv.org/abs/2609.09887)
中文标题：被告陈述何时重要？ LLM模拟陪审员中的偏见和说服力研究
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [When Does Low-Bit Quantization Preserve the Decisions of Vector Search?](https://arxiv.org/abs/2609.09854)
中文标题：低位量化何时保留矢量搜索的决策？
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Subgroup Membership Inference Audits of Differentially Private Synthetic Text](https://arxiv.org/abs/2609.09848)
中文标题：差异私有合成文本的亚组成员资格推断审计
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Distilling Image Prototypes for Guided Test-Time Adaptation](https://arxiv.org/abs/2609.09737)
中文标题：蒸馏图像原型，用于引导测试时间适应
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Settling: Equilibrium Inference for Non-Convex Validity Sets](https://arxiv.org/abs/2609.09682)
中文标题：结算：非凸有效性集的平衡推断
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [TEFM: Token-Efficient Faithful Modeling for Structured Data](https://arxiv.org/abs/2609.09552)
中文标题：TEFM：Token-Efficient Faithful Modeling 面向 Structured Data
关注理由：涉及数据工程中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [IdeaAMBIG: Benchmarking Implementation-Critical Gaps in Research-Idea Specifications](https://arxiv.org/abs/2609.10539)
中文标题：IdeaAMBIG：基准ing Implementation-Critical Gaps in Research-Idea Specifications
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ConvMem: Convolutional Memory for Long-Context Reasoning](https://arxiv.org/abs/2609.10441)
中文标题：ConvMem：Convolutional Memory 面向 Long-Context Reasoning
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs](https://arxiv.org/abs/2609.10439)
中文标题：仅忘记重要的事情：对强大的LLM进行层级选择性学习
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology Tagging of Enterprise Data Catalogs](https://arxiv.org/abs/2609.10430)
中文标题：Glyph：A Multi-Strategy Agentic System 面向 Column Description 与 Sensitivity-Ontology Tagging of Enterprise Data Catalogs
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [PACE: Perceived-Latency-Aware Cascading Service Routing and Filler Control for QoE-Efficient Retrieval-Augmented Dialogue Serving](https://arxiv.org/abs/2609.10372)
中文标题：PACE：Perceived-Latency-Aware Cascading Service Routing 与 Filler Control 面向 QoE-Efficient Retrieval-Augmented Dialogue Serving
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs](https://arxiv.org/abs/2609.10355)
中文标题：为什么视频仍然如此昂贵？视频和视听LLM中的推理效率机制调查
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Cyber-Financial Contagion: Modeling the Propagation of an AI Vendor Compromise Through the Banking System](https://arxiv.org/abs/2609.10350)
中文标题：网络金融蔓延：通过银行系统模拟人工智能供应商妥协的传播
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Learning to Adapt and Calibrate: Score Distribution Alignment for Few-Shot Uncertainty Prediction in Medical VLMs](https://arxiv.org/abs/2609.10333)
中文标题：学习适应和校准：医学VLM中少量不确定性预测的分数分布一致性
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [TRACE: Training Reasoning Agents for Causal Exploration with Synthesized Rewards](https://arxiv.org/abs/2609.10315)
中文标题：TRACE ：使用综合奖励培训因果探索的推理代理
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
