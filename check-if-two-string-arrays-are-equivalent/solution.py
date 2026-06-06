"""Check If Two String Arrays Are Equivalent."""

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """Return True if both string arrays represent the same string.

        Args:
            word1: First array of strings.
            word2: Second array of strings.

        Returns:
            True if concatenations are equal, False otherwise.
        """
        return "".join(word1) == "".join(word2)
