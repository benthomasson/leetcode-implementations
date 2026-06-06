import unittest
from solution import Solution


class TestSmallestRangeI(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_single_element(self):
        self.assertEqual(self.s.smallestRangeI([1], 0), 0)

    def test_example2(self):
        self.assertEqual(self.s.smallestRangeI([0, 10], 2), 6)

    def test_example3(self):
        self.assertEqual(self.s.smallestRangeI([1, 3, 6], 3), 0)

    def test_all_same(self):
        self.assertEqual(self.s.smallestRangeI([5, 5, 5], 3), 0)

    def test_k_zero(self):
        self.assertEqual(self.s.smallestRangeI([1, 5, 9], 0), 8)

    def test_range_exactly_2k(self):
        self.assertEqual(self.s.smallestRangeI([0, 10], 5), 0)

    def test_range_less_than_2k(self):
        self.assertEqual(self.s.smallestRangeI([3, 5], 10), 0)

    def test_large_values(self):
        self.assertEqual(self.s.smallestRangeI([0, 10000], 10000), 0)


if __name__ == "__main__":
    unittest.main()
