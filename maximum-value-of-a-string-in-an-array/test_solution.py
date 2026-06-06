import unittest
from solution import Solution


class TestMaxValue(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.maxValue(["alic3", "bob", "3", "4", "00000"]), 5)

    def test_example2(self):
        self.assertEqual(self.s.maxValue(["1", "01", "001", "0001"]), 1)

    def test_single_digit_string(self):
        self.assertEqual(self.s.maxValue(["9"]), 9)

    def test_single_alpha_string(self):
        self.assertEqual(self.s.maxValue(["abc"]), 3)

    def test_leading_zeros(self):
        self.assertEqual(self.s.maxValue(["000"]), 0)

    def test_large_digit_string(self):
        self.assertEqual(self.s.maxValue(["999999999"]), 999999999)

    def test_mixed(self):
        self.assertEqual(self.s.maxValue(["a1b2c3", "123"]), 123)

    def test_all_letters(self):
        self.assertEqual(self.s.maxValue(["abcdefghi", "ab"]), 9)


if __name__ == "__main__":
    unittest.main()
