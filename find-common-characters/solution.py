from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """Find characters common to all words, including duplicates."""
        common = Counter(words[0])
        for word in words[1:]:
            common &= Counter(word)
        return list(common.elements())
