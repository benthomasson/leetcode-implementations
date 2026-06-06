def hamming_weight(n: int) -> int:
    """Return the number of '1' bits in the binary representation of n.

    Args:
        n: An unsigned 32-bit integer.

    Returns:
        The count of set bits (Hamming weight).
    """
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
