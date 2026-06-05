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

Project and domain:

```text
Cloudflare Pages Project: ai-research
Domain: aici.ccwu.cc
DNS: CNAME aici -> ai-research.pages.dev or the Pages default domain shown by Cloudflare
Custom domain: aici.ccwu.cc
```

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
- If GitHub pushed new generated content but Pages did not deploy, create a Pages deploy hook and save it as GitHub secret `CLOUDFLARE_PAGES_DEPLOY_HOOK`.

## DNS Record

In the `ccwu.cc` zone, confirm this record exists:

```text
Type: CNAME
Name: aici
Target: ai-research.pages.dev
Proxy status: Proxied, recommended
```

Cloudflare Pages may create an equivalent record automatically when adding the custom domain. If `dig CNAME aici.ccwu.cc` returns no answer, add or repair this DNS record first.

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
- DNS does not resolve: confirm the `ccwu.cc` zone is active in Cloudflare and has `CNAME aici -> ai-research.pages.dev`.
- Search index empty: run `ai-brief build-content --date YYYY-MM-DD`.
- Domain certificate pending: wait for Cloudflare validation and verify DNS points to Pages.
- Old content visible: check the latest GitHub commit, latest Pages deployment, and browser cache.
- GitHub schedule delayed or missed: configure the optional Cloudflare Workers Cron trigger in [cloudflare-cron-dispatch.md](cloudflare-cron-dispatch.md).

## Workers KV

Do not add Workers KV for the current static publishing flow. Content is statically generated, state is in `data/processed` and GitHub Actions logs, and Cloudflare Pages serves static output. Add KV, D1, or R2 only when the product needs dynamic subscription state, send-state storage, online APIs, reading state, or an admin dashboard. If a strong-consistency subscription system is needed, evaluate Cloudflare D1 before KV.
