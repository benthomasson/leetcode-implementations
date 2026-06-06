"""LeetCode 2022: Convert 1D Array Into 2D Array."""

import unittest


class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        """Convert a 1D array into a 2D array with m rows and n columns.

        Args:
            original: The 1D source array.
            m: Number of rows.
            n: Number of columns.

        Returns:
            The reshaped 2D array, or [] if impossible.
        """
        if len(original) != m * n:
            return []
        return [original[i * n : (i + 1) * n] for i in range(m)]


class TestConstruct2DArray(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.construct2DArray([1, 2, 3, 4], 2, 2), [[1, 2], [3, 4]])

    def test_example2(self):
        self.assertEqual(self.s.construct2DArray([1, 2, 3], 1, 3), [[1, 2, 3]])

    def test_example3_impossible(self):
        self.assertEqual(self.s.construct2DArray([1, 2], 1, 1), [])

    def test_single_element(self):
        self.assertEqual(self.s.construct2DArray([1], 1, 1), [[1]])

    def test_single_column(self):
        self.assertEqual(self.s.construct2DArray([1, 2, 3], 3, 1), [[1], [2], [3]])

    def test_too_few_elements(self):
        self.assertEqual(self.s.construct2DArray([1], 2, 2), [])

    def test_too_many_elements(self):
        self.assertEqual(self.s.construct2DArray([1, 2, 3, 4, 5], 2, 2), [])


if __name__ == "__main__":
    unittest.main()
