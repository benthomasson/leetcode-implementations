"""Convert a Number to Hexadecimal - LeetCode"""

import unittest


def to_hex(num: int) -> str:
    """Convert integer to hexadecimal string using two's complement for negatives.

    Args:
        num: Integer in range [-2^31, 2^31 - 1].

    Returns:
        Lowercase hexadecimal string without leading zeros.
    """
    if num == 0:
        return "0"

    hex_chars = "0123456789abcdef"
    num &= 0xFFFFFFFF
    result = []
    while num > 0:
        result.append(hex_chars[num & 0xF])
        num >>= 4
    return "".join(reversed(result))


class TestToHex(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(to_hex(0), "0")

    def test_positive(self):
        self.assertEqual(to_hex(26), "1a")

    def test_negative_one(self):
        self.assertEqual(to_hex(-1), "ffffffff")

    def test_one(self):
        self.assertEqual(to_hex(1), "1")

    def test_fifteen(self):
        self.assertEqual(to_hex(15), "f")

    def test_sixteen(self):
        self.assertEqual(to_hex(16), "10")

    def test_int_max(self):
        self.assertEqual(to_hex(2**31 - 1), "7fffffff")

    def test_int_min(self):
        self.assertEqual(to_hex(-(2**31)), "80000000")


if __name__ == "__main__":
    unittest.main()
