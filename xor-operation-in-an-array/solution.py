class Solution:
    def findTheDistanceValue(self, n: int, start: int) -> int:
        """Return bitwise XOR of all elements where nums[i] = start + 2*i.

        Args:
            n: Length of the array.
            start: Starting value.

        Returns:
            Bitwise XOR of all elements.
        """
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result
