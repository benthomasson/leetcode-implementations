class Solution:
    def maxPower(self, s: str) -> int:
        """Return the length of the longest substring of one unique character."""
        max_count = 1
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1
        return max_count
