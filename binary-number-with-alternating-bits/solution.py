def has_alternating_bits(n: int) -> bool:
    """Check whether a positive integer has alternating bits.

    Args:
        n: A positive integer (1 <= n <= 2^31 - 1).

    Returns:
        True if the binary representation has alternating bits.
    """
    m = n ^ (n >> 1)
    return (m & (m + 1)) == 0
