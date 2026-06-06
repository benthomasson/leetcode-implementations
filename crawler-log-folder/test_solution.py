"""Tests for Crawler Log Folder solution."""

import unittest
from solution import Solution


class TestMinOperations(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.minOperations(["d1/", "d2/", "../", "d21/", "./"]), 2)

    def test_example2(self):
        self.assertEqual(self.s.minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]), 3)

    def test_example3(self):
        self.assertEqual(self.s.minOperations(["d1/", "../", "../", "../"]), 0)

    def test_all_parent_moves(self):
        self.assertEqual(self.s.minOperations(["../", "../", "../"]), 0)

    def test_all_same_folder(self):
        self.assertEqual(self.s.minOperations(["./", "./", "./"]), 0)

    def test_single_child(self):
        self.assertEqual(self.s.minOperations(["a/"]), 1)

    def test_single_parent(self):
        self.assertEqual(self.s.minOperations(["../"]), 0)

    def test_single_stay(self):
        self.assertEqual(self.s.minOperations(["./"]), 0)

    def test_deep_nesting(self):
        self.assertEqual(self.s.minOperations(["a/", "b/", "c/", "d/", "e/"]), 5)

    def test_down_then_all_the_way_up(self):
        self.assertEqual(self.s.minOperations(["a/", "b/", "../", "../"]), 0)


if __name__ == "__main__":
    unittest.main()
