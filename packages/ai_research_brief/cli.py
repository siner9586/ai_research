from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from .logging_config import configure_logging
from .config import REPO_ROOT, site_config
from .pipeline.run_daily import (
    build_static_stage,
    enrich_stage,
    fetch_stage,
    generate_stage,
    qa_stage,
    run_daily,
    score_stage,
)
from .utils.dates import resolve_date


DEFAULT_DELAY_DAYS = 2
DEFAULT_FALLBACK_DAYS = 0
PUBLISH_TIMEZONE = "Asia/Shanghai"


def main(argv=None):
    configure_logging()
    parser = argparse.ArgumentParser(prog="ai-brief")
    sub = parser.add_subparsers(dest="cmd", required=True)

    for name in ["fetch", "enrich", "score", "generate", "build-content", "run-daily", "qa"]:
        cmd = sub.add_parser(name)
        cmd.add_argument("--date")
        cmd.add_argument("--delay-days", type=int)
        cmd.add_argument("--fallback-days", type=int)
        cmd.add_argument("--lang", choices=["zh", "en"])
        cmd.add_argument("--mock", action="store_true")
        cmd.add_argument("--allow-qa-warnings", action="store_true")

    mock = sub.add_parser("mock-run")
    mock.add_argument("--date", default="2026-06-03")
    mock.add_argument("--fallback-days", type=int)
    mock.add_argument("--allow-qa-warnings", action="store_true")

    args = parser.parse_args(argv)
    pipeline = site_config().get("pipeline", {})
    try:
        if args.cmd == "mock-run":
            fallback_days = args.fallback_days if args.fallback_days is not None else int(pipeline.get("fallback_days", DEFAULT_FALLBACK_DAYS))
            result = run_daily(resolve_date(args.date), mock=True, allow_qa_warnings=args.allow_qa_warnings, fallback_days=fallback_days)
        else:
            delay_days = getattr(args, "delay_days", None)
            if delay_days is None:
                delay_days = int(pipeline.get("delay_days", DEFAULT_DELAY_DAYS))
            day = resolve_date(getattr(args, "date", None), delay_days)
            result = _dispatch(args, day)
    except Exception:
        _print_failure_reports()
        raise
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))


def _dispatch(args, day):
    if args.cmd == "fetch":
        papers = fetch_stage(day, mock=args.mock)
        return {"date": str(day), "papers": len(papers)}
    if args.cmd == "enrich":
        signals = enrich_stage(day, mock=args.mock)
        return {"date": str(day), "signals": len(signals)}
    if args.cmd == "score":
        scored, featured, mentions = score_stage(day)
        return {"date": str(day), "scored": len(scored), "featured": len(featured), "mentions": len(mentions)}
    if args.cmd == "generate":
        files, slugs = generate_stage(day, lang=args.lang)
        return {"date": str(day), "generated": files, "slugs": slugs}
    if args.cmd == "build-content":
        files, slugs = generate_stage(day)
        static_files = build_static_stage()
        return {"date": str(day), "generated": files + static_files, "slugs": slugs}
    if args.cmd == "qa":
        report = qa_stage(day, allow_warnings=args.allow_qa_warnings)
        return report.model_dump(mode="json")
    if args.cmd == "run-daily":
        fallback_days = args.fallback_days
        if fallback_days is None:
            fallback_days = int(site_config().get("pipeline", {}).get("fallback_days", DEFAULT_FALLBACK_DAYS))
        return run_daily(day, mock=args.mock, allow_qa_warnings=args.allow_qa_warnings, fallback_days=fallback_days)
    raise SystemExit(f"Unknown command: {args.cmd}")


def _print_failure_reports() -> None:
    publish_date = datetime.now(ZoneInfo(PUBLISH_TIMEZONE)).date().isoformat()
    paths = [
        REPO_ROOT / "data" / "reports" / "qa" / f"{publish_date}.json",
        REPO_ROOT / "data" / "reports" / "runs" / f"{publish_date}.json",
        REPO_ROOT / "data" / "reports" / "runs" / "last-run.json",
    ]
    for path in paths:
        if not path.exists():
            continue
        print(f"::group::failure-report {path.relative_to(REPO_ROOT)}")
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            print(json.dumps(payload, ensure_ascii=False, indent=2, default=str))
        except Exception as exc:
            print(f"Could not read {path}: {exc}")
        print("::endgroup::")


if __name__ == "__main__":
    main()
