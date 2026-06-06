"""Count the number of vowel strings in range."""

from typing import List

VOWELS = set("aeiou")


def is_vowel(char: str) -> bool:
    """Check if a character is a vowel."""
    return char in VOWELS


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        """Count vowel strings in the given range.

        Args:
            words: List of strings.
            left: Start index (inclusive).
            right: End index (inclusive).

        Returns:
            Number of vowel strings in words[left..right].
        """
        return sum(
            1 for i in range(left, right + 1)
            if is_vowel(words[i][0]) and is_vowel(words[i][-1])
        )
