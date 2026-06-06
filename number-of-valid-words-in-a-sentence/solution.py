"""LeetCode 2047: Number of Valid Words in a Sentence."""

import unittest


class Solution:
    def countValidWords(self, sentence: str) -> int:
        """Count valid words in a sentence.

        Args:
            sentence: String of lowercase letters, digits, hyphens, punctuation, spaces.

        Returns:
            Number of tokens that are valid words.
        """

        def is_valid(token: str) -> bool:
            hyphen_count = 0
            punct_count = 0
            for i, c in enumerate(token):
                if c.isdigit():
                    return False
                if c == '-':
                    hyphen_count += 1
                    if hyphen_count > 1:
                        return False
                    if i == 0 or i == len(token) - 1:
                        return False
                    if not token[i - 1].isalpha() or not token[i + 1].isalpha():
                        return False
                if c in '!.,':
                    punct_count += 1
                    if punct_count > 1:
                        return False
                    if i != len(token) - 1:
                        return False
            return True

        return sum(is_valid(t) for t in sentence.split() if t)


class TestCountValidWords(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.countValidWords("cat and  dog"), 3)

    def test_example2(self):
        self.assertEqual(self.s.countValidWords("!this  1-s b8d!"), 0)

    def test_example3(self):
        self.assertEqual(self.s.countValidWords("alice and  bob are playing stone-game10"), 5)

    def test_single_punctuation(self):
        self.assertEqual(self.s.countValidWords("!"), 1)

    def test_hyphenated_with_punctuation(self):
        self.assertEqual(self.s.countValidWords("a-b."), 1)

    def test_leading_hyphen(self):
        self.assertEqual(self.s.countValidWords("-ab"), 0)

    def test_trailing_hyphen(self):
        self.assertEqual(self.s.countValidWords("ab-"), 0)

    def test_multiple_hyphens(self):
        self.assertEqual(self.s.countValidWords("a-b-c"), 0)

    def test_multiple_punctuation(self):
        self.assertEqual(self.s.countValidWords("c.,"), 0)

    def test_mid_punctuation(self):
        self.assertEqual(self.s.countValidWords("a!b"), 0)

    def test_digit_in_token(self):
        self.assertEqual(self.s.countValidWords("3g"), 0)

    def test_only_spaces(self):
        self.assertEqual(self.s.countValidWords("   "), 0)

    def test_single_letter(self):
        self.assertEqual(self.s.countValidWords("a"), 1)

    def test_punctuation_before_hyphen(self):
        # "!-a" — punctuation not at end, hyphen at start
        self.assertEqual(self.s.countValidWords("!-a"), 0)


if __name__ == "__main__":
    unittest.main()
