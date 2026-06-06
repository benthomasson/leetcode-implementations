import unittest
from solution import Solution


class TestMinCostClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.minCostClimbingStairs([3, 6, 1, 0]), 1)

    def test_example2(self):
        self.assertEqual(self.s.minCostClimbingStairs([1, 2, 3, 4]), -1)

    def test_two_elements_dominant(self):
        self.assertEqual(self.s.minCostClimbingStairs([1, 0]), 0)

    def test_exactly_twice(self):
        self.assertEqual(self.s.minCostClimbingStairs([1, 2]), 1)

    def test_zeros(self):
        self.assertEqual(self.s.minCostClimbingStairs([0, 0, 0, 1]), 3)

    def test_max_at_start(self):
        self.assertEqual(self.s.minCostClimbingStairs([10, 5, 2, 1]), 0)

    def test_not_quite_twice(self):
        self.assertEqual(self.s.minCostClimbingStairs([1, 2, 3, 5]), -1)

    def test_dominant_at_end(self):
        self.assertEqual(self.s.minCostClimbingStairs([1, 2, 3, 7]), 3)

    def test_single_nonzero(self):
        self.assertEqual(self.s.minCostClimbingStairs([0, 100]), 1)


if __name__ == "__main__":
    unittest.main()
