"""Tests for Valid Palindrome solution."""

import unittest
from solution import Solution


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        assert self.sol.isPalindrome("A man, a plan, a canal: Panama") is True

    def test_example2(self):
        assert self.sol.isPalindrome("race a car") is False

    def test_example3_empty(self):
        assert self.sol.isPalindrome(" ") is True

    def test_single_char(self):
        assert self.sol.isPalindrome("a") is True

    def test_non_alpha_only(self):
        assert self.sol.isPalindrome(",.!@#") is True

    def test_mixed_case(self):
        assert self.sol.isPalindrome("Aa") is True

    def test_numeric_palindrome(self):
        assert self.sol.isPalindrome("12321") is True

    def test_numeric_non_palindrome(self):
        assert self.sol.isPalindrome("12345") is False

    def test_alphanumeric_mix(self):
        assert self.sol.isPalindrome("0P") is False


if __name__ == "__main__":
    unittest.main()
