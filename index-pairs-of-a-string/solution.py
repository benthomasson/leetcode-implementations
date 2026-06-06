from typing import List


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        """Find all index pairs [i, j] where text[i..j] matches a word.

        Args:
            text: The string to search in.
            words: List of words to find as substrings.

        Returns:
            Sorted list of [i, j] pairs where text[i..j] is in words.
        """
        result = []
        for word in words:
            wlen = len(word)
            for i in range(len(text) - wlen + 1):
                if text[i:i + wlen] == word:
                    result.append([i, i + wlen - 1])
        result.sort()
        return result


def has_all_codes_in_range(text: str, words: List[str]) -> List[List[int]]:
    """Wrapper for Solution.indexPairs."""
    return Solution().indexPairs(text, words)
