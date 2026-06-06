"""Count common words with exactly one occurrence in each array."""

from collections import Counter


class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        """Return count of strings appearing exactly once in both arrays."""
        c1, c2 = Counter(words1), Counter(words2)
        return sum(1 for w in c1 if c1[w] == 1 and c2[w] == 1)
