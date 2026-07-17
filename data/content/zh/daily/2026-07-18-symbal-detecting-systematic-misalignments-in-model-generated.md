---
title: "让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升代码生成、执行反馈和自动修复能力"
date: "2026-07-18"
target_date: "2026-07-16"
actual_date: "2026-07-16"
fallback_from: ""
lang: "zh"
slug: "2026-07-18-symbal-detecting-systematic-misalignments-in-model-generated"
summary: "今天主要跟进：让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升代码生成、执行反馈和自动修复能力。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "robotics", "safety", "systems", "training"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "robotics", "safety", "systems", "training"]
sources_page: "/zh/daily/2026-07-18-symbal-detecting-systematic-misalignments-in-model-generated-sources/"
generated_at: "2026-07-17T22:04:11.032151+00:00"
page_type: "brief"
candidate_count: 326
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Symbal: Detecting Systematic Misalignments in Model-Generated Captions", "RoboTTT: Context Scaling for Robot Policies", "SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment", "Learning Agile Navigation in Crowded Environments for Quadruped Robots", "On Success and Simplicity: A Second Look at Transferable Vision-Language Attack Pipeline", "StructureClaw: Traceable LLM Agents and an Executable Benchmark for Structural Engineering Workflows"]
featured_paper_urls: ["https://arxiv.org/abs/2607.15216", "https://arxiv.org/abs/2607.15275", "https://arxiv.org/abs/2607.15058", "https://arxiv.org/abs/2607.15036", "https://arxiv.org/abs/2607.14974", "https://arxiv.org/abs/2607.14896"]
featured_paper_titles_zh: ["Symbal ：检测模型生成字幕中的系统性错位", "RoboTTT：Context Scaling 面向 Robot Policies", "SUFLECA：Scaling Up Feature Learning 面向 CAD-to-image Alignment", "四足机器人在拥挤环境中学习敏捷导航", "成功与简单：可转移视觉-语言攻击管道的第二个视角", "StructureClaw：Traceable LLM Agents 与 an Executable 基准 面向 Structural Engineering Workflows"]
---

# 让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升代码生成、执行反馈和自动修复能力

## 今天最值得跟进的方向

今天的高分论文主要指向：让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力、提升代码生成、执行反馈和自动修复能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Symbal: Detecting Systematic Misalignments in Model-Generated Captions (Maya Varma, Jean-Benoit Delbrouck, Sophie Ostmeier, Akshay Chaudhari, Curtis Langlotz)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.15216">2607.15216</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.15216">PDF</a></p>

中文标题：Symbal ：检测模型生成字幕中的系统性错位

信号显示：多模态大语言模型（ MLLM ）在生成图像标题时经常引入错误，导致图像-文本对错。关键词：alignment、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 2. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>RoboTTT: Context Scaling for Robot Policies (Yunfan Jiang, Yevgen Chebotar, Ruijie Zheng, Fengyuan Hu, Yunhao Ge, Jimmy Wu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.15275">2607.15275</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.15275">PDF</a></p>

中文标题：RoboTTT：Context Scaling 面向 Robot Policies

信号显示：最近的机器人基础模型在单步或短历史视觉运动环境下运行。关键词：inference、latency、vision-language、robot。代码/数据可用性需查看原文确认。

### 3. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment (Saad Ejaz, Miguel Fernandez-Cortizas, Javier Civera, Holger Voos, Jose Luis Sanchez-Lopez)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.15058">2607.15058</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.15058">PDF</a></p>

中文标题：SUFLECA：Scaling Up Feature Learning 面向 CAD-to-image Alignment

信号显示：CAD到图像对齐旨在从单个RGB图像估计物体的9D姿态（旋转、平移和各向异性尺度） ，从而实现机器人和增强现实中的应用。关键词：alignment、benchmark、code、robotics。代码/数据可用性需查看原文确认。

### 4. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>Learning Agile Navigation in Crowded Environments for Quadruped Robots (Shuyu Wu, Zeyu Liu, Tianbao Zhang, Fanxing Li, Fangyu Sun, Mingkang Xiong, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.15036">2607.15036</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.15036">PDF</a></p>

中文标题：四足机器人在拥挤环境中学习敏捷导航

信号显示：由于严重的传感器阻塞和不可预测的人类运动，在动态和拥挤的环境中导航对四足机器人来说构成了重大挑战。关键词：rag、inference、deployment、safety。代码/数据可用性需查看原文确认。

### 5. 提升 RAG 检索和知识库问答可靠性

<p class="paper-meta-line"><span>On Success and Simplicity: A Second Look at Transferable Vision-Language Attack Pipeline (Yuchen Ren, Zhengyu Zhao, Chenhao Lin, Bo Yang, Chao Shen)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.14974">2607.14974</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.14974">PDF</a></p>

中文标题：成功与简单：可转移视觉-语言攻击管道的第二个视角

信号显示：已知视觉语言预训练模型（ VLPM ）容易受到对抗性攻击。关键词：rag、retrieval、code、vision-language。代码/数据可用性需查看原文确认。

### 6. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>StructureClaw: Traceable LLM Agents and an Executable Benchmark for Structural Engineering Workflows (Sizhong Qin, Yi Gu, Yao Jiang, Ao Cai, Changjian Zhou, Shaoxuan Shuai, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2607.14896">2607.14896</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2607.14896">PDF</a></p>

中文标题：StructureClaw：Traceable LLM Agents 与 an Executable 基准 面向 Structural Engineering Workflows

信号显示：解决结构工程请求需要不止一个答案；它需要一系列相互依赖的工件：解释需求、可计算模型、验证记录、求解器输出、代码检查记录和最终报告。关键词：agent、workflow、rag、evaluation。代码/数据可用性需查看原文确认。

## 其他值得关注
- [The Energy Society: A Simulation Environment for Studying Agent Cooperation under Survival Pressure](https://arxiv.org/abs/2607.14865)
中文标题：Energy Society：A Simulation Environment 面向 Studying Agent Cooperation under Survival Pressure
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [GlobalForge: Towards Robust AI-Generated Image Detection](https://arxiv.org/abs/2607.14684)
中文标题：GlobalForge ：实现强大的人工智能生成图像检测
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems](https://arxiv.org/abs/2607.14611)
中文标题：Bad Memory：Evaluating Prompt Injection Risks 来自 Memory in Agentic Systems
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Uni-AdaVD: Universal Concept Erasure for Visual Generation via Orthogonal Value Decomposition](https://arxiv.org/abs/2607.14521)
中文标题：Uni-AdaVD ：通过正交值分解进行视觉生成的通用概念擦除
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Contextualized Evaluation of Vision Language Models through Dynamic, Multi-turn Interactions](https://arxiv.org/abs/2607.14499)
中文标题：通过动态、多轮交互对视觉语言模型进行情境化评估
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [TAMF-VTON: Texture-Aware Mask-Free Virtual Try-On via High-Fidelity Image Synthesis](https://arxiv.org/abs/2607.14807)
中文标题：TAMF-VTON ：通过高保真图像合成实现纹理感知无掩模虚拟试用
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [WorkDrive: Roadwork Chain of Causation for Autonomous Driving](https://arxiv.org/abs/2607.14727)
中文标题：WorkDrive：Roadwork Chain of Causation 面向 Autonomous Driving
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Alipay-PIBench: A Realistic Payment Integration Benchmark for Coding Agents](https://arxiv.org/abs/2607.14573)
中文标题：Alipay-PIBench：A Realistic Payment Integration 基准 面向 Coding Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Democratizing Agent Deployment Safety: A Structural Monitoring Approach](https://arxiv.org/abs/2607.14570)
中文标题：民主化代理部署安全：结构性监控方法
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [A Modern Multimodal Assistant on a 6 GB 2011 GPU: Stage-Validated, All-GPU CUDA Inference for Fermi](https://arxiv.org/abs/2607.14568)
中文标题：一种Modern Multimodal Assistant on a 6 GB 2011 GPU：Stage-Validated，All-GPU CUDA Inference 面向 Fermi
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/abs/2607.15263)
中文标题：超越成功率：进攻性和防御性安全代理的成本意识评估
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [HoloGeo: Mitigating Landmark Bias in Geo-localization via Evidence-Driven Reasoning](https://arxiv.org/abs/2607.15255)
中文标题：HoloGeo ：通过循证推理减轻地理定位中的地标偏差
关注理由：涉及多模态模型中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [AutoSynthesis: An agentic system for automated meta-analysis](https://arxiv.org/abs/2607.15247)
中文标题：AutoSynthesis：An agentic system 面向 automated meta-analysis
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [BadWAM: When World-Action Models Dream Right but Act Wrong](https://arxiv.org/abs/2607.15207)
中文标题：BadWAM ：当世界行动模特梦想正确但行动错误时
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [MM-IssueLoc: A Controlled Benchmark for Evaluating Visual Evidence in Multimodal Repository-Level Issue Localization](https://arxiv.org/abs/2607.15205)
中文标题：MM-IssueLoc：A Controlled 基准 面向 Evaluating Visual Evidence in Multimodal Repository-Level Issue Localization
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Can We Trust Item Response Theory for AI Evaluation?](https://arxiv.org/abs/2607.15190)
中文标题：Can We Trust Item Response Theory 面向 AI 评测?
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy](https://arxiv.org/abs/2607.15176)
中文标题：为科学可视化素养建立多模态大型语言模型的基准
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents](https://arxiv.org/abs/2607.15095)
中文标题：数字万神殿：与LLM代理模拟和审计联盟组建
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [AlphaWiSE: Adaptive Weight Interpolation for Continual Multimodal Representation Learning](https://arxiv.org/abs/2607.15094)
中文标题：AlphaWiSE：Adaptive Weight Interpolation 面向 Continual Multimodal Representation Learning
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Introspective Attention Modulation for Safe Text-to-Image Generation](https://arxiv.org/abs/2607.14945)
中文标题：用于安全生成文本图像的内省注意力调制
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
