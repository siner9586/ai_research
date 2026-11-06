---
title: "让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升 RAG 检索和知识库问答可靠性"
date: "2026-11-07"
target_date: "2026-11-05"
actual_date: "2026-11-05"
fallback_from: ""
lang: "zh"
slug: "2026-11-07-beyond-instruction-override-benchmarking-indirect-prompt-injection"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "reasoning", "systems", "training", "vision-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "reasoning", "systems", "training", "vision-generation"]
sources_page: "/zh/daily/2026-11-07-beyond-instruction-override-benchmarking-indirect-prompt-injection-sources/"
generated_at: "2026-11-06T16:40:39.224941+00:00"
page_type: "brief"
candidate_count: 499
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks", "Multimodal Hierarchical Mixture-of-Experts for 3D Medical Vision-Language Modeling", "Adaptive Semantic Branching: Disagreement-Localized Cross-Trajectory Regeneration for Reasoning Candidate Expansion", "Redacting Personal Data: A Speed and Accuracy Comparison of Regex, Presidio and Hybrid Designs", "MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents", "Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety"]
featured_paper_urls: ["https://arxiv.org/abs/2611.07640", "https://arxiv.org/abs/2611.08185", "https://arxiv.org/abs/2611.07918", "https://arxiv.org/abs/2611.07633", "https://arxiv.org/abs/2611.07631", "https://arxiv.org/abs/2611.08438"]
featured_paper_titles_zh: ["Beyond InstruCTion Override ：将间接提示注入与任务篡改攻击进行基准测试", "用于3D医学视觉语言建模的多模态分层混合专家", "自适应语义分支：用于推理候选人扩展的分歧-局部跨轨迹再生", "Redacting Personal Data：A Speed 与 Accuracy Comparison of Regex，Presidio 与 Hybrid Designs", "MEMOIR：A Training-Free Memory Lifecycle 面向 Long-Horizon LLM Agents", "从内部理解人工智能：人工智能安全的机械可解释性状态"]
---

# 让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks (Rongting Zhang, Martin Bertran, Sandeep Avula, Chia-Jung Lee, Vanessa Murdock)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.07640">2611.07640</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.07640">PDF</a></p>

中文标题：Beyond InstruCTion Override ：将间接提示注入与任务篡改攻击进行基准测试

信号显示：间接提示注入（ IPI ）基准主要测试植入的指令，这些指令将使用工具的代理重定向到攻击者选择的任务。关键词：agent、rag、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 2. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Multimodal Hierarchical Mixture-of-Experts for 3D Medical Vision-Language Modeling (Gizem Mert, Szymon Płotka, Pedro R. A. S. Bassi, Wenxuan Li, Zongwei Zhou, Jarosław B. Ćwikła, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.08185">2611.08185</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.08185">PDF</a></p>

中文标题：用于3D医学视觉语言建模的多模态分层混合专家

信号显示：医学3D扫描和报告本质上是分层的，诊断线索集中在组织多个层次的特定解剖区域。关键词：alignment、code、multimodal、vision-language。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Adaptive Semantic Branching: Disagreement-Localized Cross-Trajectory Regeneration for Reasoning Candidate Expansion (Jeong-Yoon Kim, Tae-Yoon Lee)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.07918">2611.07918</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.07918">PDF</a></p>

中文标题：自适应语义分支：用于推理候选人扩展的分歧-局部跨轨迹再生

信号显示：为同一问题生成的推理轨迹往往会得到相互矛盾的答案。关键词：rag、inference、alignment、evaluation。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Redacting Personal Data: A Speed and Accuracy Comparison of Regex, Presidio and Hybrid Designs (Sai Yashwant, Manoj Kumar Gondimalla, Arjun Sharma, Shubham)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.07633">2611.07633</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.07633">PDF</a></p>

中文标题：Redacting Personal Data：A Speed 与 Accuracy Comparison of Regex，Presidio 与 Hybrid Designs

信号显示：许多企业项目现在将自由文本传递给大语言模型（ LLM ） ，该文本通常包含个人身份信息（ PII ） ，例如姓名、电话号码、电子邮件地址、家庭住址和出生日期。关键词：workflow、rag、latency、safety。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents (Mayank Anand, Subham Raj, Aman Vaibhav Jha, Sriparna Saha)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.07631">2611.07631</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.07631">PDF</a></p>

中文标题：MEMOIR：A Training-Free Memory Lifecycle 面向 Long-Horizon LLM Agents

信号显示：长期LLM代理需要能够跨会话保存有用信息并在需要时检索的内存系统。关键词：agent、rag、retrieval、deployment。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety (Fazl Barez, Tung-Yu Wu, Hunar Batra, Gabriele Dominici, Florent Draye, Yanai Elazar, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.08438">2611.08438</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.08438">PDF</a></p>

中文标题：从内部理解人工智能：人工智能安全的机械可解释性状态

信号显示：神经网络可能是人类历史上最重要的人工制品之一。关键词：safety、evaluation、code、interpretability。代码/数据可用性需查看原文确认。

## 其他值得关注
- [XStack: A Benchmark for ML Repo Migration](https://arxiv.org/abs/2611.08472)
中文标题：XStack：A 基准 面向 ML Repo Migration
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [The Power of Meta Access in the Software of the Future --- Demonstrated on LLM Chat UIs and Chat AI](https://arxiv.org/abs/2611.08428)
中文标题：未来软件中元访问的力量---在LLM聊天UI和聊天AI上演示
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Adaptive Low-Light Enhancement for Road Anomaly Detection: A Multi-Architecture Benchmark and Edge Deployment Study](https://arxiv.org/abs/2611.08393)
中文标题：用于道路异常检测的自适应低光增强：多架构基准和边缘部署研究
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [MCUFlowNet: Hardware-Aware Neural Architecture Search for Optical Flow on Microcontrollers](https://arxiv.org/abs/2611.08147)
中文标题：MCUFlowNet：Hardware-Aware Neural Architecture Search 面向 Optical Flow on Microcontrollers
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Reinforcing End-to-End Autonomous Driving Safety via Negative-Aware Planning in a Unified World-Action Model](https://arxiv.org/abs/2611.08111)
中文标题：在统一的世界行动模型中通过负面感知规划加强端到端自动驾驶安全
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [BiGrounder: Bidirectional Training Unlocks the Potential of GUI Grounding](https://arxiv.org/abs/2611.07765)
中文标题：BiGrounder ：双向培训释放了GUI接地的潜力
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Fast and Accurate Hand Estimation in Pixels, Interaction and World Space](https://arxiv.org/abs/2611.07711)
中文标题：像素、交互和世界空间中的快速准确的手部估计
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents](https://arxiv.org/abs/2611.07689)
中文标题：MCPHallu：基准ing Reasoning，Execution，与 Memory Hallucinations in MCP Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [GEKey: Learning Geodesic Eccentric 3D Keypoints via Self-Supervision](https://arxiv.org/abs/2611.07677)
中文标题：GEKey ：通过自我监督学习测地线偏心3D关键点
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Neural Image Compression with Internal-External Prior Fusion and Alignment](https://arxiv.org/abs/2611.07644)
中文标题：具有内部-外部先验融合和对齐的神经图像压缩
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Binding Paraphrased Instructions to Encountered Objects in sLLM Agents under Partial Observability](https://arxiv.org/abs/2611.07599)
中文标题：在部分可观察性下将复述说明绑定到sLLM药剂中遇到的对象
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [RLGPA: A Reinforcement Learning-Guided Granularity Planning Attack for Decision-Based Sparse Adversarial Examples](https://arxiv.org/abs/2611.07512)
中文标题：RLGPA：A Reinforcement Learning-Guided Granularity Planning Attack 面向 Decision-Based Sparse Adversarial Examples
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [ZYFA: Speed and Accuracy of FP8 FlashAttention on AMD CDNA4](https://arxiv.org/abs/2611.07496)
中文标题：ZYFA：Speed 与 Accuracy of FP8 FlashAttention on AMD CDNA4
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [How Should Agents See Code? Rethinking Code Representations for Agentic Software Engineering](https://arxiv.org/abs/2611.07286)
中文标题：客服代表应如何查看代码？重新思考Agent软件工程的代码表示
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks](https://arxiv.org/abs/2611.08417)
中文标题：作为软件的基准：终端工作台和持续基准的案例
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [GINGER: Spicing Up Graph-Based Vector Search](https://arxiv.org/abs/2611.08306)
中文标题：GINGER ：为基于图的矢量搜索加香料
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [GTAFL: Addressing Test-Agnostic Long-Tailed Federated Learning in Medical Image](https://arxiv.org/abs/2611.08021)
中文标题：GTAFL ：解决医学图像中与测试无关的长尾联合学习
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [EDGAR: Efficient Diffusion-Driven Gaussian Avatar Refinement via Synthetic Failure](https://arxiv.org/abs/2611.07909)
中文标题：EDGAR ：通过合成失败实现高效扩散驱动的高斯化身细化
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Do Recommenders Need to Think in Words? Latent Reasoning for Efficient LLM-Based Recommendation](https://arxiv.org/abs/2611.07866)
中文标题：推荐人需要用言语思考吗？基于LLM的高效推荐的潜在推理
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Towards Foundation Decision Models: Drex](https://arxiv.org/abs/2611.07854)
中文标题：迈向基础决策模型： Drex
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
