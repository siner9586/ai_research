# Cloudflare Workers Cron Dispatch

This is an optional last-resort fallback trigger for GitHub Actions schedule delays or missed runs. The repository already schedules 80 idempotent checks in `.github/workflows/daily-brief-auto.yml`; use a Worker only if you want an external watchdog. Cloudflare Workers Cron only calls the GitHub API. The daily brief is still generated, tested, committed, pushed, and deployed by GitHub Actions.

## GitHub Token

Create a fine-grained GitHub personal access token for `siner9586/ai_research`.

Minimum permissions for `workflow_dispatch`:

```text
Actions: write
Contents: read
```

Use `workflow_dispatch` to target `.github/workflows/daily-brief-auto.yml` directly.

## Cloudflare Worker Secrets

Set these with `wrangler secret put` or in the Cloudflare dashboard:

```text
GITHUB_TOKEN
GITHUB_OWNER=siner9586
GITHUB_REPO=ai_research
GITHUB_WORKFLOW=daily-brief-auto.yml
```

Optional variables:

```text
GITHUB_REF=main
```

## Worker Example

```js
export default {
  async scheduled(event, env, ctx) {
    ctx.waitUntil(triggerGitHub(env));
  },

  async fetch(request, env) {
    if (request.method !== "POST") {
      return new Response("Not found", { status: 404 });
    }
    await triggerGitHub(env);
    return new Response("Triggered daily brief\n", { status: 200 });
  },
};

async function triggerGitHub(env) {
  const owner = env.GITHUB_OWNER || "siner9586";
  const repo = env.GITHUB_REPO || "ai_research";
  const ref = env.GITHUB_REF || "main";

  if (!env.GITHUB_TOKEN) {
    throw new Error("Missing GITHUB_TOKEN");
  }

  const headers = {
    Authorization: `Bearer ${env.GITHUB_TOKEN}`,
    "Content-Type": "application/json",
    "User-Agent": "ai-research-cloudflare-cron",
    "X-GitHub-Api-Version": "2022-11-28",
  };

  const inputs = {
    delay_days: "2",
    fallback_days: "2",
  };

  const workflow = env.GITHUB_WORKFLOW || "daily-brief-auto.yml";
  const url = `https://api.github.com/repos/${owner}/${repo}/actions/workflows/${workflow}/dispatches`;
  const body = {
    ref,
    inputs,
  };

  const response = await fetch(url, {
    method: "POST",
    headers,
    body: JSON.stringify(body),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(`GitHub dispatch failed: ${response.status} ${text}`);
  }
}
```

## wrangler.toml

Run after the first native GitHub Actions check. Beijing/Taipei 05:12 is UTC 21:12 on the previous UTC day:

```toml
name = "ai-research-daily-dispatch"
main = "src/index.js"
compatibility_date = "2026-06-05"

[triggers]
crons = ["17 21 * * *"]
```

The native GitHub workflow already checks every 10 minutes through 18:22 Beijing/Taipei, so a Worker should normally dispatch at most once as an external watchdog.

The production cadence is T+2: each run normally covers arXiv papers from two Beijing/Taipei calendar days earlier.

## Verification

After deployment, check:

```bash
gh run list --workflow=daily-brief-auto.yml --limit 10
```

Expected events:

```text
workflow_dispatch
```
The workflow logs should show `production_mode=real`, `delay_days=2`, and `fallback_days=2`.
