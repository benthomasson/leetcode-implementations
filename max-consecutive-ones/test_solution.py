"""Tests for findMaxConsecutiveOnes."""

import unittest
from solution import findMaxConsecutiveOnes


class TestFindMaxConsecutiveOnes(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)

    def test_example2(self):
        self.assertEqual(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]), 2)

    def test_all_ones(self):
        self.assertEqual(findMaxConsecutiveOnes([1, 1, 1, 1]), 4)

    def test_all_zeros(self):
        self.assertEqual(findMaxConsecutiveOnes([0, 0, 0]), 0)

    def test_single_one(self):
        self.assertEqual(findMaxConsecutiveOnes([1]), 1)

    def test_single_zero(self):
        self.assertEqual(findMaxConsecutiveOnes([0]), 0)

    def test_streak_at_end(self):
        self.assertEqual(findMaxConsecutiveOnes([0, 0, 1, 1, 1]), 3)

    def test_streak_at_start(self):
        self.assertEqual(findMaxConsecutiveOnes([1, 1, 1, 0, 0]), 3)

    def test_alternating(self):
        self.assertEqual(findMaxConsecutiveOnes([1, 0, 1, 0, 1]), 1)


if __name__ == "__main__":
    unittest.main()
