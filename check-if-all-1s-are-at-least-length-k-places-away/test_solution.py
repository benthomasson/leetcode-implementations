import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

import unittest
from solution import Solution


class TestKLengthApart(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(self.sol.kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2))

    def test_example2(self):
        self.assertFalse(self.sol.kLengthApart([1, 0, 0, 1, 0, 1], 2))

    def test_all_zeros(self):
        self.assertTrue(self.sol.kLengthApart([0, 0, 0, 0], 3))

    def test_single_one(self):
        self.assertTrue(self.sol.kLengthApart([1], 0))

    def test_single_zero(self):
        self.assertTrue(self.sol.kLengthApart([0], 5))

    def test_k_zero_consecutive(self):
        self.assertTrue(self.sol.kLengthApart([1, 1, 1], 0))

    def test_consecutive_ones_fail(self):
        self.assertFalse(self.sol.kLengthApart([1, 1], 1))

    def test_exact_boundary(self):
        # Distance between indices 0 and 3 is 2 (positions between), equals k
        self.assertTrue(self.sol.kLengthApart([1, 0, 0, 1], 2))

    def test_one_less_than_k(self):
        # Distance is 1, k is 2 -> fail
        self.assertFalse(self.sol.kLengthApart([1, 0, 1], 2))

    def test_ones_at_boundaries(self):
        self.assertTrue(self.sol.kLengthApart([1, 0, 0, 0, 0, 1], 4))


if __name__ == '__main__':
    unittest.main()
