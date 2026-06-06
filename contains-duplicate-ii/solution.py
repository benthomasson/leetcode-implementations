from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """Check if array contains duplicates within k distance.

        Args:
            nums: List of integers.
            k: Maximum allowed index distance between duplicates.

        Returns:
            True if duplicate exists within k distance, False otherwise.
        """
        last_seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i
        return False
