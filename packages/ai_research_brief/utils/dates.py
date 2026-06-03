from datetime import date, datetime, timedelta


def resolve_date(date_str: str | None = None, delay_days: int = 3) -> date:
    if date_str:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    return date.today() - timedelta(days=delay_days)
