from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        """Check if each index i has digit i occurring num[i] times.

        Args:
            num: A string of digits.

        Returns:
            True if the condition holds for every index.
        """
        count = Counter(num)
        return all(count[str(i)] == int(num[i]) for i in range(len(num)))


# Alias per requirements
rearrange_array = Solution().digitCount
