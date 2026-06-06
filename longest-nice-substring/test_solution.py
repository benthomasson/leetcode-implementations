import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution

import unittest

class TestLongestNiceSubstring(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.longestNiceSubstring("YazaAay"), "aAa")

    def test_example2(self):
        self.assertEqual(self.sol.longestNiceSubstring("Bb"), "Bb")

    def test_example3(self):
        self.assertEqual(self.sol.longestNiceSubstring("c"), "")

    def test_empty_string(self):
        self.assertEqual(self.sol.longestNiceSubstring(""), "")

    def test_single_char(self):
        self.assertEqual(self.sol.longestNiceSubstring("A"), "")

    def test_all_nice(self):
        self.assertEqual(self.sol.longestNiceSubstring("aAbB"), "aAbB")

    def test_no_nice(self):
        self.assertEqual(self.sol.longestNiceSubstring("ABC"), "")

    def test_earliest_wins_on_tie(self):
        # "Aa" and "Bb" are both length 2; earliest should win
        self.assertEqual(self.sol.longestNiceSubstring("AaCBb"), "Aa")

    def test_longer_mixed(self):
        self.assertEqual(self.sol.longestNiceSubstring("dDzeE"), "dD")

if __name__ == "__main__":
    unittest.main()
