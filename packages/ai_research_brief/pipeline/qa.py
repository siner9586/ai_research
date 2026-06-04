from datetime import date
import json
import re
from pathlib import Path
from ..models import QAReport

def run_qa(day: date, content_dir: Path, reports_dir: Path) -> QAReport:
    checked = [str(p) for p in content_dir.glob(f'*/daily/{day}-*.md')]
    warnings: list[str] = []
    errors: list[str] = []

    for lang in ("zh", "en"):
        pages = list((content_dir / lang / "daily").glob(f"{day}-*.md"))
        brief_pages = [p for p in pages if not p.stem.endswith("-sources")]
        source_pages = [p for p in pages if p.stem.endswith("-sources")]
        if not brief_pages:
            errors.append(f"Missing {lang} daily brief for {day}")
        if not source_pages:
            errors.append(f"Missing {lang} sources page for {day}")
        for path in pages:
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---"):
                errors.append(f"Missing frontmatter: {path}")
            if "arxiv.org/abs/" not in text:
                warnings.append(f"No arXiv link found: {path}")
            if path.stem.endswith("-sources") and "Score breakdown:" not in text:
                errors.append(f"Sources page lacks scoring details: {path}")

    public = content_dir.parents[1] / "apps" / "web" / "public"
    for path in [public / "zh" / "feed.xml", public / "en" / "feed.xml", public / "sitemap.xml", public / "search-index.json"]:
        checked.append(str(path))
        if not path.exists():
            errors.append(f"Missing static artifact: {path}")

    search_index = public / "search-index.json"
    if search_index.exists():
        try:
            rows = json.loads(search_index.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append("search-index.json is not valid JSON")
        else:
            if not any(str(row.get("date")) == str(day) for row in rows):
                errors.append(f"Search index does not include {day}")

    checked_count = len(re.findall(r"Score breakdown:", "\n".join(Path(p).read_text(encoding="utf-8") for p in checked if p.endswith(".md"))))
    if checked_count < 3:
        warnings.append("Fewer than three scored source records found")

    report = QAReport(date=day, passed=not errors, warnings=warnings, errors=errors, checked_files=checked)
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / (str(day) + '.json')).write_text(report.model_dump_json(indent=2), encoding='utf-8')
    return report
