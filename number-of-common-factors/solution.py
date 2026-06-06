"""Solution for LeetCode: Number of Common Factors."""

import math


def common_factors(a: int, b: int) -> int:
    """Count the number of common factors of a and b.

    Args:
        a: Positive integer.
        b: Positive integer.

    Returns:
        Number of integers that divide both a and b.
    """
    g = math.gcd(a, b)
    count = 0
    i = 1
    while i * i <= g:
        if g % i == 0:
            count += 1
            if i != g // i:
                count += 1
        i += 1
    return count
