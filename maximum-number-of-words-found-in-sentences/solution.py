from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        """Return the maximum number of words in any single sentence.

        Args:
            sentences: List of sentences, each with space-separated words.

        Returns:
            Maximum word count across all sentences.
        """
        return max(len(s.split()) for s in sentences)
