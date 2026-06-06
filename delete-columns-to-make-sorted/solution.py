"""LeetCode 944: Delete Columns to Make Sorted."""

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """Count columns that are not sorted lexicographically.

        Args:
            strs: List of equal-length strings forming a grid.

        Returns:
            Number of columns to delete.
        """
        count = 0
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if strs[i][j] < strs[i - 1][j]:
                    count += 1
                    break
        return count
