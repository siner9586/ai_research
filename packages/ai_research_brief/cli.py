from __future__ import annotations

import argparse
import json

from .logging_config import configure_logging
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


def main(argv=None):
    configure_logging()
    parser = argparse.ArgumentParser(prog="ai-brief")
    sub = parser.add_subparsers(dest="cmd", required=True)

    for name in ["fetch", "enrich", "score", "generate", "build-content", "run-daily", "qa"]:
        cmd = sub.add_parser(name)
        cmd.add_argument("--date")
        cmd.add_argument("--delay-days", type=int, default=3)
        cmd.add_argument("--lang", choices=["zh", "en"])
        cmd.add_argument("--mock", action="store_true")
        cmd.add_argument("--allow-qa-warnings", action="store_true")

    mock = sub.add_parser("mock-run")
    mock.add_argument("--date", default="2026-06-03")
    mock.add_argument("--allow-qa-warnings", action="store_true")

    args = parser.parse_args(argv)
    if args.cmd == "mock-run":
        result = run_daily(resolve_date(args.date), mock=True, allow_qa_warnings=args.allow_qa_warnings)
    else:
        day = resolve_date(getattr(args, "date", None), getattr(args, "delay_days", 3))
        result = _dispatch(args, day)
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
        return run_daily(day, mock=args.mock, allow_qa_warnings=args.allow_qa_warnings)
    raise SystemExit(f"Unknown command: {args.cmd}")


if __name__ == "__main__":
    main()
