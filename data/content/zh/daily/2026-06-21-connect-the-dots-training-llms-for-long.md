---
title: "让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升 RAG 检索和知识库问答可靠性"
date: "2026-06-21"
target_date: "2026-06-19"
actual_date: "2026-06-18"
fallback_from: "2026-06-19"
lang: "zh"
slug: "2026-06-21-connect-the-dots-training-llms-for-long"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、增强多模态模型理解图表和文档的能力。"
tags: ["agents", "data-engineering", "evaluation", "multimodal", "rag", "robotics", "speech-audio", "systems", "training", "vision-generation"]
topics: ["agents", "data-engineering", "evaluation", "multimodal", "rag", "robotics", "speech-audio", "systems", "training", "vision-generation"]
sources_page: "/zh/daily/2026-06-21-connect-the-dots-training-llms-for-long-sources/"
generated_at: "2026-06-20T22:21:17.975150+00:00"
page_type: "brief"
candidate_count: 419
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning", "FFinRED: An Expert-Guided Benchmark Generation and Evaluation Framework for Financial LLM Red-Teaming", "StylisticBias: A Few Human Visual Cues Drive Most Social Biases in MLLMs", "SARLO-80: Worldwide Slant SAR Language Optic Dataset 80cm", "FlowBender: Feedback-Aware Training for Self-Correcting Conditional Flows", "Towards Modality-imbalanced Federated Graph Learning: A Data Synthesis-based Approach"]
featured_paper_urls: ["https://arxiv.org/abs/2606.20002", "https://arxiv.org/abs/2606.19887", "https://arxiv.org/abs/2606.20527", "https://arxiv.org/abs/2606.20523", "https://arxiv.org/abs/2606.20404", "https://arxiv.org/abs/2606.20382"]
featured_paper_titles_zh: ["连接点：通过强化学习，通过跨域泛化培训长生命周期代理的LLM", "FFinRED：An Expert-Guided 基准 Generation 与 评测 框架 面向 Financial LLM Red-Teaming", "StylisticBias ：少数人类视觉线索推动了传销中的大多数社会偏见", "SARLO-80 ：全球倾斜SAR语言光学数据集80厘米", "FlowBender：Feedback-Aware Training 面向 Self-Correcting Conditional Flows", "走向模态不平衡的联合图学习：一种基于数据合成的方法"]
---

# 让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升 RAG 检索和知识库问答可靠性

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、增强多模态模型理解图表和文档的能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning (Yanxi Chen, Weijie Shi, Yuexiang Xie, Boyi Hu, Yaliang Li, Bolin Ding, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.20002">2606.20002</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.20002">PDF</a></p>

中文标题：连接点：通过强化学习，通过跨域泛化培训长生命周期代理的LLM

信号显示：这项工作为训练大语言模型（ LLM ）提供了一个通用框架，以“连接点” （ CoD ） ，这是长生命周期代理所需的元能力：当基于LLM的人工智能代理部署在环境中时，它可以解决。关键词：agent、evaluation、agents、Agents and Tool Use。代码/数据可用性需查看原文确认。

### 2. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>FFinRED: An Expert-Guided Benchmark Generation and Evaluation Framework for Financial LLM Red-Teaming (Chaeyun Kim, Daeyoung Park, Junghwan Kim, Jinyoung Jeong, Eunji Song, Yongtaek Lim, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.19887">2606.19887</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.19887">PDF</a></p>

中文标题：FFinRED：An Expert-Guided 基准 Generation 与 评测 框架 面向 Financial LLM Red-Teaming

信号显示：现有的安全基准针对一般对抗情景，但忽略了财务特定风险。关键词：safety、evaluation、benchmark、eval。代码/数据可用性需查看原文确认。

### 3. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>StylisticBias: A Few Human Visual Cues Drive Most Social Biases in MLLMs (Shaghayegh Kolli, Timo Cavelius, Nafiseh Nikeghbal, Samantha Dalal, Jana Diesner)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.20527">2606.20527</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.20527">PDF</a></p>

中文标题：StylisticBias ：少数人类视觉线索推动了传销中的大多数社会偏见

信号显示：多模态大语言模型（ MLM ）越来越多地部署在个人和社会重要环境中，但这些模型如何判断人们的视觉线索仍然知之甚少。关键词：evaluation、benchmark、code、multimodal。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>SARLO-80: Worldwide Slant SAR Language Optic Dataset 80cm (Solène Debuysère, Nicolas Trouvé, Nathan Letheule, Elise Colin, Georgia Channing)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.20523">2606.20523</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.20523">PDF</a></p>

中文标题：SARLO-80 ：全球倾斜SAR语言光学数据集80厘米

信号显示：得益于大型光学基准，多模态基础模型已迅速发展，但合成孔径雷达（ SAR ）的可比资源仍然有限。关键词：retrieval、alignment、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 5. 改进图像生成、视觉理解和可控渲染

<p class="paper-meta-line"><span>FlowBender: Feedback-Aware Training for Self-Correcting Conditional Flows (Daniel Gilo, Sven Elflein, Ido Sobol, Or Litany)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.20404">2606.20404</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.20404">PDF</a></p>

中文标题：FlowBender：Feedback-Aware Training 面向 Self-Correcting Conditional Flows

信号显示：条件扩散和流程模型通常无法满足定义其任务的约束条件。关键词：inference、compression、alignment、systems。代码/数据可用性需查看原文确认。

### 6. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Towards Modality-imbalanced Federated Graph Learning: A Data Synthesis-based Approach (Zhengyu Wu, Hongchao Qin, Xunkai Li, Zekai Chen, Rong-Hua Li, Guoren Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.20382">2606.20382</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.20382">PDF</a></p>

中文标题：走向模态不平衡的联合图学习：一种基于数据合成的方法

信号显示：多模态联合图学习（ MM-FGL ）提供了一种自然的协作训练范式，但其实际部署受到两种模态不平衡粒度的挑战。关键词：deployment、alignment、code、multimodal。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Sovereign Execution Brokers: Enforcing Certificate-Bound Authority in Agentic Control Planes](https://arxiv.org/abs/2606.20520)
中文标题：主权执行经纪人：在代理控制平面上执行证书绑定授权
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [FreeStyle: Free Control of Style-Content Dual-Reference Generation from Community LoRA Mining](https://arxiv.org/abs/2606.20506)
中文标题：FreeStyle：Free Control of Style-Content Dual-Reference Generation 来自 Community LoRA Mining
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems](https://arxiv.org/abs/2606.20408)
中文标题：LLM代理安全、多回合红队、越狱基准、对抗鲁棒性、安全关键系统
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [CRAX: Fast Safe Reinforcement Learning Benchmarking](https://arxiv.org/abs/2606.20376)
中文标题：CRAX：Fast Safe Reinforcement Learning 基准ing
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [The Register Gap: A Meaning Intelligence Framework for Nigerian Public Discourse](https://arxiv.org/abs/2606.20255)
中文标题：注册差距：尼日利亚公共话语的意义情报框架
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think](https://arxiv.org/abs/2606.20246)
中文标题：微调视觉-语言-行动模型所需的层数比您想象的要少
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments](https://arxiv.org/abs/2606.20235)
中文标题：ScholarQuest：A Taxonomy-Guided 基准 面向 Agentic Academic Paper Search in Open Literature Environments
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [DeepForestVisionV2: Ecology-Driven Taxonomy Expansion for Camera-Trap Monitoring in African Tropical Forests](https://arxiv.org/abs/2606.20223)
中文标题：DeepForestVisionV2：Ecology-Driven Taxonomy Expansion 面向 Camera-Trap Monitoring in African Tropical Forests
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [ReNikud: Audio-Supervised Hebrew Grapheme-to-Phoneme Conversion](https://arxiv.org/abs/2606.20179)
中文标题：ReNikud ：音频监督希伯来语语素到音素的转换
关注理由：涉及语音与音频中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [MedRLM: Recursive Multimodal Health Intelligence for Long-Context Clinical Reasoning, Sensor-Guided Screening, Evidence-Grounded Decision Support, and Community-to-Tertiary Referral Optimization](https://arxiv.org/abs/2606.20164)
中文标题：MedRLM：Recursive Multimodal Health Intelligence 面向 Long-Context Clinical Reasoning，Sensor-Guided Screening，Evidence-Grounded Decision Support，与 Community-to-Tertiary Referral Optimization
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Modularity-Free Conflict-Averse Training for Generalized PINNs](https://arxiv.org/abs/2606.20156)
中文标题：Modularity-Free Conflict-Averse Training 面向 Generalized PINNs
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Personalized Keyword Spotting for User-Defined Keywords Leveraging Text-Independent Speaker Verification](https://arxiv.org/abs/2606.20106)
中文标题：利用与文本无关的说话者验证，为用户定义的关键词提供个性化关键词识别
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents](https://arxiv.org/abs/2606.20023)
中文标题：当低权限足够时：调查法学硕士客服代表的过度特权工具选择
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Repository-Level Solidity Code Generation with Large Language Models: From Prompting to Fine-Tuning](https://arxiv.org/abs/2606.19988)
中文标题：大型语言模型的存储库级固体代码生成：从提示到微调
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Advancing DialNav through Automatic Embodied Dialog Augmentation](https://arxiv.org/abs/2606.19948)
中文标题：通过自动嵌入式对话框增强来推进DialNav
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Timage: A Generative Text-in-Image Paradigm for Fine-Tuning Vision-Language Models](https://arxiv.org/abs/2606.19944)
中文标题：Timage：A Generative Text-in-Image Paradigm 面向 Fine-Tuning Vision-Language Models
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [PhysDrift: Bridging the Embodiment Gap in Humanoid Co-Speech Motion Generation](https://arxiv.org/abs/2606.19935)
中文标题：PhysDrift ：弥合人形共语运动生成中的实施方案差距
关注理由：涉及数据工程中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Speeding up the annotation process in semantic segmentation industrial applications](https://arxiv.org/abs/2606.19934)
中文标题：加快语义分割工业应用中的标注过程
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [CARE: Competence-Aware Reward Shaping for Adaptive Reasoning Length in Video-MLLMs](https://arxiv.org/abs/2606.19927)
中文标题：CARE：Competence-Aware Reward Shaping 面向 Adaptive Reasoning Length in Video-MLLMs
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Co-policy: Responsive Human-Robot Co-Creation for Musical Performances](https://arxiv.org/abs/2606.19914)
中文标题：共同政策：针对音乐表演的响应式人类-机器人共同创作
关注理由：涉及机器人与具身智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
