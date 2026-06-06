from typing import List


class Solution:
    def add_rooms(self, nums: List[int]) -> List[int]:
        """Decompress a run-length encoded list.

        Args:
            nums: List of integers where each pair [freq, val] represents
                freq occurrences of val.

        Returns:
            The decompressed list.
        """
        result = []
        for i in range(0, len(nums), 2):
            result.extend([nums[i + 1]] * nums[i])
        return result
