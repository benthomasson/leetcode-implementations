import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))
from solution import Solution


class TestUniqueMorseCodeWords(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.uniqueMorseCodeWords(["gin", "zen", "gig", "msg"]), 2)

    def test_example2(self):
        self.assertEqual(self.sol.uniqueMorseCodeWords(["a"]), 1)

    def test_all_same_words(self):
        self.assertEqual(self.sol.uniqueMorseCodeWords(["abc", "abc", "abc"]), 1)

    def test_all_unique_single_chars(self):
        self.assertEqual(self.sol.uniqueMorseCodeWords(["a", "b", "c"]), 3)

    def test_same_morse_different_words(self):
        self.assertEqual(self.sol.uniqueMorseCodeWords(["gig", "msg"]), 1)

    def test_single_word(self):
        self.assertEqual(self.sol.uniqueMorseCodeWords(["z"]), 1)

    def test_all_unique(self):
        self.assertEqual(self.sol.uniqueMorseCodeWords(["a", "ab", "abc"]), 3)

    def test_max_constraint_same(self):
        # 100 identical words -> 1 transformation
        self.assertEqual(self.sol.uniqueMorseCodeWords(["hello"] * 100), 1)


if __name__ == "__main__":
    unittest.main()
