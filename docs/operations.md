# Operations Runbook

## Daily Automation

GitHub Actions workflow:

```text
.github/workflows/daily-brief.yml
Schedule: UTC 00:30 daily
Mode: real by default
Manual mode: mock or real
```

The scheduled run installs Python 3.11 and Node 22, runs `ai-brief run-daily --delay-days 3`, executes `pytest -q`, builds Astro, commits generated `data/` and `apps/web/public/`, pushes to `main`, and optionally sends notifications.

## Manual Trigger

With GitHub CLI:

```bash
gh workflow run daily-brief.yml -f mode=mock
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
→ Run workflow
```

## Switch From Mock To Real

Mock mode is only for validation:

```bash
ai-brief mock-run
```

Real mode uses arXiv for the target date:

```bash
ai-brief run-daily --delay-days 3
```

Scheduled GitHub Actions runs use real mode unless the manual dispatch input is `mock`.

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

If `ai-brief run-daily --delay-days 3` fails:

1. Check network access to `https://export.arxiv.org/api/query`.
2. Confirm the target date has papers in configured categories.
3. Re-run with a specific date: `ai-brief run-daily --date YYYY-MM-DD`.
4. Do not commit mock content as a real daily issue.
5. Use `ai-brief mock-run` only for workflow validation.

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

## Workers KV

Current project does not need Workers KV. Content is static, state is saved in `data/processed` and GitHub Actions logs, and Cloudflare Pages serves the built Astro site. KV is useful later for subscription users, send status, online configuration, or dynamic APIs. For strong-consistency subscription data, evaluate Cloudflare D1 before KV.
