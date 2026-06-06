import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution

import unittest


class TestDigitSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.digitSum("11111222223", 3), "135")

    def test_example2(self):
        self.assertEqual(self.sol.digitSum("00000000", 3), "000")

    def test_no_rounds_needed(self):
        self.assertEqual(self.sol.digitSum("123", 3), "123")
        self.assertEqual(self.sol.digitSum("12", 5), "12")

    def test_single_character(self):
        self.assertEqual(self.sol.digitSum("5", 2), "5")

    def test_length_equals_k(self):
        self.assertEqual(self.sol.digitSum("99", 2), "99")

    def test_large_digits(self):
        self.assertEqual(self.sol.digitSum("9999", 2), "99")

    def test_k_equals_2(self):
        self.assertEqual(self.sol.digitSum("1234", 2), "37")

    def test_all_ones(self):
        # "111111" k=3 -> "333" (len==k, done)
        self.assertEqual(self.sol.digitSum("111111", 3), "33")


if __name__ == "__main__":
    unittest.main()
