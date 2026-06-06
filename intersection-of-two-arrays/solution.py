from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Return the unique intersection of two integer arrays.

        Args:
            nums1: First integer array.
            nums2: Second integer array.

        Returns:
            List of unique elements present in both arrays.
        """
        return list(set(nums1) & set(nums2))
