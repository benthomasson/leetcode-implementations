"""Remove Palindromic Subsequences - LeetCode"""

import unittest


def countStrings(s: str) -> int:
    """Return minimum steps to remove all chars via palindromic subsequences.

    Args:
        s: String of only 'a' and 'b' characters.

    Returns:
        0 if empty, 1 if palindrome, 2 otherwise.
    """
    if not s:
        return 0
    # Two-pointer palindrome check: O(n) time, O(1) space
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return 2
        left += 1
        right -= 1
    return 1


class TestCountStrings(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(countStrings(""), 0)

    def test_single_char(self):
        self.assertEqual(countStrings("a"), 1)
        self.assertEqual(countStrings("b"), 1)

    def test_palindrome(self):
        self.assertEqual(countStrings("ababa"), 1)
        self.assertEqual(countStrings("aa"), 1)
        self.assertEqual(countStrings("aba"), 1)
        self.assertEqual(countStrings("abba"), 1)

    def test_not_palindrome(self):
        self.assertEqual(countStrings("abb"), 2)
        self.assertEqual(countStrings("baabb"), 2)
        self.assertEqual(countStrings("ab"), 2)

    def test_all_same(self):
        self.assertEqual(countStrings("aaaa"), 1)
        self.assertEqual(countStrings("bbbb"), 1)

    def test_alternating(self):
        self.assertEqual(countStrings("abab"), 2)
        self.assertEqual(countStrings("baba"), 1)

    def test_long(self):
        self.assertEqual(countStrings("a" * 1000), 1)
        self.assertEqual(countStrings("ab" * 500), 2)


if __name__ == "__main__":
    unittest.main()
