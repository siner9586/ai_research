from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n([\s\S]*?)\n---\n", text)
    if not match:
        raise SystemExit(f"Missing frontmatter: {path}")
    meta: dict = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        try:
            meta[key] = json.loads(value)
        except json.JSONDecodeError:
            meta[key] = value.strip('"')
    return meta


def has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text or ""))


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    zh_dir = root / "data" / "content" / "zh" / "daily"
    candidates = []
    for path in zh_dir.glob("*.md"):
        if path.stem.endswith("-sources"):
            continue
        meta = parse_frontmatter(path)
        if meta.get("page_type") != "brief":
            continue
        candidates.append((str(meta.get("date", "")), path, meta))
    if not candidates:
        raise SystemExit("No Chinese daily brief found")
    _date, path, meta = sorted(candidates, key=lambda item: item[0])[-1]
    titles = meta.get("featured_paper_titles_zh") or []
    if len(titles) != 6:
        raise SystemExit(f"{path}: expected 6 featured_paper_titles_zh, got {len(titles)}")
    bad = [title for title in titles if not isinstance(title, str) or not title.strip() or not has_cjk(title)]
    if bad:
        raise SystemExit(f"{path}: non-localized featured_paper_titles_zh entries: {bad}")
    urls = meta.get("featured_paper_urls") or []
    if len(urls) != 6:
        raise SystemExit(f"{path}: expected 6 featured_paper_urls, got {len(urls)}")
    print(f"featured_titles_guard=passed date={meta.get('date')} path={path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
