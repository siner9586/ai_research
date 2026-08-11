---
title: "让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力"
date: "2026-08-12"
target_date: "2026-08-10"
actual_date: "2026-08-10"
fallback_from: ""
lang: "zh"
slug: "2026-08-12-dream-technical-report"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "robotics", "systems", "training"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "robotics", "systems", "training"]
sources_page: "/zh/daily/2026-08-12-dream-technical-report-sources/"
generated_at: "2026-08-11T22:10:22.772070+00:00"
page_type: "brief"
candidate_count: 453
featured_count: 6
mentions_count: 20
featured_paper_titles: ["DREAM Technical Report", "Stealing Reasoning Traces from Proprietary LLM APIs", "MedPixel: A Unified Pixel-Language Model for Medical Reasoning and Segmentation", "ActBench: Self-Evolving Benchmark of Behavioral Safety in Cowork Agents", "Entropy-based Code Adversarial Translation for Real-world Repository Migration", "Multimodal Federated Learning under Dual-Axis Modality Missingness"]
featured_paper_urls: ["https://arxiv.org/abs/2608.09408", "https://arxiv.org/abs/2608.09867", "https://arxiv.org/abs/2608.09818", "https://arxiv.org/abs/2608.09476", "https://arxiv.org/abs/2608.09273", "https://arxiv.org/abs/2608.09240"]
featured_paper_titles_zh: ["DREAM技术报告", "从专有LLM API中窃取推理痕迹", "MedPixel：A Unified Pixel-Language Model 面向 Medical Reasoning 与 Segmentation", "ActBench：Self-Evolving 基准 of Behavioral Safety in Cowork Agents", "用于现实存储库迁移的基于熵的代码对抗翻译", "双轴模式下的多模态联合学习缺失"]
---

# 让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>DREAM Technical Report (Bin Zhang, Bowen Zheng, Chao Yi, Chengyu Lai, Dian Chen, Dimin Wang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.09408">2608.09408</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.09408">PDF</a></p>

中文标题：DREAM技术报告

信号显示：Industrial 推荐系统 commonly use cascaded retrieval, ranking, and re-ranking pipelines。关键词：agent、rag、retrieval、serving。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Stealing Reasoning Traces from Proprietary LLM APIs (Alexander Panfilov, David Schmotz, Ilia Shumailov, Luca Beurer-Kellner, Joachim Schaeffer, Ameya Prabhu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.09867">2608.09867</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.09867">PDF</a></p>

中文标题：从专有LLM API中窃取推理痕迹

信号显示：该研究围绕题名与摘要所揭示的问题展开，具体信号需结合原文进一步核验：Leading large language model providers now conceal their models' step-by-step reasoning, or chain-of-thought, to protect intellectual property and limit information leakage。关键词：agent、rag、code、reasoning。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>MedPixel: A Unified Pixel-Language Model for Medical Reasoning and Segmentation (Haoyu Yang, Meixing Shi, Zengjie Chen, Haoran Sun, Haitao Leng, Xiaoming Shi, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.09818">2608.09818</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.09818">PDF</a></p>

中文标题：MedPixel：A Unified Pixel-Language Model 面向 Medical Reasoning 与 Segmentation

信号显示：该研究围绕题名与摘要所揭示的问题展开，具体信号需结合原文进一步核验：Reliable medical image understanding requires models to connect clinical language and visual reasoning with pixel-level grounding。关键词：benchmark、code、vision-language、fine-tuning。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>ActBench: Self-Evolving Benchmark of Behavioral Safety in Cowork Agents (Hongwei Yao, Yiming Liu, Meihui Chen, Jieling Chen, Zikun Chen, Yiling He, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.09476">2608.09476</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.09476">PDF</a></p>

中文标题：ActBench：Self-Evolving 基准 of Behavioral Safety in Cowork Agents

信号显示：该研究围绕题名与摘要所揭示的问题展开，具体信号需结合原文进一步核验：Cowork agents may complete benign tasks while disclosing protected data, manipulating unauthorized state, invocate unauthorized API。关键词：agent、safety、benchmark、open-source。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Entropy-based Code Adversarial Translation for Real-world Repository Migration (Yushun Tang, Yisen Cao, Zhicheng Chen, Lin Peng, Junkang Mao, Fengyi Song, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.09273">2608.09273</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.09273">PDF</a></p>

中文标题：用于现实存储库迁移的基于熵的代码对抗翻译

信号显示：该研究围绕题名与摘要所揭示的问题展开，具体信号需结合原文进一步核验：LLMs have demonstrated strong capabilities in code generation and automated program repair, but migrating an entire repository rarely produces a runnable application because long-horizon translation challenges LLM-based agents' ability to maintain repository-l。关键词：agent、alignment、benchmark、code。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Multimodal Federated Learning under Dual-Axis Modality Missingness (Adiba Orzikulova, Jaehyun Kwak, Jaemin Shin, Yunqi Guo, Xiaomin Ouyang, Guoliang Xing, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.09240">2608.09240</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.09240">PDF</a></p>

中文标题：双轴模式下的多模态联合学习缺失

信号显示：该研究围绕题名与摘要所揭示的问题展开，具体信号需结合原文进一步核验：Multimodal federated learning (FL) supports collaborative modeling in privacy-sensitive health-sensing and medical settings, but realistic deployments often exhibit dual-axis modality missingness: clients have different modality sets, and individual samples ma。关键词：rag、deployment、code、multimodal。代码/数据可用性需查看原文确认。

## 其他值得关注
- [GRASP: Granularity-Aware Region Alignment and Semantic Prototype Learning for Fine-Grained Cross-Modal Understanding in Drone Views](https://arxiv.org/abs/2608.09270)
中文标题：把握：粒度感知区域对齐和语义原型学习，用于无人机视图中的细粒度跨模态理解
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Governing the KV Cache: Preventing Timing Side-Channel Leakage in Multi-Tenant LLM Inference](https://arxiv.org/abs/2608.09225)
中文标题：管理KV缓存：防止多租户LLM推断中的定时侧通道泄漏
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction](https://arxiv.org/abs/2608.09146)
中文标题：具有局部到全局循环闭包的多子图隐式神经SLAM ，用于大规模场景重建
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SI-Edit: Toward Sketch-Instruction Guided Local Image Editing with Pixel-Level Precision](https://arxiv.org/abs/2608.09097)
中文标题：SI-Edit ：使用像素级精度进行本地图像编辑的草图指导
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [PolicyKG: An Agentic LLM Pipeline for Translating Institutional Policies into SHACL Knowledge Graphs](https://arxiv.org/abs/2608.09028)
中文标题：PolicyKG：An Agentic LLM Pipeline 面向 Translating Institutional Policies into SHACL Knowledge Graphs
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [TeaMatch: Teachable Cross-Modal Representation Learning for 2D-3D Matching](https://arxiv.org/abs/2608.09590)
中文标题：TeaMatch：Teachable Cross-Modal Representation Learning 面向 2D-3D Matching
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Towards Expressive and Faithful Audio-to-Image Generation: A Unified Multimodal Dataset and Synthesis Framework](https://arxiv.org/abs/2608.09529)
中文标题：朝着富有表现力和忠实的音频图像生成：统一的多模态数据集和合成框架
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Learning Preference Adaptation for Large Language Model Personalization via Verbal Reinforcement Learning](https://arxiv.org/abs/2608.09507)
中文标题：通过语言强化学习实现大型语言模型个性化的学习偏好适应
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [VANE: Reliable Test-Time Training for Vision-Language-Action Models via Future Visual Representation Prediction](https://arxiv.org/abs/2608.09448)
中文标题：VANE ：通过未来视觉表示预测为视觉-语言-动作模型提供可靠的测试时间培训
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Temporal Misgrounding in Legal RAG: A Versioned-Corpus Benchmark for French Tax Law](https://arxiv.org/abs/2608.09393)
中文标题：Temporal Mis落地 in Legal RAG：A Versioned-Corpus 基准 面向 French Tax Law
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SAFE-CHEM: Uncertainty-Aware Policy Switching for Robust Robotic Chemistry](https://arxiv.org/abs/2608.09303)
中文标题：SAFE-CHEM：Uncertainty-Aware Policy Switching 面向 Robust Robotic Chemistry
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Bootstrapping Vision-Language Model for Hysteroscopic Surgical Scene Segmentation](https://arxiv.org/abs/2608.09302)
中文标题：宫腔镜手术场景分割的引导视觉语言模型
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Beyond Naturalness: Probing Automated Text-To-Speech Evaluators on Linguistically Grounded Dimensions](https://arxiv.org/abs/2608.09930)
中文标题：超越自然：探索基于语言学维度的自动文本到语音评估器
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Multimodal Model Diffing for Feature Discovery and Control](https://arxiv.org/abs/2608.09928)
中文标题：用于特征发现和控制的多模态模型差异
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Beyond Hazard Resemblance: Contrastive Event Adjudication for Training-Free Video Anomaly Detection](https://arxiv.org/abs/2608.09908)
中文标题：Beyond Hazard Resemblance：Contrastive Event Adjudication 面向 Training-Free Video Anomaly Detection
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [DistMoE: Private-data Rehearsal-free Routing in Mixture-of-Experts for Distributed Instruction Tuning](https://arxiv.org/abs/2608.09907)
中文标题：DistMoE：Private-data Rehearsal-free Routing in Mixture-of-Experts 面向 Distributed Instruction Tuning
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness](https://arxiv.org/abs/2608.09900)
中文标题：Decoding-Level Taboo：A Diagnostic Stress Test 面向 LLM Robustness
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [SHE: Trajectory-driven Safety Harness Evolution for LLM Agents](https://arxiv.org/abs/2608.09885)
中文标题：SHE：Trajectory-driven Safety Harness Evolution 面向 LLM Agents
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Mismatch Matters: On-Policy Distillation Beyond Token Agreement](https://arxiv.org/abs/2608.09836)
中文标题：Mismatch Matters：On-Policy Distillation Beyond Token Agreement
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Multi-Agent AI Safety as an Institutional Design Problem](https://arxiv.org/abs/2608.09828)
中文标题：多Agent AI安全作为制度设计问题
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
