"""Tests for reformat phone number."""
import sys
import unittest

sys.path.insert(0, '../implementer')
from solution import Solution, reformat_number


class TestReformatNumber(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # LeetCode examples
    def test_example1(self):
        self.assertEqual(self.s.reformatNumber("1-23-45 6"), "123-456")

    def test_example2(self):
        self.assertEqual(self.s.reformatNumber("123 4-567"), "123-45-67")

    def test_example3(self):
        self.assertEqual(self.s.reformatNumber("123 4-5678"), "123-456-78")

    # Edge cases: small digit counts
    def test_two_digits(self):
        self.assertEqual(self.s.reformatNumber("1-2"), "12")

    def test_three_digits(self):
        self.assertEqual(self.s.reformatNumber("1 2 3"), "123")

    def test_four_digits(self):
        self.assertEqual(self.s.reformatNumber("1234"), "12-34")

    # Tail handling: 5 digits -> 3 + 2
    def test_five_digits(self):
        self.assertEqual(self.s.reformatNumber("12345"), "123-45")

    # Longer input: 12 digits -> all blocks of 3
    def test_long_input(self):
        self.assertEqual(self.s.reformatNumber("1-2-3-4-5-6-7-8-9-0-1-2"), "123-456-789-012")

    # 7 digits -> 3 + 2 + 2 (tail=4 splits into two 2s)
    def test_seven_digits(self):
        self.assertEqual(self.s.reformatNumber("1234567"), "123-45-67")

    # reformat_number alias works
    def test_alias(self):
        self.assertEqual(reformat_number("1-23-45 6"), "123-456")


if __name__ == "__main__":
    unittest.main()
