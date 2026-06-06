"""Remove Outermost Parentheses - LeetCode 1021."""

import unittest


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """Remove outermost parentheses from each primitive decomposition.

        Args:
            s: A valid parentheses string.

        Returns:
            String with outermost parentheses of each primitive removed.
        """
        result = []
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > 1:
                    result.append(c)
            else:
                depth -= 1
                if depth > 0:
                    result.append(c)
        return ''.join(result)


class TestRemoveOuterParentheses(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.removeOuterParentheses("(()())(())"), "()()()")

    def test_example2(self):
        self.assertEqual(self.sol.removeOuterParentheses("(()())(())(()(()))"), "()()()()(())")

    def test_example3(self):
        self.assertEqual(self.sol.removeOuterParentheses("()()"), "")

    def test_single_primitive(self):
        self.assertEqual(self.sol.removeOuterParentheses("()"), "")

    def test_deeply_nested(self):
        self.assertEqual(self.sol.removeOuterParentheses("(((())))"), "((()))")

    def test_empty(self):
        self.assertEqual(self.sol.removeOuterParentheses(""), "")

    def test_many_primitives(self):
        self.assertEqual(self.sol.removeOuterParentheses("()()()()"), "")


if __name__ == "__main__":
    unittest.main()
