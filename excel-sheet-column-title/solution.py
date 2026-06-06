"""Excel Sheet Column Title - LeetCode Solution."""

import unittest


def convert_to_title(columnNumber: int) -> str:
    """Convert column number to Excel column title (1-indexed base-26).

    Args:
        columnNumber: Integer between 1 and 2^31 - 1.

    Returns:
        Excel column title string (e.g., 1 -> "A", 28 -> "AB").
    """
    result = []
    while columnNumber > 0:
        columnNumber -= 1
        result.append(chr(columnNumber % 26 + ord('A')))
        columnNumber //= 26
    return ''.join(reversed(result))


class TestConvertToTitle(unittest.TestCase):

    def test_single_letters(self):
        self.assertEqual(convert_to_title(1), "A")
        self.assertEqual(convert_to_title(26), "Z")

    def test_two_letters(self):
        self.assertEqual(convert_to_title(27), "AA")
        self.assertEqual(convert_to_title(28), "AB")
        self.assertEqual(convert_to_title(701), "ZY")
        self.assertEqual(convert_to_title(702), "ZZ")

    def test_three_letters(self):
        self.assertEqual(convert_to_title(703), "AAA")

    def test_large_value(self):
        self.assertEqual(convert_to_title(2147483647), "FXSHRXW")


if __name__ == "__main__":
    unittest.main()
