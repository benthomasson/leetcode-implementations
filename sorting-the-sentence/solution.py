"""LeetCode: Sorting the Sentence."""


class Solution:
    def sort_sentence(self, s: str) -> str:
        """Reconstruct original sentence from a shuffled sentence.

        Args:
            s: Shuffled sentence where each word has its 1-indexed position appended.

        Returns:
            The original sentence with words in correct order.
        """
        words = s.split()
        result = [""] * len(words)
        for word in words:
            pos = int(word[-1]) - 1
            result[pos] = word[:-1]
        return " ".join(result)
