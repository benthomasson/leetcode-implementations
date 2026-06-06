from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """Return True if the number of occurrences of each value is unique.

        Args:
            arr: List of integers.

        Returns:
            True if all occurrence counts are distinct, False otherwise.
        """
        counts = Counter(arr).values()
        return len(counts) == len(set(counts))
