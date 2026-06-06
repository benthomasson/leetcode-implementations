"""LeetCode: Truncate Sentence."""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """Truncate sentence to first k words.

        Args:
            s: Space-separated sentence of words.
            k: Number of words to keep.

        Returns:
            The first k words joined by spaces.
        """
        return " ".join(s.split()[:k])
