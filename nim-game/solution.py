"""Nim Game - LeetCode Problem."""


def canWinNim(n: int) -> bool:
    """Determine if you can win the Nim Game going first.

    Args:
        n: Number of stones in the heap (1 <= n <= 2^31 - 1).

    Returns:
        True if you can win with optimal play, False otherwise.
    """
    return n % 4 != 0
