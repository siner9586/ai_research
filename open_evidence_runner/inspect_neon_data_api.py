from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path

import requests

AUDIENCE = "neon-open-evidence-import"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)

    request_url = os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"]
    separator = "&" if "?" in request_url else "?"
    token_response = requests.get(
        f"{request_url}{separator}audience={AUDIENCE}",
        headers={"Authorization": f"bearer {os.environ['ACTIONS_ID_TOKEN_REQUEST_TOKEN']}"},
        timeout=60,
    )
    token_response.raise_for_status()
    token = token_response.json()["value"]
    payload = token.split(".")[1]
    payload += "=" * (-len(payload) % 4)
    claims = json.loads(base64.urlsafe_b64decode(payload))
    workflow_ref = str(claims.get("workflow_ref", ""))
    if not workflow_ref.startswith(
        "siner9586/ai_research/.github/workflows/open-evidence-neon-import.yml@refs/pull/"
    ):
        raise RuntimeError("Unexpected workflow identity")

    response = requests.get(
        args.endpoint.rstrip("/") + "/",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/openapi+json",
        },
        timeout=(30, 120),
    )
    result = {
        "status_code": response.status_code,
        "content_type": response.headers.get("content-type"),
        "workflow_ref": workflow_ref,
        "paths": [],
    }
    if response.status_code == 200:
        document = response.json()
        result["paths"] = sorted(document.get("paths", {}).keys())
        result["definitions"] = sorted(document.get("definitions", {}).keys())
    else:
        result["response_excerpt"] = response.text[:1000]
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if response.status_code != 200:
        raise SystemExit("OpenAPI inspection failed")


if __name__ == "__main__":
    main()
