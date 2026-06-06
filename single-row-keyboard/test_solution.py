"""Tests for Single Row Keyboard solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import calculate_time


class TestCalculateTime(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(calculate_time("abcdefghijklmnopqrstuvwxyz", "cba"), 4)

    def test_example2(self):
        self.assertEqual(calculate_time("pqrstuvwxyzabcdefghijklmno", "leetcode"), 73)

    def test_single_char_at_start(self):
        self.assertEqual(calculate_time("abcdefghijklmnopqrstuvwxyz", "a"), 0)

    def test_single_char_at_end(self):
        self.assertEqual(calculate_time("abcdefghijklmnopqrstuvwxyz", "z"), 25)

    def test_repeated_same_char(self):
        self.assertEqual(calculate_time("abcdefghijklmnopqrstuvwxyz", "aaa"), 0)

    def test_worst_case_alternating(self):
        self.assertEqual(calculate_time("abcdefghijklmnopqrstuvwxyz", "azaz"), 75)

    def test_sequential_alphabet(self):
        kb = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(calculate_time(kb, kb), 25)

    def test_reversed_keyboard(self):
        kb = "zyxwvutsrqponmlkjihgfedcba"
        # z=0, a=25. Word "az": |0-25|=25, then |25-0|=25 -> 50
        self.assertEqual(calculate_time(kb, "az"), 50)

    def test_adjacent_chars(self):
        self.assertEqual(calculate_time("abcdefghijklmnopqrstuvwxyz", "ab"), 1)


if __name__ == "__main__":
    unittest.main()
