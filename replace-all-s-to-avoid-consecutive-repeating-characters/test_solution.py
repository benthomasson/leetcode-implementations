"""Tests for Replace All ?'s to Avoid Consecutive Repeating Characters."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def _assert_valid(self, result, original):
        """Check result has no '?', no consecutive repeats, and preserves non-? chars."""
        self.assertEqual(len(result), len(original))
        self.assertNotIn("?", result)
        for ch in result:
            self.assertTrue(ch.islower(), f"Non-lowercase char: {ch}")
        for i, ch in enumerate(original):
            if ch != "?":
                self.assertEqual(result[i], ch, f"Modified non-? char at {i}")
        for i in range(1, len(result)):
            self.assertNotEqual(result[i], result[i - 1],
                                f"Consecutive repeat at {i}: '{result}'")

    def test_example1(self):
        self._assert_valid(self.sol.dfs("?zs"), "?zs")

    def test_example2(self):
        self._assert_valid(self.sol.dfs("ubv?w"), "ubv?w")

    def test_single_question(self):
        self._assert_valid(self.sol.dfs("?"), "?")

    def test_no_questions(self):
        self.assertEqual(self.sol.dfs("abc"), "abc")

    def test_all_questions(self):
        self._assert_valid(self.sol.dfs("?????"), "?????")

    def test_question_between_same(self):
        self._assert_valid(self.sol.dfs("a?a"), "a?a")

    def test_question_at_boundaries(self):
        self._assert_valid(self.sol.dfs("?b"), "?b")
        self._assert_valid(self.sol.dfs("a?"), "a?")

    def test_two_questions(self):
        self._assert_valid(self.sol.dfs("??"), "??")

    def test_max_length_all_questions(self):
        s = "?" * 100
        self._assert_valid(self.sol.dfs(s), s)


if __name__ == "__main__":
    unittest.main()
