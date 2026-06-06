"""Tests for Excel Sheet Column Title solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import convert_to_title


class TestConvertToTitle(unittest.TestCase):
    """Test cases for convert_to_title."""

    def test_example_1(self):
        self.assertEqual(convert_to_title(1), "A")

    def test_example_2(self):
        self.assertEqual(convert_to_title(28), "AB")

    def test_example_3(self):
        self.assertEqual(convert_to_title(701), "ZY")

    def test_boundary_z(self):
        self.assertEqual(convert_to_title(26), "Z")

    def test_two_letter_start(self):
        self.assertEqual(convert_to_title(27), "AA")

    def test_two_letter_end(self):
        self.assertEqual(convert_to_title(702), "ZZ")

    def test_three_letter_start(self):
        self.assertEqual(convert_to_title(703), "AAA")

    def test_mid_alphabet(self):
        self.assertEqual(convert_to_title(14), "N")

    def test_max_constraint(self):
        self.assertEqual(convert_to_title(2147483647), "FXSHRXW")


if __name__ == "__main__":
    unittest.main()
