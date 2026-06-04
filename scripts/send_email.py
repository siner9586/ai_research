from __future__ import annotations

import os

import httpx


def main() -> int:
    api_key = os.environ.get("RESEND_API_KEY")
    mail_from = os.environ.get("MAIL_FROM")
    mail_to = os.environ.get("MAIL_TO")
    site_url = os.environ.get("SITE_URL", "https://aici.ccwu.cc").rstrip("/")
    if not api_key or not mail_from or not mail_to:
        print("Email notification skipped: RESEND_API_KEY, MAIL_FROM, or MAIL_TO is missing.")
        return 0
    text = (
        "今日 AI 论文简报已更新\n"
        f"中文：{site_url}/zh/\n"
        f"英文：{site_url}/en/\n"
        f"RSS：{site_url}/zh/feed.xml"
    )
    response = httpx.post(
        "https://api.resend.com/emails",
        timeout=20,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={
            "from": mail_from,
            "to": [addr.strip() for addr in mail_to.split(",") if addr.strip()],
            "subject": "今日 AI 论文简报已更新",
            "text": text,
        },
    )
    response.raise_for_status()
    print("Email notification sent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
