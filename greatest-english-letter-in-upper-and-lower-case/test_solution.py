"""Tests for get_max_occurrences."""

import unittest
from solution import get_max_occurrences


class TestGetMaxOccurrences(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(get_max_occurrences("lEeTcOdE"), "E")

    def test_example2(self):
        self.assertEqual(get_max_occurrences("arRAzFif"), "R")

    def test_example3(self):
        self.assertEqual(get_max_occurrences("AbCdEfGhIjK"), "")

    def test_all_lowercase(self):
        self.assertEqual(get_max_occurrences("abcdef"), "")

    def test_all_uppercase(self):
        self.assertEqual(get_max_occurrences("ABCDEF"), "")

    def test_single_pair(self):
        self.assertEqual(get_max_occurrences("aA"), "A")

    def test_single_char(self):
        self.assertEqual(get_max_occurrences("a"), "")

    def test_z_pair(self):
        self.assertEqual(get_max_occurrences("zZ"), "Z")

    def test_multiple_pairs_returns_greatest(self):
        self.assertEqual(get_max_occurrences("aAbBcC"), "C")

    def test_all_26_pairs(self):
        s = "".join(c + c.upper() for c in "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(get_max_occurrences(s), "Z")


if __name__ == "__main__":
    unittest.main()
