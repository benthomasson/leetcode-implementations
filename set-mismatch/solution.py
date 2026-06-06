from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """Find the duplicate and missing numbers in a 1-to-n set.

        Args:
            nums: Array of integers where one number is duplicated and one is missing.

        Returns:
            List of [duplicate, missing].
        """
        seen = set()
        duplicate = -1
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        missing = expected_sum - actual_sum + duplicate
        return [duplicate, missing]
