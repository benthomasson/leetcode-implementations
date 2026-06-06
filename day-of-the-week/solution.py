import datetime


def day_of_the_week(day: int, month: int, year: int) -> str:
    """Return the day of the week for a given date.

    Args:
        day: Day of the month.
        month: Month (1-12).
        year: Year (1971-2100).

    Returns:
        Day name with trailing space, e.g. "Saturday ".
    """
    days = ["Monday ", "Tuesday ", "Wednesday ", "Thursday ",
            "Friday ", "Saturday ", "Sunday "]
    return days[datetime.date(year, month, day).weekday()]
