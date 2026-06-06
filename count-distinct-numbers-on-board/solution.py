"""Count Distinct Numbers on Board."""


def distinct_numbers(n: int) -> int:
    """Return the count of distinct integers on the board after 10^9 days.

    Args:
        n: The positive integer initially placed on the board.

    Returns:
        The number of distinct integers present on the board.
    """
    return 1 if n == 1 else n - 1
