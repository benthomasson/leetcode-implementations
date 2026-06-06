"""Longer Contiguous Segments of Ones than Zeros."""


def checkZeroOnes(s: str) -> bool:
    """Return True if longest segment of 1s is strictly longer than longest segment of 0s.

    Args:
        s: Binary string of '0's and '1's.

    Returns:
        True if max contiguous 1s > max contiguous 0s.
    """
    max_ones = max_zeros = cur = 0
    prev = ""
    for c in s:
        if c == prev:
            cur += 1
        else:
            cur = 1
            prev = c
        if c == "1":
            max_ones = max(max_ones, cur)
        else:
            max_zeros = max(max_zeros, cur)
    return max_ones > max_zeros
