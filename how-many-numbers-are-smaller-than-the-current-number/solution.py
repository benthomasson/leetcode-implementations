"""Solution for LeetCode: How Many Numbers Are Smaller Than the Current Number."""

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """Count how many numbers in the array are smaller than each element.

        For each nums[i], counts the number of indices j where j != i and
        nums[j] < nums[i]. Uses counting sort with prefix sums for O(n + k)
        time complexity where k is the value range (101).

        Args:
            nums: List of integers where 2 <= len(nums) <= 500 and
                0 <= nums[i] <= 100.

        Returns:
            A list where the i-th element is the count of numbers in nums
            that are strictly less than nums[i].

        Examples:
            >>> Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3])
            [4, 0, 1, 1, 3]
            >>> Solution().smallerNumbersThanCurrent([6, 5, 4, 8])
            [2, 1, 0, 3]
            >>> Solution().smallerNumbersThanCurrent([7, 7, 7, 7])
            [0, 0, 0, 0]
        """
        # Build frequency array for values 0..100
        count = [0] * 101
        for num in nums:
            count[num] += 1

        # Convert to prefix sums: prefix[v] = number of elements < v
        prefix = [0] * 101
        for v in range(1, 101):
            prefix[v] = prefix[v - 1] + count[v - 1]

        return [prefix[num] for num in nums]
