from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        """Check if all characters in s have equal frequency."""
        return len(set(Counter(s).values())) == 1


make_string_sorted = Solution().areOccurrencesEqual
