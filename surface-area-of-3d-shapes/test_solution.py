"""Tests for Surface Area of 3D Shapes (LeetCode 892)."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution


class TestSurfaceArea(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.s.surfaceArea([[1, 2], [3, 4]]), 34)

    def test_example2(self):
        self.assertEqual(self.s.surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), 32)

    def test_example3(self):
        self.assertEqual(self.s.surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]), 46)

    # --- Edge cases ---
    def test_single_zero(self):
        self.assertEqual(self.s.surfaceArea([[0]]), 0)

    def test_single_cube(self):
        self.assertEqual(self.s.surfaceArea([[1]]), 6)

    def test_single_tall_tower(self):
        # 1 tower of height 50: top + bottom + 4*50 sides = 2 + 200 = 202
        self.assertEqual(self.s.surfaceArea([[50]]), 202)

    def test_all_zeros(self):
        self.assertEqual(self.s.surfaceArea([[0, 0], [0, 0]]), 0)

    def test_adjacent_different_heights(self):
        # 2x2: [[1,3],[0,0]] -> tower(0,0)=6, tower(0,1)=14, adj horiz hide 2*1=2, adj vert hide 0 -> 18
        self.assertEqual(self.s.surfaceArea([[1, 3], [0, 0]]), 18)

    def test_large_uniform(self):
        # 2x2 all height 50: 4*(2+200)=808, 4 adj pairs hide 2*50*4=400 -> 408
        self.assertEqual(self.s.surfaceArea([[50, 50], [50, 50]]), 408)


if __name__ == "__main__":
    unittest.main()
