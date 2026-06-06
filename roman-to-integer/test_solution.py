"""Tests for roman_to_int."""

import unittest
from solution import roman_to_int


class TestRomanToInt(unittest.TestCase):

    def test_single_characters(self):
        assert roman_to_int("I") == 1
        assert roman_to_int("V") == 5
        assert roman_to_int("X") == 10
        assert roman_to_int("L") == 50
        assert roman_to_int("C") == 100
        assert roman_to_int("D") == 500
        assert roman_to_int("M") == 1000

    def test_additive(self):
        assert roman_to_int("III") == 3
        assert roman_to_int("LVIII") == 58
        assert roman_to_int("XXVII") == 27

    def test_subtractive(self):
        assert roman_to_int("IV") == 4
        assert roman_to_int("IX") == 9
        assert roman_to_int("XL") == 40
        assert roman_to_int("XC") == 90
        assert roman_to_int("CD") == 400
        assert roman_to_int("CM") == 900

    def test_mixed(self):
        assert roman_to_int("MCMXCIV") == 1994

    def test_boundaries(self):
        assert roman_to_int("I") == 1
        assert roman_to_int("MMMCMXCIX") == 3999


if __name__ == "__main__":
    unittest.main()
