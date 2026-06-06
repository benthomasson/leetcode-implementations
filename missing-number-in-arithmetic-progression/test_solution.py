import sys
import unittest

sys.path.insert(0, '/Users/ben/git/leetcode-results/workspaces/missing-number-in-arithmetic-progression/implementer')
from solution import Solution


class TestMissingNumber(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.mctFromLeafValues([5, 7, 11, 13]), 9)

    def test_example2(self):
        self.assertEqual(self.s.mctFromLeafValues([15, 13, 12]), 14)

    def test_decreasing(self):
        self.assertEqual(self.s.mctFromLeafValues([20, 16, 12, 8, 0]), 4)

    def test_all_same(self):
        self.assertEqual(self.s.mctFromLeafValues([3, 3, 3]), 3)

    def test_missing_second(self):
        self.assertEqual(self.s.mctFromLeafValues([1, 5, 7, 9]), 3)

    def test_missing_second_to_last(self):
        self.assertEqual(self.s.mctFromLeafValues([1, 3, 5, 9]), 7)

    def test_large_values(self):
        self.assertEqual(self.s.mctFromLeafValues([0, 25000, 75000, 100000]), 50000)

    def test_gap_in_middle(self):
        self.assertEqual(self.s.mctFromLeafValues([1, 3, 7]), 5)

    def test_minimum_length(self):
        self.assertEqual(self.s.mctFromLeafValues([2, 6]), 4)

    def test_step_of_one(self):
        self.assertEqual(self.s.mctFromLeafValues([1, 2, 3, 5, 6]), 4)


if __name__ == '__main__':
    unittest.main()
