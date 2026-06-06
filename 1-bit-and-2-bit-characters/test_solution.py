"""Tests for 1-bit and 2-bit Characters."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import is_one_bit_character


class TestIsOneBitCharacter(unittest.TestCase):

    # Problem examples
    def test_example1(self):
        self.assertTrue(is_one_bit_character([1, 0, 0]))

    def test_example2(self):
        self.assertFalse(is_one_bit_character([1, 1, 1, 0]))

    # Edge cases
    def test_single_zero(self):
        self.assertTrue(is_one_bit_character([0]))

    def test_two_bit_10(self):
        self.assertFalse(is_one_bit_character([1, 0]))

    def test_two_zeros(self):
        self.assertTrue(is_one_bit_character([0, 0]))

    def test_11_then_0(self):
        self.assertTrue(is_one_bit_character([1, 1, 0]))

    # Longer patterns
    def test_all_zeros(self):
        self.assertTrue(is_one_bit_character([0, 0, 0, 0, 0]))

    def test_mixed_pattern(self):
        # 10 | 11 | 10 | 0 -> last is 1-bit
        self.assertTrue(is_one_bit_character([1, 0, 1, 1, 1, 0, 0]))

    def test_ends_as_two_bit(self):
        # 10 | 10 -> last is 2-bit
        self.assertFalse(is_one_bit_character([1, 0, 1, 0]))

    def test_large_input(self):
        # 500 pairs of "10" + trailing "0" = 1001 elements, last is 1-bit
        bits = [1, 0] * 500 + [0]
        self.assertTrue(is_one_bit_character(bits))


if __name__ == "__main__":
    unittest.main()
