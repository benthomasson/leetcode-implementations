"""LeetCode 1619: Mean of Array After Removing Some Elements."""

from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        """Return mean after removing smallest and largest 5% of elements."""
        arr.sort()
        k = len(arr) // 20
        trimmed = arr[k : len(arr) - k]
        return sum(trimmed) / len(trimmed)


import unittest


class TestTrimMean(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
        self.assertAlmostEqual(self.s.trimMean(arr), 2.00000, places=5)

    def test_example2(self):
        arr = [6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]
        self.assertAlmostEqual(self.s.trimMean(arr), 4.00000, places=5)

    def test_example3(self):
        arr = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4,
               8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2, 3, 4]
        self.assertAlmostEqual(self.s.trimMean(arr), 4.77778, places=5)

    def test_all_same(self):
        arr = [5] * 20
        self.assertAlmostEqual(self.s.trimMean(arr), 5.0, places=5)

    def test_large_array(self):
        arr = list(range(1000))
        self.assertAlmostEqual(self.s.trimMean(arr), 499.5, places=5)

    def test_boundary_values(self):
        arr = [0] * 10 + [100000] * 10
        # trim 1 from each end: 9 zeros + 9 100000s
        expected = (9 * 100000) / 18
        self.assertAlmostEqual(self.s.trimMean(arr), expected, places=5)


if __name__ == "__main__":
    unittest.main()
