from __future__ import annotations

import json
import os
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ..config import REPO_ROOT, load_yaml

_CACHE_PATH = REPO_ROOT / "data" / "translations" / "title_zh_cache.json"
_GLOSSARY_NAME = "title_translation_glossary.yml"

# High-confidence curated translations. These seed the localizer and override external tools.
_EXACT: dict[str, str] = {
    "A Privacy-Preserving Framework Using Remote Data Science for Inter-Institutional Student Retention Prediction": "一种利用远程数据科学进行跨机构学生留存预测的隐私保护框架",
    "Rigel: Reverse-Engineering the Metal 4.1 Tensor Compute Path on the Apple M4 Max GPU": "Rigel：逆向解析 Apple M4 Max GPU 上 Metal 4.1 张量计算路径",
    "EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery": "EurekAgent：面向自主科学发现的 Agent 环境工程",
    "AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility": "AgentBeats：面向开放性、标准化与可复现性的 Agent 化评测框架",
    "SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale": "SPARC：从大规模机器人示范中生成可靠空间标注",
    "Mod-Guide: An LLM-based Content Moderation Feedback System to Address Insensitive Speech toward Indigenous Ethnic and Religious Minority Communities": "Mod-Guide：面向原住民、少数族裔与宗教少数群体不敏感言论的 LLM 内容审核反馈系统",
    "An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics": "面向湿实验室机器人的具身仿真平台、基准与数据高效增强框架",
    "MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems": "MAStrike：面向多智能体系统的 Shapley 引导合谋红队测试",
    "SafeLLM: Extraction as a Hallucination-Resistant Alternative to Rewriting in Safety-Critical Settings": "SafeLLM：安全关键场景中以抽取替代改写的抗幻觉方案",
    "LongSpike: Fractional Order Spiking State Space Models for Efficient Long Sequence Learning": "LongSpike：用于高效长序列学习的分数阶脉冲状态空间模型",
    "SMGFM: Spectral Multimodal Graph Pretraining for Multimodal-Attributed Graphs": "SMGFM：面向多模态属性图的谱域多模态图预训练",
    "LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories": "LabVLA：将视觉-语言-动作模型落地到科学实验室",
    "ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation": "ActiveSAM：面向快速准确开放词汇分割的图像条件类别剪枝",
    "ARB4WM: An Adversarial Robustness Benchmark for World Models in Continuous Control": "ARB4WM：面向连续控制世界模型的对抗鲁棒性基准",
    "When Confidence Lacks Concepts: Interpretable OOD Detection via Representation Perturbations": "当置信度缺少概念：基于表征扰动的可解释分布外检测",
    "Selection Without Signal, Recovery Through Expression: A Measurement Study of Post-Hoc Falsification Operators for Frozen Small Code Models": "无信号选择与表达恢复：面向冻结小型代码模型的事后证伪算子测量研究",
    "Semantic Flip: Synthetic OOD Generation for Robust Refusal in Embodied Question Answering and Spatial Localization": "语义翻转：面向具身问答与空间定位鲁棒拒答的合成式分布外样本生成",
    "Decoupling Semantics from Distortions: Multi-Scale Two-Stream Vision-Language Alignment for AI-Generated Image Quality Assessment": "解耦语义与失真：面向 AI 生成图像质量评估的多尺度双流视觉语言对齐",
    "All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code": "烟雾缭绕却未报警：Agent 编写测试代码中的 Oracle 信号",
}

_DEFAULT_TERM_RULES: list[tuple[str, str]] = [
    ("Privacy-Preserving", "隐私保护"),
    ("Remote Data Science", "远程数据科学"),
    ("Inter-Institutional", "跨机构"),
    ("Student Retention Prediction", "学生留存预测"),
    ("Embodied Simulation Platform", "具身仿真平台"),
    ("Wet-Lab Robotics", "湿实验室机器人"),
    ("Data-Efficient Augmentation Framework", "数据高效增强框架"),
    ("Shapley-Guided", "Shapley 引导"),
    ("Collusive Red-Teaming", "合谋红队测试"),
    ("Multi-Agent Systems", "多智能体系统"),
    ("Hallucination-Resistant", "抗幻觉"),
    ("Safety-Critical Settings", "安全关键场景"),
    ("Fractional Order Spiking State Space Models", "分数阶脉冲状态空间模型"),
    ("Long Sequence Learning", "长序列学习"),
    ("Spectral Multimodal Graph Pretraining", "谱域多模态图预训练"),
    ("Multimodal-Attributed Graphs", "多模态属性图"),
    ("Vision-Language-Action Models", "视觉-语言-动作模型"),
    ("Scientific Laboratories", "科学实验室"),
    ("Open-Vocabulary Segmentation", "开放词汇分割"),
    ("Image-Conditional Class Pruning", "图像条件类别剪枝"),
    ("Adversarial Robustness Benchmark", "对抗鲁棒性基准"),
    ("World Models", "世界模型"),
    ("Continuous Control", "连续控制"),
    ("Interpretable OOD Detection", "可解释分布外检测"),
    ("Representation Perturbations", "表征扰动"),
    ("Post-Hoc Falsification Operators", "事后证伪算子"),
    ("Frozen Small Code Models", "冻结小型代码模型"),
    ("Synthetic OOD Generation", "合成式分布外样本生成"),
    ("Robust Refusal", "鲁棒拒答"),
    ("Embodied Question Answering", "具身问答"),
    ("Spatial Localization", "空间定位"),
    ("AI-Generated Image Quality Assessment", "AI 生成图像质量评估"),
    ("Multi-Scale Two-Stream Vision-Language Alignment", "多尺度双流视觉语言对齐"),
    ("Oracle Signals", "Oracle 信号"),
    ("Agent-Authored Test Code", "Agent 编写测试代码"),
    ("Reverse-Engineering", "逆向解析"),
    ("Tensor Compute Path", "张量计算路径"),
    ("Autonomous Scientific Discovery", "自主科学发现"),
    ("Agent Environment Engineering", "Agent 环境工程"),
    ("Agent Assessment", "Agent 评测"),
    ("Openness", "开放性"),
    ("Standardization", "标准化"),
    ("Reproducibility", "可复现性"),
    ("Reliable Spatial Annotations", "可靠空间标注"),
    ("Robot Demonstrations", "机器人示范"),
    ("Content Moderation Feedback System", "内容审核反馈系统"),
    ("Insensitive Speech", "不敏感言论"),
    ("Indigenous Ethnic and Religious Minority Communities", "原住民、少数族裔与宗教少数群体"),
    ("LLM-based", "基于 LLM 的"),
    ("Framework", "框架"),
    ("Platform", "平台"),
    ("Benchmark", "基准"),
    ("Evaluation", "评测"),
    ("Assessment", "评估"),
    ("Agentifying", "Agent 化"),
    ("Extraction", "抽取"),
    ("Rewriting", "改写"),
    ("Grounding", "落地"),
    ("at Scale", "的大规模方法"),
]

_DEFAULT_KEEP_TERMS = {
    "AI", "Agent", "LLM", "LRM", "RAG", "VLM", "VLA", "SAM", "OOD", "Oracle", "Shapley",
    "Mamba", "Transformer", "Diffusion", "LaTeX", "API", "GPU", "CPU", "CT", "EEG", "OCT",
    "PDF", "arXiv",
}


def localize_title_zh(title: str, *, use_network: bool | None = None, write_cache: bool = True) -> str:
    """Localize an AI paper title to Chinese without making daily publishing fragile.

    Order: cache -> curated exact -> glossary/template rules -> optional free online fallback -> safe fallback.
    Online translation is disabled unless TITLE_TRANSLATION_USE_NETWORK=1, because daily publishing must not
    depend on a rate-limited third-party service.
    """
    clean = normalize_title(title)
    if not clean:
        return "未命名论文"

    cache = _load_cache()
    cached = cache.get(clean)
    if isinstance(cached, dict) and cached.get("zh"):
        return normalize_title(str(cached["zh"]))

    if clean in _EXACT:
        zh = _EXACT[clean]
        _cache_translation(clean, zh, "exact", cache, write_cache)
        return zh

    glossary = _load_glossary()
    rule_based = _rule_based_translation(clean, glossary)
    rule_score = score_translation_quality(clean, rule_based)
    best_zh = rule_based
    best_source = "rules"
    best_score = rule_score

    if _network_enabled(use_network):
        online = _translate_with_mymemory(clean)
        if online:
            online = _apply_post_terms(online, glossary)
            online = normalize_title(online)
            online_score = score_translation_quality(clean, online)
            if online_score > best_score:
                best_zh = online
                best_source = "mymemory"
                best_score = online_score

    if not _has_cjk(best_zh):
        best_zh = _safe_structural_fallback(clean)
        best_source = "fallback"
        best_score = score_translation_quality(clean, best_zh)

    _cache_translation(clean, best_zh, best_source, cache, write_cache, best_score)
    return best_zh


def score_translation_quality(original: str, zh: str) -> float:
    if not zh:
        return 0.0
    score = 0.0
    if _has_cjk(zh):
        score += 0.45
    if "：" in zh or ":" in original:
        score += 0.08
    if len(zh) >= max(8, min(len(original) // 3, 18)):
        score += 0.12
    if _english_residue_ratio(zh) <= 0.45:
        score += 0.15
    if _preserves_keep_terms(original, zh):
        score += 0.15
    if not re.search(r"\b(the|and|for|with|from|via|using|toward)\b", zh, re.I):
        score += 0.05
    return min(score, 1.0)


def normalize_title(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").replace(" ,", ",").replace(" :", ":").strip()


def _load_glossary() -> dict[str, Any]:
    glossary = load_yaml(_GLOSSARY_NAME)
    terms = glossary.get("terms") or {}
    keep_terms = set(glossary.get("keep_terms") or []) | _DEFAULT_KEEP_TERMS
    return {"terms": terms, "keep_terms": keep_terms, "phrase_rules": glossary.get("phrase_rules") or []}


def _rule_based_translation(title: str, glossary: dict[str, Any]) -> str:
    text = title
    for phrase, replacement in sorted(_merged_terms(glossary).items(), key=lambda item: len(item[0]), reverse=True):
        text = re.sub(re.escape(phrase), replacement, text, flags=re.I)
    text = _apply_phrase_rules(text, glossary)
    text = re.sub(r"\s*:\s*", "：", text)
    text = re.sub(r"\s*,\s*", "，", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _merged_terms(glossary: dict[str, Any]) -> dict[str, str]:
    merged = {phrase: replacement for phrase, replacement in _DEFAULT_TERM_RULES}
    for phrase, replacement in (glossary.get("terms") or {}).items():
        merged[str(phrase)] = str(replacement)
    return merged


def _apply_phrase_rules(text: str, glossary: dict[str, Any]) -> str:
    out = text
    raw_rules = list(glossary.get("phrase_rules") or [])
    if not raw_rules:
        raw_rules = [
            {"pattern": r"^A\s+", "replacement": "一种"},
            {"pattern": r"^An\s+", "replacement": "一种"},
            {"pattern": r"^The\s+", "replacement": ""},
            {"pattern": r"\band\b", "replacement": "与"},
            {"pattern": r"\bfor\b", "replacement": "面向"},
            {"pattern": r"\bfrom\b", "replacement": "来自"},
            {"pattern": r"\btoward\b", "replacement": "面向"},
            {"pattern": r"\busing\b", "replacement": "使用"},
        ]
    for row in raw_rules:
        pattern = str(row.get("pattern", ""))
        replacement = str(row.get("replacement", ""))
        if not pattern:
            continue
        try:
            out = re.sub(pattern, replacement, out, flags=re.I)
        except re.error:
            continue
    return out


def _apply_post_terms(text: str, glossary: dict[str, Any]) -> str:
    out = text
    for term in glossary.get("keep_terms") or []:
        if not term:
            continue
        out = re.sub(re.escape(str(term)), str(term), out, flags=re.I)
    for phrase, replacement in sorted(_merged_terms(glossary).items(), key=lambda item: len(item[0]), reverse=True):
        out = re.sub(re.escape(phrase), replacement, out, flags=re.I)
    return out


def _network_enabled(value: bool | None) -> bool:
    if value is not None:
        return value
    return os.getenv("TITLE_TRANSLATION_USE_NETWORK", "0").lower() in {"1", "true", "yes", "on"}


def _translate_with_mymemory(title: str) -> str | None:
    try:
        params = {
            "q": title[:500],
            "langpair": "en|zh-CN",
        }
        email = os.getenv("TITLE_TRANSLATION_EMAIL")
        if email:
            params["de"] = email
        url = "https://api.mymemory.translated.net/get?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"User-Agent": "ai-research-brief/1.0"})
        timeout = float(os.getenv("TITLE_TRANSLATION_TIMEOUT", "4"))
        with urllib.request.urlopen(req, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
        translated = (payload.get("responseData") or {}).get("translatedText")
        if translated and isinstance(translated, str):
            return translated
    except Exception as exc:  # noqa: BLE001 - network fallback must never break publishing.
        print(f"title_localizer_mymemory_warning={exc!r}")
    return None


def _safe_structural_fallback(title: str) -> str:
    text = re.sub(r"\s*:\s*", "：", title)
    text = re.sub(r"\s*,\s*", "，", text)
    text = re.sub(r"\bfor\b", "面向", text, flags=re.I)
    text = re.sub(r"\bwith\b", "结合", text, flags=re.I)
    text = re.sub(r"\bvia\b", "通过", text, flags=re.I)
    text = re.sub(r"\band\b", "与", text, flags=re.I)
    return normalize_title(text)


def _load_cache() -> dict[str, Any]:
    if not _CACHE_PATH.exists():
        return {}
    try:
        return json.loads(_CACHE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _cache_translation(
    title: str,
    zh: str,
    source: str,
    cache: dict[str, Any],
    write_cache: bool,
    quality_score: float | None = None,
) -> None:
    if not write_cache:
        return
    quality_score = score_translation_quality(title, zh) if quality_score is None else quality_score
    existing = cache.get(title)
    if isinstance(existing, dict) and existing.get("zh") == zh and float(existing.get("quality_score") or 0) >= quality_score:
        return
    cache[title] = {
        "zh": zh,
        "source": source,
        "quality_score": round(float(quality_score), 3),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    _CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    _CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text or ""))


def _english_residue_ratio(text: str) -> float:
    tokens = re.findall(r"[A-Za-z][A-Za-z\-]{2,}", text or "")
    if not tokens:
        return 0.0
    keep = {term.lower() for term in _DEFAULT_KEEP_TERMS}
    residue = [token for token in tokens if token.lower() not in keep]
    return len(residue) / max(len(tokens), 1)


def _preserves_keep_terms(original: str, zh: str) -> bool:
    keep_terms = [term for term in _DEFAULT_KEEP_TERMS if re.search(rf"\b{re.escape(term)}\b", original)]
    if not keep_terms:
        return True
    return all(term in zh for term in keep_terms if len(term) > 2 or term in {"AI", "CT"})
