import unittest
from solution import Solution


class TestDietPlanPerformance(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.dietPlanPerformance([1, 2, 3, 4, 5], 1, 3, 3), 0)

    def test_example2(self):
        self.assertEqual(self.s.dietPlanPerformance([3, 2], 2, 0, 1), 1)

    def test_example3(self):
        self.assertEqual(self.s.dietPlanPerformance([6, 5, 0, 0], 2, 1, 5), 0)

    def test_single_element(self):
        self.assertEqual(self.s.dietPlanPerformance([5], 1, 3, 7), 0)
        self.assertEqual(self.s.dietPlanPerformance([1], 1, 3, 7), -1)
        self.assertEqual(self.s.dietPlanPerformance([10], 1, 3, 7), 1)

    def test_k_equals_length(self):
        self.assertEqual(self.s.dietPlanPerformance([1, 2, 3], 3, 10, 20), -1)
        self.assertEqual(self.s.dietPlanPerformance([1, 2, 3], 3, 1, 2), 1)
        self.assertEqual(self.s.dietPlanPerformance([1, 2, 3], 3, 5, 7), 0)

    def test_all_gain(self):
        self.assertEqual(self.s.dietPlanPerformance([10, 10, 10], 1, 1, 5), 3)

    def test_all_lose(self):
        self.assertEqual(self.s.dietPlanPerformance([1, 1, 1], 1, 5, 10), -3)

    def test_large_input(self):
        cals = [100] * 100000
        self.assertEqual(self.s.dietPlanPerformance(cals, 1, 50, 99), 100000)


if __name__ == "__main__":
    unittest.main()
