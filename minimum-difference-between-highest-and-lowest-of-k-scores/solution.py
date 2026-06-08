"""Minimum Difference Between Highest and Lowest of K Scores."""

from typing import List


def max_distance(nums: List[int], k: int) -> int:
    """Return min difference between highest and lowest of k picked scores.

    Args:
        nums: List of student scores.
        k: Number of students to pick.

    Returns:
        Minimum possible difference between highest and lowest of k scores.
    """
    nums = sorted(nums)
    return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))


import unittest


class TestMaxDistance(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(max_distance([90], 1), 0)

    def test_example2(self):
        self.assertEqual(max_distance([9, 4, 1, 7], 2), 2)

    def test_k_equals_length(self):
        self.assertEqual(max_distance([9, 4, 1, 7], 4), 8)

    def test_k_equals_one(self):
        self.assertEqual(max_distance([5, 3, 8, 1], 1), 0)

    def test_all_identical(self):
        self.assertEqual(max_distance([5, 5, 5, 5], 3), 0)

    def test_sorted_input(self):
        self.assertEqual(max_distance([1, 2, 3, 4, 5], 3), 2)

    def test_large_spread(self):
        self.assertEqual(max_distance([0, 100000], 2), 100000)

    def test_two_elements_k2(self):
        self.assertEqual(max_distance([1, 3], 2), 2)


if __name__ == "__main__":
    unittest.main()
