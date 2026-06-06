"""Tests for Sorting the Sentence."""

import unittest
from solution import Solution


class TestSortSentence(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        assert self.sol.sort_sentence("is2 sentence4 This1 a3") == "This is a sentence"

    def test_example2(self):
        assert self.sol.sort_sentence("Myself2 Me1 I4 and3") == "Me Myself and I"

    def test_single_word(self):
        assert self.sol.sort_sentence("Hello1") == "Hello"

    def test_nine_words(self):
        s = "d4 e5 f6 g7 h8 i9 a1 b2 c3"
        assert self.sol.sort_sentence(s) == "a b c d e f g h i"

    def test_mixed_case(self):
        assert self.sol.sort_sentence("HeLLo1 WoRLd2") == "HeLLo WoRLd"


if __name__ == "__main__":
    unittest.main()
