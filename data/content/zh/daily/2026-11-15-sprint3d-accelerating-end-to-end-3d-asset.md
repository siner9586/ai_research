---
title: "提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力"
date: "2026-11-15"
target_date: "2026-11-13"
actual_date: "2026-11-12"
fallback_from: "2026-11-13"
lang: "zh"
slug: "2026-11-15-sprint3d-accelerating-end-to-end-3d-asset"
summary: "今天主要跟进：提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力。"
tags: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "safety", "systems", "training"]
topics: ["agents", "code", "data-engineering", "evaluation", "multimodal", "rag", "reasoning", "safety", "systems", "training"]
sources_page: "/zh/daily/2026-11-15-sprint3d-accelerating-end-to-end-3d-asset-sources/"
generated_at: "2026-11-14T16:32:06.316893+00:00"
page_type: "brief"
candidate_count: 397
featured_count: 6
mentions_count: 20
featured_paper_titles: ["Sprint3D: Accelerating End-to-End 3D Asset Generation through Pipeline Optimization", "MobileProbe: Adaptive Security Evaluation of Mobile Agents via Trajectory-Aware Injection", "Safety as a Budget: Calibrating the Control Channel of Constrained GRPO for Vision-Language Models", "ReA-Bench: Benchmarking Responsible Agent Auditing", "Gravity and Flight: Learning to Navigate Fine-Grained Remote Sensing Scenes", "AntEmbed: Dual-Mode Multimodal Embedding Model for Efficient and Fine-Grained Retrieval"]
featured_paper_urls: ["https://arxiv.org/abs/2611.16701", "https://arxiv.org/abs/2611.16693", "https://arxiv.org/abs/2611.16628", "https://arxiv.org/abs/2611.16493", "https://arxiv.org/abs/2611.16408", "https://arxiv.org/abs/2611.16405"]
featured_paper_titles_zh: ["Sprint3D：通过管道优化加速端到端3D资产生成", "MobileProbe：通过轨迹感知注入对移动代理进行自适应安全评估", "安全作为预算：校准受限 GRPO 的控制通道，用于视觉-语言模型", "ReA-Bench：基准ing Responsible Agent Auditing", "重力和飞行：学习在精细遥感场景中导航", "AntEmbed：Dual-Mode Multimodal Embedding Model 面向 Efficient 与 Fine-Grained Retrieval"]
---

# 提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力

## 今天最值得跟进的方向

今天的高分论文主要指向：提升代码生成、执行反馈和自动修复能力、让 Agent 更可靠地调用工具和复用技能、增强多模态模型理解图表和文档的能力。下面按核心问题、方法线索、主要论点和关键词整理，便于快速判断后续跟进价值。

## 重点论文：核心问题、方法线索与关键词

### 1. 提升代码生成、执行反馈和自动修复能力

<p class="paper-meta-line"><span>Sprint3D: Accelerating End-to-End 3D Asset Generation through Pipeline Optimization (Sho Kuno, Ruihan Yu, Yonghao Yu, Guixu Lin, Lian Fu, Muyao Niu, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.16701">2611.16701</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.16701">PDF</a></p>

中文标题：Sprint3D：通过管道优化加速端到端3D资产生成

信号显示：图像转 3D 生成模型现在可以生成具有资产质量的纹理网格，但由于每个资产需要几分钟的时间，因此迭代速度仍然很慢，部署成本也很高。关键词：latency、alignment、evaluation、code。代码/数据可用性需查看原文确认。

### 2. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>MobileProbe: Adaptive Security Evaluation of Mobile Agents via Trajectory-Aware Injection (Yingbin Jin, Ji&#x27;an Wang, HaoYang Chai, Hanjun Luo, Li Hu, Xinfeng Li, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.16693">2611.16693</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.16693">PDF</a></p>

中文标题：MobileProbe：通过轨迹感知注入对移动代理进行自适应安全评估

信号显示：移动端 GUI 智能体读取手机屏幕，并代表用户操作应用程序，以完成多步任务，例如在线购物或发消息。关键词：agent、rag、deployment、evaluation。代码/数据可用性需查看原文确认。

### 3. 增强多模态模型理解图表和文档的能力

<p class="paper-meta-line"><span>Safety as a Budget: Calibrating the Control Channel of Constrained GRPO for Vision-Language Models (Bo Han)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.16628">2611.16628</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.16628">PDF</a></p>

中文标题：安全作为预算：校准受限 GRPO 的控制通道，用于视觉-语言模型

信号显示：强化学习可以教会视觉-语言模型 (VLM) 拒绝有害的图像-文本请求，但结果的安全程度是通过试运行中发现的奖励权重间接设定的。关键词：serving、safety、benchmark、vision-language。代码/数据可用性需查看原文确认。

### 4. 让 Agent 更可靠地调用工具和复用技能

<p class="paper-meta-line"><span>ReA-Bench: Benchmarking Responsible Agent Auditing (Zipeng Ye, Shenyu Dai, Yong Xie, Kun Wang, Jiyang Guan, Zhikai Chen, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.16493">2611.16493</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.16493">PDF</a></p>

中文标题：ReA-Bench：基准ing Responsible Agent Auditing

信号显示：随着代理在本地和云环境中自主执行任务，审计其执行轨迹可以帮助服务提供商识别风险并改进代理线束和基础模型。关键词：agent、retrieval、safety、benchmark。代码/数据可用性需查看原文确认。

### 5. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>Gravity and Flight: Learning to Navigate Fine-Grained Remote Sensing Scenes (Yuheng Zong, Minghua Wang, Xin Zhao, Xiaobin Liu, Yongjian Dong, Chanho Eom)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.16408">2611.16408</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.16408">PDF</a></p>

中文标题：重力和飞行：学习在精细遥感场景中导航

信号显示：视觉-语言模型的能力日益增强，但在复杂遥感场景中的推理仍可能较为粗略，且在任务相关视觉证据方面的依据不足。关键词：rag、evaluation、vision-language、fine-tuning。代码/数据可用性需查看原文确认。

### 6. 提升模型推理、规划和验证能力

<p class="paper-meta-line"><span>AntEmbed: Dual-Mode Multimodal Embedding Model for Efficient and Fine-Grained Retrieval (Kehang Jia, Teng Liu, Juntao Li, Hua Chen, Jinxiong Chang, Xiaobo Liang, et al.)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2611.16405">2611.16405</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2611.16405">PDF</a></p>

中文标题：AntEmbed：Dual-Mode Multimodal Embedding Model 面向 Efficient 与 Fine-Grained Retrieval

信号显示：判别性嵌入能够高效地编码原始多模态输入，但在处理细粒度语义方面存在困难。关键词：retrieval、alignment、code、multimodal。代码/数据可用性需查看原文确认。

## 其他值得关注
- [Contain, Conform, Compare (Extended Version): A Red-Teamed Evaluation Kit for Small Coding Agents and the Full Record of Its Experiments](https://arxiv.org/abs/2611.16485)
中文标题：ContAIn、Conform、Compare（扩展版）：用于小型编码代理的红队评估工具包及其完整实验记录
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [HIFC-IQA: Train-Free Cross-Domain Image Quality Assessment via Dual-Process Cognition](https://arxiv.org/abs/2611.16451)
中文标题：HIFC-IQA：通过双重过程认知实现的无训练跨域图像质量评估
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Model Distribution-Aware Multimodal Dataset Distillation](https://arxiv.org/abs/2611.16418)
中文标题：模型分布感知多模态数据集蒸馏
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [RICapBench: A Fine-Grained Visual Understanding Benchmark Dataset for Vision-Language Models in Remote Sensing](https://arxiv.org/abs/2611.16413)
中文标题：RICapBench：A Fine-Grained Visual Understanding 基准 Dataset 面向 Vision-Language Models in Remote Sensing
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [ReSID: Rethinking Long-Tail Retrieval in Generative Recommendation through Item Reachability](https://arxiv.org/abs/2611.16404)
中文标题：ReSID：通过项目可达性重新思考生成式推荐中的长尾检索
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Teach with Blinks: Breaking Linguistic Momentum in On-Policy Distillation for Fine-Grained Multimodal Perception](https://arxiv.org/abs/2611.16402)
中文标题：使用Blinks进行教学：在基于策略的蒸馏中打破语言惯性，以实现精细的多模态感知
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [TransXplainRRG: A Radiologist-Evaluated LVLM for Chest Radiograph Report Generation](https://arxiv.org/abs/2611.16393)
中文标题：TransXplainRRG：A Radiologist-Evaluated LVLM 面向 Chest Radiograph Report Generation
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Beyond Compressing Everything: Contrastive Memory Learning for Selective Context Compression](https://arxiv.org/abs/2611.16384)
中文标题：超越压缩一切：用于选择性上下文压缩的对比记忆学习
关注理由：涉及推理成本、延迟、吞吐和部署约束，可补充系统优化方向。
- [RADIANT: Redundancy-Aware Information Allocation for Universal Multi-Modal Fusion](https://arxiv.org/abs/2611.16382)
中文标题：RADIANT：Redundancy-Aware Information Allocation 面向 Universal Multi-Modal Fusion
关注理由：涉及任务设置、指标和失效案例，可补充模型评测与回归测试。
- [Evidence-Governed Adoption of Self-Generated Updates in Autonomous AI Agents](https://arxiv.org/abs/2611.16378)
中文标题：自主人工智能体对自生成更新的证据驱动型采用
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Rectified Looped Transformer](https://arxiv.org/abs/2611.16265)
中文标题：整流环路变压器
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [Few-Shot Cross-Subject Neural--Image Retrieval via Stimulus-Anchored Latent Bias Calibration](https://arxiv.org/abs/2611.16257)
中文标题：通过刺激锚定潜在偏差校准的少样本跨主体神经——图像检索
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [BWM-Forge: Agentic World Programming for Embodied Intelligence](https://arxiv.org/abs/2611.16221)
中文标题：BWM-Forge：Agentic World Programming 面向 Embodied Intelligence
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [WorldDraft: If Code Builds the World, Can Video Models Just Render It?](https://arxiv.org/abs/2611.16217)
中文标题：WorldDraft：如果代码构建了世界，那么视频模型是否就能将其渲染出来？
关注理由：涉及工具调用、执行反馈和可复用能力，可作为 Agent 工作流可靠性的补充线索。
- [When can an interpretability claim be trusted? Stability and certification of feature dimensionality, ridge leverage and the feature recovery rate](https://arxiv.org/abs/2611.16190)
中文标题：何时可以相信可解释性主张？特征维数、岭杠杆和特征恢复率的稳定性与认证
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Data-Efficient LLM Safety Alignment Guided by Interpretable Features](https://arxiv.org/abs/2611.16183)
中文标题：以可解释特征为指导的数据高效LLM安全对齐
关注理由：涉及模型安全、护栏路由、风险分类或治理评测，可作为安全评测与治理工具链的补充线索。
- [TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models](https://arxiv.org/abs/2611.17331)
中文标题：TTB：Test-time Baking 面向 Efficient Rendering of Decoder-only View Synthesis Models
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Learning When Diffusion Language Models Should Regenerate](https://arxiv.org/abs/2611.17320)
中文标题：了解扩散语言模型何时应重新生成
关注理由：涉及推理与规划中的新任务、数据或系统线索，可作为后续跟进清单的一部分。
- [Sketching Language Models for Context Attribution](https://arxiv.org/abs/2611.17313)
中文标题：为上下文归因勾勒语言模型
关注理由：涉及检索、知识库问答与证据可靠性，可作为 RAG 评测和企业知识系统的补充线索。
- [Al-Ghasali: A Computational Framework for Simulating Islamic Jurisprudential Rulings via Finite State Automata and Large Language Models](https://arxiv.org/abs/2611.17235)
中文标题：Al-Ghasali：一种通过有限状态自动机和大语言模型模拟伊斯兰教法判决的计算框架
关注理由：涉及代码智能中的新任务、数据或系统线索，可作为后续跟进清单的一部分。

## 阅读边界
- 自动排序会偏向有社区信号、代码信号和工程关键词的论文。
- 简报默认基于标题、摘要和公开元数据，不替代全文精读。
- 外部 API 限流或不可用时，相关信号会降级为空并在内部记录中保留说明。
