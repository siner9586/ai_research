from __future__ import annotations

import json
import os
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

from ..config import REPO_ROOT

_CACHE_PATH = REPO_ROOT / "data" / "translations" / "signal_zh_cache.json"

_EXACT: dict[str, str] = {
    "Despite the remarkable progress of Video Large Language Models (Video-LLMs), current online architectures still struggle to simultaneously process continuous video streams, decide autonomously when to respond, and preserve long-horizon contextual memory": "尽管 Video-LLM 已取得显著进展，现有在线架构仍难以同时处理连续视频流、自主判断何时回应，并保留长时程上下文记忆",
    "Software practitioners increasingly use AI coding agents that generate test code alongside production code in open source pull requests (PRs)": "软件从业者越来越多地使用 AI 编码 Agent，它们会在开源 PR 中与生产代码一起生成测试代码",
    "Reinforcement learning has improved the reasoning ability of large language models, but applying outcome-only rewards to video multimodal large language models (Video-MLLMs) provides limited guidance on which visual evidence should support the answer": "强化学习提升了大语言模型的推理能力，但将仅基于结果的奖励用于 Video-MLLM 时，难以充分指示哪些视觉证据应支撑答案",
    "The LLM-empowered personal health agents with user health (sensor) metrics have offered a promising pathway to alleviate global disparities in healthcare access": "由 LLM 驱动、结合用户健康传感指标的个人健康 Agent，为缓解全球医疗服务可及性差异提供了有前景的路径",
    "Recommender systems alleviate information overload, yet repeated feedback between recommendations and user interactions can reinforce existing preferences and narrow users' exposure, forming information cocoons": "推荐系统可以缓解信息过载，但推荐与用户交互之间的反复反馈会强化既有偏好、收窄用户接触范围，从而形成信息茧房",
}


def localize_signal_zh(text: str, *, use_network: bool | None = None, write_cache: bool = True) -> str:
    clean = _normalize(text)
    if not clean:
        return "摘要信号暂缺，需结合原文进一步核验"
    cache = _load_cache()
    cached = cache.get(clean)
    if isinstance(cached, dict) and cached.get("zh"):
        return _normalize(str(cached["zh"])).rstrip("。")
    if clean in _EXACT:
        zh = _EXACT[clean]
        _cache_translation(clean, zh, "exact", cache, write_cache)
        return zh
    zh = _translate_with_mymemory(clean) if _network_enabled(use_network) else None
    if zh and _has_cjk(zh):
        zh = _polish(zh)
        _cache_translation(clean, zh, "mymemory", cache, write_cache)
        return zh
    fallback = _safe_fallback(clean)
    _cache_translation(clean, fallback, "fallback", cache, write_cache)
    return fallback


def _translate_with_mymemory(text: str) -> str | None:
    try:
        params: dict[str, Any] = {
            "q": text[:500],
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
    except Exception as exc:  # noqa: BLE001 - external translation must never break publishing.
        print(f"signal_localizer_mymemory_warning={exc!r}")
    return None


def _safe_fallback(text: str) -> str:
    out = text
    replacements = [
        (r"Video Large Language Models \(Video-LLMs\)", "Video-LLM"),
        (r"large language models", "大语言模型"),
        (r"Reinforcement learning", "强化学习"),
        (r"AI coding agents", "AI 编码 Agent"),
        (r"Recommender systems", "推荐系统"),
        (r"information overload", "信息过载"),
        (r"information cocoons", "信息茧房"),
        (r"user interactions", "用户交互"),
        (r"continuous video streams", "连续视频流"),
        (r"long-horizon contextual memory", "长时程上下文记忆"),
        (r"semantic similarity", "语义相似性"),
        (r"unlabeled documents", "未标注文档"),
        (r"contrastive learning", "对比学习"),
        (r"temporal relevance", "时间相关性"),
    ]
    for pattern, replacement in replacements:
        out = re.sub(pattern, replacement, out, flags=re.I)
    if _has_cjk(out):
        return _polish(out)
    return f"该研究围绕题名与摘要所揭示的问题展开，具体信号需结合原文进一步核验：{text}"


def _polish(text: str) -> str:
    out = _normalize(text)
    out = out.replace("Video-LLMs", "Video-LLM").replace("Video MLLMs", "Video-MLLM")
    out = out.replace("LLM 授权", "LLM 驱动").replace("大型语言模型", "大语言模型")
    out = re.sub(r"\s+", " ", out).strip().rstrip("。.")
    return out


def _network_enabled(value: bool | None) -> bool:
    if value is not None:
        return value
    return os.getenv("TITLE_TRANSLATION_USE_NETWORK", "0").lower() in {"1", "true", "yes", "on"}


def _load_cache() -> dict[str, Any]:
    if not _CACHE_PATH.exists():
        return {}
    try:
        return json.loads(_CACHE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _cache_translation(title: str, zh: str, source: str, cache: dict[str, Any], write_cache: bool) -> None:
    if not write_cache:
        return
    cache[title] = {
        "zh": zh,
        "source": source,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    _CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    _CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip().rstrip("。.")


def _has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text or ""))
