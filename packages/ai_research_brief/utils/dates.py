from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

DEFAULT_SCHEDULE_TIMEZONE = "Asia/Shanghai"


def resolve_date(date_str: str | None = None, delay_days: int = 2) -> date:
    if date_str:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    today = datetime.now(ZoneInfo(DEFAULT_SCHEDULE_TIMEZONE)).date()
    return today - timedelta(days=delay_days)
