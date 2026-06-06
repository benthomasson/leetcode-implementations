"""Tests for LeetCode 2022: Convert 1D Array Into 2D Array."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestConstruct2DArray(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.s.construct2DArray([1, 2, 3, 4], 2, 2), [[1, 2], [3, 4]])

    def test_example2(self):
        self.assertEqual(self.s.construct2DArray([1, 2, 3], 1, 3), [[1, 2, 3]])

    def test_example3_impossible(self):
        self.assertEqual(self.s.construct2DArray([1, 2], 1, 1), [])

    # --- Edge cases ---
    def test_single_element(self):
        self.assertEqual(self.s.construct2DArray([1], 1, 1), [[1]])

    def test_single_column(self):
        self.assertEqual(self.s.construct2DArray([1, 2, 3], 3, 1), [[1], [2], [3]])

    def test_too_few_elements(self):
        self.assertEqual(self.s.construct2DArray([1], 2, 2), [])

    def test_too_many_elements(self):
        self.assertEqual(self.s.construct2DArray([1, 2, 3, 4, 5], 2, 2), [])

    def test_large_single_row(self):
        arr = list(range(1, 101))
        result = self.s.construct2DArray(arr, 1, 100)
        self.assertEqual(result, [arr])

    def test_large_single_column(self):
        arr = list(range(1, 101))
        result = self.s.construct2DArray(arr, 100, 1)
        self.assertEqual(result, [[x] for x in arr])

    def test_result_dimensions(self):
        result = self.s.construct2DArray(list(range(12)), 3, 4)
        self.assertEqual(len(result), 3)
        for row in result:
            self.assertEqual(len(row), 4)


if __name__ == "__main__":
    unittest.main()
