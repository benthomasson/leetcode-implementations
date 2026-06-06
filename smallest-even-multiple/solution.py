"""Solution for LeetCode problem: Smallest Even Multiple."""


def smallest_multiple(n: int) -> int:
    """Return the smallest positive integer that is a multiple of both 2 and n.

    Args:
        n: A positive integer (1 <= n <= 150).

    Returns:
        The smallest positive integer that is a multiple of both 2 and n.

    Raises:
        ValueError: If n is not a positive integer in the range [1, 150].

    Examples:
        >>> smallest_multiple(5)
        10
        >>> smallest_multiple(6)
        6
        >>> smallest_multiple(1)
        2
    """
    if not isinstance(n, int) or n < 1 or n > 150:
        raise ValueError(f"n must be an integer in [1, 150], got {n}")

    return n if n % 2 == 0 else n * 2
