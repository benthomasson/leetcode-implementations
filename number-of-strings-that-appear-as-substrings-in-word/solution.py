from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """Count how many strings in patterns appear as substrings in word.

        Args:
            patterns: List of strings to search for.
            word: The string to search within.

        Returns:
            Number of patterns that are substrings of word.
        """
        return sum(1 for p in patterns if p in word)
