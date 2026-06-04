from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class JsonStore:
    """Small JSON store for local run metadata.

    The production path is static generation plus Git commits, so this is only a
    convenience abstraction for future notification state or ad hoc reports.
    """

    def __init__(self, path: Path):
        self.path = path

    def read(self) -> dict[str, Any]:
        if not self.path.exists():
            return {}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def write(self, payload: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
