# Operations Runbook

## Daily Automation

GitHub Actions workflow:

```text
.github/workflows/daily-brief-auto.yml
Schedule: 80 idempotent checks from 05:12 to 18:22 Beijing/Taipei
Mode: real arXiv production only
Manual mode: workflow_dispatch with optional delay_days and fallback_days
```

Each scheduled tick first fast-forwards to `main` and checks whether current-date zh/en brief files already exist. If both exist, it exits before Python/Node setup. If generation is needed, it installs Python 3.11 and Node 22, runs `ai-brief run-daily --delay-days 2 --fallback-days 2`, validates the run report, runs `candidate_lineage_guard.py` and `strict_t2_guard.py`, builds Astro, commits generated `data/` and `apps/web/public/`, pushes to `main`, and triggers a Cloudflare Pages deploy hook when configured.

## Manual Trigger

With GitHub CLI:

```bash
gh workflow run daily-brief-auto.yml -f delay_days=2 -f fallback_days=2
gh run list --workflow=daily-brief-auto.yml --limit 5
gh run view --log
```

In the browser:

```text
GitHub repository
→ Actions
→ Daily AI Brief Auto Publish
→ Run workflow
→ optional delay_days, fallback_days
→ Run workflow
```

## Production Vs Mock

Mock mode is only for validation:

```bash
ai-brief mock-run
```

Real mode uses arXiv for the target date:

```bash
ai-brief run-daily --delay-days 2 --fallback-days 2
```

Scheduled GitHub Actions runs use real arXiv production mode only. Production real mode never publishes mock papers. If the target date has no real arXiv papers, it searches backward within the fallback window and labels `target_date`, `actual_date`, and `fallback_from` in generated pages and run reports. With `delay_days=2` and `fallback_days=2`, the maximum source date is `publish_date - 4`.

## Rollback

To roll back the site:

```bash
git log --oneline -5
git revert <bad_commit>
git push origin main
```

Cloudflare Pages will deploy the reverted `main` commit. Avoid deleting generated history unless there is a sensitive-data incident.

## QA Reports

Reports are written to:

```text
data/reports/qa/YYYY-MM-DD.json
data/reports/runs/YYYY-MM-DD.json
data/reports/runs/last-run.json
```

Run:

```bash
ai-brief qa --date YYYY-MM-DD
```

QA errors fail the CLI and GitHub Actions. Warnings are visible but do not block by default.

## Generated Content

Daily Markdown:

```text
data/content/zh/daily/
data/content/en/daily/
```

Processed pipeline state:

```text
data/processed/YYYY-MM-DD/
```

Public static artifacts:

```text
apps/web/public/zh/feed.xml
apps/web/public/en/feed.xml
apps/web/public/sitemap.xml
apps/web/public/search-index.json
```

## Notifications

Telegram:

```bash
export TELEGRAM_BOT_TOKEN=...
export TELEGRAM_CHAT_ID=...
export SITE_URL=https://aici.ccwu.cc
python scripts/notify_telegram.py
```

Email through Resend:

```bash
export RESEND_API_KEY=...
export MAIL_FROM=brief@example.com
export MAIL_TO=you@example.com
export SITE_URL=https://aici.ccwu.cc
python scripts/send_email.py
```

Missing config prints `missing config, skipped` and exits 0.

## arXiv Failures

If `ai-brief run-daily --delay-days 2 --fallback-days 2` fails:

1. Check network access to `https://export.arxiv.org/api/query`.
2. Confirm the target date has papers in configured categories.
3. Inspect `data/reports/runs/last-run.json` or the JSON summary printed in the `Generate daily brief` Actions step.
4. Re-run with a specific source date only for controlled backfill: `ai-brief run-daily --date YYYY-MM-DD --fallback-days 0`.
5. Do not commit mock content as a real daily issue.
6. Use `ai-brief mock-run` only for workflow validation.

If the workflow succeeds but no commit appears, inspect the `Commit generated content` step. It prints target date, actual data date, generated files, latest slugs, and whether `git diff --cached --quiet` found changes.

## Cloudflare Deployment Failures

Recommended Pages configuration:

```text
Project: ai-research
Production branch: main
Root directory: apps/web
Build command: npm install && npm run build
Build output directory: dist
```

If deployment fails, inspect:

```text
Cloudflare Dashboard
→ Workers & Pages
→ ai-research
→ Deployments
```

Common fixes:

- Build failed: reproduce locally with `cd apps/web && npm install && npm run build`.
- 404: verify root directory and output directory.
- RSS 404: confirm generated feed files are committed in `apps/web/public`.
- DNS not resolving: add `CNAME aici -> ai-research.pages.dev` in the `ccwu.cc` zone.
- Certificate pending: wait for Cloudflare validation and keep the custom domain attached.
- Push succeeded but Pages did not deploy: confirm Pages watches branch `main`; optionally configure GitHub secret `CLOUDFLARE_PAGES_DEPLOY_HOOK` so the workflow POSTs a deploy hook after a successful push.
- GitHub schedule is delayed or skipped: the authoritative workflow already has 80 scheduled checks; use manual `workflow_dispatch` only if all checks miss.

## Workers KV

Current project does not need Workers KV. Content is static, state is saved in `data/processed` and GitHub Actions logs, and Cloudflare Pages serves the built Astro site. KV is useful later for subscription users, send status, online configuration, or dynamic APIs. For strong-consistency subscription data, evaluate Cloudflare D1 before KV.
