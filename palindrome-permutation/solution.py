from collections import Counter


def canPermutePalindrome(s: str) -> bool:
    """Check if any permutation of s can form a palindrome.

    Args:
        s: Input string of lowercase English letters.

    Returns:
        True if a permutation of s could form a palindrome.
    """
    return sum(c % 2 for c in Counter(s).values()) <= 1
