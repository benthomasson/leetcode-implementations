import unittest
from solution import Solution


class TestCountTriplets(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.countTriplets([4, 4, 2, 4, 3]), 3)

    def test_example2(self):
        self.assertEqual(self.s.countTriplets([1, 1, 1, 1, 1]), 0)

    def test_all_distinct(self):
        self.assertEqual(self.s.countTriplets([1, 2, 3]), 1)

    def test_minimum_all_same(self):
        self.assertEqual(self.s.countTriplets([5, 5, 5]), 0)

    def test_two_distinct_values(self):
        # Only two distinct values -> no valid triplet possible
        self.assertEqual(self.s.countTriplets([1, 1, 2, 2]), 0)

    def test_larger_all_distinct(self):
        # [1,2,3,4] -> C(4,3) = 4 triplets
        self.assertEqual(self.s.countTriplets([1, 2, 3, 4]), 4)

    def test_mixed(self):
        # [1,2,3,1,2] has 3 distinct values with counts {1:2, 2:2, 3:1}
        # Combinatorial: 2*2*1 = 4
        self.assertEqual(self.s.countTriplets([1, 2, 3, 1, 2]), 4)


if __name__ == "__main__":
    unittest.main()
