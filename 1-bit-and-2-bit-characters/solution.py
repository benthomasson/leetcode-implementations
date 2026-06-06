"""1-bit and 2-bit Characters."""

import unittest


def is_one_bit_character(bits: list[int]) -> bool:
    """Determine if the last character in bits must be a one-bit character.

    Args:
        bits: Binary array ending with 0.

    Returns:
        True if the last character must be a one-bit character.
    """
    i = 0
    while i < len(bits) - 1:
        i += 2 if bits[i] == 1 else 1
    return i == len(bits) - 1


class TestIsOneBitCharacter(unittest.TestCase):

    def test_single_zero(self):
        self.assertTrue(is_one_bit_character([0]))

    def test_example1(self):
        self.assertTrue(is_one_bit_character([1, 0, 0]))

    def test_example2(self):
        self.assertFalse(is_one_bit_character([1, 1, 1, 0]))

    def test_two_bit_then_end(self):
        self.assertFalse(is_one_bit_character([1, 0]))

    def test_two_zeros(self):
        self.assertTrue(is_one_bit_character([0, 0]))

    def test_11_then_0(self):
        self.assertTrue(is_one_bit_character([1, 1, 0]))

    def test_all_zeros(self):
        self.assertTrue(is_one_bit_character([0, 0, 0, 0, 0]))

    def test_long_pattern(self):
        self.assertTrue(is_one_bit_character([1, 0, 1, 1, 1, 0, 0]))

    def test_alternating_10(self):
        self.assertFalse(is_one_bit_character([1, 0, 1, 0]))


if __name__ == "__main__":
    unittest.main()
