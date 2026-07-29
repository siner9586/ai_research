from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import shutil
import sqlite3
from pathlib import Path
from typing import Any

import pandas as pd


def extract_mag_id(value: Any) -> str | None:
    if isinstance(value, dict):
        raw = value.get("MAG")
    elif isinstance(value, str) and value.strip():
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return None
        raw = parsed.get("MAG") if isinstance(parsed, dict) else None
    else:
        return None
    if raw is None:
        return None
    text = str(raw).strip()
    return text or None


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repair_csv(path: Path) -> tuple[int, int]:
    frame = pd.read_csv(path, compression="gzip", dtype=str, keep_default_na=False)
    if "external_ids" not in frame.columns:
        raise ValueError(f"{path.name} lacks external_ids")
    mag = frame["external_ids"].map(extract_mag_id)
    if "mag_id" in frame.columns:
        existing = frame["mag_id"].replace("", pd.NA)
        conflicts = existing.notna() & mag.notna() & existing.ne(mag)
        if conflicts.any():
            raise ValueError(f"{path.name} contains conflicting mag_id values")
        frame["mag_id"] = existing.fillna(mag)
    else:
        insert_at = frame.columns.get_loc("openalex_id") if "openalex_id" in frame.columns else len(frame.columns)
        frame.insert(insert_at, "mag_id", mag)
    if "openalex_id" in frame.columns:
        suspicious = frame["openalex_id"].fillna("").str.fullmatch(r"\d+")
        if suspicious.any():
            raise ValueError(f"{path.name} contains numeric MAG-like values in openalex_id")
    tmp = path.with_suffix(path.suffix + ".tmp")
    frame.to_csv(tmp, index=False, compression="gzip")
    tmp.replace(path)
    return int(frame["mag_id"].replace("", pd.NA).notna().sum()), len(frame)


def repair_sqlite(path: Path) -> tuple[int, int]:
    with sqlite3.connect(path) as connection:
        columns = {row[1] for row in connection.execute("PRAGMA table_info(candidate_records)")}
        if "mag_id" not in columns:
            connection.execute("ALTER TABLE candidate_records ADD COLUMN mag_id TEXT")
        rows = connection.execute("SELECT rowid, external_ids, openalex_id, mag_id FROM candidate_records").fetchall()
        updates: list[tuple[str, int]] = []
        for rowid, external_ids, openalex_id, current_mag in rows:
            mag_id = extract_mag_id(external_ids)
            if current_mag and mag_id and str(current_mag) != mag_id:
                raise ValueError(f"conflicting mag_id at candidate_records rowid={rowid}")
            if openalex_id and str(openalex_id).isdigit():
                raise ValueError(f"numeric MAG-like value in openalex_id at rowid={rowid}")
            if not current_mag and mag_id:
                updates.append((mag_id, rowid))
        connection.executemany("UPDATE candidate_records SET mag_id=? WHERE rowid=?", updates)
        connection.execute("CREATE INDEX IF NOT EXISTS ix_candidate_mag_id ON candidate_records(mag_id)")
        connection.commit()
        count = connection.execute("SELECT count(*) FROM candidate_records WHERE mag_id IS NOT NULL AND mag_id <> ''").fetchone()[0]
        total = connection.execute("SELECT count(*) FROM candidate_records").fetchone()[0]
    return int(count), int(total)


def main() -> None:
    parser = argparse.ArgumentParser(description="Materialize Semantic Scholar externalIds.MAG as mag_id without touching openalex_id.")
    parser.add_argument("--artifact-dir", type=Path, required=True)
    args = parser.parse_args()

    root = args.artifact_dir
    targets = [
        root / "candidate_records_s2_rescue.csv.gz",
        root / "candidate_records_selected.csv.gz",
    ]
    sqlite_path = root / "s2_rescue_selected.sqlite"
    for path in [*targets, sqlite_path]:
        if not path.exists():
            raise FileNotFoundError(path)
        shutil.copy2(path, path.with_suffix(path.suffix + ".pre_mag_id.bak"))

    results: dict[str, dict[str, int]] = {}
    for path in targets:
        mapped, total = repair_csv(path)
        results[path.name] = {"mag_id_nonempty": mapped, "rows": total}
    mapped, total = repair_sqlite(sqlite_path)
    results[sqlite_path.name] = {"mag_id_nonempty": mapped, "rows": total}

    manifest = root / "sha256sums.txt"
    files = sorted(path for path in root.iterdir() if path.is_file() and not path.name.endswith(".bak"))
    manifest.write_text("".join(f"{sha256(path)}  {path.name}\n" for path in files if path != manifest), encoding="utf-8")
    audit = {
        "repair": "semantic_scholar_mag_id_materialization",
        "rule": "externalIds.MAG -> mag_id; never openalex_id",
        "results": results,
    }
    (root / "mag_id_repair_audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(audit, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
