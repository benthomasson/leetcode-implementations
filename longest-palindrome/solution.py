"""Longest Palindrome - LeetCode"""

from collections import Counter


def longestPalindrome(s: str) -> int:
    """Return the length of the longest palindrome buildable from letters in s.

    Args:
        s: String of lowercase and/or uppercase English letters.

    Returns:
        Length of the longest palindrome.
    """
    length = 0
    has_odd = False
    for count in Counter(s).values():
        length += count // 2 * 2
        if count % 2:
            has_odd = True
    return length + has_odd
