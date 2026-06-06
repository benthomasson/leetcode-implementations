"""Maximum 69 Number - LeetCode"""


def maximum69Number(num: int) -> int:
    """Return max number by changing at most one digit (6→9 or 9→6).

    Args:
        num: Positive integer consisting only of digits 6 and 9.

    Returns:
        Maximum number achievable by changing at most one digit.
    """
    return int(str(num).replace("6", "9", 1))
