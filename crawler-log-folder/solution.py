"""LeetCode 1598: Crawler Log Folder."""

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """Return minimum operations to get back to main folder.

        Args:
            logs: List of folder change operations.

        Returns:
            Number of "../" operations needed to return to main folder.
        """
        depth = 0
        for log in logs:
            if log == "../":
                depth = max(0, depth - 1)
            elif log != "./":
                depth += 1
        return depth
