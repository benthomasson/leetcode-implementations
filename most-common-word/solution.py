"""LeetCode 819: Most Common Word."""

import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        """Find the most frequent word in a paragraph that is not banned.

        Extracts words from the paragraph (ignoring punctuation), converts
        to lowercase, and returns the most frequent word not in the banned list.

        Args:
            paragraph: A string of words separated by spaces and/or punctuation.
                Contains English letters, spaces, and symbols: !?',;.
            banned: A list of lowercase banned words to exclude.

        Returns:
            The most frequent non-banned word in lowercase.

        Examples:
            >>> s = Solution()
            >>> s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
            'ball'
            >>> s.mostCommonWord("a.", [])
            'a'
        """
        words = re.findall(r'[a-z]+', paragraph.lower())
        banned_set = set(banned)
        counts = Counter(w for w in words if w not in banned_set)
        return counts.most_common(1)[0][0]
