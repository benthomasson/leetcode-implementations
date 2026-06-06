"""Count integers with even digit sum."""


def max_tasks(num: int) -> int:
    """Return count of positive integers <= num with even digit sum.

    Args:
        num: Upper bound (1 <= num <= 1000).

    Returns:
        Count of integers with even digit sum.
    """
    return sum(1 for n in range(1, num + 1) if sum(int(d) for d in str(n)) % 2 == 0)
