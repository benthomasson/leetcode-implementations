"""Valid Palindrome II - LeetCode solution."""


def validPalindrome(s: str) -> bool:
    """Return True if s can be a palindrome after deleting at most one character.

    Args:
        s: Input string of lowercase English letters.

    Returns:
        True if s is a valid palindrome with at most one deletion.
    """

    def is_palindrome(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1
    return True
