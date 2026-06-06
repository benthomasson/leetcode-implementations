"""Check if Array is Sorted and Rotated."""

from typing import List
import unittest


class Solution:
    def check(self, nums: List[int]) -> bool:
        """Return True if nums is a sorted array rotated by some positions.

        Args:
            nums: List of integers.

        Returns:
            True if the array is sorted and rotated, False otherwise.
        """
        n = len(nums)
        breaks = sum(nums[i] > nums[(i + 1) % n] for i in range(n))
        return breaks <= 1


class TestCheck(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_rotated(self):
        self.assertTrue(self.s.check([3, 4, 5, 1, 2]))

    def test_not_sorted(self):
        self.assertFalse(self.s.check([2, 1, 3, 4]))

    def test_already_sorted(self):
        self.assertTrue(self.s.check([1, 2, 3]))

    def test_single_element(self):
        self.assertTrue(self.s.check([1]))

    def test_all_equal(self):
        self.assertTrue(self.s.check([2, 2, 2]))

    def test_two_sorted(self):
        self.assertTrue(self.s.check([1, 2]))

    def test_two_rotated(self):
        self.assertTrue(self.s.check([2, 1]))

    def test_duplicates_at_break(self):
        self.assertTrue(self.s.check([2, 2, 1, 2]))

    def test_multiple_breaks(self):
        self.assertFalse(self.s.check([3, 1, 2, 1]))


if __name__ == "__main__":
    unittest.main()
