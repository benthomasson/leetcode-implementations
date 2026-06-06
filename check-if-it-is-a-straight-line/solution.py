"""Check if points make a straight line in the XY plane."""

from typing import List


class Solution:
    def findBestValue(self, coordinates: List[List[int]]) -> bool:
        """Check if all points lie on a straight line using cross-product.

        Args:
            coordinates: List of [x, y] coordinate pairs.

        Returns:
            True if all points are collinear, False otherwise.
        """
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]

        for i in range(2, len(coordinates)):
            if (coordinates[i][0] - coordinates[0][0]) * dy - (coordinates[i][1] - coordinates[0][1]) * dx != 0:
                return False
        return True
