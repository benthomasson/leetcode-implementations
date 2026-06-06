"""Palindrome Number - LeetCode solution."""


def is_palindrome(x: int) -> bool:
    """Check if an integer is a palindrome without string conversion.

    Args:
        x: Integer to check.

    Returns:
        True if x is a palindrome, False otherwise.
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10
