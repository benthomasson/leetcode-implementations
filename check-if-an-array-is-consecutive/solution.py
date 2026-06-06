"""Check if an array is consecutive."""

from typing import List


class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        """Check if nums contains every number in [min, min + n - 1].

        Args:
            nums: List of integers to check.

        Returns:
            True if the array is consecutive, False otherwise.
        """
        n = len(nums)
        num_set = set(nums)
        if len(num_set) != n:
            return False
        return max(nums) - min(nums) + 1 == n


import unittest


class TestIsConsecutive(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertTrue(self.s.isConsecutive([1, 3, 4, 2]))

    def test_example2(self):
        self.assertFalse(self.s.isConsecutive([1, 3]))

    def test_example3(self):
        self.assertTrue(self.s.isConsecutive([3, 5, 4]))

    def test_single_element(self):
        self.assertTrue(self.s.isConsecutive([0]))
        self.assertTrue(self.s.isConsecutive([100000]))

    def test_duplicates(self):
        self.assertFalse(self.s.isConsecutive([1, 1, 2, 3]))

    def test_two_consecutive(self):
        self.assertTrue(self.s.isConsecutive([5, 6]))

    def test_starting_at_zero(self):
        self.assertTrue(self.s.isConsecutive([0, 1, 2, 3]))

    def test_gap_in_middle(self):
        self.assertFalse(self.s.isConsecutive([1, 2, 4, 5]))


if __name__ == "__main__":
    unittest.main()
