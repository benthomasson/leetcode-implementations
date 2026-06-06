"""LeetCode: Reformat The String."""


class Solution:
    def reformat(self, s: str) -> str:
        """Reformat string so no two adjacent chars are the same type.

        Args:
            s: Alphanumeric string of lowercase letters and digits.

        Returns:
            Reformatted string, or empty string if impossible.
        """
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]

        if abs(len(letters) - len(digits)) > 1:
            return ""

        # Longer list goes first
        if len(digits) > len(letters):
            letters, digits = digits, letters

        result = []
        for i in range(len(digits)):
            result.append(letters[i])
            result.append(digits[i])
        if len(letters) > len(digits):
            result.append(letters[-1])

        return "".join(result)


import unittest


class TestReformat(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_mixed_equal(self):
        res = self.sol.reformat("a0b1c2")
        self.assertEqual(len(res), 6)
        for i in range(len(res) - 1):
            self.assertNotEqual(res[i].isdigit(), res[i + 1].isdigit())

    def test_all_letters(self):
        self.assertEqual(self.sol.reformat("leetcode"), "")

    def test_all_digits(self):
        self.assertEqual(self.sol.reformat("1229857369"), "")

    def test_single_letter(self):
        self.assertEqual(self.sol.reformat("a"), "a")

    def test_single_digit(self):
        self.assertEqual(self.sol.reformat("5"), "5")

    def test_two_chars_valid(self):
        res = self.sol.reformat("a1")
        self.assertIn(res, ["a1", "1a"])

    def test_off_by_one_more_letters(self):
        res = self.sol.reformat("ab1")
        self.assertEqual(len(res), 3)
        for i in range(len(res) - 1):
            self.assertNotEqual(res[i].isdigit(), res[i + 1].isdigit())

    def test_off_by_one_more_digits(self):
        res = self.sol.reformat("a12")
        self.assertEqual(len(res), 3)
        for i in range(len(res) - 1):
            self.assertNotEqual(res[i].isdigit(), res[i + 1].isdigit())

    def test_diff_too_large(self):
        self.assertEqual(self.sol.reformat("aab1"), "")

    def test_empty_after_filter(self):
        # All same type, length 2
        self.assertEqual(self.sol.reformat("ab"), "")


if __name__ == "__main__":
    unittest.main()
