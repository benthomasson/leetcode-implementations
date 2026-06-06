import unittest
from solution import Solution


class TestReverseVowels(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.reverseVowels("hello"), "holle")

    def test_example2(self):
        self.assertEqual(self.sol.reverseVowels("leetcode"), "leotcede")

    def test_no_vowels(self):
        self.assertEqual(self.sol.reverseVowels("bcdfg"), "bcdfg")

    def test_all_vowels(self):
        self.assertEqual(self.sol.reverseVowels("aeiou"), "uoiea")

    def test_single_char(self):
        self.assertEqual(self.sol.reverseVowels("a"), "a")
        self.assertEqual(self.sol.reverseVowels("b"), "b")

    def test_mixed_case_vowels(self):
        self.assertEqual(self.sol.reverseVowels("aA"), "Aa")

    def test_spaces_and_punctuation(self):
        self.assertEqual(self.sol.reverseVowels("hello world!"), "hollo werld!")

    def test_long_string(self):
        s = "a" * 300000
        self.assertEqual(self.sol.reverseVowels(s), s)

    def test_uppercase_vowels(self):
        self.assertEqual(self.sol.reverseVowels("HELLO"), "HOLLE")


if __name__ == "__main__":
    unittest.main()
