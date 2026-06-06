from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """Return True if arr contains three consecutive odd numbers.

        Args:
            arr: List of integers (1 <= len <= 1000, 1 <= arr[i] <= 1000).

        Returns:
            True if three consecutive odd numbers exist, False otherwise.
        """
        count = 0
        for num in arr:
            if num % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False
