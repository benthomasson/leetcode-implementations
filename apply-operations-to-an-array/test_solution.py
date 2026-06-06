"""Tests for Apply Operations to an Array."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import performOps


class TestPerformOps(unittest.TestCase):
    # Problem examples
    def test_example1(self):
        self.assertEqual(performOps([1, 2, 2, 1, 1, 0]), [1, 4, 2, 0, 0, 0])

    def test_example2(self):
        self.assertEqual(performOps([0, 1]), [1, 0])

    # Edge cases
    def test_minimum_length(self):
        self.assertEqual(performOps([5, 5]), [10, 0])

    def test_all_zeros(self):
        self.assertEqual(performOps([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_no_adjacent_duplicates(self):
        self.assertEqual(performOps([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_sequential_matters(self):
        # [2,2,2]: i=0: 2==2 -> [4,0,2]; i=1: 0!=2 skip -> [4,0,2]; shift -> [4,2,0]
        self.assertEqual(performOps([2, 2, 2]), [4, 2, 0])

    def test_all_same_even_length(self):
        # [1,1,1,1]: i=0: [2,0,1,1]; i=1: skip; i=2: [2,0,2,0]; shift -> [2,2,0,0]
        self.assertEqual(performOps([1, 1, 1, 1]), [2, 2, 0, 0])

    def test_does_not_mutate_input(self):
        original = [1, 2, 2, 1]
        copy = original[:]
        performOps(original)
        self.assertEqual(original, copy)

    def test_chain_doubling(self):
        # [4,4,8]: i=0: 4==4 -> [8,0,8]; i=1: 0!=8 skip; shift -> [8,8,0]
        self.assertEqual(performOps([4, 4, 8]), [8, 8, 0])

    def test_zeros_between_values(self):
        # [1,0,0,1]: i=0: skip; i=1: 0==0 -> [1,0,0,1] (no-op); i=2: 0!=1 skip; shift -> [1,1,0,0]
        self.assertEqual(performOps([1, 0, 0, 1]), [1, 1, 0, 0])


if __name__ == "__main__":
    unittest.main()
