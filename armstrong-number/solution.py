"""Armstrong Number solution."""


def is_armstrong(n: int) -> bool:
    """Check if n is an Armstrong number.

    Args:
        n: Positive integer to check.

    Returns:
        True if n is an Armstrong number, False otherwise.
    """
    digits = str(n)
    k = len(digits)
    return sum(int(d) ** k for d in digits) == n
