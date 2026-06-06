"""Tests for count_binary_substrings."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import count_binary_substrings


class TestCountBinarySubstrings(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(count_binary_substrings("00110011"), 6)

    def test_example2(self):
        self.assertEqual(count_binary_substrings("10101"), 4)

    def test_single_char(self):
        self.assertEqual(count_binary_substrings("0"), 0)
        self.assertEqual(count_binary_substrings("1"), 0)

    def test_all_same(self):
        self.assertEqual(count_binary_substrings("0000"), 0)
        self.assertEqual(count_binary_substrings("1111"), 0)

    def test_two_chars(self):
        self.assertEqual(count_binary_substrings("01"), 1)
        self.assertEqual(count_binary_substrings("10"), 1)

    def test_alternating(self):
        self.assertEqual(count_binary_substrings("010101"), 5)

    def test_equal_runs(self):
        self.assertEqual(count_binary_substrings("000111"), 3)

    def test_unequal_runs(self):
        self.assertEqual(count_binary_substrings("00011"), 2)
        self.assertEqual(count_binary_substrings("00111"), 2)

    def test_long_string(self):
        # Large input: 50000 zeros followed by 50000 ones
        s = "0" * 50000 + "1" * 50000
        self.assertEqual(count_binary_substrings(s), 50000)


if __name__ == "__main__":
    unittest.main()
