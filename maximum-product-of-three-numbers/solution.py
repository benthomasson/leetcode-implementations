"""Maximum Product of Three Numbers."""

from typing import List
import unittest


def maximumProduct(nums: List[int]) -> int:
    """Find the maximum product of three numbers in the array.

    Args:
        nums: List of integers with length >= 3.

    Returns:
        Maximum product of any three numbers.
    """
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


class TestMaximumProduct(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(maximumProduct([1, 2, 3]), 6)

    def test_example2(self):
        self.assertEqual(maximumProduct([1, 2, 3, 4]), 24)

    def test_example3(self):
        self.assertEqual(maximumProduct([-1, -2, -3]), -6)

    def test_two_negatives_one_positive(self):
        self.assertEqual(maximumProduct([-100, -99, 1, 2, 3]), 29700)

    def test_all_zeros(self):
        self.assertEqual(maximumProduct([0, 0, 0, 0]), 0)

    def test_mixed_with_zero(self):
        self.assertEqual(maximumProduct([-1, 0, 1]), 0)

    def test_exactly_three(self):
        self.assertEqual(maximumProduct([5, 6, 7]), 210)

    def test_large_negatives_beat_positives(self):
        self.assertEqual(maximumProduct([-1000, -999, 1, 2, 3]), 2997000)

    def test_all_same(self):
        self.assertEqual(maximumProduct([2, 2, 2, 2]), 8)

    def test_negative_and_positive(self):
        self.assertEqual(maximumProduct([-4, -3, -2, -1, 5]), 60)


if __name__ == "__main__":
    unittest.main()
