from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        """Check if array can be partitioned into three parts with equal sums.

        Args:
            arr: List of integers to partition.

        Returns:
            True if the array can be split into three non-empty parts with equal sums.
        """
        total = sum(arr)
        if total % 3 != 0:
            return False

        target = total // 3
        running_sum = 0
        parts_found = 0

        for i in range(len(arr) - 1):  # stop before last element to ensure 3rd part is non-empty
            running_sum += arr[i]
            if running_sum == target * (parts_found + 1):
                parts_found += 1
                if parts_found == 2:
                    return True

        return False
