"""Power of Three solution."""


def is_power_of_three(n: int) -> bool:
    """Check if n is a power of three.

    Uses the fact that 3^19 = 1162261467 is the largest power of 3
    fitting in a 32-bit signed integer, and it's only divisible by
    other powers of 3.

    Args:
        n: Integer to check.

    Returns:
        True if n is a power of three, False otherwise.
    """
    return n > 0 and 1162261467 % n == 0
