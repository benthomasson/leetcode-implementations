"""LeetCode 1370: Increasing Decreasing String."""

import unittest


class Solution:
    def sortString(self, s: str) -> str:
        """Reorder string by alternating ascending/descending character sweeps.

        Args:
            s: Input string of lowercase English letters.

        Returns:
            Reordered string per the increasing-decreasing algorithm.
        """
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []
        remaining = len(s)

        while remaining > 0:
            # Forward sweep: a -> z
            for i in range(26):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1
                    remaining -= 1

            # Backward sweep: z -> a
            for i in range(25, -1, -1):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1
                    remaining -= 1

        return ''.join(result)


class TestSortString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.sortString("aaaabbbbcccc"), "abccbaabccba")

    def test_example2(self):
        self.assertEqual(self.sol.sortString("rat"), "art")

    def test_single_char(self):
        self.assertEqual(self.sol.sortString("a"), "a")

    def test_all_same(self):
        self.assertEqual(self.sol.sortString("aaaa"), "aaaa")

    def test_already_sorted(self):
        self.assertEqual(self.sol.sortString("abc"), "abc")

    def test_reverse_sorted(self):
        self.assertEqual(self.sol.sortString("cba"), "abccba"[:3])  # "abc"

    def test_two_chars(self):
        self.assertEqual(self.sol.sortString("ab"), "ab")

    def test_longer_mixed(self):
        self.assertEqual(self.sol.sortString("ggggggg"), "ggggggg")

    def test_full_alphabet_single(self):
        s = "zyxwvutsrqponmlkjihgfedcba"
        self.assertEqual(self.sol.sortString(s), "abcdefghijklmnopqrstuvwxyz")


if __name__ == "__main__":
    unittest.main()
