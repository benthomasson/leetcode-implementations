"""Number of Days in a Month."""


def number_of_days(year: int, month: int) -> int:
    """Return the number of days in the given month/year.

    Args:
        year: Year (1583-2100).
        month: Month (1-12).

    Returns:
        Number of days in that month.
    """
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return 29
    return days[month - 1]
