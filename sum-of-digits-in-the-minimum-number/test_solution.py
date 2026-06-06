import unittest
from solution import Solution


class TestSumOfDigits(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.sum_of_digits([34, 23, 1, 24, 75, 33, 54, 8]), 0)

    def test_example2(self):
        self.assertEqual(self.s.sum_of_digits([99, 77, 33, 66, 55]), 1)

    def test_single_odd_digit_sum(self):
        self.assertEqual(self.s.sum_of_digits([5]), 0)

    def test_single_even_digit_sum(self):
        self.assertEqual(self.s.sum_of_digits([2]), 1)

    def test_min_value_1(self):
        self.assertEqual(self.s.sum_of_digits([1]), 0)

    def test_max_value_100(self):
        # 100 -> 1+0+0 = 1 (odd) -> 0
        self.assertEqual(self.s.sum_of_digits([100]), 0)

    def test_all_same(self):
        # 11 -> 1+1 = 2 (even) -> 1
        self.assertEqual(self.s.sum_of_digits([11, 11, 11]), 1)

    def test_min_with_two_digits_even_sum(self):
        # min is 24 -> 2+4 = 6 (even) -> 1
        self.assertEqual(self.s.sum_of_digits([50, 24, 30]), 1)

    def test_min_with_two_digits_odd_sum(self):
        # min is 14 -> 1+4 = 5 (odd) -> 0
        self.assertEqual(self.s.sum_of_digits([50, 14, 30]), 0)


if __name__ == "__main__":
    unittest.main()
