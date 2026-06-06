"""Tests for Image Smoother - LeetCode 661."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestImageSmoother(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
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

    # --- Edge cases ---
    def test_1x1(self):
        self.assertEqual(self.s.imageSmoother([[42]]), [[42]])

    def test_single_row(self):
        # (1+2)/2=1, (1+2+3)/3=2, (2+3)/2=2
        self.assertEqual(self.s.imageSmoother([[1, 2, 3]]), [[1, 2, 2]])

    def test_single_column(self):
        # (1+2)/2=1, (1+2+3)/3=2, (2+3)/2=2
        self.assertEqual(self.s.imageSmoother([[1], [2], [3]]), [[1], [2], [2]])

    def test_all_zeros(self):
        self.assertEqual(
            self.s.imageSmoother([[0, 0], [0, 0]]), [[0, 0], [0, 0]]
        )

    def test_all_max(self):
        self.assertEqual(
            self.s.imageSmoother([[255, 255], [255, 255]]), [[255, 255], [255, 255]]
        )

    def test_2x2_mixed(self):
        # (0,0): (0+1+3+4)/4=2, (0,1): (0+1+3+4)/4=2
        # (1,0): (0+1+3+4)/4=2, (1,1): (0+1+3+4)/4=2
        self.assertEqual(
            self.s.imageSmoother([[0, 1], [3, 4]]), [[2, 2], [2, 2]]
        )

    def test_output_is_new_matrix(self):
        img = [[10, 20], [30, 40]]
        result = self.s.imageSmoother(img)
        self.assertIsNot(result, img)
        # Original should be unmodified
        self.assertEqual(img, [[10, 20], [30, 40]])


if __name__ == "__main__":
    unittest.main()
