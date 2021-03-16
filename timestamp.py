
""" An error would occur when dealing with timestampe before 1970 (negative timestamp),
    this package help to dealing with these cases.
"""

from datetime import datetime, timedelta


def to_timestampe(date: datetime) -> int:
    """
    Convert datetime to timestamp.
    """
    time0 = datetime.fromtimestamp(0)
    delta = (date-time0)
    timestamp = delta.days * 86400 + delta.seconds
    return int(timestamp)


def to_datetime(timestamp: int) -> datetime:
    """
    Convert timestamp to datetime.
    """
    time0 = datetime.fromtimestamp(0)
    delta = timedelta(seconds=timestamp)
    return time0 + delta


def to_midnight(timestamp: int) -> int:
    """
    Convert the timestamp to midnight 00:00 am of that day.
    """
    d = to_datetime(timestamp)
    d = datetime(d.year, d.month, d.day)
    return to_timestampe(d)
