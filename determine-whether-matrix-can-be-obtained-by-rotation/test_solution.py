"""Tests for Determine Whether Matrix Can Be Obtained By Rotation."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestMatrixRotation(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1_90_rotation(self):
        self.assertTrue(self.s.findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]))

    def test_example2_no_match(self):
        self.assertFalse(self.s.findRotation([[0, 1], [1, 1]], [[1, 0], [0, 1]]))

    def test_example3_180_rotation(self):
        self.assertTrue(self.s.findRotation(
            [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
            [[1, 1, 1], [0, 1, 0], [0, 0, 0]],
        ))

    # --- Edge cases ---
    def test_identity_no_rotation_needed(self):
        self.assertTrue(self.s.findRotation([[1, 0], [0, 1]], [[1, 0], [0, 1]]))

    def test_1x1_same(self):
        self.assertTrue(self.s.findRotation([[0]], [[0]]))

    def test_1x1_different(self):
        self.assertFalse(self.s.findRotation([[0]], [[1]]))

    def test_all_ones(self):
        self.assertTrue(self.s.findRotation([[1, 1], [1, 1]], [[1, 1], [1, 1]]))

    def test_270_rotation(self):
        # mat rotated 270° clockwise (= 90° counter-clockwise) should match target
        self.assertTrue(self.s.findRotation([[1, 0], [0, 1]], [[0, 1], [1, 0]]))

    def test_no_rotation_matches_3x3(self):
        # top-left 1 can never rotate to middle
        self.assertFalse(self.s.findRotation(
            [[1, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        ))


if __name__ == "__main__":
    unittest.main()
