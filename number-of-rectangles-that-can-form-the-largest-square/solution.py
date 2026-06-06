from typing import List


class Solution:
    def numberOfSets(self, rectangles: List[List[int]]) -> int:
        """Count rectangles that can form the largest possible square.

        Args:
            rectangles: List of [length, width] pairs.

        Returns:
            Number of rectangles that can make a square with the maximum side length.
        """
        max_len = 0
        count = 0
        for l, w in rectangles:
            side = min(l, w)
            if side > max_len:
                max_len = side
                count = 1
            elif side == max_len:
                count += 1
        return count
