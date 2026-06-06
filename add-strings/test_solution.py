"""Tests for Add Strings solution."""
import unittest
from solution import Solution


class TestAddStrings(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.addStrings("11", "123"), "134")

    def test_example2(self):
        self.assertEqual(self.s.addStrings("456", "77"), "533")

    def test_example3(self):
        self.assertEqual(self.s.addStrings("0", "0"), "0")

    def test_carry_propagation(self):
        self.assertEqual(self.s.addStrings("999", "1"), "1000")

    def test_single_digits(self):
        self.assertEqual(self.s.addStrings("5", "3"), "8")

    def test_single_digit_with_carry(self):
        self.assertEqual(self.s.addStrings("9", "9"), "18")

    def test_unequal_lengths(self):
        self.assertEqual(self.s.addStrings("1", "9999"), "10000")

    def test_zero_plus_number(self):
        self.assertEqual(self.s.addStrings("0", "12345"), "12345")

    def test_large_numbers(self):
        a = "9" * 10000
        b = "1"
        result = self.s.addStrings(a, b)
        self.assertEqual(result, "1" + "0" * 10000)


if __name__ == "__main__":
    unittest.main()
