"""Alternating digit sum."""


def sum_of_digits(n: int) -> int:
    """Return the alternating sum of digits of n, starting positive from the most significant digit.

    Args:
        n: A positive integer (1 <= n <= 10^9).

    Returns:
        The alternating digit sum.
    """
    s = str(n)
    return sum(int(d) * (-1) ** i for i, d in enumerate(s))
