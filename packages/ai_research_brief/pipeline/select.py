from __future__ import annotations

import json
import re
from datetime import date, timedelta
from pathlib import Path
from string import punctuation
from typing import Any

from ..config import REPO_ROOT


def select_papers(
    scored,
    featured_min=3,
    featured_max=5,
    mentions_min=8,
    mentions_max=12,
    repeat_history: dict[str, dict[str, Any]] | None = None,
    repeat_guard_featured_strict: bool = True,
):
    repeat_history = repeat_history or {}
    featured = []
    used_topics = set()
    used_keys = set()

    for row in scored:
        if len(featured) >= featured_max:
            break
        duplicate = _history_match(row, repeat_history)
        if duplicate and repeat_guard_featured_strict:
            _mark_repeat(row, duplicate, "excluded_recent_duplicate", "recently selected; not eligible for featured")
            continue
        if _overlaps_current(row, used_keys):
            _mark_repeat(row, None, "excluded_current_duplicate", "duplicate within the current issue")
            continue
        if row.topic_slug not in used_topics or len(featured) < featured_min:
            row.selection_tier = "featured"
            _mark_repeat(row, duplicate, "fallback_recent_duplicate" if duplicate else "new", "selected as featured")
            featured.append(row)
            used_topics.add(row.topic_slug)
            used_keys.update(paper_identity_keys(row))

    featured_ids = {row.paper.arxiv_id for row in featured}
    mentions = []
    for row in scored:
        if len(mentions) >= mentions_max:
            break
        if row.paper.arxiv_id in featured_ids or row in featured:
            continue
        if _overlaps_current(row, used_keys):
            _mark_repeat(row, None, "excluded_current_duplicate", "duplicate within the current issue")
            continue
        duplicate = _history_match(row, repeat_history)
        if duplicate:
            _mark_repeat(row, duplicate, "excluded_recent_duplicate", "recently selected; reserved for fallback mentions only")
            continue
        row.selection_tier = "mention"
        _mark_repeat(row, None, "new", "selected as mention")
        mentions.append(row)
        used_keys.update(paper_identity_keys(row))

    if len(mentions) < mentions_min:
        for row in scored:
            if len(mentions) >= min(mentions_min, mentions_max):
                break
            if row.paper.arxiv_id in featured_ids or row in featured or row in mentions:
                continue
            if _overlaps_current(row, used_keys):
                continue
            duplicate = _history_match(row, repeat_history)
            if duplicate and duplicate.get("section") == "featured":
                _mark_repeat(row, duplicate, "excluded_recent_duplicate", "recently featured; not reused in fallback mentions")
                continue
            row.selection_tier = "mention"
            _mark_repeat(row, duplicate, "fallback_recent_duplicate" if duplicate else "new", "fallback mention fill")
            mentions.append(row)
            used_keys.update(paper_identity_keys(row))

    return featured, mentions


def build_repeat_history(current_day: date, days: int = 30, scope: str = "featured_and_mentions", repo_root: Path = REPO_ROOT) -> dict[str, dict[str, Any]]:
    history: dict[str, dict[str, Any]] = {}
    include_mentions = scope != "featured_only"
    content_cutoff = _content_history_cutoff(repo_root / "data" / "content", current_day)
    for offset in range(1, max(days, 0) + 1):
        item_day = current_day - timedelta(days=offset)
        selected_path = repo_root / "data" / "processed" / str(item_day) / "selected_papers.json"
        if selected_path.exists():
            _read_selected_history(selected_path, item_day, include_mentions, history)
    _read_content_history(repo_root / "data" / "content", content_cutoff, days, include_mentions, history)
    return history


def repeat_guard_summary(scored, featured, mentions, repeat_history: dict[str, dict[str, Any]], days: int) -> dict[str, Any]:
    selected = set()
    for row in featured + mentions:
        selected.update(paper_identity_keys(row))
    excluded = []
    for row in scored:
        duplicate = _history_match(row, repeat_history)
        if duplicate and not any(key in selected for key in paper_identity_keys(row)):
            excluded.append({
                "arxiv_id": row.paper.arxiv_id,
                "title": row.paper.title,
                "previous_seen_date": duplicate.get("date"),
                "previous_seen_section": duplicate.get("section"),
            })
    fallback_selected = [
        {
            "arxiv_id": row.paper.arxiv_id,
            "title": row.paper.title,
            "previous_seen_date": row.previous_seen_date,
            "previous_seen_section": row.previous_seen_section,
            "section": row.selection_tier,
        }
        for row in featured + mentions
        if row.repeat_guard_status == "fallback_recent_duplicate"
    ]
    return {
        "repeat_guard_days": days,
        "excluded_recent_duplicates_count": len(excluded),
        "excluded_recent_duplicates": excluded[:20],
        "fallback_allowed": bool(fallback_selected),
        "fallback_reason": "mentions_min fallback only" if fallback_selected else None,
        "fallback_selected_recent_duplicates": fallback_selected[:20],
    }


def paper_identity_keys(row) -> set[str]:
    keys = set()
    arxiv_id = str(getattr(row.paper, "arxiv_id", "") or "").strip().lower()
    if arxiv_id:
        keys.add(f"arxiv:{arxiv_id}")
    title = normalize_title(getattr(row.paper, "title", ""))
    if title:
        keys.add(f"title:{title}")
    return keys


def normalize_title(title: str) -> str:
    value = str(title or "").lower()
    value = re.sub(r"\barxiv\s*:?\s*", " ", value)
    value = re.sub(r"\bv\d+\b", " ", value)
    value = value.translate(str.maketrans({char: " " for char in punctuation + "：，。；、（）【】《》“”‘’"}))
    value = re.sub(r"\s+", " ", value).strip()
    return value


def _history_match(row, repeat_history: dict[str, dict[str, Any]]) -> dict[str, Any] | None:
    matches = [repeat_history[key] for key in paper_identity_keys(row) if key in repeat_history]
    if not matches:
        return None
    return max(matches, key=lambda item: str(item.get("date", "")))


def _overlaps_current(row, used_keys: set[str]) -> bool:
    return bool(paper_identity_keys(row) & used_keys)


def _mark_repeat(row, duplicate: dict[str, Any] | None, status: str, reason: str) -> None:
    row.repeat_guard_status = status
    row.previous_seen_date = duplicate.get("date") if duplicate else None
    row.previous_seen_section = duplicate.get("section") if duplicate else None
    row.repeat_guard_reason = reason


def _read_selected_history(path: Path, item_day: date, include_mentions: bool, history: dict[str, dict[str, Any]]) -> None:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return
    sections = ["featured"] + (["mentions"] if include_mentions else [])
    for section in sections:
        for row in payload.get(section, []):
            paper = row.get("paper", {}) if isinstance(row, dict) else {}
            _remember(history, paper.get("arxiv_id"), paper.get("title"), str(item_day), section, str(path))


def _content_history_cutoff(content_root: Path, current_day: date) -> date:
    latest: date | None = None
    if content_root.exists():
        for path in content_root.glob("*/daily/*.md"):
            if path.stem.endswith("-sources"):
                continue
            try:
                value = _frontmatter_value(path.read_text(encoding="utf-8"), "date")
                item_day = date.fromisoformat(value)
            except (OSError, TypeError, ValueError):
                continue
            if item_day <= current_day:
                continue
            if latest is None or item_day > latest:
                latest = item_day
    return max(current_day, latest + timedelta(days=1) if latest else current_day)


def _read_content_history(content_root: Path, current_day: date, days: int, include_mentions: bool, history: dict[str, dict[str, Any]]) -> None:
    if not content_root.exists():
        return
    oldest = current_day - timedelta(days=days)
    for path in content_root.glob("*/daily/*.md"):
        if path.stem.endswith("-sources"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        meta_date = _frontmatter_value(text, "date")
        try:
            item_day = date.fromisoformat(meta_date)
        except (TypeError, ValueError):
            continue
        if not (oldest <= item_day < current_day):
            continue
        featured_text, mentions_text = _split_sections(text)
        for arxiv_id, title in _paper_refs(featured_text):
            _remember(history, arxiv_id, title, str(item_day), "featured", str(path))
        if include_mentions:
            for arxiv_id, title in _paper_refs(mentions_text):
                _remember(history, arxiv_id, title, str(item_day), "mentions", str(path))


def _frontmatter_value(text: str, key: str) -> str | None:
    match = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if line.startswith(f"{key}:"):
            value = line.split(":", 1)[1].strip()
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value.strip('"')
    return None


def _split_sections(text: str) -> tuple[str, str]:
    match = re.search(r"\n##\s+(其他值得关注|Other papers worth tracking)\b", text)
    if not match:
        return text, ""
    return text[: match.start()], text[match.start():]


def _paper_refs(text: str) -> list[tuple[str, str | None]]:
    refs = []
    span_titles = re.findall(r"<span>(.*?)\s*\([^<]*?\)</span>.*?arxiv\.org/abs/(\d{4}\.\d{4,5})", text, flags=re.S)
    refs.extend((arxiv_id, re.sub(r"<.*?>", "", title).strip()) for title, arxiv_id in span_titles)
    linked_titles = re.findall(r"\[([^\]]+)\]\(https://arxiv\.org/abs/(\d{4}\.\d{4,5})\)", text)
    refs.extend((arxiv_id, title.strip()) for title, arxiv_id in linked_titles)
    for arxiv_id in re.findall(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", text):
        refs.append((arxiv_id, None))
    unique = []
    seen = set()
    for arxiv_id, title in refs:
        key = (arxiv_id, title or "")
        if key not in seen:
            seen.add(key)
            unique.append((arxiv_id, title))
    return unique


def _remember(history: dict[str, dict[str, Any]], arxiv_id: str | None, title: str | None, item_day: str, section: str, source: str) -> None:
    info = {"date": item_day, "section": section, "source": source}
    keys = []
    if arxiv_id:
        keys.append(f"arxiv:{str(arxiv_id).strip().lower()}")
    normalized = normalize_title(title or "")
    if normalized:
        keys.append(f"title:{normalized}")
    for key in keys:
        old = history.get(key)
        if old is None or str(info["date"]) > str(old.get("date", "")):
            history[key] = info
