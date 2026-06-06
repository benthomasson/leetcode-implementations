from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """Determine which kids can have the greatest number of candies.

        Args:
            candies: Number of candies each kid currently has.
            extraCandies: Extra candies available to give to one kid.

        Returns:
            List where result[i] is True if kid i would have the max after receiving extraCandies.
        """
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]
