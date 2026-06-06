"""Tests for Reshape the Matrix solution."""

import unittest
from solution import Solution


class TestMatrixReshape(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_reshape_2x2_to_1x4(self):
        self.assertEqual(self.s.matrixReshape([[1, 2], [3, 4]], 1, 4), [[1, 2, 3, 4]])

    def test_impossible_reshape(self):
        self.assertEqual(self.s.matrixReshape([[1, 2], [3, 4]], 2, 4), [[1, 2], [3, 4]])

    def test_same_shape(self):
        self.assertEqual(self.s.matrixReshape([[1, 2], [3, 4]], 2, 2), [[1, 2], [3, 4]])

    def test_reshape_to_column(self):
        self.assertEqual(self.s.matrixReshape([[1, 2, 3, 4]], 4, 1), [[1], [2], [3], [4]])

    def test_reshape_to_row(self):
        self.assertEqual(self.s.matrixReshape([[1], [2], [3]], 1, 3), [[1, 2, 3]])

    def test_single_element(self):
        self.assertEqual(self.s.matrixReshape([[5]], 1, 1), [[5]])

    def test_negative_values(self):
        self.assertEqual(self.s.matrixReshape([[-1, -2], [-3, -4]], 1, 4), [[-1, -2, -3, -4]])

    def test_3x2_to_2x3(self):
        self.assertEqual(
            self.s.matrixReshape([[1, 2], [3, 4], [5, 6]], 2, 3),
            [[1, 2, 3], [4, 5, 6]],
        )


if __name__ == "__main__":
    unittest.main()
