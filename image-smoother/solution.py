"""Image Smoother - LeetCode 661."""

from typing import List
import unittest


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """Apply a 3x3 averaging filter to each cell, using floor division.

        Args:
            img: m x n matrix of grayscale values (0-255).

        Returns:
            Smoothed image matrix of the same dimensions.
        """
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total = count = 0
                for di in range(max(0, i - 1), min(m, i + 2)):
                    for dj in range(max(0, j - 1), min(n, j + 2)):
                        total += img[di][dj]
                        count += 1
                result[i][j] = total // count
        return result


class TestImageSmoother(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(
            self.s.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        )

    def test_example2(self):
        self.assertEqual(
            self.s.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]),
            [[137, 141, 137], [141, 138, 141], [137, 141, 137]],
        )

    def test_1x1(self):
        self.assertEqual(self.s.imageSmoother([[42]]), [[42]])

    def test_single_row(self):
        self.assertEqual(self.s.imageSmoother([[1, 2, 3]]), [[1, 2, 2]])

    def test_single_column(self):
        self.assertEqual(self.s.imageSmoother([[1], [2], [3]]), [[1], [2], [2]])

    def test_all_zeros(self):
        self.assertEqual(
            self.s.imageSmoother([[0, 0], [0, 0]]), [[0, 0], [0, 0]]
        )

    def test_all_max(self):
        self.assertEqual(
            self.s.imageSmoother([[255, 255], [255, 255]]), [[255, 255], [255, 255]]
        )


if __name__ == "__main__":
    unittest.main()
