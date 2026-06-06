"""Tests for LeetCode 1619: Mean of Array After Removing Some Elements."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestTrimMean(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- LeetCode examples ---

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

    # --- Edge cases ---

    def test_all_same_values(self):
        arr = [7] * 20
        self.assertAlmostEqual(self.s.trimMean(arr), 7.0, places=5)

    def test_min_length_sorted(self):
        arr = list(range(20))  # 0..19, trim 1 each end -> 1..18, mean=9.5
        self.assertAlmostEqual(self.s.trimMean(arr), 9.5, places=5)

    def test_max_length_array(self):
        arr = list(range(1000))  # trim 50 each end -> 50..949, mean=499.5
        self.assertAlmostEqual(self.s.trimMean(arr), 499.5, places=5)

    def test_boundary_values(self):
        arr = [0] * 10 + [100000] * 10
        # trim 1 from each end: 9 zeros + 9 of 100000
        expected = (9 * 100000) / 18
        self.assertAlmostEqual(self.s.trimMean(arr), expected, places=5)

    def test_all_zeros(self):
        arr = [0] * 40
        self.assertAlmostEqual(self.s.trimMean(arr), 0.0, places=5)

    def test_input_not_mutated_semantically(self):
        """Verify result is correct even though sort mutates input."""
        arr = [9, 1, 5, 3, 7, 2, 8, 4, 6, 0,
               9, 1, 5, 3, 7, 2, 8, 4, 6, 0]
        result = self.s.trimMean(arr)
        # sorted: [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
        # trim 1 each end -> [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9] -> mean=4.5
        self.assertAlmostEqual(result, 4.5, places=5)


if __name__ == "__main__":
    unittest.main()
