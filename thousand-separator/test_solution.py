import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution

import unittest

class TestThousandSeparator(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1_no_separator(self):
        self.assertEqual(self.sol.thousand_separator(987), "987")

    def test_example2_one_separator(self):
        self.assertEqual(self.sol.thousand_separator(1234), "1.234")

    def test_zero(self):
        self.assertEqual(self.sol.thousand_separator(0), "0")

    def test_single_digit(self):
        self.assertEqual(self.sol.thousand_separator(5), "5")

    def test_exactly_three_digits(self):
        self.assertEqual(self.sol.thousand_separator(100), "100")

    def test_six_digits(self):
        self.assertEqual(self.sol.thousand_separator(123456), "123.456")

    def test_nine_digits(self):
        self.assertEqual(self.sol.thousand_separator(123456789), "123.456.789")

    def test_max_constraint(self):
        self.assertEqual(self.sol.thousand_separator(2**31 - 1), "2.147.483.647")

    def test_one_thousand(self):
        self.assertEqual(self.sol.thousand_separator(1000), "1.000")

if __name__ == "__main__":
    unittest.main()
