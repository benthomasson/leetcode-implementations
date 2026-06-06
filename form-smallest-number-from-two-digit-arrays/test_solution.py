"""Tests for Form Smallest Number From Two Digit Arrays."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import smallest_number_with_at_least_one_digit_from_each_array

f = smallest_number_with_at_least_one_digit_from_each_array


class TestSmallestNumber(unittest.TestCase):
    # LeetCode examples
    def test_example1_no_common(self):
        self.assertEqual(f([4, 1, 3], [5, 7]), 15)

    def test_example2_common_digit(self):
        self.assertEqual(f([3, 5, 2, 6], [3, 1, 7]), 3)

    # Edge: single element arrays
    def test_single_common(self):
        self.assertEqual(f([5], [5]), 5)

    def test_single_no_common(self):
        self.assertEqual(f([9], [1]), 19)

    # Ordering: smaller min in second array forms correct two-digit number
    def test_smaller_in_second_array(self):
        self.assertEqual(f([5, 8], [3, 7]), 35)

    # Multiple common digits returns smallest
    def test_multiple_common(self):
        self.assertEqual(f([7, 3, 5], [5, 3, 9]), 3)

    # All digits shared
    def test_all_shared(self):
        self.assertEqual(f([1, 2, 3], [3, 2, 1]), 1)

    # Same minimums but no common digit
    def test_same_min_no_common(self):
        self.assertEqual(f([1, 4], [2, 5]), 12)

    # Max possible values
    def test_large_two_digit(self):
        self.assertEqual(f([8], [9]), 89)


if __name__ == "__main__":
    unittest.main()
