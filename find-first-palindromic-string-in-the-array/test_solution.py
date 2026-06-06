import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution, minimizeTheDifference


class TestFirstPalindrome(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]), "ada")

    def test_example2(self):
        self.assertEqual(self.s.firstPalindrome(["notapalindrome", "racecar"]), "racecar")

    def test_example3(self):
        self.assertEqual(self.s.firstPalindrome(["def", "ghi"]), "")

    def test_single_palindrome(self):
        self.assertEqual(self.s.firstPalindrome(["aba"]), "aba")

    def test_single_non_palindrome(self):
        self.assertEqual(self.s.firstPalindrome(["ab"]), "")

    def test_single_char(self):
        self.assertEqual(self.s.firstPalindrome(["a"]), "a")

    def test_all_palindromes(self):
        self.assertEqual(self.s.firstPalindrome(["aa", "bb", "cc"]), "aa")

    def test_even_length_palindrome(self):
        self.assertEqual(self.s.firstPalindrome(["abba", "xyz"]), "abba")

    def test_wrapper(self):
        self.assertEqual(minimizeTheDifference(["abc", "aba"]), "aba")

    def test_palindrome_at_end(self):
        self.assertEqual(self.s.firstPalindrome(["abc", "def", "ghi", "aba"]), "aba")


if __name__ == "__main__":
    unittest.main()
