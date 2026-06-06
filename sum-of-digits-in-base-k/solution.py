"""Sum of Digits in Base K."""


def sum_base(n: int, k: int) -> int:
    """Return the sum of digits of n when expressed in base k.

    Args:
        n: Integer in base 10 (1 <= n <= 100).
        k: Target base (2 <= k <= 10).

    Returns:
        Sum of digits of the base-k representation, in base 10.
    """
    total = 0
    while n:
        total += n % k
        n //= k
    return total
