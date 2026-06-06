"""LeetCode 1945: Sum of Digits of String After Convert."""

import unittest


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        """Convert string to number by letter positions, then sum digits k times.

        Args:
            s: String of lowercase English letters.
            k: Number of digit-sum transforms to apply.

        Returns:
            The resulting integer after conversion and k transforms.
        """
        num_str = "".join(str(ord(c) - ord("a") + 1) for c in s)
        result = sum(int(d) for d in num_str)
        for _ in range(k - 1):
            result = sum(int(d) for d in str(result))
        return result


class TestGetLucky(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.getLucky("iiii", 1), 36)

    def test_example2(self):
        self.assertEqual(self.sol.getLucky("leetcode", 2), 6)

    def test_example3(self):
        self.assertEqual(self.sol.getLucky("zbax", 2), 8)

    def test_single_char_a(self):
        self.assertEqual(self.sol.getLucky("a", 1), 1)

    def test_single_char_z(self):
        # z -> 26 -> 2+6=8
        self.assertEqual(self.sol.getLucky("z", 1), 8)

    def test_all_z_k1(self):
        # zzzz -> 26262626 -> 2+6+2+6+2+6+2+6=32
        self.assertEqual(self.sol.getLucky("zzzz", 1), 32)

    def test_high_k(self):
        # zzzz -> 32 -> 5 -> 5 -> ... (stabilizes)
        self.assertEqual(self.sol.getLucky("zzzz", 10), 5)


if __name__ == "__main__":
    unittest.main()
