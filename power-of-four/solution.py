def isPowerOfFour(n: int) -> bool:
    """Check if an integer is a power of four.

    Args:
        n: Integer to check.

    Returns:
        True if n is a power of four, False otherwise.
    """
    return n > 0 and n & (n - 1) == 0 and n & 0x55555555 != 0
