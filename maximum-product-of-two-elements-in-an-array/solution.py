"""Maximum Product of Two Elements in an Array."""

import unittest
from typing import List


def minSetSize(nums: List[int]) -> int:
    """Return max value of (nums[i]-1)*(nums[j]-1) for two different indices.

    Args:
        nums: Array of integers with length >= 2.

    Returns:
        Maximum product of two decremented elements.
    """
    max1 = max2 = 0
    for n in nums:
        if n >= max1:
            max2 = max1
            max1 = n
        elif n > max2:
            max2 = n
    return (max1 - 1) * (max2 - 1)


class TestMinSetSize(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(minSetSize([3, 4, 5, 2]), 12)

    def test_example2(self):
        self.assertEqual(minSetSize([1, 5, 4, 5]), 16)

    def test_example3(self):
        self.assertEqual(minSetSize([3, 7]), 12)

    def test_all_ones(self):
        self.assertEqual(minSetSize([1, 1, 1]), 0)

    def test_identical(self):
        self.assertEqual(minSetSize([5, 5, 5]), 16)

    def test_max_values(self):
        self.assertEqual(minSetSize([1000, 1000]), 999 * 999)

    def test_ascending(self):
        self.assertEqual(minSetSize([1, 2, 3, 4, 5]), 12)

    def test_descending(self):
        self.assertEqual(minSetSize([5, 4, 3, 2, 1]), 12)


if __name__ == "__main__":
    unittest.main()
