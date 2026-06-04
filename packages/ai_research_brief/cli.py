import argparse, json
from .utils.dates import resolve_date
from .pipeline.run_daily import run_daily


def main(argv=None):
    p = argparse.ArgumentParser(prog='ai-brief')
    s = p.add_subparsers(dest='cmd', required=True)
    for name in ['fetch','enrich','score','generate','build-content','run-daily','qa']:
        x = s.add_parser(name)
        x.add_argument('--date')
        x.add_argument('--delay-days', type=int, default=3)
        x.add_argument('--lang')
        x.add_argument('--mock', action='store_true')
        x.add_argument('--allow-qa-warnings', action='store_true')
    mock = s.add_parser('mock-run')
    mock.add_argument('--date', default='2026-06-03')
    a = p.parse_args(argv)
    if a.cmd == 'mock-run':
        out = run_daily(resolve_date(a.date), mock=True)
    else:
        out = run_daily(resolve_date(getattr(a, 'date', None), getattr(a, 'delay_days', 3)), mock=getattr(a, 'mock', False))
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
