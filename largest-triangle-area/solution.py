from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        """Return the area of the largest triangle formed by any three points.

        Args:
            points: List of [x, y] coordinates.

        Returns:
            Maximum triangle area.
        """
        max_area = 0.0
        for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3):
            area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
            if area > max_area:
                max_area = area
        return max_area
