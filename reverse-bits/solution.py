"""Reverse Bits - LeetCode Problem."""


def reverse_bits(n: int) -> int:
    """Reverse bits of a 32-bit unsigned integer.

    Args:
        n: A 32-bit unsigned integer.

    Returns:
        The integer with its bits reversed.
    """
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
