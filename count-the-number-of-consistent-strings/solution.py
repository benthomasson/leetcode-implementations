class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        """Count words where all characters appear in allowed.

        Args:
            allowed: String of distinct allowed characters.
            words: List of strings to check.

        Returns:
            Number of consistent strings.
        """
        allowed_set = set(allowed)
        return sum(all(c in allowed_set for c in word) for word in words)

    find_latest_step = countConsistentStrings
