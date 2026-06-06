"""Replace All ?'s to Avoid Consecutive Repeating Characters."""

import unittest


class Solution:
    def dfs(self, s: str) -> str:
        """Replace all '?' so no two adjacent characters are the same.

        Args:
            s: String of lowercase letters and '?' characters.

        Returns:
            String with all '?' replaced, no consecutive repeats.
        """
        chars = list(s)
        n = len(chars)
        for i in range(n):
            if chars[i] == '?':
                for c in 'abc':
                    if (i > 0 and chars[i - 1] == c) or (i < n - 1 and chars[i + 1] == c):
                        continue
                    chars[i] = c
                    break
        return ''.join(chars)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        result = self.sol.dfs("?zs")
        self.assertNotEqual(result[0], 'z')
        self.assertEqual(result[1:], "zs")
        self._assert_no_consecutive(result)

    def test_example2(self):
        result = self.sol.dfs("ubv?w")
        self.assertEqual(result[:3], "ubv")
        self.assertEqual(result[4], "w")
        self.assertNotIn(result[3], ('v', 'w'))
        self._assert_no_consecutive(result)

    def test_single_question(self):
        result = self.sol.dfs("?")
        self.assertEqual(len(result), 1)
        self.assertTrue(result.islower())

    def test_two_questions(self):
        result = self.sol.dfs("??")
        self.assertEqual(len(result), 2)
        self.assertNotEqual(result[0], result[1])
        self._assert_no_consecutive(result)

    def test_all_questions(self):
        result = self.sol.dfs("?????")
        self.assertEqual(len(result), 5)
        self._assert_no_consecutive(result)

    def test_no_questions(self):
        self.assertEqual(self.sol.dfs("abc"), "abc")

    def test_question_at_start(self):
        result = self.sol.dfs("?b")
        self.assertNotEqual(result[0], 'b')
        self._assert_no_consecutive(result)

    def test_question_at_end(self):
        result = self.sol.dfs("a?")
        self.assertNotEqual(result[1], 'a')
        self._assert_no_consecutive(result)

    def test_questions_between_same_neighbors(self):
        result = self.sol.dfs("a?a")
        self.assertEqual(len(result), 3)
        self._assert_no_consecutive(result)

    def _assert_no_consecutive(self, s):
        for i in range(1, len(s)):
            self.assertNotEqual(s[i], s[i - 1], f"Consecutive repeat at index {i}: '{s}'")


if __name__ == "__main__":
    unittest.main()
