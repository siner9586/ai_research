from __future__ import annotations

import json
import re
from xml.sax.saxutils import escape

from ..config import REPO_ROOT, site_config, topics_config


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
BRIEF_TITLE_PREFIX_RE = re.compile(r"^(今日重点[:：]\s*|Today's focus:\s*)", re.I)
DEPRECATED_TEXT_PATTERNS = [
    (r"建议\s*先看每篇[^。]*。?", "下面按核心问题、方法线索、主要论点和关键词整理。"),
    (r"摘要\s*显示[:：]?", "核心线索："),
    (r"\s*重点\s*核验[:：]?[^。]*。?", " 代码/数据可用性需查看原文确认。"),
    (r"Open\s+the\s+original\s+paper[^.]*\.", "The notes below focus on the core problem, method signal, main claim, and keywords."),
    (r"The\s+abstract\s+points\s+to[:：]?", "Core signal:"),
    (r"Verify\s+whether[^.]*\.", "Code/data availability and transfer limits should be checked in the source paper."),
    (r"evaluation\s+setup", "evaluation details"),
]


def read_content_documents(lang: str | None = None) -> list[dict]:
    root = REPO_ROOT / "data" / "content"
    pattern = f"{lang}/daily/*.md" if lang else "*/daily/*.md"
    docs = []
    for path in sorted(root.glob(pattern), reverse=True):
        match = FRONTMATTER_RE.match(path.read_text(encoding="utf-8"))
        if not match:
            continue
        meta = _parse_frontmatter(match.group(1))
        body = match.group(2)
        doc_lang = meta.get("lang") or path.parts[-3]
        slug = meta.get("slug") or path.stem
        docs.append({
            "path": path,
            "meta": meta,
            "body": body,
            "lang": doc_lang,
            "slug": slug,
            "url": f"/{doc_lang}/daily/{slug}/",
        })
    docs.sort(key=lambda doc: (str(doc["meta"].get("date", "")), doc["slug"]), reverse=True)
    return docs


def build_search_index() -> str:
    rows = []
    for doc in _public_briefs(read_content_documents()):
        meta = doc["meta"]
        text = _clean_generated_text(_strip_markdown(doc["body"]))
        rows.append({
            "title": _clean_title(meta.get("title", "")),
            "date": meta.get("date", ""),
            "lang": doc["lang"],
            "url": doc["url"],
            "source_url": meta.get("sources_page", ""),
            "summary": _clean_generated_text(meta.get("summary", "")),
            "tags": meta.get("tags", []),
            "topics": meta.get("topics", meta.get("tags", [])),
            "authors": _extract_authors(doc["body"]),
            "content_excerpt": _clean_generated_text(_clean_title(text[:800])),
            "type": meta.get("page_type", "page"),
            "text": _clean_generated_text(_clean_title(text[:5000])),
        })
    out = REPO_ROOT / "apps" / "web" / "public" / "search-index.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(out)


def build_sitemap() -> str:
    base_url = site_config().get("site", {}).get("base_url", "").rstrip("/")
    static_paths = [
        "/", "/zh/", "/en/", "/zh/archive/", "/en/archive/",
        "/zh/search/", "/en/search/", "/zh/topics/", "/en/topics/",
        "/zh/methodology/", "/en/methodology/", "/zh/privacy/", "/en/privacy/",
        "/zh/whatsnew/", "/en/whatsnew/",
    ]
    topic_paths = []
    for lang in ("zh", "en"):
        for topic in topics_config().get("topics", []):
            topic_paths.append(f"/{lang}/topics/{topic['slug']}/")
    urls = static_paths + topic_paths
    for doc in _public_briefs(read_content_documents()):
        urls.append(doc["url"])
        source_url = str(doc["meta"].get("sources_page") or "")
        if source_url:
            urls.append(source_url)
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in dict.fromkeys(urls):
        xml += f"  <url><loc>{escape(base_url + url)}</loc></url>\n"
    xml += "</urlset>\n"
    out = REPO_ROOT / "apps" / "web" / "public" / "sitemap.xml"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(xml, encoding="utf-8")
    return str(out)


def _parse_frontmatter(text: str) -> dict:
    meta = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        try:
            meta[key.strip()] = json.loads(value)
        except json.JSONDecodeError:
            meta[key.strip()] = int(value) if value.isdigit() else value.strip('"')
    return meta


def _strip_markdown(text: str) -> str:
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    text = re.sub(r"[#*_`>-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _clean_title(text: str) -> str:
    return BRIEF_TITLE_PREFIX_RE.sub("", str(text or "")).strip()


def _clean_generated_text(text: str) -> str:
    value = str(text or "")
    for pattern, replacement in DEPRECATED_TEXT_PATTERNS:
        value = re.sub(pattern, replacement, value, flags=re.I)
    return re.sub(r"\s+", " ", value).strip()


def _extract_authors(markdown: str) -> list[str]:
    authors: list[str] = []
    for match in re.finditer(r"(?:Authors / institutions|作者/机构|Authors):\s*([^\n]+)", markdown):
        value = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", match.group(1)).strip()
        if value and value.lower() not in {"unknown", "未知"}:
            authors.extend([part.strip() for part in value.split(",") if part.strip()])
    for match in re.finditer(r"<span>([^<(]+)\(([^<]+)\)</span>", markdown):
        authors.extend([part.strip() for part in match.group(2).split(",") if part.strip()])
    return list(dict.fromkeys(authors))[:20]


def _public_briefs(docs: list[dict]) -> list[dict]:
    by_key: dict[tuple[str, str], dict] = {}
    for doc in docs:
        meta = doc["meta"]
        if meta.get("page_type") != "brief":
            continue
        key = (doc["lang"], str(meta.get("date", "")))
        existing = by_key.get(key)
        if existing is None or _doc_sort_key(doc) > _doc_sort_key(existing):
            by_key[key] = doc
    return sorted(by_key.values(), key=_doc_sort_key, reverse=True)


def _doc_sort_key(doc: dict) -> tuple:
    meta = doc["meta"]
    return (
        str(meta.get("date", "")),
        str(meta.get("generated_at", "")),
        int(meta.get("candidate_count") or 0),
        str(doc.get("slug", "")),
    )
