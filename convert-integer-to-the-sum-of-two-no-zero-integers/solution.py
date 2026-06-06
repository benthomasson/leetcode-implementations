"""Convert integer to the sum of two No-Zero integers."""


def no_zero_integers(n: int) -> list[int]:
    """Return two No-Zero integers that sum to n.

    Args:
        n: Integer to split (2 <= n <= 10^4).

    Returns:
        List of two positive integers without digit 0 that sum to n.
    """
    for a in range(1, n):
        b = n - a
        if '0' not in str(a) and '0' not in str(b):
            return [a, b]
