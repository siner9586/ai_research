from __future__ import annotations

from ..config import topics_config


def classify_topic(title: str, abstract: str, lang: str = "en") -> tuple[str, str, list[str]]:
    text = f"{title} {abstract}".lower()
    best_topic = None
    best_hits: list[str] = []

    for topic in topics_config().get("topics", []):
        hits = [keyword for keyword in topic.get("keywords", []) if keyword.lower() in text]
        if len(hits) > len(best_hits):
            best_topic = topic
            best_hits = hits

    if best_topic:
        return best_topic.get(lang, best_topic.get("en", best_topic["slug"])), best_topic["slug"], best_hits
    return ("其他" if lang == "zh" else "Other"), "other", []
