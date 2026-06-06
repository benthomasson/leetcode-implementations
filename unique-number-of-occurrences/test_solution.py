import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

import unittest
from solution import Solution


class TestUniqueOccurrences(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- LeetCode examples ---
    def test_example1(self):
        self.assertTrue(self.s.uniqueOccurrences([1, 2, 2, 1, 1, 3]))

    def test_example2(self):
        self.assertFalse(self.s.uniqueOccurrences([1, 2]))

    def test_example3(self):
        self.assertTrue(self.s.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))

    # --- Edge cases ---
    def test_single_element(self):
        self.assertTrue(self.s.uniqueOccurrences([0]))

    def test_all_same(self):
        self.assertTrue(self.s.uniqueOccurrences([7, 7, 7, 7]))

    def test_two_values_equal_counts(self):
        self.assertFalse(self.s.uniqueOccurrences([1, 1, 2, 2]))

    def test_boundary_values(self):
        # min and max constraint values
        self.assertTrue(self.s.uniqueOccurrences([-1000, -1000, 1000]))

    def test_three_values_two_share_count(self):
        # 1 appears 2x, 2 appears 2x, 3 appears 1x -> False
        self.assertFalse(self.s.uniqueOccurrences([1, 1, 2, 2, 3]))

    def test_large_unique_counts(self):
        # build arr where value i appears i times: 1x1, 2x2, 3x3 -> True
        arr = [1] + [2, 2] + [3, 3, 3]
        self.assertTrue(self.s.uniqueOccurrences(arr))


if __name__ == "__main__":
    unittest.main()
