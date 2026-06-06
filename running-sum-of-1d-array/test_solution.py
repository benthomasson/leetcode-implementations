import unittest
from solution import Solution


class TestRunningSum(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.runningSum([1, 2, 3, 4]), [1, 3, 6, 10])

    def test_example2(self):
        self.assertEqual(self.s.runningSum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])

    def test_example3(self):
        self.assertEqual(self.s.runningSum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])

    def test_single_element(self):
        self.assertEqual(self.s.runningSum([5]), [5])

    def test_negative_numbers(self):
        self.assertEqual(self.s.runningSum([-1, -2, -3]), [-1, -3, -6])

    def test_mixed_signs(self):
        self.assertEqual(self.s.runningSum([1, -1, 1, -1]), [1, 0, 1, 0])

    def test_all_zeros(self):
        self.assertEqual(self.s.runningSum([0, 0, 0]), [0, 0, 0])

    def test_large_values(self):
        self.assertEqual(self.s.runningSum([1000000, -1000000]), [1000000, 0])


if __name__ == "__main__":
    unittest.main()
