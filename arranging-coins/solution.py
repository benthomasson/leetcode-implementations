"""Arranging Coins - LeetCode problem solution."""

from math import isqrt


def arrange_coins(n: int) -> int:
    """Return the number of complete rows in a coin staircase.

    Args:
        n: Number of coins (1 <= n <= 2^31 - 1).

    Returns:
        Number of complete rows.
    """
    return (isqrt(8 * n + 1) - 1) // 2
