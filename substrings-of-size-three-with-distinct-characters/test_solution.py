import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

import unittest
from solution import Solution


class TestHighestIsland(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.highest_island("xyzzaz"), 1)

    def test_example2(self):
        self.assertEqual(self.sol.highest_island("aababcabc"), 4)

    def test_short_string_len1(self):
        self.assertEqual(self.sol.highest_island("a"), 0)

    def test_short_string_len2(self):
        self.assertEqual(self.sol.highest_island("ab"), 0)

    def test_exact_len3_good(self):
        self.assertEqual(self.sol.highest_island("abc"), 1)

    def test_exact_len3_bad(self):
        self.assertEqual(self.sol.highest_island("aab"), 0)

    def test_all_same(self):
        self.assertEqual(self.sol.highest_island("aaaa"), 0)

    def test_all_distinct(self):
        self.assertEqual(self.sol.highest_island("abcdef"), 4)

    def test_alternating(self):
        # aba, bab, aba, bab — "aba" has repeated 'a', "bab" has repeated 'b'
        self.assertEqual(self.sol.highest_island("ababab"), 0)

    def test_repeated_pair(self):
        # aab, abb — neither good
        self.assertEqual(self.sol.highest_island("aabb"), 0)


if __name__ == "__main__":
    unittest.main()
