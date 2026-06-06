"""Tests for LeetCode 944: Delete Columns to Make Sorted."""

import unittest
from solution import Solution


class TestMinDeletionSize(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.minDeletionSize(["cba", "daf", "ghi"]), 1)

    def test_example2(self):
        self.assertEqual(self.s.minDeletionSize(["a", "b"]), 0)

    def test_example3(self):
        self.assertEqual(self.s.minDeletionSize(["zyx", "wvu", "tsr"]), 3)

    def test_single_string(self):
        self.assertEqual(self.s.minDeletionSize(["abc"]), 0)

    def test_all_same(self):
        self.assertEqual(self.s.minDeletionSize(["aaa", "aaa", "aaa"]), 0)

    def test_single_column_sorted(self):
        self.assertEqual(self.s.minDeletionSize(["a", "b", "c"]), 0)

    def test_single_column_unsorted(self):
        self.assertEqual(self.s.minDeletionSize(["c", "b", "a"]), 1)

    def test_all_sorted(self):
        self.assertEqual(self.s.minDeletionSize(["abc", "bcd", "cde"]), 0)


if __name__ == "__main__":
    unittest.main()
