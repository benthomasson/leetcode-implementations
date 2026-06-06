"""Decrypt String from Alphabet to Integer Mapping."""

import unittest


class Solution:
    def sortItems(self, s: str) -> str:
        """Decode a digit string to letters where 1-9 map to a-i and 10#-26# map to j-z.

        Args:
            s: Encoded string of digits and '#' characters.

        Returns:
            Decoded lowercase letter string.
        """
        result = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                num = int(s[i : i + 2])
                i += 3
            else:
                num = int(s[i])
                i += 1
            result.append(chr(ord("a") + num - 1))
        return "".join(result)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.sortItems("10#11#12"), "jkab")

    def test_example2(self):
        self.assertEqual(self.sol.sortItems("1326#"), "acz")

    def test_all_single_digits(self):
        self.assertEqual(self.sol.sortItems("123456789"), "abcdefghi")

    def test_all_double_digits(self):
        self.assertEqual(self.sol.sortItems("10#11#12#13#"), "jklm")

    def test_single_char(self):
        self.assertEqual(self.sol.sortItems("1"), "a")

    def test_boundary_9_vs_10(self):
        self.assertEqual(self.sol.sortItems("910#"), "ij")

    def test_max_double_digit(self):
        self.assertEqual(self.sol.sortItems("26#"), "z")

    def test_mixed(self):
        self.assertEqual(self.sol.sortItems("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"), "abcdefghijklmnopqrstuvwxyz")


if __name__ == "__main__":
    unittest.main()
