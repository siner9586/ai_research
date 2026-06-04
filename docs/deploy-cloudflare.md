# Cloudflare Pages Deployment

Recommended configuration for this repository:

```text
Cloudflare Pages Project: ai-research
Production branch: main
Root directory: apps/web
Build command: npm install && npm run build
Build output directory: dist
```

This is the preferred setup because `apps/web/package.json`, `astro.config.mjs`, and `public/` are all inside `apps/web`.

Alternative if Root directory is left blank:

```text
Build command: cd apps/web && npm install && npm run build
Build output directory: apps/web/dist
```

## Dashboard Checks

Open:

```text
https://dash.cloudflare.com/9a442b0a75c68fd2bfe8cf126bfb2c58/pages/view/ai-research
```

Confirm:

- Production branch is `main`.
- Build command matches one of the two configurations above.
- Build output directory matches the chosen root directory.
- Latest production deployment finished successfully.
- Custom domain `aici.ccwu.cc` is listed under Custom domains.
- DNS and certificate status are active, or certificate is pending validation.

## Custom Domain Verification

After deployment:

```bash
curl -I https://aici.ccwu.cc/
curl -I https://aici.ccwu.cc/zh/
curl -I https://aici.ccwu.cc/zh/feed.xml
```

Expected: HTTP 200 or a normal Cloudflare redirect/200 chain.

## Troubleshooting

- Site 404: check production branch, root directory, and output directory.
- Build failed: run `cd apps/web && npm install && npm run build` locally.
- RSS 404: confirm `apps/web/public/zh/feed.xml` and `apps/web/public/en/feed.xml` are committed.
- Search index empty: run `ai-brief build-content --date YYYY-MM-DD`.
- Domain certificate pending: wait for Cloudflare validation and verify DNS points to Pages.
- Old content visible: check the latest GitHub commit, latest Pages deployment, and browser cache.

## Workers KV

Do not add Workers KV for the current static publishing flow. Add KV, D1, or R2 only when the product needs dynamic subscription state, send-state storage, online APIs, reading state, or an admin dashboard.
