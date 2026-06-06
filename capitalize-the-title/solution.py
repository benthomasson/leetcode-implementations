"""LeetCode 2129: Capitalize the Title."""

import unittest


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        """Capitalize title by word length rules.

        Args:
            title: Space-separated words of English letters.

        Returns:
            Title with words <=2 chars lowercased, others title-cased.
        """
        return " ".join(
            w.lower() if len(w) <= 2 else w[0].upper() + w[1:].lower()
            for w in title.split()
        )


class TestCapitalizeTitle(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.capitalizeTitle("capiTalIze tHe titLe"), "Capitalize The Title")

    def test_example2(self):
        self.assertEqual(self.s.capitalizeTitle("First leTTeR of EACH Word"), "First Letter of Each Word")

    def test_example3(self):
        self.assertEqual(self.s.capitalizeTitle("i lOve leetcode"), "i Love Leetcode")

    def test_single_short_word(self):
        self.assertEqual(self.s.capitalizeTitle("aB"), "ab")

    def test_single_long_word(self):
        self.assertEqual(self.s.capitalizeTitle("hELLO"), "Hello")

    def test_single_char(self):
        self.assertEqual(self.s.capitalizeTitle("Z"), "z")

    def test_all_short(self):
        self.assertEqual(self.s.capitalizeTitle("a bb CC"), "a bb cc")

    def test_three_letter_word(self):
        self.assertEqual(self.s.capitalizeTitle("THE"), "The")


if __name__ == "__main__":
    unittest.main()
