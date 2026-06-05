from __future__ import annotations

import json
import re

from .base import LLMProvider


def _first_sentence(text: str, lang: str = "en") -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return "这篇论文的摘要未提供足够细节" if lang == "zh" else "the abstract does not provide enough detail"
    return re.split(r"(?<=[.!?。！？])\s+", text)[0][:260]


def _focus(title: str, abstract: str, lang: str) -> str:
    text = f"{title} {abstract}".lower()
    rules = [
        (("agent", "tool", "trajectory"), "让 Agent 更可靠地调用工具和复用技能", "make agents use tools and reusable skills more reliably"),
        (("reason", "planning", "verifier", "math"), "提升模型推理、规划和验证能力", "improve model reasoning, planning, and verification"),
        (("rag", "retrieval", "database", "index"), "提升 RAG 检索和知识库问答可靠性", "make RAG retrieval and knowledge-base QA more reliable"),
        (("multimodal", "vision-language", "vlm", "chart", "document"), "增强多模态模型理解图表和文档的能力", "strengthen multimodal understanding of charts, documents, and visual evidence"),
        (("code", "program", "execution", "repair", "api"), "提升代码生成、执行反馈和自动修复能力", "improve code generation, execution feedback, and automated repair"),
        (("diffusion", "image", "render", "visual"), "改进图像生成、视觉理解和可控渲染", "improve image generation, visual understanding, and controllable rendering"),
        (("video", "temporal", "motion", "frame"), "评测视频生成的时间一致性和运动真实感", "test temporal consistency and motion realism in video generation"),
        (("safety", "alignment", "jailbreak", "guardrail", "red team"), "识别并缓解模型安全、越狱和对齐风险", "identify and reduce safety, jailbreak, and alignment risks"),
        (("speech", "audio", "voice", "sound"), "扩展语音、音频和声音场景的 AI 能力", "extend AI capabilities across speech, audio, and sound tasks"),
        (("robot", "embodied", "manipulation", "navigation"), "把模型能力落到机器人和具身任务", "bring model capabilities into robotics and embodied tasks"),
        (("interpret", "attribution", "mechanistic", "representation"), "解释模型内部表征和行为归因", "explain internal representations and behavioral attribution"),
        (("benchmark", "evaluation", "eval", "dataset", "metric"), "用新基准和评测方法暴露模型短板", "use benchmarks and evaluations to expose model weaknesses"),
        (("data", "synthetic", "curation", "deduplication"), "改进训练数据筛选、合成和去重流程", "improve training-data curation, synthesis, and deduplication"),
        (("inference", "serving", "latency", "throughput", "cache", "quantization"), "降低推理成本并提升部署效率", "reduce inference cost and improve deployment efficiency"),
    ]
    for keys, zh_desc, en_desc in rules:
        if any(key in text for key in keys):
            return zh_desc if lang == "zh" else en_desc
    return "提供一个值得进一步核验的 AI 研究方向" if lang == "zh" else "track a high-signal AI research lead"


class MockLLMProvider(LLMProvider):
    def complete(self, prompt: str, *, system: str | None = None) -> str:
        if "OUTPUT_JSON" in prompt:
            lang = "zh" if "lang=zh" in prompt else "en"
            title_match = re.search(r"title=(.+)", prompt)
            abstract_match = re.search(r"abstract=(.+)", prompt)
            title = title_match.group(1).strip() if title_match else "paper"
            abstract = abstract_match.group(1).strip() if abstract_match else ""
            sentence = _first_sentence(abstract, lang)
            focus = _focus(title, abstract, lang)
            if lang == "zh":
                payload = {
                    "why_it_matters": f"重点在于：{focus}。摘要给出的直接线索是：{sentence}",
                    "problem": f"它要解决的问题可以理解为：在真实研究或工程场景中，{focus}仍不稳定、不透明或成本较高。",
                    "method": "方法线索来自标题、摘要和公开元数据；重点看它如何设计数据、评测、训练或系统流程，而不把摘要扩展成未验证结论。",
                    "practitioner_takeaway": "从业者可优先检查三点：是否有可复现资产，评测是否贴近真实场景，以及方案是否能迁移到自己的模型、检索、Agent 或部署链路。",
                    "limitations": "当前只是基于 arXiv 预印本元数据的筛选判断，不代表论文结论已经被同行评审或生产环境验证。",
                    "bullets": [
                        f"一句话：{focus}。",
                        "看点：摘要是否给出清晰任务、数据、评测或系统收益。",
                        "核验：优先打开原文确认实验设置、基线和代码/数据是否可用。",
                    ],
                }
            else:
                payload = {
                    "why_it_matters": f"Core idea: {focus}. The abstract signal is: {sentence}",
                    "problem": f"The paper targets a concrete bottleneck: {focus} is still unreliable, opaque, costly, or hard to evaluate in real workflows.",
                    "method": "The method note is constrained to the title, abstract, and public metadata; check how the paper sets up data, evaluation, training, or systems design before trusting the claim.",
                    "practitioner_takeaway": "First check whether code or data exist, whether the evaluation matches real use, and whether the idea can transfer into your model, RAG, agent, or deployment stack.",
                    "limitations": "This is an arXiv preprint triage note, not peer-reviewed validation or production evidence.",
                    "bullets": [
                        f"One-line read: {focus}.",
                        "Look for an explicit task, dataset, evaluation, or system gain.",
                        "Verify the setup, baselines, and code/data availability in the paper.",
                    ],
                }
            return json.dumps(payload, ensure_ascii=False)
        head = " ".join(prompt.split())[:220]
        return f"Mock provider summary based only on supplied metadata: {head}"
