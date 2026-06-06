"""Tests for Remove Outermost Parentheses - LeetCode 1021."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestRemoveOuterParentheses(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- LeetCode examples ---
    def test_example1(self):
        self.assertEqual(self.sol.removeOuterParentheses("(()())(())"), "()()()")

    def test_example2(self):
        self.assertEqual(self.sol.removeOuterParentheses("(()())(())(()(()))"), "()()()()(())")

    def test_example3(self):
        self.assertEqual(self.sol.removeOuterParentheses("()()"), "")

    # --- Edge cases ---
    def test_empty(self):
        self.assertEqual(self.sol.removeOuterParentheses(""), "")

    def test_single_primitive(self):
        self.assertEqual(self.sol.removeOuterParentheses("()"), "")

    def test_deeply_nested(self):
        self.assertEqual(self.sol.removeOuterParentheses("(((())))"), "((()))")

    def test_many_simple_primitives(self):
        self.assertEqual(self.sol.removeOuterParentheses("()()()()"), "")

    def test_single_deep_primitive(self):
        self.assertEqual(self.sol.removeOuterParentheses("(())"), "()")

    def test_large_input(self):
        # 50000 simple "()" primitives -> all outermost removed -> ""
        s = "()" * 50000
        self.assertEqual(self.sol.removeOuterParentheses(s), "")


if __name__ == "__main__":
    unittest.main()
