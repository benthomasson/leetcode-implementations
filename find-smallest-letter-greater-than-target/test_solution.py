"""Tests for Find Smallest Letter Greater Than Target (LeetCode 744)."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestNextGreatestLetter(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # --- Problem examples ---
    def test_example1(self):
        self.assertEqual(self.s.nextGreatestLetter(["c", "f", "j"], "a"), "c")

    def test_example2(self):
        self.assertEqual(self.s.nextGreatestLetter(["c", "f", "j"], "c"), "f")

    def test_example3_wrap_around(self):
        self.assertEqual(self.s.nextGreatestLetter(["x", "x", "y", "y"], "z"), "x")

    # --- Edge cases ---
    def test_target_less_than_all(self):
        self.assertEqual(self.s.nextGreatestLetter(["b", "d"], "a"), "b")

    def test_target_greater_than_all(self):
        self.assertEqual(self.s.nextGreatestLetter(["a", "b"], "z"), "a")

    def test_target_equals_last_wraps(self):
        self.assertEqual(self.s.nextGreatestLetter(["a", "b"], "b"), "a")

    def test_duplicates_skipped(self):
        self.assertEqual(self.s.nextGreatestLetter(["a", "a", "b", "b"], "a"), "b")

    def test_two_element_minimum(self):
        self.assertEqual(self.s.nextGreatestLetter(["a", "z"], "m"), "z")

    def test_all_same_except_one(self):
        self.assertEqual(self.s.nextGreatestLetter(["a", "a", "a", "b"], "a"), "b")

    def test_target_between_letters(self):
        self.assertEqual(self.s.nextGreatestLetter(["c", "f", "j"], "d"), "f")


if __name__ == "__main__":
    unittest.main()
