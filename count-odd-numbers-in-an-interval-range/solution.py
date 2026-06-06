"""Count odd numbers in an interval range."""


def count_odds(low: int, high: int) -> int:
    """Return the count of odd numbers between low and high (inclusive).

    Args:
        low: Lower bound of the interval.
        high: Upper bound of the interval.

    Returns:
        Number of odd integers in [low, high].
    """
    return (high + 1) // 2 - low // 2
