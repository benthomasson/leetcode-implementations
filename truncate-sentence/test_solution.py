"""Tests for truncate sentence solution."""

import unittest
from solution import Solution


class TestTruncateSentence(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        assert self.sol.truncateSentence("Hello how are you Contestant", 4) == "Hello how are you"

    def test_example2(self):
        assert self.sol.truncateSentence("What is the solution to this problem", 4) == "What is the solution"

    def test_example3(self):
        assert self.sol.truncateSentence("chopper is not a tanuki", 5) == "chopper is not a tanuki"

    def test_single_word(self):
        assert self.sol.truncateSentence("Hello", 1) == "Hello"

    def test_k_equals_total_words(self):
        assert self.sol.truncateSentence("a b c", 3) == "a b c"

    def test_two_words_take_one(self):
        assert self.sol.truncateSentence("Hello World", 1) == "Hello"

    def test_mixed_case(self):
        assert self.sol.truncateSentence("aA bB cC dD", 2) == "aA bB"


if __name__ == "__main__":
    unittest.main()
