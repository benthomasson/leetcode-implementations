"""Longest Uncommon Subsequence I."""


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        """Return length of the longest uncommon subsequence, or -1 if none.

        Args:
            a: First string of lowercase English letters.
            b: Second string of lowercase English letters.

        Returns:
            Length of the longest uncommon subsequence, or -1 if equal.
        """
        if a == b:
            return -1
        return max(len(a), len(b))
