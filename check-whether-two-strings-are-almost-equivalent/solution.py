from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        """Check if two strings are almost equivalent (freq diffs <= 3).

        Args:
            word1: First string of lowercase English letters.
            word2: Second string of lowercase English letters.

        Returns:
            True if all character frequency differences are at most 3.
        """
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        for c in set(freq1) | set(freq2):
            if abs(freq1[c] - freq2[c]) > 3:
                return False
        return True
