from datetime import datetime, timezone


class UTime:
    datetime_format_ = "%Y-%m-%d %H:%M:%S"

    @classmethod
    def now(cls):
        return int(datetime.utcnow().replace(tzinfo=timezone.utc).timestamp())
