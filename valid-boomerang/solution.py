from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        """Determine if three points form a boomerang (distinct and non-collinear).

        Args:
            points: List of three [x, y] coordinate pairs.

        Returns:
            True if the points form a valid boomerang.
        """
        (x1, y1), (x2, y2), (x3, y3) = points
        return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) != 0
