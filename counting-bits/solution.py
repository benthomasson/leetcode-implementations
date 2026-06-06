"""Counting Bits - LeetCode problem solution."""


def countBits(n: int) -> list[int]:
    """Return array where ans[i] is the number of 1's in binary representation of i.

    Args:
        n: Non-negative integer upper bound.

    Returns:
        List of length n+1 with popcount for each index.
    """
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans
