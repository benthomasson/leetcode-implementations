"""Check If Word Equals Summation of Two Words."""

import unittest


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        """Return True if numerical values of firstWord + secondWord equal targetWord.

        Args:
            firstWord: String of lowercase letters 'a'-'j'.
            secondWord: String of lowercase letters 'a'-'j'.
            targetWord: String of lowercase letters 'a'-'j'.

        Returns:
            True if sum of numerical values of first two words equals the target.
        """
        def word_to_num(word: str) -> int:
            return int("".join(str(ord(c) - ord("a")) for c in word))

        return word_to_num(firstWord) + word_to_num(secondWord) == word_to_num(targetWord)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertTrue(self.s.isSumEqual("acb", "cba", "cdb"))

    def test_example2(self):
        self.assertFalse(self.s.isSumEqual("aaa", "a", "aab"))

    def test_example3(self):
        self.assertTrue(self.s.isSumEqual("aaa", "a", "aaaa"))

    def test_single_chars(self):
        # b(1) + c(2) == d(3)? -> 1+2==3 -> True
        self.assertTrue(self.s.isSumEqual("b", "c", "d"))

    def test_single_chars_false(self):
        # a(0) + a(0) == b(1)? -> False
        self.assertFalse(self.s.isSumEqual("a", "a", "b"))

    def test_all_j(self):
        # j=9, "jj" -> 99, "jj" + "jj" = 99+99 = 198
        # 198 -> "b"(1) + "j"(9) + "i"(8) = "bji" -> 198
        self.assertTrue(self.s.isSumEqual("jj", "jj", "bji"))

    def test_all_a(self):
        # All zeros
        self.assertTrue(self.s.isSumEqual("a", "a", "a"))


if __name__ == "__main__":
    unittest.main()
