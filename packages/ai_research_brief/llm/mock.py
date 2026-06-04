from __future__ import annotations

import json
import re

from .base import LLMProvider


class MockLLMProvider(LLMProvider):
    def complete(self, prompt: str, *, system: str | None = None) -> str:
        if "OUTPUT_JSON" in prompt:
            lang = "zh" if "lang=zh" in prompt else "en"
            title_match = re.search(r"title=(.+)", prompt)
            abstract_match = re.search(r"abstract=(.+)", prompt)
            title = title_match.group(1).strip() if title_match else "paper"
            abstract = abstract_match.group(1).strip() if abstract_match else ""
            sentence = abstract.split(". ")[0][:240] if abstract else title
            if lang == "zh":
                payload = {
                    "why_it_matters": f"它围绕可验证的 AI 研究问题展开，摘要中的核心线索是：{sentence}",
                    "problem": f"论文试图处理的问题是：{sentence}",
                    "method": "方法描述来自标题、摘要和公开元数据；在阅读全文前不扩展为未经验证的结论。",
                    "practitioner_takeaway": "从业者可以重点核查其评测设置、数据假设和是否有可复现实验资产。",
                    "limitations": "当前判断基于 arXiv 预印本元数据，不代表结论已经被同行评审确认。",
                    "bullets": ["保留原始 arXiv 链接作为事实来源。", "代码链接只在输入已验证时呈现。", "评分只是筛选信号，不是论文质量定论。"],
                }
            else:
                payload = {
                    "why_it_matters": f"It targets a verifiable AI research question. The abstract signal is: {sentence}",
                    "problem": f"The problem signal is: {sentence}",
                    "method": "The method description is constrained to the title, abstract, and public metadata.",
                    "practitioner_takeaway": "Practitioners should inspect the evaluation setup, data assumptions, and reproducibility assets.",
                    "limitations": "This assessment is based on arXiv preprint metadata and is not peer-review confirmation.",
                    "bullets": ["The original arXiv link remains the factual source.", "Code links are shown only when verified.", "Scores are ranking signals, not final quality judgments."],
                }
            return json.dumps(payload, ensure_ascii=False)
        head = " ".join(prompt.split())[:220]
        return f"Mock provider summary based only on supplied metadata: {head}"
