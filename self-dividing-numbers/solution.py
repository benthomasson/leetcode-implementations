def is_self_dividing(n: int) -> bool:
    """Check if a number is self-dividing.

    Args:
        n: Positive integer to check.

    Returns:
        True if n is divisible by each of its digits and contains no zeros.
    """
    num = n
    while num:
        digit = num % 10
        if digit == 0 or n % digit != 0:
            return False
        num //= 10
    return True


def self_dividing_numbers(left: int, right: int) -> list[int]:
    """Return all self-dividing numbers in [left, right].

    Args:
        left: Start of range (inclusive).
        right: End of range (inclusive).

    Returns:
        List of self-dividing numbers in the range.
    """
    return [n for n in range(left, right + 1) if is_self_dividing(n)]
