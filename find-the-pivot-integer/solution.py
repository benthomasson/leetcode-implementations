"""Solution for LeetCode problem: Find the Pivot Integer."""

from math import isqrt


def find_pivot(n: int) -> int:
    """Find the pivot integer x where sum(1..x) == sum(x..n).

    The pivot integer x satisfies the equation x^2 = n*(n+1)/2.
    We compute the total sum, take the integer square root, and check
    if it squares back to the total exactly.

    Args:
        n: A positive integer (1 <= n <= 1000).

    Returns:
        The pivot integer x, or -1 if no such integer exists.

    Examples:
        >>> find_pivot(8)
        6
        >>> find_pivot(1)
        1
        >>> find_pivot(4)
        -1
    """
    total = n * (n + 1) // 2
    x = isqrt(total)
    if x * x == total:
        return x
    return -1
