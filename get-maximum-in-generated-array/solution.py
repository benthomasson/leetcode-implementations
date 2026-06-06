"""LeetCode 1646: Get Maximum in Generated Array."""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        """Return the maximum value in the generated array of length n+1.

        Args:
            n: Length parameter for the generated array.

        Returns:
            Maximum integer in the generated array.
        """
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
        return max(nums)
