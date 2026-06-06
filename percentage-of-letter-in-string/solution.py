"""LeetCode 2278: Percentage of Letter in String."""


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        """Return the percentage of characters in s that equal letter, rounded down.

        Args:
            s: Input string of lowercase English letters.
            letter: Target lowercase English letter.

        Returns:
            Floor percentage of letter occurrences in s.
        """
        return s.count(letter) * 100 // len(s)
