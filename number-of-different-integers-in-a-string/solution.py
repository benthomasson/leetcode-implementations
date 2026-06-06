"""Number of Different Integers in a String."""
import re
import unittest


def min_moves(word: str) -> int:
    """Count distinct integers in a string after replacing letters with spaces.

    Args:
        word: String of digits and lowercase English letters.

    Returns:
        Number of different integers found.
    """
    nums = re.sub(r'[a-z]', ' ', word).split()
    return len({n.lstrip('0') or '0' for n in nums})


class TestMinMoves(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(min_moves("a123bc34d8ef34"), 3)

    def test_example2(self):
        self.assertEqual(min_moves("leet1234code234"), 2)

    def test_example3(self):
        self.assertEqual(min_moves("a1b01c001"), 1)

    def test_all_letters(self):
        self.assertEqual(min_moves("abc"), 0)

    def test_all_digits(self):
        self.assertEqual(min_moves("12345"), 1)

    def test_single_zero(self):
        self.assertEqual(min_moves("0"), 1)

    def test_multiple_zeros(self):
        self.assertEqual(min_moves("0a0b0"), 1)

    def test_adjacent_single_digits(self):
        self.assertEqual(min_moves("a1b2c3"), 3)

    def test_leading_zeros(self):
        self.assertEqual(min_moves("a000123b"), 1)


if __name__ == "__main__":
    unittest.main()
