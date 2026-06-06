from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """Find all strings that are substrings of another string in the array.

        Args:
            words: List of unique lowercase strings.

        Returns:
            List of strings that are substrings of at least one other word.
        """
        result = []
        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and word in other:
                    result.append(word)
                    break
        return result
