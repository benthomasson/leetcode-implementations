"""Determine Whether Matrix Can Be Obtained By Rotation."""

import unittest
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """Check if mat can be rotated in 90-degree increments to equal target.

        Args:
            mat: Source binary matrix.
            target: Target binary matrix.

        Returns:
            True if any 90-degree rotation of mat equals target.
        """
        n = len(mat)
        for _ in range(4):
            if mat == target:
                return True
            mat = [[mat[n - 1 - j][i] for j in range(n)] for i in range(n)]
        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1_90_rotation(self):
        self.assertTrue(self.s.findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]))

    def test_example2_no_match(self):
        self.assertFalse(self.s.findRotation([[0, 1], [1, 1]], [[1, 0], [0, 1]]))

    def test_example3_180_rotation(self):
        self.assertTrue(self.s.findRotation(
            [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
            [[1, 1, 1], [0, 1, 0], [0, 0, 0]],
        ))

    def test_identity(self):
        self.assertTrue(self.s.findRotation([[1, 0], [0, 1]], [[1, 0], [0, 1]]))

    def test_270_rotation(self):
        self.assertTrue(self.s.findRotation([[1, 0], [0, 1]], [[0, 1], [1, 0]]))

    def test_1x1(self):
        self.assertTrue(self.s.findRotation([[0]], [[0]]))
        self.assertFalse(self.s.findRotation([[0]], [[1]]))

    def test_all_same(self):
        self.assertTrue(self.s.findRotation([[1, 1], [1, 1]], [[1, 1], [1, 1]]))
        self.assertTrue(self.s.findRotation([[0, 0], [0, 0]], [[0, 0], [0, 0]]))


if __name__ == "__main__":
    unittest.main()
