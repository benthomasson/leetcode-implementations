class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Search for target in sorted array using binary search.

        Args:
            nums: Sorted array of unique integers.
            target: Value to find.

        Returns:
            Index of target, or -1 if not found.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
