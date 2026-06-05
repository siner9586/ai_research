# Operations Runbook

## Daily Automation

GitHub Actions workflow:

```text
.github/workflows/daily-brief.yml
Schedule: UTC 02:30 daily, 10:30 Beijing/Taipei
Mode: real by default
Manual mode: mock or real
External fallback trigger: repository_dispatch type daily-brief
```

The scheduled run installs Python 3.11 and Node 22, runs `ai-brief run-daily --delay-days 3 --fallback-days 4`, executes `pytest -q`, builds Astro, commits generated `data/` and `apps/web/public/`, pushes to `main`, optionally triggers a Cloudflare Pages deploy hook, and optionally sends notifications.

## Manual Trigger

With GitHub CLI:

```bash
gh workflow run daily-brief.yml -f mode=mock
gh workflow run daily-brief.yml -f mode=real -f delay_days=3 -f fallback_days=4
gh workflow run daily-brief.yml -f mode=real -f date=YYYY-MM-DD -f fallback_days=4
gh run list --workflow=daily-brief.yml --limit 5
gh run view --log
```

In the browser:

```text
GitHub repository
→ Actions
→ Daily AI Research Brief
→ Run workflow
→ mode = mock or real
→ optional date, delay_days, fallback_days
→ Run workflow
```

## Switch From Mock To Real

Mock mode is only for validation:

```bash
ai-brief mock-run
```

Real mode uses arXiv for the target date:

```bash
ai-brief run-daily --delay-days 3 --fallback-days 4
```

Scheduled GitHub Actions runs use real mode unless the manual dispatch input is `mock`. Production real mode never publishes mock papers. If the target date has no real arXiv papers, it searches backward within the fallback window and labels `target_date`, `actual_date`, and `fallback_from` in generated pages and run reports.

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

If `ai-brief run-daily --delay-days 3 --fallback-days 4` fails:

1. Check network access to `https://export.arxiv.org/api/query`.
2. Confirm the target date has papers in configured categories.
3. Inspect `data/reports/runs/last-run.json` or the JSON summary printed in the `Generate daily brief` Actions step.
4. Re-run with a specific date: `ai-brief run-daily --date YYYY-MM-DD --fallback-days 4`.
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
Output directory: dist
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
- GitHub schedule is delayed or skipped: use manual `workflow_dispatch`, or configure the Cloudflare Workers Cron fallback in `docs/cloudflare-cron-dispatch.md` to call GitHub `repository_dispatch`.

## Workers KV

Current project does not need Workers KV. Content is static, state is saved in `data/processed` and GitHub Actions logs, and Cloudflare Pages serves the built Astro site. KV is useful later for subscription users, send status, online configuration, or dynamic APIs. For strong-consistency subscription data, evaluate Cloudflare D1 before KV.
