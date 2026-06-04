from __future__ import annotations

import os

import httpx


def main() -> int:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    site_url = os.environ.get("SITE_URL", "https://aici.ccwu.cc").rstrip("/")
    if not token or not chat_id:
        print("Telegram missing config, skipped: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID is missing.")
        return 0
    text = (
        "今日 AI 论文简报已更新\n"
        f"中文：{site_url}/zh/\n"
        f"英文：{site_url}/en/\n"
        f"RSS：{site_url}/zh/feed.xml"
    )
    response = httpx.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        timeout=15,
        json={"chat_id": chat_id, "text": text, "disable_web_page_preview": True},
    )
    response.raise_for_status()
    print("Telegram notification sent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
