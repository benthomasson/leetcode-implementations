"""Minimum Subsequence in Non-Increasing Order."""

from typing import List


class Solution:
    def min_changes_to_divide_string(self, nums: List[int]) -> List[int]:
        """Return the minimum subsequence whose sum exceeds the remaining elements.

        Args:
            nums: Array of positive integers.

        Returns:
            Subsequence in non-increasing order with sum strictly greater
            than the sum of excluded elements.
        """
        total = sum(nums)
        nums.sort(reverse=True)
        result = []
        subseq_sum = 0
        for num in nums:
            subseq_sum += num
            result.append(num)
            if subseq_sum > total - subseq_sum:
                break
        return result


# --- Tests ---
import unittest


class TestMinSubsequence(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.min_changes_to_divide_string([4, 3, 10, 9, 8]), [10, 9])

    def test_example2(self):
        self.assertEqual(self.s.min_changes_to_divide_string([4, 4, 7, 6, 7]), [7, 7, 6])

    def test_single_element(self):
        self.assertEqual(self.s.min_changes_to_divide_string([5]), [5])

    def test_all_equal(self):
        self.assertEqual(self.s.min_changes_to_divide_string([3, 3, 3]), [3, 3])

    def test_two_elements(self):
        self.assertEqual(self.s.min_changes_to_divide_string([1, 2]), [2])

    def test_already_sorted_desc(self):
        self.assertEqual(self.s.min_changes_to_divide_string([10, 5, 1]), [10])


if __name__ == "__main__":
    unittest.main()
