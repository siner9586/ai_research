# Cloudflare Workers Cron Dispatch

This is an optional fallback trigger for GitHub Actions schedule delays or missed runs. Cloudflare Workers Cron only calls the GitHub API. The daily brief is still generated, tested, committed, pushed, and deployed by GitHub Actions.

## GitHub Token

Create a fine-grained GitHub personal access token for `siner9586/ai_research`.

Minimum permissions for `workflow_dispatch`:

```text
Actions: write
Contents: read
```

Alternative permissions for `repository_dispatch`:

```text
Contents: write
```

Use `workflow_dispatch` when you want to target `.github/workflows/daily-brief.yml` directly. Use `repository_dispatch` when you want an external event type such as `daily-brief`.

## Cloudflare Worker Secrets

Set these with `wrangler secret put` or in the Cloudflare dashboard:

```text
GITHUB_TOKEN
GITHUB_OWNER=siner9586
GITHUB_REPO=ai_research
GITHUB_WORKFLOW=daily-brief.yml
```

Optional variables:

```text
GITHUB_REF=main
DISPATCH_KIND=workflow
```

Set `DISPATCH_KIND=repository` to call `repository_dispatch` instead of `workflow_dispatch`.

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
  const kind = env.DISPATCH_KIND || "workflow";

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
    mode: "real",
    delay_days: "2",
    fallback_days: "4",
  };

  let url;
  let body;
  if (kind === "repository") {
    url = `https://api.github.com/repos/${owner}/${repo}/dispatches`;
    body = {
      event_type: "daily-brief",
      client_payload: inputs,
    };
  } else {
    const workflow = env.GITHUB_WORKFLOW || "daily-brief.yml";
    url = `https://api.github.com/repos/${owner}/${repo}/actions/workflows/${workflow}/dispatches`;
    body = {
      ref,
      inputs,
    };
  }

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

Run at the same nominal time as GitHub Actions. Beijing/Taipei 07:12 is UTC 23:12 on the previous UTC day:

```toml
name = "ai-research-daily-dispatch"
main = "src/index.js"
compatibility_date = "2026-06-05"

[triggers]
crons = ["12 23 * * *"]
```

Or run a few minutes later so GitHub's native schedule gets the first chance:

```toml
[triggers]
crons = ["17 23 * * *"]
```

The target time is UTC 23:12, which is 07:12 the next day in Beijing/Taipei time. The production cadence is T+2: each run normally covers arXiv papers from two Beijing/Taipei calendar days earlier.

## Verification

After deployment, check:

```bash
gh run list --workflow=daily-brief.yml --limit 10
```

Expected events:

```text
workflow_dispatch
```

or, if `DISPATCH_KIND=repository`:

```text
repository_dispatch
```

The workflow logs should show `mode=real`, `delay_days=2`, and `fallback_days=4`.
