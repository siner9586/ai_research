from __future__ import annotations

import re


def collapse_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def first_sentence(text: str, max_chars: int = 260) -> str:
    clean = collapse_ws(text)
    match = re.search(r"(.+?[.!?])\s", clean)
    value = match.group(1) if match else clean
    return value[:max_chars].rstrip()


def markdown_excerpt(text: str, max_chars: int = 500) -> str:
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    text = re.sub(r"[#*_`>-]", " ", text)
    return collapse_ws(text)[:max_chars]
