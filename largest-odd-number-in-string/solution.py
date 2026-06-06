"""Largest Odd Number in String."""

import unittest


def largest_odd_number(num: str) -> str:
    """Return the largest-valued odd integer that is a substring of num.

    Args:
        num: A string representing a large integer with no leading zeros.

    Returns:
        The largest odd substring, or "" if none exists.
    """
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[: i + 1]
    return ""


class TestLargestOddNumber(unittest.TestCase):
    def test_odd_at_start(self):
        self.assertEqual(largest_odd_number("52"), "5")

    def test_all_even(self):
        self.assertEqual(largest_odd_number("4206"), "")

    def test_last_digit_odd(self):
        self.assertEqual(largest_odd_number("35427"), "35427")

    def test_single_odd(self):
        self.assertEqual(largest_odd_number("5"), "5")

    def test_single_even(self):
        self.assertEqual(largest_odd_number("2"), "")

    def test_rightmost_odd_in_middle(self):
        self.assertEqual(largest_odd_number("1234"), "123")

    def test_all_odd(self):
        self.assertEqual(largest_odd_number("13579"), "13579")

    def test_long_even_string(self):
        self.assertEqual(largest_odd_number("2" * 100000), "")

    def test_odd_at_very_end(self):
        self.assertEqual(largest_odd_number("2" * 99999 + "1"), "2" * 99999 + "1")


if __name__ == "__main__":
    unittest.main()
