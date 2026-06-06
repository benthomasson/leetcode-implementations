from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        """Return the first palindromic string in the array, or empty string if none.

        Args:
            words: List of lowercase English letter strings.

        Returns:
            The first palindromic string, or "" if none exists.
        """
        for word in words:
            if word == word[::-1]:
                return word
        return ""


def minimizeTheDifference(words: List[str]) -> str:
    """Wrapper per task requirements."""
    return Solution().firstPalindrome(words)
