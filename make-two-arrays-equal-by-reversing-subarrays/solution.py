from typing import List


class Solution:
    def numberOfSubstrings(self, target: List[int], arr: List[int]) -> bool:
        """Determine if arr can be made equal to target by reversing subarrays.

        Args:
            target: The target array.
            arr: The array to transform.

        Returns:
            True if arr can be made equal to target, False otherwise.
        """
        return sorted(target) == sorted(arr)
