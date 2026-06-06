import unittest
from solution import Solution


class TestCountGoodTriplets(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3), 4)

    def test_example2(self):
        self.assertEqual(self.s.countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1), 0)

    def test_min_length_good(self):
        self.assertEqual(self.s.countGoodTriplets([1, 1, 1], 0, 0, 0), 1)

    def test_min_length_bad(self):
        self.assertEqual(self.s.countGoodTriplets([1, 2, 3], 0, 0, 0), 0)

    def test_all_equal(self):
        self.assertEqual(self.s.countGoodTriplets([5, 5, 5, 5], 0, 0, 0), 4)

    def test_large_thresholds(self):
        # All triplets valid when thresholds are large enough
        self.assertEqual(self.s.countGoodTriplets([0, 500, 1000], 1000, 1000, 1000), 1)

    def test_zero_thresholds_mixed(self):
        self.assertEqual(self.s.countGoodTriplets([1, 2, 1, 2], 0, 0, 0), 0)


if __name__ == "__main__":
    unittest.main()
