#!/usr/bin/env bash
set -euo pipefail

SITE_URL="${SITE_URL:-https://aici.ccwu.cc}"
VERIFY_ATTEMPTS="${VERIFY_ATTEMPTS:-20}"
VERIFY_INTERVAL_SECONDS="${VERIFY_INTERVAL_SECONDS:-30}"

resolve_publish_date() {
  if [ -n "${PUBLISH_DATE:-}" ]; then
    echo "$PUBLISH_DATE"
    return 0
  fi
  python - <<'PY'
from __future__ import annotations
import json
from pathlib import Path

report = Path('data/reports/runs/last-run.json')
if report.exists():
    data = json.loads(report.read_text(encoding='utf-8'))
    value = data.get('publish_date') or data.get('date')
    if value:
        print(value)
        raise SystemExit(0)

zh_dir = Path('data/content/zh/daily')
values = []
for path in zh_dir.glob('*.md'):
    if path.stem.endswith('-sources'):
        continue
    prefix = path.name[:10]
    if len(prefix) == 10 and prefix[4] == '-' and prefix[7] == '-':
        values.append(prefix)
if not values:
    raise SystemExit('Could not resolve publish date from PUBLISH_DATE, last-run.json, or zh daily content')
print(sorted(values)[-1])
PY
}

PUBLISH_DATE="$(resolve_publish_date)"
DEPLOY_HOOK="${DEPLOY_HOOK:-${CLOUDFLARE_PAGES_DEPLOY_HOOK_SECRET:-${CLOUDFLARE_PAGES_DEPLOY_HOOK_VAR:-}}}"

urls=(
  "${SITE_URL}/"
  "${SITE_URL}/zh/"
  "${SITE_URL}/en/"
  "${SITE_URL}/search-index.json"
)

verify_once() {
  local stamp
  stamp="$(date +%s)"
  for url in "${urls[@]}"; do
    local body
    body="$(mktemp)"
    echo "Checking ${url} for ${PUBLISH_DATE}"
    if ! curl -fsSL \
      -H "Cache-Control: no-cache" \
      -H "Pragma: no-cache" \
      --output "${body}" \
      "${url}?v=${PUBLISH_DATE}-${stamp}"; then
      rm -f "${body}"
      return 1
    fi
    if ! grep -Fq -- "${PUBLISH_DATE}" "${body}"; then
      rm -f "${body}"
      return 1
    fi
    rm -f "${body}"
  done
}

echo "production_publish_date=${PUBLISH_DATE}"
echo "production_site_url=${SITE_URL}"

if verify_once; then
  echo "production_verify=success date=${PUBLISH_DATE} mode=already_live"
  exit 0
fi

echo "::warning::Production pages do not yet contain ${PUBLISH_DATE}; triggering Cloudflare Pages deploy hook."

if [ -z "${DEPLOY_HOOK}" ]; then
  echo "::error::DEPLOY_HOOK/CLOUDFLARE_PAGES_DEPLOY_HOOK is not configured. Cloudflare Git auto deploy is off, so stale production cannot self-heal."
  exit 1
fi

curl -fsSL -X POST "${DEPLOY_HOOK}"
echo "deploy_hook_status=triggered"

for attempt in $(seq 1 "${VERIFY_ATTEMPTS}"); do
  echo "production_verify_attempt=${attempt}/${VERIFY_ATTEMPTS} date=${PUBLISH_DATE}"
  sleep "${VERIFY_INTERVAL_SECONDS}"
  if verify_once; then
    echo "production_verify=success date=${PUBLISH_DATE} mode=after_deploy_hook attempt=${attempt}"
    exit 0
  fi
done

echo "::error::Production pages still do not contain ${PUBLISH_DATE} after deploy hook and ${VERIFY_ATTEMPTS} verification attempts."
exit 1
