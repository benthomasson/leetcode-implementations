class Solution:
    def min_operations(self, sentence: str) -> bool:
        """Check if sentence is a pangram.

        Args:
            sentence: String of lowercase English letters.

        Returns:
            True if sentence contains every letter of the alphabet.
        """
        return len(set(sentence)) == 26
