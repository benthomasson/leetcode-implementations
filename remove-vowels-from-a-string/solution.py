class Solution:
    def removeVowels(self, s: str) -> str:
        """Remove vowels from a string.

        Args:
            s: Input string of lowercase English letters.

        Returns:
            String with all vowels removed.
        """
        return "".join(c for c in s if c not in "aeiou")
