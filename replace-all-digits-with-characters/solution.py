"""Replace All Digits With Characters - LeetCode 1844."""

import unittest


class Solution:
    def replaceDigits(self, s: str) -> str:
        """Replace digits at odd indices with shifted characters.

        Args:
            s: String with letters at even indices and digits at odd indices.

        Returns:
            String with all digits replaced by shifted characters.
        """
        chars = list(s)
        for i in range(1, len(s), 2):
            chars[i] = chr(ord(chars[i - 1]) + int(chars[i]))
        return "".join(chars)


replace_digits = Solution().replaceDigits


class TestReplaceDigits(unittest.TestCase):
    def setUp(self):
        self.solve = Solution().replaceDigits

    def test_example1(self):
        self.assertEqual(self.solve("a1c1e1"), "abcdef")

    def test_example2(self):
        self.assertEqual(self.solve("a1b2c3d4e"), "abbdcfdhe")

    def test_single_char(self):
        self.assertEqual(self.solve("a"), "a")

    def test_zero_shift(self):
        self.assertEqual(self.solve("a0"), "aa")

    def test_near_z(self):
        self.assertEqual(self.solve("z0"), "zz")

    def test_large_shift(self):
        self.assertEqual(self.solve("a9"), "aj")


if __name__ == "__main__":
    unittest.main()
