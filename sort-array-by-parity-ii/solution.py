class Solution:
    def possible_bipartition(self, nums: list[int]) -> list[int]:
        """Sort array so evens are at even indices and odds at odd indices.

        Args:
            nums: Array where half the elements are even and half are odd.

        Returns:
            The same array modified in-place to satisfy the parity condition.
        """
        i, j = 0, 1  # i scans even indices, j scans odd indices
        n = len(nums)
        while i < n and j < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                # nums[i] is odd (wrong), nums[j] is even (wrong) — swap
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        return nums
