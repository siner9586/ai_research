---
title: "提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-08-13"
target_date: "2026-08-11"
actual_date: "2026-08-11"
fallback_from: ""
lang: "zh"
slug: "2026-08-13-conftriage-a-calibration-aware-llm-triage-framework"
summary: "今天主要跟进：提升 RAG 检索和知识库问答可靠性、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "robotics", "safety", "speech-audio", "training", "vision-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "robotics", "safety", "speech-audio", "training", "vision-generation"]
sources_page: "/zh/daily/2026-08-13-conftriage-a-calibration-aware-llm-triage-framework-sources/"
generated_at: "2026-08-12T21:58:39.067178+00:00"
page_type: "brief"
candidate_count: 382
featured_count: 6
mentions_count: 20
featured_paper_titles: ["ConfTriage: A Calibration-Aware LLM Triage Framework for Pulmonary Nodule Malignancy with Selective Specialist Deferral", "FedCGR: Federated Cross-Domain Generative Recommendation", "Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting", "Detecting an Effect Is Not Learning to Act on It: A Reward-SNR Floor for LLM Acquisition Agents", "From Interpretability to Control: Insights from Six Years of the TrustNLP Workshop", "TACTICL: Task-Aware Compression of Tabular ICL Models"]
featured_paper_urls: ["https://arxiv.org/abs/2608.10885", "https://arxiv.org/abs/2608.10929", "https://arxiv.org/abs/2608.10756", "https://arxiv.org/abs/2608.10441", "https://arxiv.org/abs/2608.11171", "https://arxiv.org/abs/2608.10837"]
featured_paper_titles_zh: ["ConfTriage ：选择性专科延期治疗肺结节恶性肿瘤的校准感知LLM分类框架", "FedCGR ：联合跨域生成推荐", "通过语义3D高斯拼接实现开放式词汇移动操作的嵌入式多模态接地", "Detecting an Effect Is Not Learning to Act on It：A Reward-SNR Floor 面向 LLM Acquisition Agents", "从可解释性到控制性：六年TrustNLP研讨会的见解", "TACTICL ：表格ICL模型的任务感知压缩"]
---

# 提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：提升 RAG 检索和知识库问答可靠性、提升 RAG 检索和知识库问答可靠性、提升模型推理、规划和验证能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>ConfTriage: A Calibration-Aware LLM Triage Framework for Pulmonary Nodule Malignancy with Selective Specialist Deferral (Md Rabiul Islam, Samir Abdaljalil, Erchin Serpedin, Hasan Kurban)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.10885">2608.10885</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.10885">PDF</a></p>

中文标题：ConfTriage ：选择性专科延期治疗肺结节恶性肿瘤的校准感知LLM分类框架

信号显示：肺结节恶性肿瘤预测通常依赖于图像训练的专业深度学习（ DL ）模型，这些模型需要大量的注释成像数据和特定任务的训练。关键词：rag、inference、safety、code。代码/数据可用性需查看原文确认。

### 2. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>FedCGR: Federated Cross-Domain Generative Recommendation (Zhuodong Liu, Hugen Lv, Xiangyu Li, Bohan Guo, Peiyu Hu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.10929">2608.10929</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.10929">PDF</a></p>

中文标题：FedCGR ：联合跨域生成推荐

信号显示：跨域推荐(CDR)跨相关域传输偏好知识，但联合部署使跨域对齐变得困难，因为对齐项目空间的行为锚点（例如重叠用户和共享交互签名）。关键词：rag、deployment、alignment、evaluation。代码/数据可用性需查看原文确认。

### 3. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting (Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.10756">2608.10756</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.10756">PDF</a></p>

中文标题：通过语义3D高斯拼接实现开放式词汇移动操作的嵌入式多模态接地

信号显示：具体的移动操作需要在执行前对齐语言、视觉观察、三维场景结构和动作可行性。关键词：evaluation、multimodal、vision-language、robot。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Detecting an Effect Is Not Learning to Act on It: A Reward-SNR Floor for LLM Acquisition Agents (Ying Yuan)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.10441">2608.10441</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.10441">PDF</a></p>

中文标题：Detecting an Effect Is Not Learning to Act on It：A Reward-SNR Floor 面向 LLM Acquisition Agents

信号显示：许多管道可以支付每个示例的成本来获取辅助，模型衍生的观察- LLM的结构化推理，缓慢的预言机，昂贵的测量-然后必须决定获取的信号何时值得使用。关键词：agent、rag、code、data。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>From Interpretability to Control: Insights from Six Years of the TrustNLP Workshop (Rahul Gupta, Abhinav Mohanty, Anaelia Ovalle, Anil Ramakrishna, Anubrata Das, Apurv Verma, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.11171">2608.11171</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.11171">PDF</a></p>

中文标题：从可解释性到控制性：六年TrustNLP研讨会的见解

信号显示：值得信赖的自然语言处理研讨会（ TrustNLP ）自2021年以来与主要的ACL会议同地举办，六个版本的论文从8篇增加到41篇，记录了整个领域从静态模式事后可解释性的转变。关键词：rag、alignment、safety、search。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>TACTICL: Task-Aware Compression of Tabular ICL Models (Mykhailo Koshil, Matthias Feurer, Katharina Eggensperger)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.10837">2608.10837</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.10837">PDF</a></p>

中文标题：TACTICL ：表格ICL模型的任务感知压缩

信号显示：表格任务的基础模型的强大性能需要大量的推理成本。关键词：inference、compression、benchmark、code。代码/数据可用性需查看原文确认。

## 其他值得关注
- [PEAK: Precise and Persistent Concept Erasure via k-Sparse Autoencoders](https://arxiv.org/abs/2608.10985)
中文标题：峰值：通过k-Sparse自动编码器进行精确和持久的概念擦除
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [GitSkills: A Dataset of Agent Skills on GitHub](https://arxiv.org/abs/2608.10906)
中文标题：GitSkills ： GitHub上的代理技能数据集
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [DistilVDR: A Compact End-to-End Visual Document Retriever via Dual-Student Distillation](https://arxiv.org/abs/2608.10636)
中文标题：DistilVDR ：通过双学生蒸馏的紧凑型端到端视觉文档检索器
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Reference-Free Post-Training of Open Large Language Models for Multilingual Machine Translation](https://arxiv.org/abs/2608.10812)
中文标题：用于多语言机器翻译的开放式大型语言模型的无引用后训练
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Rethinking LLM Verification: Evidence Structure, Uncertainty, and Selective Refinement](https://arxiv.org/abs/2608.10725)
中文标题：重新思考LLM验证：证据结构、不确定性和选择性细化
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SQuaT: Self-Supervised Knowledge Distillation via Student-Aware Quantized Teacher Features](https://arxiv.org/abs/2608.10709)
中文标题：SQuaT ：通过学生感知量化教师功能进行自我监督的知识蒸馏
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [MEGA: Self-Evolving Agent Optimization Infrastructure via Wisdom Graph](https://arxiv.org/abs/2608.10504)
中文标题：MEGA ：通过智能图进行自我进化Agent优化基础设施
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Never Stop Speaking: a Denial-of-Service Attack on End-to-End Speech Language Models](https://arxiv.org/abs/2608.10405)
中文标题：永不停止说话：对端到端语音语言模型的拒绝服务攻击
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Are We Really Making Progress in Group Recommendation? Unmasking the Tie-Breaking Illusion](https://arxiv.org/abs/2608.11190)
中文标题：我们真的在小组推荐方面取得了进展吗？揭开打破捆绑的幻觉
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [How to Verify Consistency of Probabilistic Claims](https://arxiv.org/abs/2608.11181)
中文标题：如何验证概率性声明的一致性
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [MultiModal Code-Switching: Interleaving Visual Objects into Language for Explicit Object-Level Alignment](https://arxiv.org/abs/2608.11167)
中文标题：多模态代码切换：将可视化对象交织到语言中以实现显式对象级对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Agentic Configuration Management (ACM): A Reference Configuration Model for Governed Agentic Systems](https://arxiv.org/abs/2608.11166)
中文标题：Agentic Configuration Management (ACM)：A Reference Configuration Model 面向 Governed Agentic Systems
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [PRMU: A Corpus-Free Benchmark for Person-Centric Knowledge Unlearning in Multimodal Large Language Models](https://arxiv.org/abs/2608.11149)
中文标题：PRMU：A Corpus-Free 基准 面向 Person-Centric Knowledge Unlearning in Multimodal Large Language Models
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [The Illusion of Cross-Lingual Safety in Low-Resource Languages](https://arxiv.org/abs/2608.11146)
中文标题：低资源语言中的跨语言安全错觉
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding](https://arxiv.org/abs/2608.11095)
中文标题：为什么CLAUDE.md不断增长？ Agentic编码中的灾难性记忆
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Static in Frames, Dynamic in Events: Rethinking Features in Event Cameras as Motion Cues](https://arxiv.org/abs/2608.11075)
中文标题：帧中的静态，事件中的动态：将事件摄像机中的功能重新思考为运动线索
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CapProbe: Evaluating Detailed Image Captions via Full-Scene Dense Question Answering](https://arxiv.org/abs/2608.11074)
中文标题：CapProbe ：通过全景密集问答评估详细的图像标题
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Mapping and Measuring the Behavioral Evolution of Large Language Models](https://arxiv.org/abs/2608.11027)
中文标题：绘制和测量大型语言模型的行为进化
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Data Attribution of Emergent Misalignment with Persona Features](https://arxiv.org/abs/2608.11025)
中文标题：紧急错位的数据归因与角色特征
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [TimeRoute: Time-Aware Modality Routing and Diffusion for Multi-Modal Recommendation](https://arxiv.org/abs/2608.10983)
中文标题：TimeRoute：Time-Aware Modality Routing 与 Diffusion 面向 Multi-Modal Recommendation
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
