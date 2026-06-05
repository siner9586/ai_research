from __future__ import annotations

import json
import re

from .base import LLMProvider


def _first_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return "这篇论文的摘要未提供足够细节"
    return re.split(r"(?<=[.!?。！？])\s+", text)[0][:260]


def _zh_focus(title: str, abstract: str) -> str:
    text = f"{title} {abstract}".lower()
    rules = [
        (("agent", "tool"), "让 Agent 更可靠地调用工具和复用技能"),
        (("reason", "planning", "verifier", "math"), "改进模型推理、规划或验证过程"),
        (("rag", "retrieval", "database", "index"), "提升检索增强生成和知识库问答的可靠性"),
        (("multimodal", "vision-language", "vlm", "chart", "document"), "强化多模态模型对图表、文档和视觉信息的理解"),
        (("code", "program", "execution", "repair", "api"), "提升代码生成、执行反馈和自动修复能力"),
        (("diffusion", "image", "render", "visual"), "改进图像生成、视觉理解或可控渲染"),
        (("video", "temporal", "motion", "frame"), "评测或提升视频生成的时间一致性"),
        (("safety", "alignment", "jailbreak", "guardrail", "red team"), "发现并缓解模型安全、越狱和对齐风险"),
        (("speech", "audio", "voice", "sound"), "扩展语音、音频或声音场景中的 AI 能力"),
        (("robot", "embodied", "manipulation", "navigation"), "把模型能力落到机器人和具身任务中"),
        (("interpret", "attribution", "mechanistic", "representation"), "解释模型内部表征和行为归因"),
        (("benchmark", "evaluation", "dataset", "metric"), "用新基准或评测方法暴露模型短板"),
        (("data", "synthetic", "curation", "deduplication"), "改进训练数据筛选、合成和去重流程"),
        (("inference", "serving", "latency", "throughput", "cache", "quantization"), "降低推理成本并提升部署效率"),
    ]
    for keys, desc in rules:
        if any(key in text for key in keys):
            return desc
    return "提供一个值得进一步核验的 AI 研究方向"


class MockLLMProvider(LLMProvider):
    def complete(self, prompt: str, *, system: str | None = None) -> str:
        if "OUTPUT_JSON" in prompt:
            lang = "zh" if "lang=zh" in prompt else "en"
            title_match = re.search(r"title=(.+)", prompt)
            abstract_match = re.search(r"abstract=(.+)", prompt)
            title = title_match.group(1).strip() if title_match else "paper"
            abstract = abstract_match.group(1).strip() if abstract_match else ""
            sentence = _first_sentence(abstract)
            if lang == "zh":
                focus = _zh_focus(title, abstract)
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
                    "why_it_matters": f"It matters because the paper targets a concrete AI research or engineering bottleneck: {sentence}",
                    "problem": f"The problem signal is: {sentence}",
                    "method": "The method description is constrained to the title, abstract, and public metadata.",
                    "practitioner_takeaway": "Practitioners should inspect the evaluation setup, data assumptions, and reproducibility assets.",
                    "limitations": "This assessment is based on arXiv preprint metadata and is not peer-review confirmation.",
                    "bullets": ["The original arXiv link remains the factual source.", "Code links are shown only when verified.", "Scores are ranking signals, not final quality judgments."],
                }
            return json.dumps(payload, ensure_ascii=False)
        head = " ".join(prompt.split())[:220]
        return f"Mock provider summary based only on supplied metadata: {head}"
