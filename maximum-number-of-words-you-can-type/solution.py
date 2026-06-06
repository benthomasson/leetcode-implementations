"""Maximum Number of Words You Can Type."""

import unittest


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """Count words fully typeable with broken keyboard.

        Args:
            text: Space-separated words of lowercase letters.
            brokenLetters: Distinct lowercase broken letter keys.

        Returns:
            Number of words with no broken letters.
        """
        broken = set(brokenLetters)
        return sum(broken.isdisjoint(word) for word in text.split())


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.canBeTypedWords("hello world", "ad"), 1)

    def test_example2(self):
        self.assertEqual(self.s.canBeTypedWords("leet code", "lt"), 1)

    def test_example3(self):
        self.assertEqual(self.s.canBeTypedWords("leet code", "e"), 0)

    def test_no_broken(self):
        self.assertEqual(self.s.canBeTypedWords("hello world", ""), 2)

    def test_single_word(self):
        self.assertEqual(self.s.canBeTypedWords("abc", "a"), 0)

    def test_single_char_words(self):
        self.assertEqual(self.s.canBeTypedWords("a b c", "b"), 2)

    def test_all_broken(self):
        self.assertEqual(self.s.canBeTypedWords("abc", "abc"), 0)


if __name__ == "__main__":
    unittest.main()
