"""Tests for Finding 3-Digit Even Numbers."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution


class TestFinding3DigitEvenNumbers(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- LeetCode examples ---

    def test_example1(self):
        self.assertEqual(
            self.s.findThreeDigitEvenNumbers([2, 1, 3, 0]),
            [102, 120, 130, 132, 210, 230, 302, 310, 312, 320],
        )

    def test_example2(self):
        self.assertEqual(
            self.s.findThreeDigitEvenNumbers([2, 2, 8, 8, 2]),
            [222, 228, 282, 288, 822, 828, 882],
        )

    def test_example3_all_odd(self):
        self.assertEqual(self.s.findThreeDigitEvenNumbers([3, 7, 5]), [])

    # --- Edge cases ---

    def test_all_zeros(self):
        """All zeros can't form a 3-digit number (leading zero)."""
        self.assertEqual(self.s.findThreeDigitEvenNumbers([0, 0, 0]), [])

    def test_single_repeated_even_digit(self):
        self.assertEqual(self.s.findThreeDigitEvenNumbers([2, 2, 2]), [222])

    def test_result_is_sorted(self):
        result = self.s.findThreeDigitEvenNumbers([1, 0, 2])
        self.assertEqual(result, sorted(result))
        self.assertEqual(result, [102, 120, 210])

    def test_no_duplicates_in_output(self):
        """Many repeated digits should not produce duplicate results."""
        result = self.s.findThreeDigitEvenNumbers([4, 4, 4, 4, 4])
        self.assertEqual(result, [444])
        self.assertEqual(len(result), len(set(result)))

    def test_all_digits_present(self):
        """With digits 0-9, many results but all must be 3-digit and even."""
        result = self.s.findThreeDigitEvenNumbers(list(range(10)))
        self.assertTrue(all(100 <= n <= 998 for n in result))
        self.assertTrue(all(n % 2 == 0 for n in result))

    def test_digit_frequency_respected(self):
        """[1, 1, 0] has only two 1s, so 110 is valid but 111 is not."""
        result = self.s.findThreeDigitEvenNumbers([1, 1, 0])
        self.assertIn(110, result)
        self.assertNotIn(111, result)


if __name__ == "__main__":
    unittest.main()
