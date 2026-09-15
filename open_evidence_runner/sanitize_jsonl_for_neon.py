from __future__ import annotations

import argparse
import gzip
import json
import math
from pathlib import Path
from typing import Any


def sanitize(value: Any) -> Any:
    if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
        return None
    if isinstance(value, dict):
        return {str(key): sanitize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=Path, required=True)
    args = parser.parse_args()

    source = args.path
    temporary = source.with_suffix(source.suffix + ".tmp")
    rows = 0
    replacements = 0

    with gzip.open(source, "rt", encoding="utf-8") as reader, gzip.open(
        temporary, "wt", encoding="utf-8"
    ) as writer:
        for line_number, line in enumerate(reader, start=1):
            if not line.strip():
                continue
            try:
                payload = json.loads(line, parse_constant=lambda _: None)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at line {line_number}: {exc}") from exc
            before = json.dumps(payload, ensure_ascii=False, sort_keys=True, allow_nan=True)
            cleaned = sanitize(payload)
            after = json.dumps(cleaned, ensure_ascii=False, sort_keys=True, allow_nan=False)
            if before != after:
                replacements += 1
            writer.write(json.dumps(cleaned, ensure_ascii=False, allow_nan=False) + "\n")
            rows += 1

    temporary.replace(source)
    print(json.dumps({"path": str(source), "rows": rows, "rows_changed": replacements}))


if __name__ == "__main__":
    main()
