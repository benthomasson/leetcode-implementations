def binary_gap(n: int) -> int:
    """Find longest distance between adjacent 1-bits in binary representation of n.

    Args:
        n: Positive integer (1 <= n <= 10^9).

    Returns:
        Longest gap between adjacent 1-bits, or 0 if fewer than two 1-bits.
    """
    max_gap = 0
    last_one = -1
    pos = 0
    while n:
        if n & 1:
            if last_one >= 0:
                max_gap = max(max_gap, pos - last_one)
            last_one = pos
        pos += 1
        n >>= 1
    return max_gap
