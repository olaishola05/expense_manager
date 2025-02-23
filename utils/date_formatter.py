from datetime import datetime, timezone

def create_date():
    now_utc = datetime.now(timezone.utc)
    return now_utc.strftime('%Y-%m-%dT%H:%M:%SZ')