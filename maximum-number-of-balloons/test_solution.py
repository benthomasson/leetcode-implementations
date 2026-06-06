"""Tests for Maximum Number of Balloons."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import max_number_of_balloons


class TestMaxNumberOfBalloons(unittest.TestCase):
    # --- LeetCode examples ---
    def test_example1(self):
        self.assertEqual(max_number_of_balloons("nlaebolko"), 1)

    def test_example2(self):
        self.assertEqual(max_number_of_balloons("loonbalxballpoon"), 2)

    def test_example3(self):
        self.assertEqual(max_number_of_balloons("leetcode"), 0)

    # --- Edge cases ---
    def test_empty_string(self):
        self.assertEqual(max_number_of_balloons(""), 0)

    def test_exact_balloon(self):
        self.assertEqual(max_number_of_balloons("balloon"), 1)

    def test_no_matching_chars(self):
        self.assertEqual(max_number_of_balloons("zzzzz"), 0)

    def test_missing_double_l(self):
        # Only one 'l' — need two for "balloon"
        self.assertEqual(max_number_of_balloons("balon"), 0)

    def test_multiple_instances(self):
        self.assertEqual(max_number_of_balloons("balloonballoon"), 2)

    def test_large_input(self):
        # 10 copies of "balloon" mixed with noise
        self.assertEqual(max_number_of_balloons("balloon" * 10 + "x" * 100), 10)

    def test_single_char(self):
        self.assertEqual(max_number_of_balloons("b"), 0)


if __name__ == "__main__":
    unittest.main()
