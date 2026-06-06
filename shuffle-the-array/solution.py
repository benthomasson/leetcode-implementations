from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """Shuffle array by interleaving first and second halves.

        Args:
            nums: Array of 2n elements [x1,x2,...,xn,y1,y2,...,yn].
            n: Half the length of nums.

        Returns:
            Interleaved array [x1,y1,x2,y2,...,xn,yn].
        """
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n + i])
        return result
