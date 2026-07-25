from __future__ import annotations

import argparse
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
    request_url = os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"]
    separator = "&" if "?" in request_url else "?"
    token_response = requests.get(
        f"{request_url}{separator}audience={AUDIENCE}",
        headers={"Authorization": f"bearer {os.environ['ACTIONS_ID_TOKEN_REQUEST_TOKEN']}"},
        timeout=60,
    )
    token_response.raise_for_status()
    token = token_response.json()["value"]
    response = requests.post(
        f"{args.endpoint.rstrip('/')}/rpc/open_evidence_whoami",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        data="{}",
        timeout=(30, 120),
    )
    result = {"status_code": response.status_code, "response": response.json() if response.text else None}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    if response.status_code != 200:
        raise SystemExit("Data API identity preflight failed")


if __name__ == "__main__":
    main()
