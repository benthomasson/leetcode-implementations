"""Tests for greatest_letter."""

import unittest
from solution import greatest_letter


class TestGetMaxOccurrences(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(greatest_letter("lEeTcOdE"), "E")

    def test_example2(self):
        self.assertEqual(greatest_letter("arRAzFif"), "R")

    def test_example3(self):
        self.assertEqual(greatest_letter("AbCdEfGhIjK"), "")

    def test_all_lowercase(self):
        self.assertEqual(greatest_letter("abcdef"), "")

    def test_all_uppercase(self):
        self.assertEqual(greatest_letter("ABCDEF"), "")

    def test_single_pair(self):
        self.assertEqual(greatest_letter("aA"), "A")

    def test_single_char(self):
        self.assertEqual(greatest_letter("a"), "")

    def test_z_pair(self):
        self.assertEqual(greatest_letter("zZ"), "Z")

    def test_multiple_pairs_returns_greatest(self):
        self.assertEqual(greatest_letter("aAbBcC"), "C")

    def test_all_26_pairs(self):
        s = "".join(c + c.upper() for c in "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(greatest_letter(s), "Z")


if __name__ == "__main__":
    unittest.main()
