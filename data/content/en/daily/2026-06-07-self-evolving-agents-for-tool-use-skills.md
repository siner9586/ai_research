---
title: "Make agents use tools and reusable skills more reliably, Strengthen multimodal understanding of charts, documents, and visual evidence, Improve model reasoning, planning, and verification"
date: "2026-06-07"
target_date: "2026-06-05"
actual_date: "2026-06-04"
fallback_from: "2026-06-05"
lang: "en"
slug: "2026-06-07-self-evolving-agents-for-tool-use-skills"
summary: "Today tracks: make agents use tools and reusable skills more reliably, strengthen multimodal understanding of charts, documents, and visual evidence, improve model reasoning, planning, and verification."
tags: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "robotics", "safety", "systems", "training", "video-generation"]
topics: ["agents", "code", "data-engineering", "evaluation", "interpretability", "multimodal", "rag", "robotics", "safety", "systems", "training", "video-generation"]
sources_page: "/en/daily/2026-06-07-self-evolving-agents-for-tool-use-skills-sources/"
generated_at: "2026-06-07T00:16:25.259314+00:00"
page_type: "brief"
candidate_count: 18
featured_count: 6
mentions_count: 12
---

# Make agents use tools and reusable skills more reliably, Strengthen multimodal understanding of charts, documents, and visual evidence, Improve model reasoning, planning, and verification

## What is worth tracking today

Today’s high-signal papers point to: make agents use tools and reusable skills more reliably, strengthen multimodal understanding of charts, documents, and visual evidence, improve model reasoning, planning, and verification. The notes below focus on the core problem, method signal, main claim, and keywords for each featured paper.

## Featured papers: core problem, method signal, and keywords

### 1. make agents use tools and reusable skills more reliably

<p class="paper-meta-line"><span>Self Evolving Agents for Tool Use Skills (Alice Chen, Bob Smith)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00001">2606.00001</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00001">PDF</a></p>

Core idea: this paper targets the problem of how agents can retain, reuse, and improve tool-use skills across tasks. It uses iterative self-improvement, unit tests, execution feedback, and evaluation to improve reusable tool-use workflows. The main claim is that execution feedback can become a practical signal for more reliable tool invocation, while transfer to real production systems still depends on task realism and integration constraints. Keywords: agents, tool use, execution feedback, unit tests. Code/data availability should be checked in the source paper.

### 2. strengthen multimodal understanding of charts, documents, and visual evidence

<p class="paper-meta-line"><span>Multimodal Safety Evaluation for Vision Language Models (Eva Green)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00004">2606.00004</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00004">PDF</a></p>

Core idea: this paper targets the problem of evaluating vision-language models under risky visual prompts, cross-modal ambiguity, and alignment failures. It uses a multimodal safety evaluation suite to improve stress testing for chart, document, and visual-evidence understanding. The main claim is that safety risks and multimodal comprehension should be examined in a shared evaluation frame, while deployment relevance depends on the source tasks and failure categories. Keywords: multimodal, safety evaluation, vision-language models, alignment. Code/data availability should be checked in the source paper.

### 3. improve model reasoning, planning, and verification

<p class="paper-meta-line"><span>Efficient Long Context Inference with Cache Compression (Carol Li)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00002">2606.00002</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00002">PDF</a></p>

Core idea: this paper targets the trade-off between memory cost, latency, and reasoning quality in long-context inference. It uses cache compression and systems-level long-context inference optimization to improve deployment efficiency while preserving code-reasoning behavior. The main claim is that compressed context state can reduce serving cost, but the boundary depends on model size, context length, hardware, and the exact reasoning tasks. Keywords: long context, cache compression, inference, code reasoning. Code/data availability should be checked in the source paper.

### 4. make RAG retrieval and knowledge-base QA more reliable

<p class="paper-meta-line"><span>RAG Evaluation under Noisy Retrieval (Dan Wang)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00003">2606.00003</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00003">PDF</a></p>

Core idea: this paper targets the reliability of retrieval-augmented generation when retrieved evidence is noisy, citations are missing, or documents are adversarial. It uses a benchmark built around noisy retrieval settings to improve diagnosis of evidence quality and answer robustness. The main claim is that RAG reliability can be decomposed into testable evidence, citation, and document-interference factors, which makes the paper useful for enterprise knowledge-base regression tests. Keywords: RAG, retrieval, noisy evidence, citations. Code/data availability should be checked in the source paper.

### 5. improve code generation, execution feedback, and automated repair

<p class="paper-meta-line"><span>Code Model Repair with Execution Feedback (Frank Moore)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00005">2606.00005</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00005">PDF</a></p>

Core idea: this paper targets patch generation and automated repair for code models when actual execution results are available. It uses execution-feedback loops, repository tests, and API-aware repair signals to improve code-fix workflows in more realistic engineering settings. The main claim is that test and execution signals can guide better patches, while performance on large repositories, complex dependencies, and multi-language stacks needs source-level verification. Keywords: code repair, execution feedback, repository tests, API-aware repair. Code/data availability should be checked in the source paper.

### 6. improve training-data curation, synthesis, and deduplication

<p class="paper-meta-line"><span>Synthetic Data Curation for Post Training (Henry Liu)</span> <a class="paper-meta-link" href="https://arxiv.org/abs/2606.00007">2606.00007</a> <a class="paper-meta-link" href="https://arxiv.org/pdf/2606.00007">PDF</a></p>

Core idea: this paper targets how post-training pipelines select higher-quality examples from synthetic instruction data. It uses data-pipeline curation, quality filters, and synthetic data organization to improve fine-tuning and post-training inputs. The main claim is that filtering and curation can shape downstream training value, while the exact rules, evaluation tasks, and generalization boundary should be confirmed in the source paper. Keywords: synthetic data, curation, post-training, quality filters. Code/data availability should be checked in the source paper.

## Other papers worth tracking
- [Preference Optimization for Safer Tool Agents](https://arxiv.org/abs/2606.00012): Covers tool use, execution feedback, and reusable capabilities; useful as an agent reliability lead.
- [Red Teaming Open Source LLM Guardrails](https://arxiv.org/abs/2606.00017): Covers model safety, guardrail routing, risk classification, or governance evaluation; useful as a safety workflow lead.
- [Database Native Retrieval for Enterprise RAG](https://arxiv.org/abs/2606.00013): Covers retrieval, knowledge-base QA, and evidence reliability; useful as a RAG evaluation lead.
- [Chart Understanding for Vision Language Models](https://arxiv.org/abs/2606.00014): Covers a concrete multimodal-model signal; useful as a follow-up candidate.
- [Agentic 3D Modeling through Code Execution](https://arxiv.org/abs/2606.00015): Covers tool use, execution feedback, and reusable capabilities; useful as an agent reliability lead.
- [Low Rank Adapters as Model Memory Probes](https://arxiv.org/abs/2606.00018): Covers model memory and adapter analysis; useful as a representation-analysis lead.
- [Mechanistic Attribution for Factual Editing](https://arxiv.org/abs/2606.00008): Covers attribution for factual editing; useful for interpretability and model-editing work.
- [Video Diffusion Models Need Temporal Tests](https://arxiv.org/abs/2606.00010): Covers temporal consistency and motion realism; useful for generative-video evaluation.
- [Training Data Deduplication for Foundation Models](https://arxiv.org/abs/2606.00016): Covers training-data deduplication and data governance; useful for data-engineering workflows.
- [Robotics Policies with Memory Grounded Planning](https://arxiv.org/abs/2606.00006): Covers robotic policies, memory, and planning; useful for embodied-agent follow-up.
- [Open Speech Agent Benchmark](https://arxiv.org/abs/2606.00009): Covers speech agents and benchmark design; useful for audio-agent evaluation.
- [Serving Quantized Models with Adaptive Batching](https://arxiv.org/abs/2606.00011): Covers inference cost, latency, throughput, and deployment constraints; useful for systems optimization.

## Reading boundaries
- Automated ranking favors papers with community, code, and applied-engineering signals.
- Briefs are based on titles, abstracts, and public metadata by default, not full-paper review.
- External API failures degrade optional signals and are reflected in internal records.
