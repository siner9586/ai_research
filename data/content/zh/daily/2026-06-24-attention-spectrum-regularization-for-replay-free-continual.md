---
title: "增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-06-24"
target_date: "2026-06-22"
actual_date: "2026-06-22"
fallback_from: ""
lang: "zh"
slug: "2026-06-24-attention-spectrum-regularization-for-replay-free-continual"
summary: "今天主要跟进：增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "robotics", "speech-audio", "training", "video-generation", "vision-generation"]
topics: ["agents", "code", "evaluation", "multimodal", "rag", "reasoning", "robotics", "speech-audio", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-06-24-attention-spectrum-regularization-for-replay-free-continual-sources/"
generated_at: "2026-06-23T22:22:05.051895+00:00"
page_type: "brief"
candidate_count: 457
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Attention-Spectrum Regularization for Replay-Free Continual Multimodal LLMs", "IPO Finance Agent: Evaluation of LLM Financial Analysts beyond Finance Agent v2, with Automated Rubric Generation -- the Case of the SpaceX (SPCX) IPO", "AIR: Adaptive Interleaved Reasoning with Code in MLLMs", "Self-Compacting Language Model Agents", "Teaching LLMs String Matching, Backtracking, and Error Recovery to Deduce Bases and Truth Tables for the Combinatorially Exploding Bit Manipulation Puzzles", "NGPS: Structure-Preserving Self-Supervised Denoising via Neighbor-Guided Patch Sampling"]
featured_paper_urls: ["https://arxiv.org/abs/2606.23063", "https://arxiv.org/abs/2606.23032", "https://arxiv.org/abs/2606.23678", "https://arxiv.org/abs/2606.23525", "https://arxiv.org/abs/2606.23672", "https://arxiv.org/abs/2606.23200"]
featured_paper_titles_zh: ["无重播连续多模态LLM的注意力频谱正则化", "IPO Finance Agent：评测 of LLM Financial Analysts beyond Finance Agent v2，with Automated Rubric Generation -- the Case of the SpaceX (SPCX) IPO", "AIR ：使用MLLM中的代码进行自适应交错推理", "自我压缩语言模型代理", "教授LLM字符串匹配、回溯和错误恢复，以推导组合爆炸位操作拼图的基础和真值表", "NGPS ：通过邻居引导补丁采样进行结构保留自监督去噪"]
---

# 增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：增强多模态模型理解图表和文档的能力、让 Agent 更可靠地调用工具和复用技能、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Attention-Spectrum Regularization for Replay-Free Continual Multimodal LLMs (Chuangxin Zhao, Canran Xiao, Siyuan Ma, Mengyao Lyu, Yanbiao Ma, Jun Xia, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.23063">2606.23063</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.23063">PDF</a></p>

中文标题：无重播连续多模态LLM的注意力频谱正则化

信号显示：多模态大语言模型（ MLLM ）越来越需要适应视觉领域、问题类型和用户指令的非平稳流，但持续的微调往往会严重忘记以前获得的多模态技能。关键词：serving、benchmark、code、multimodal。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>IPO Finance Agent: Evaluation of LLM Financial Analysts beyond Finance Agent v2, with Automated Rubric Generation -- the Case of the SpaceX (SPCX) IPO (Mostapha Benhenda)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.23032">2606.23032</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.23032">PDF</a></p>

中文标题：IPO Finance Agent：评测 of LLM Financial Analysts beyond Finance Agent v2，with Automated Rubric Generation -- the Case of the SpaceX (SPCX) IPO

信号显示：财务代理v2 （由Vals AI开发）已成为评估财务任务中Anthropic Claude和OpenAI ChatGPT前沿语言模型的参考基准。关键词：agent、retrieval、deployment、evaluation。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>AIR: Adaptive Interleaved Reasoning with Code in MLLMs (Cong Han, Xiaohan Lan, Haibo Qiu, Yujie Zhong)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.23678">2606.23678</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.23678">PDF</a></p>

中文标题：AIR ：使用MLLM中的代码进行自适应交错推理

信号显示：在OpenAI o3发起的范式转变之后，交错推理与代码以增强多模态大语言模型（ MLLM ）已成为一个关键的研究前沿。关键词：rag、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Self-Compacting Language Model Agents (Tianjian Li, Jingyu Zhang, William Jurayj, Xi Wang, Chuanyang Jin, Mehrdad Farajtabar, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.23525">2606.23525</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.23525">PDF</a></p>

中文标题：自我压缩语言模型代理

信号显示：由思想链和工具调用组成的长代理跟踪积累了锚定后代的陈旧内容，并最终超出了上下文窗口。关键词：agent、inference、benchmark、fine-tuning。代码/数据可用性需查看原文确认。

### 5. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Teaching LLMs String Matching, Backtracking, and Error Recovery to Deduce Bases and Truth Tables for the Combinatorially Exploding Bit Manipulation Puzzles (Prateek Agnihotri, Sanchit Jain, Prabhat Agnihotri, Aditya Prasad, Shubham Jain)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.23672">2606.23672</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.23672">PDF</a></p>

中文标题：教授LLM字符串匹配、回溯和错误恢复，以推导组合爆炸位操作拼图的基础和真值表

信号显示：本文介绍了我们针对NVIDIA Nemotron模型推理挑战赛的算法创新，重点介绍了位操作难题。关键词：rag、code、reasoning、search。代码/数据可用性需查看原文确认。

### 6. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>NGPS: Structure-Preserving Self-Supervised Denoising via Neighbor-Guided Patch Sampling (Jaehyun Cho, YoungJoon Yoo)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.23200">2606.23200</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.23200">PDF</a></p>

中文标题：NGPS ：通过邻居引导补丁采样进行结构保留自监督去噪

信号显示：相邻切片自监督去噪对于体积医学成像具有吸引力，但切片间错位会破坏解剖学对应关系，并且当相邻切片被天真地用作目标时，通常会产生重影和边缘模糊。关键词：retrieval、serving、alignment、code。代码/数据可用性需查看原文确认。

## 其他值得关注
- [TriggerBench: Investigating Prospective Memory for Large Language Models](https://arxiv.org/abs/2606.23459)
中文标题：TriggerBench：Investigating Prospective Memory 面向 Large Language Models
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection](https://arxiv.org/abs/2606.23060)
中文标题：来自 Text Metrics to Model Internals：A Study of Whisper ASR Hallucination Detection
关注理由：涉及语音与音频中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Boosting Neural Video Codec via Scale-Driven Online Flow Refinement](https://arxiv.org/abs/2606.23023)
中文标题：通过规模驱动的在线流细化提升神经视频编解码器
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [PG-MAP: Joint MAP Optimization for Inference-Time Alignment of Diffusion and Flow-Matching Models](https://arxiv.org/abs/2606.22958)
中文标题：PG-MAP：Joint MAP Optimization 面向 Inference-Time Alignment of Diffusion 与 Flow-Matching Models
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [SingGuard: A Policy-Adaptive Multimodal LLM Guardrail with Dynamic Reasoning](https://arxiv.org/abs/2606.22873)
中文标题：SingGuard ：具有动态推理的政策自适应多模式LLM护栏
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [Text Dictates, Music Decorates: Energy-based Attention for Editable Dance Motion Generation](https://arxiv.org/abs/2606.22726)
中文标题：文字指示，音乐装饰：基于能量的关注可编辑的舞蹈动作生成
关注理由：涉及视频生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [UI-LIC: A Unified Framework for Evaluating Learned Image Compression Models](https://arxiv.org/abs/2606.23545)
中文标题：UI-LIC：A Unified 框架 面向 Evaluating Learned Image Compression Models
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [TTFT-Aware Graph Chain-of-Thought:Distance-Indexed Neural A* for Low-Hallucination Multi-Hop Medical Reasoning](https://arxiv.org/abs/2606.23108)
中文标题：TTFT-Aware Graph Chain-of-Thought：Distance-Indexed Neural A* 面向 Low-Hallucination Multi-Hop Medical Reasoning
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models](https://arxiv.org/abs/2606.22966)
中文标题：攻击可信的想象力：对Imagine-then-ACT世界模型的Oracle级诚信攻击
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Neural Operator Processes for Probabilistic Operator Learning under Partial Observations](https://arxiv.org/abs/2606.22946)
中文标题：局部观测下概率算子学习的神经算子过程
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [KaLM-Reranker-V1: Fast but Not Late Interaction for Compressed Document Reranking](https://arxiv.org/abs/2606.22807)
中文标题：KaLM-Reranker-V1：Fast but Not Late Interaction 面向 Compressed Document Reranking
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions](https://arxiv.org/abs/2606.22778)
中文标题：HAKARI-Bench：A Lightweight 基准 面向 Comparing Retrieval Architectures 与 Efficiency Settings under Unified Conditions
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [On the Limits of Prompt-Conditioned Language Models as General-Purpose Learners](https://arxiv.org/abs/2606.23668)
中文标题：作为通用学习者的即时条件语言模型的局限性
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions](https://arxiv.org/abs/2606.23654)
中文标题：EnterpriseClawBench：基准ing Agents 来自 Real Workplace Sessions
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [TailorMind: Towards Preference-Aligned Multimodal Content Generation](https://arxiv.org/abs/2606.23643)
中文标题：TAIlorMind ：朝着偏好一致的多模式内容生成迈进
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Pose Anything Anywhere:Model-free Object Poses from Arbitrary References](https://arxiv.org/abs/2606.23634)
中文标题：在任何地方摆出任何姿势：从任意引用中摆出无模型的对象姿势
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [MORL-A2C: Multi-Objective Reinforcement Learning Reranker for Optimizing Healthiness in MOPI-HFRS](https://arxiv.org/abs/2606.23603)
中文标题：MORL-A2C：Multi-Objective Reinforcement Learning Reranker 面向 Optimizing Healthiness in MOPI-HFRS
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Real-Time Multimodal Activity-Aware Error Detection in Robot-Assisted Surgery](https://arxiv.org/abs/2606.23593)
中文标题：机器人辅助手术中的实时多模式活动感知错误检测
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Evaluation Awareness Is Not One Capability: Evidence from Open Language Models](https://arxiv.org/abs/2606.23583)
中文标题：评估意识不是一种能力：来自开放语言模型的证据
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [LangMAP: A Language-Adaptive Approach to Tokenization](https://arxiv.org/abs/2606.23566)
中文标题：LangMAP ：一种语言自适应的令牌化方法
关注理由：涉及训练与后训练中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
