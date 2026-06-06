import unittest
from solution import to_hexspeak


class TestToHexspeak(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(to_hexspeak("257"), "IOI")

    def test_example_2(self):
        self.assertEqual(to_hexspeak("3"), "ERROR")

    def test_one(self):
        self.assertEqual(to_hexspeak("1"), "I")

    def test_zero(self):
        self.assertEqual(to_hexspeak("256"), "IOO")

    def test_pure_letters(self):
        self.assertEqual(to_hexspeak("171"), "AB")
        self.assertEqual(to_hexspeak("255"), "FF")
        self.assertEqual(to_hexspeak("3735928559"), "DEADBEEF")

    def test_invalid_digits(self):
        self.assertEqual(to_hexspeak("2"), "ERROR")
        self.assertEqual(to_hexspeak("9"), "ERROR")
        self.assertEqual(to_hexspeak("100"), "ERROR")

    def test_sixteen(self):
        self.assertEqual(to_hexspeak("16"), "IO")

    def test_large_invalid(self):
        self.assertEqual(to_hexspeak("1000000000000"), "ERROR")

    def test_boundary_all_zeros_and_ones(self):
        self.assertEqual(to_hexspeak("273"), "III")
        self.assertEqual(to_hexspeak("17"), "II")

    def test_mixed_valid(self):
        self.assertEqual(to_hexspeak("2989"), "BAD")
        self.assertEqual(to_hexspeak("64206"), "FACE")


if __name__ == "__main__":
    unittest.main()
