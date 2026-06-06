"""Power of Two - LeetCode solution."""


def is_power_of_two(n: int) -> bool:
    """Check if n is a power of two.

    Args:
        n: Integer to check.

    Returns:
        True if n is a power of two, False otherwise.
    """
    return n > 0 and (n & (n - 1)) == 0
