---
title: "改进图像生成、视觉理解和可控渲染、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能"
date: "2026-11-19"
target_date: "2026-11-17"
actual_date: "2026-11-17"
fallback_from: ""
lang: "zh"
slug: "2026-11-19-lutbench-benchmarking-text-driven-photographic-look-transfer"
summary: "今天主要跟进：改进图像生成、视觉理解和可控渲染、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能。"
tags: ["agents", "code", "data-engineering", "evaluation", "robotics", "systems", "training", "video-generation", "vision-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "robotics", "systems", "training", "video-generation", "vision-generation"]
sources_page: "/zh/daily/2026-11-19-lutbench-benchmarking-text-driven-photographic-look-transfer-sources/"
generated_at: "2026-11-18T16:20:10.987211+00:00"
page_type: "brief"
candidate_count: 523
featured_count: 6
mentions_count: 20
featured_paper_titles: ["LUTBench: Benchmarking Text-Driven Photographic Look Transfer", "The Kernel Reality Check: Benchmarking and Distilling Efficient Attention at Scale", "Verifying Agents in Rubric-Graded Environments", "TRIDENT: Efficient Triple-Task Learning of Dehazing, Depth, and Uncertainty Estimation for Underwater 3-D Robot Visual Perception", "RoadAnnoter: An AI-Assisted Desktop Tool for Semantic Segmentation Annotation of Road-Scene Images", "SignAligner: Dual-Granularity Span Generation for Sign Language Alignment"]
featured_paper_urls: ["https://arxiv.org/abs/2611.23113", "https://arxiv.org/abs/2611.22947", "https://arxiv.org/abs/2611.22841", "https://arxiv.org/abs/2611.22224", "https://arxiv.org/abs/2611.22884", "https://arxiv.org/abs/2611.22409"]
featured_paper_titles_zh: ["LUTBench：基准ing Text-Driven Photographic Look Transfer", "内核现实检验：大规模基准测试和提炼高效注意力", "在评分细则评分环境中验证代理", "TRIDENT：Efficient Triple-Task Learning of Dehazing，Depth，与 Uncertainty Estimation 面向 Underwater 3-D Robot Visual Perception", "RoadAnnoter：An AI-Assisted Desktop Tool 面向 Semantic Segmentation Annotation of Road-Scene Images", "SignAligner：Dual-Granularity Span Generation 面向 Sign Language Alignment"]
---

# 改进图像生成、视觉理解和可控渲染、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能

## 今天最值得跟进的方向

今天的高分论文主要指向：改进图像生成、视觉理解和可控渲染、提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 改进图像生成、视觉理解和可控渲染

<p class="paper-meta-line"><span>LUTBench: Benchmarking Text-Driven Photographic Look Transfer (Chuanzhi Xu, Boyu Wei, Chengkun Yue, Xuanhua Yin, Yiyang Li, Chupeng Liu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.23113">2611.23113</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.23113">PDF</a></p>

中文标题：LUTBench：基准ing Text-Driven Photographic Look Transfer

信号显示：摄影调色可以塑造照片的色调和色彩，以达到理想的效果。关键词：serving、alignment、evaluation、benchmark。代码/数据可用性需查看原文确认。

### 2. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>The Kernel Reality Check: Benchmarking and Distilling Efficient Attention at Scale (Fırat Öncel, Cem Subakan, Mirco Ravanelli, Çağatay Yıldız)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.22947">2611.22947</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.22947">PDF</a></p>

中文标题：内核现实检验：大规模基准测试和提炼高效注意力

信号显示：核化注意力方法旨在用 $O(N)$ 的替代方法来替代 softmax 注意力的 $O(N^2)$ 复杂度，在过去五年中一直是研究的重点。关键词：inference、evaluation、benchmark、code。代码/数据可用性需查看原文确认。

### 3. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>Verifying Agents in Rubric-Graded Environments (Markus Dücker, Vaibhav Kumar, Yi Liu, Ronak Chaudhary, Andreas Plesner, Francisco Guzmán, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.22841">2611.22841</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.22841">PDF</a></p>

中文标题：在评分细则评分环境中验证代理

信号显示：随着人工智能代理承担的任务越来越开放和复杂，验证其输出结果已被证明是一项艰巨的任务。关键词：agent、alignment、evaluation、code。代码/数据可用性需查看原文确认。

### 4. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>TRIDENT: Efficient Triple-Task Learning of Dehazing, Depth, and Uncertainty Estimation for Underwater 3-D Robot Visual Perception (Geonmo Yang, Younggun Cho)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.22224">2611.22224</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.22224">PDF</a></p>

中文标题：TRIDENT：Efficient Triple-Task Learning of Dehazing，Depth，与 Uncertainty Estimation 面向 Underwater 3-D Robot Visual Perception

信号显示：由于不可避免的光传播，水下视觉系统通常存在纹理模糊和色彩对比度低的问题。关键词：inference、evaluation、code、memory。代码/数据可用性需查看原文确认。

### 5. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>RoadAnnoter: An AI-Assisted Desktop Tool for Semantic Segmentation Annotation of Road-Scene Images (Nazmul Haque, Arnob Protim Roy)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.22884">2611.22884</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.22884">PDF</a></p>

中文标题：RoadAnnoter：An AI-Assisted Desktop Tool 面向 Semantic Segmentation Annotation of Road-Scene Images

信号显示：道路场景图像的准确语义分割对于道路安全研究至关重要；然而，多边形级别的标注仍然需要大量的人力，并限制了标注数据集的开发。关键词：safety、vision-language、open-source、data。代码/数据可用性需查看原文确认。

### 6. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>SignAligner: Dual-Granularity Span Generation for Sign Language Alignment (Jongbhin Woo, Youngjoon Jang, Joon Son Chung)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.22409">2611.22409</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.22409">PDF</a></p>

中文标题：SignAligner：Dual-Granularity Span Generation 面向 Sign Language Alignment

信号显示：大型手语语料库可从两个层面的时间标签中受益：用于字幕对齐的字幕跨度和用于手语识别的词语跨度。关键词：alignment、code、video、temporal。代码/数据可用性需查看原文确认。

## 其他值得关注
- [ForceBody: Force-Paired Parametric Body Motion with Torque Uncertainty](https://arxiv.org/abs/2611.22769)
中文标题：ForceBody：具有扭矩不确定性的力耦合参数化体运动
关注理由：涉及数据工程中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [TANGO: Real-World Unregistered RGB-Guided Hyperspectral Super-Resolution with Two-Camera Acquisitions](https://arxiv.org/abs/2611.22699)
中文标题：TANGO：采用双摄像头采集的真实世界未配准RGB引导超光谱超分辨率
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [LeViT-UNet++: Towards Balanced Fine-Grained Details and Context for Efficient Medical Image Segmentation](https://arxiv.org/abs/2611.22482)
中文标题：LeViT-UNet++：Towards Balanced Fine-Grained Details 与 Context 面向 Efficient Medical Image Segmentation
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [FIRE-Drive: Feasibility-Informed Risk Evaluation for End-to-End Diffusion Planning](https://arxiv.org/abs/2611.22297)
中文标题：FIRE-Drive：Feasibility-Informed Risk 评测 面向 End-to-End Diffusion Planning
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Transfer Once, Ask Locally: Compact Audio-Visual Memory for On-Device Question Answering](https://arxiv.org/abs/2611.23085)
中文标题：一次迁移，本地提问：用于设备端问答的紧凑型视听记忆
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [How Web Research Agents Interpret User Priorities](https://arxiv.org/abs/2611.22989)
中文标题：网页调研代理如何解读用户优先级
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [SWIR-cGAN: Synthesizing SWIR Bands Using VNIR Imagery from CBERS and AMAZONIA-1](https://arxiv.org/abs/2611.22922)
中文标题：SWIR-cGAN：Synthesizing SWIR Bands 使用 VNIR Imagery 来自 CBERS 与 AMAZONIA-1
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Network-Exposed Configuration Attacks on LLM-Controlled Social Robots](https://arxiv.org/abs/2611.22761)
中文标题：针对LLM控制的社交机器人的网络暴露配置攻击
关注理由：涉及机器人与具身智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [OVET-Consensus: Rank-Preserving Counterfactual Event Verification for Video Moment Grounding](https://arxiv.org/abs/2611.22637)
中文标题：OVET-Consensus：Rank-Preserving Counterfactual Event Verification 面向 Video Moment 落地
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [MIPR: A Benchmark for Reasoning-Intensive Multimodal Intent-to-Product Retrieval with Multi-Category Solutions](https://arxiv.org/abs/2611.22509)
中文标题：MIPR：一种用于推理密集型多模态意图到产品检索的基准，提供多类别解决方案
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Bad Apples in the Kitchen: How LLM Teams Detect, Correct, and Calibrate Against Their Misaligned Members](https://arxiv.org/abs/2611.22342)
中文标题：厨房里的害群之马：LLM 团队如何发现、纠正和调整与团队目标不一致的成员
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Breaking Visual Conventions: Spectrally Coupled Weight Perturbation for Creative Image Generation](https://arxiv.org/abs/2611.22318)
中文标题：打破视觉惯例：用于创意图像生成的谱耦合权重扰动
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding](https://arxiv.org/abs/2611.22296)
中文标题：SpecSearch：迈向硬件感知的⾼效推测解码
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [From Imperfective Paradox to Moorean Absurdity: Single-Chain Reasoning Lock-In and Multi-Candidate Verbalization Across Aspectual and Pragmatic Ambiguity](https://arxiv.org/abs/2611.22188)
中文标题：从不完悖论到穆尔式荒谬：跨越体貌和语用歧义的单链推理锁定与多候选表达
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Unsupervised Multi-modal Medical Image Registration via Invertible Translation](https://arxiv.org/abs/2611.22152)
中文标题：通过可逆转换实现的无监督多模态医学影像配准
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Text-Guided Modality Correction for Open-Vocabulary Object Detection](https://arxiv.org/abs/2611.22126)
中文标题：用于开放词汇物体检测的文本引导式模态校正
关注理由：涉及视觉与图像生成中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [RegimeCouncil: Paired-Evidence Routing For Memory Conflict Governance In LLM Agents](https://arxiv.org/abs/2611.22113)
中文标题：RegimeCouncil：Paired-Evidence Routing 面向 Memory Conflict Governance In LLM Agents
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [HyCoInfer: Cloud-Edge Collaborative Inference for Large Language Models on Heterogeneous GPU-FPGA Architectures](https://arxiv.org/abs/2611.22086)
中文标题：HyCoInfer：Cloud-Edge Collaborative Inference 面向 Large Language Models on Heterogeneous GPU-FPGA Architectures
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [CRA: Continuous Risk Assessment for Safety-critical Visual Navigation](https://arxiv.org/abs/2611.22080)
中文标题：CRA：Continuous Risk 评估 面向 Safety-critical Visual Navigation
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [SkillBuffBench: Measuring What Agent Skills Contribute across Harnesses, Models, Skill Access Modes and Memory](https://arxiv.org/abs/2611.22017)
中文标题：SkillBuffBench：Measuring What Agent Skills Contribute across Harnesses，Models，Skill Access Modes 与 Memory
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
