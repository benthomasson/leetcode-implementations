"""Hexspeak - LeetCode Problem"""

import unittest


def to_hexspeak(num: str) -> str:
    """Convert decimal string to Hexspeak representation.

    Args:
        num: Decimal integer as a string.

    Returns:
        Hexspeak string if valid, otherwise "ERROR".
    """
    hex_str = hex(int(num))[2:].upper()
    result = hex_str.replace("0", "O").replace("1", "I")
    valid = set("ABCDEFIO")
    if all(c in valid for c in result):
        return result
    return "ERROR"


class TestToHexspeak(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(to_hexspeak("257"), "IOI")

    def test_example_2(self):
        self.assertEqual(to_hexspeak("3"), "ERROR")

    def test_one(self):
        self.assertEqual(to_hexspeak("1"), "I")

    def test_zero_hex(self):
        # 256 = 0x100 -> IOO
        self.assertEqual(to_hexspeak("256"), "IOO")

    def test_pure_letter_hex(self):
        # 171 = 0xAB -> AB
        self.assertEqual(to_hexspeak("171"), "AB")

    def test_invalid_digit(self):
        # 2 = 0x2 -> "2" -> ERROR
        self.assertEqual(to_hexspeak("2"), "ERROR")

    def test_large_value(self):
        # 1000000000000 = 0xE8D4A51000
        # -> E8D4A5IOOO -> has digits 8,4,5 -> ERROR
        self.assertEqual(to_hexspeak("1000000000000"), "ERROR")

    def test_all_valid_chars(self):
        # 0xDEADBEEF = 3735928559
        # D E A D B E E F -> all valid letters
        self.assertEqual(to_hexspeak("3735928559"), "DEADBEEF")

    def test_contains_nine(self):
        # 9 = 0x9 -> ERROR
        self.assertEqual(to_hexspeak("9"), "ERROR")

    def test_hex_with_mixed(self):
        # 255 = 0xFF -> FF
        self.assertEqual(to_hexspeak("255"), "FF")

    def test_sixteen(self):
        # 16 = 0x10 -> IO
        self.assertEqual(to_hexspeak("16"), "IO")


if __name__ == "__main__":
    unittest.main()
