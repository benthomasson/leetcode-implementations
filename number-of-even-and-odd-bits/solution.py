"""Solution for LeetCode: Number of Even and Odd Bits."""


def even_odd_indices(n: int) -> list[int]:
    """Count 1-bits at even and odd indices in binary representation of n.

    Args:
        n: A positive integer (1 <= n <= 1000).

    Returns:
        A list [even_count, odd_count] of 1-bits at even/odd indices.
    """
    even = odd = 0
    i = 0
    while n:
        if n & 1:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        n >>= 1
        i += 1
    return [even, odd]
