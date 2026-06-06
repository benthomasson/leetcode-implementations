"""Hamming Distance - LeetCode Problem."""


def hammingDistance(x: int, y: int) -> int:
    """Return the Hamming distance between two integers.

    Args:
        x: First integer (0 <= x <= 2^31 - 1).
        y: Second integer (0 <= y <= 2^31 - 1).

    Returns:
        Number of bit positions where x and y differ.
    """
    return bin(x ^ y).count('1')
