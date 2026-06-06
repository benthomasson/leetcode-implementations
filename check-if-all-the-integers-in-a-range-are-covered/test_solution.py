import unittest
from solution import Solution


class TestIsCovered(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertTrue(self.s.isCovered([[1, 2], [3, 4], [5, 6]], 2, 5))

    def test_example2(self):
        self.assertFalse(self.s.isCovered([[1, 10], [10, 20]], 21, 21))

    def test_single_point_covered(self):
        self.assertTrue(self.s.isCovered([[5, 5]], 5, 5))

    def test_single_point_uncovered(self):
        self.assertFalse(self.s.isCovered([[1, 4]], 5, 5))

    def test_gap_in_coverage(self):
        self.assertFalse(self.s.isCovered([[1, 3], [5, 7]], 1, 7))

    def test_overlapping_ranges(self):
        self.assertTrue(self.s.isCovered([[1, 5], [3, 8]], 1, 8))

    def test_one_range_covers_all(self):
        self.assertTrue(self.s.isCovered([[1, 50]], 1, 50))

    def test_adjacent_ranges_no_gap(self):
        self.assertTrue(self.s.isCovered([[1, 3], [4, 6]], 1, 6))

    def test_adjacent_ranges_with_gap(self):
        self.assertFalse(self.s.isCovered([[1, 3], [5, 6]], 1, 6))


if __name__ == "__main__":
    unittest.main()
