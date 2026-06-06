"""Tests for split-a-string-in-balanced-strings solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import find_special_integer


class TestFindSpecialInteger(unittest.TestCase):
    # LeetCode examples
    def test_example1(self):
        self.assertEqual(find_special_integer("RLRRLLRLRL"), 4)

    def test_example2(self):
        self.assertEqual(find_special_integer("RLRRRLLRLL"), 2)

    def test_example3(self):
        self.assertEqual(find_special_integer("LLLLRRRR"), 1)

    # Edge cases
    def test_minimal_rl(self):
        self.assertEqual(find_special_integer("RL"), 1)

    def test_minimal_lr(self):
        self.assertEqual(find_special_integer("LR"), 1)

    def test_max_splits(self):
        # Every pair is balanced -> max splits = len/2
        self.assertEqual(find_special_integer("RLRLRLRL"), 4)

    def test_deeply_nested(self):
        self.assertEqual(find_special_integer("RRRRLLLL"), 1)

    def test_mixed_nesting(self):
        # "RLLRLRRL" -> balance: 1,0,-1,0,-1,0,1,0 -> 4 splits
        self.assertEqual(find_special_integer("RLLRLRRL"), 4)

    def test_longer_string(self):
        # 500 "RL" pairs -> 500 balanced substrings
        s = "RL" * 500
        self.assertEqual(find_special_integer(s), 500)


if __name__ == "__main__":
    unittest.main()
