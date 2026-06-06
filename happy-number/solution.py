"""Happy Number - LeetCode Solution using Floyd's cycle detection."""


def get_next(n: int) -> int:
    """Compute sum of squares of digits of n.

    Args:
        n: A positive integer.

    Returns:
        Sum of the squares of each digit in n.
    """
    total = 0
    while n > 0:
        n, digit = divmod(n, 10)
        total += digit * digit
    return total


def is_happy(n: int) -> bool:
    """Determine if n is a happy number using Floyd's cycle detection.

    Args:
        n: A positive integer (1 <= n <= 2^31 - 1).

    Returns:
        True if n is a happy number, False otherwise.
    """
    slow = n
    fast = get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return fast == 1
