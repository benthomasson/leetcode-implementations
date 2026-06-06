from collections import Counter
from typing import List


class Solution:
    def num_tile_possibilities(self, words: List[str], chars: str) -> int:
        """Return sum of lengths of words that can be formed from chars.

        Args:
            words: List of strings to check.
            chars: Available characters (each used at most once).

        Returns:
            Sum of lengths of all "good" words.
        """
        chars_count = Counter(chars)
        return sum(
            len(word) for word in words
            if not (Counter(word) - chars_count)
        )
