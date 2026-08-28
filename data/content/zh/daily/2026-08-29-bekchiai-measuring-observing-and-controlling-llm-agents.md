---
title: "让 Agent 更可靠地调用工具和复用技能、评测视频生成的时间一致性和运动真实感、提升代码生成、执行反馈和自动修复能力"
date: "2026-08-29"
target_date: "2026-08-27"
actual_date: "2026-08-27"
fallback_from: ""
lang: "zh"
slug: "2026-08-29-bekchiai-measuring-observing-and-controlling-llm-agents"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、评测视频生成的时间一致性和运动真实感、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "reasoning", "robotics", "speech-audio", "training", "video-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "reasoning", "robotics", "speech-audio", "training", "video-generation"]
sources_page: "/zh/daily/2026-08-29-bekchiai-measuring-observing-and-controlling-llm-agents-sources/"
generated_at: "2026-08-28T17:14:15.769340+00:00"
page_type: "brief"
candidate_count: 399
featured_count: 6
mentions_count: 20
featured_paper_titles: ["BekchiAI: Measuring, Observing, and Controlling LLM Agents in One Click", "Robust Neural Stimulation Response Modeling Through Meta-Learning and Pretraining", "INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment", "TempJail: Temporal Jailbreak Attacks against Image-to-Video Generation Models", "Instruction Quality Matters: Refining Instructions for Effective Preference Learning", "When Privacy Hurts Mergeability: Geometry-Aware Model Merging under Differential Privacy"]
featured_paper_urls: ["https://arxiv.org/abs/2608.26867", "https://arxiv.org/abs/2608.26649", "https://arxiv.org/abs/2608.27348", "https://arxiv.org/abs/2608.26971", "https://arxiv.org/abs/2608.26779", "https://arxiv.org/abs/2608.26655"]
featured_paper_titles_zh: ["BekchiAI：Measuring，Observing，与 Controlling LLM Agents in One Click", "通过元学习和预训练建立健壮的神经刺激反应模型", "INTENT-AS-A-TOOL使其易于跟踪代理错位", "TempJAIl ：针对图像到视频生成模型的临时越狱攻击", "教学质量很重要：为有效的偏好学习完善教学", "当隐私损害可合并性时：差异隐私下的几何感知模型合并"]
---

# 让 Agent 更可靠地调用工具和复用技能、评测视频生成的时间一致性和运动真实感、提升代码生成、执行反馈和自动修复能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、评测视频生成的时间一致性和运动真实感、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>BekchiAI: Measuring, Observing, and Controlling LLM Agents in One Click (Mesut Toruk)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.26867">2608.26867</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.26867">PDF</a></p>

中文标题：BekchiAI：Measuring，Observing，与 Controlling LLM Agents in One Click

信号显示：大语言模型代理在许多步骤中进行推理、调用工具和自主行动，但他们的代理技能（正确排序工具、在依赖关系下进行规划、判断不受信任的输入以及为生成的参数提供基础）很难准确衡量。关键词：agent、serving、latency、evaluation。代码/数据可用性需查看原文确认。

### 2. 评测视频生成的时间一致性和运动真实感

<p class="paper-meta-line"><span>Robust Neural Stimulation Response Modeling Through Meta-Learning and Pretraining (Matthew J Bryan, Daniel C Muir, Felix Schwock, Azadeh Yazdan-Shahmorad, Rajesh P N Rao)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.26649">2608.26649</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.26649">PDF</a></p>

中文标题：通过元学习和预训练建立健壮的神经刺激反应模型

信号显示：目标：基于模型的闭环神经刺激有望用于从帕金森病到感觉恢复的治疗应用，但部署受到两个障碍的限制： 1 ）预测模型，用于预测。关键词：deployment、eval、dataset、test。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment (Yutong Zhang, Jianshuo Dong, Peng Xu, Long Wang, Jie Zhang, Tianwei Zhang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.27348">2608.27348</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.27348">PDF</a></p>

中文标题：INTENT-AS-A-TOOL使其易于跟踪代理错位

信号显示：随着大语言模型(LLM)被部署为自主代理，安全故障越来越多地涉及后续行动。关键词：agent、alignment、safety、code。代码/数据可用性需查看原文确认。

### 4. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>TempJail: Temporal Jailbreak Attacks against Image-to-Video Generation Models (Qi Lu, Zehui Guo, David Yuanda Gan, Zijing Li, Hengda Zhang, Weijun Xu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.26971">2608.26971</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.26971">PDF</a></p>

中文标题：TempJAIl ：针对图像到视频生成模型的临时越狱攻击

信号显示：近年来，图像到视频（ I2V ）生成模型在主题一致性和时间一致性方面取得了显着进展，实现了高质量的视频合成。关键词：inference、serving、safety、evaluation。代码/数据可用性需查看原文确认。

### 5. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Instruction Quality Matters: Refining Instructions for Effective Preference Learning (Seohyeong Lee, Hwaran Lee, Buru Chang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.26779">2608.26779</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.26779">PDF</a></p>

中文标题：教学质量很重要：为有效的偏好学习完善教学

信号显示：偏好学习使用响应对优化模型，但这些对的信息性从根本上取决于生成它们的指令。关键词：alignment、benchmark、code、data。代码/数据可用性需查看原文确认。

### 6. 评测视频生成的时间一致性和运动真实感

<p class="paper-meta-line"><span>When Privacy Hurts Mergeability: Geometry-Aware Model Merging under Differential Privacy (Jin Liu, Junkang Liu, Ning Xi, Yinbin Miao, Dawei Wei, Ke Cheng, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2608.26655">2608.26655</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2608.26655">PDF</a></p>

中文标题：当隐私损害可合并性时：差异隐私下的几何感知模型合并

信号显示：模型合并承诺从独立微调的任务模型构建单个多任务模型，无需访问原始任务数据。关键词：serving、alignment、fine-tuning、rl。代码/数据可用性需查看原文确认。

## 其他值得关注
- [RuleWeaver: Benchmarking Rule-Centered Scenario Reasoning for Large Language Models](https://arxiv.org/abs/2608.26832)
中文标题：RuleWeaver：基准ing Rule-Centered Scenario Reasoning 面向 Large Language Models
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Your Voice Cloning System is Secretly a Voice Anonymizer](https://arxiv.org/abs/2608.27360)
中文标题：您的语音克隆系统是秘密的语音匿名器
关注理由：涉及语音与音频中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [MedFG-VQA: Low-Frequency Memory and Graph Attention for Lightweight Medical VQA](https://arxiv.org/abs/2608.26848)
中文标题：MedFG-VQA：Low-Frequency Memory 与 Graph Attention 面向 Lightweight Medical VQA
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Multi-Image Visual Token Pruning in Large Visual Language Models](https://arxiv.org/abs/2608.26806)
中文标题：大型视觉语言模型中的多图像视觉令牌修剪
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research](https://arxiv.org/abs/2608.26753)
中文标题：超越执行：在LLM驱动的科学研究中审计实验保真度
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [A Unified Descriptive-Complexity Framework for Model Selection under Correlated Designs](https://arxiv.org/abs/2608.26618)
中文标题：关联设计下模型选择的统一描述复杂性框架
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [SPEAR: Distilling Domain-Adaptive Reasoning Skeletons via Sequential Symbolic Alignment in Reinforcement Learning](https://arxiv.org/abs/2608.26550)
中文标题：SPEAR ：通过强化学习中的顺序符号对齐提取领域自适应推理骨架
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [HUG-VIS: A Multimodal Benchmark for Human-centered Understanding and Generation in Visual Intelligence](https://arxiv.org/abs/2608.26517)
中文标题：HUG-VIS：A Multimodal 基准 面向 Human-centered Understanding 与 Generation in Visual Intelligence
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [From Static to Dynamic: Benchmarking Real-World Code Review with MCR-Bench](https://arxiv.org/abs/2608.27442)
中文标题：从静态到动态：使用MCR-Bench对真实世界的代码审查进行基准测试
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution](https://arxiv.org/abs/2608.27439)
中文标题：RedEvoAgent ：经验驱动技能进化的自动红色团队代理
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Reconstructing Humans and Objects in Interaction using Large Reconstruction Models](https://arxiv.org/abs/2608.27407)
中文标题：使用大型重建模型重建交互中的人类和物体
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [BTS-AgentBench: A Deterministic, Replayable Pipeline from Read-Only Telemetry Logs to Agent Benchmarks](https://arxiv.org/abs/2608.27334)
中文标题：BTS-AgentBench：A Deterministic，Replayable Pipeline 来自 Read-Only Telemetry Logs to Agent 基准s
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware Verification](https://arxiv.org/abs/2608.27311)
中文标题：更智能地验证，进一步发展：通过行为感知验证实现高效的线束演进
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [A Point-of-Prescription Safety-Check System for Adverse Drug Reactions in Rural Bangladeshi Hospitals: A Feasibility Study](https://arxiv.org/abs/2608.27239)
中文标题：孟加拉国农村医院药物不良反应的处方安全性检查系统：可行性研究
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [PACE: A Unified Condense-and-Extract Paradigm for Fast VLM Inference](https://arxiv.org/abs/2608.27206)
中文标题：PACE：A Unified Condense-与-Extract Paradigm 面向 Fast VLM Inference
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [Unsupervised Adaptation of 3D CT Foundation Models for 3D CBCT Segmentation](https://arxiv.org/abs/2608.27190)
中文标题：Unsupervised Adaptation of 3D CT Foundation Models 面向 3D CBCT Segmentation
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [SSMB: Self-Supervised Local Feature Detection under Motion Blur](https://arxiv.org/abs/2608.27181)
中文标题：SSMB ：运动模糊下的自监督局部特征检测
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Parameter-Efficient pretrained-CT-to-MRI Transfer for Rectal Cancer Segmentation: Performance-Calibration Trade-offs](https://arxiv.org/abs/2608.27178)
中文标题：Parameter-Efficient pretrained-CT-to-MRI Transfer 面向 Rectal Cancer Segmentation：Performance-Calibration Trade-offs
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Ancient-Bench: A Comprehensive Multi-millennial, Multi-medium, and Multi-script Benchmark for Ancient Chinese Artifact Text Recognition](https://arxiv.org/abs/2608.27169)
中文标题：Ancient-Bench：A Comprehensive Multi-millennial，Multi-medium，与 Multi-script 基准 面向 Ancient Chinese Artifact Text Recognition
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [ANTShapes Benchmarking Datasets for Event-Based Neuromorphic Object Classification](https://arxiv.org/abs/2608.27150)
中文标题：ANTShapes 基准ing Datasets 面向 Event-Based Neuromorphic Object Classification
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
