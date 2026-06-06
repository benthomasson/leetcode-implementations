"""Tests for maximum69Number."""

import unittest
from solution import maximum69Number


class TestMaximum69Number(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(maximum69Number(9669), 9969)

    def test_example2(self):
        self.assertEqual(maximum69Number(9996), 9999)

    def test_example3_all_nines(self):
        self.assertEqual(maximum69Number(9999), 9999)

    def test_single_digit_six(self):
        self.assertEqual(maximum69Number(6), 9)

    def test_single_digit_nine(self):
        self.assertEqual(maximum69Number(9), 9)

    def test_all_sixes(self):
        self.assertEqual(maximum69Number(6666), 9666)

    def test_leading_six(self):
        self.assertEqual(maximum69Number(6999), 9999)

    def test_trailing_six(self):
        self.assertEqual(maximum69Number(9996), 9999)


if __name__ == "__main__":
    unittest.main()
