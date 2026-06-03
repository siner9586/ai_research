from datetime import date
from pathlib import Path
from ..models import QAReport

def run_qa(day: date, content_dir: Path, reports_dir: Path) -> QAReport:
    checked = [str(p) for p in content_dir.glob(f'*/daily/{day}-*.md')]
    report = QAReport(date=day, passed=True, warnings=[], errors=[], checked_files=checked)
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / (str(day) + '.json')).write_text(report.model_dump_json(indent=2), encoding='utf-8')
    return report
