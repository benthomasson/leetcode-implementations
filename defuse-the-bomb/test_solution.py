import unittest
from solution import Solution


class TestDefuseTheBomb(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1_positive_k(self):
        self.assertEqual(self.s.minOperations([5, 7, 1, 4], 3), [12, 10, 16, 13])

    def test_example2_zero_k(self):
        self.assertEqual(self.s.minOperations([1, 2, 3, 4], 0), [0, 0, 0, 0])

    def test_example3_negative_k(self):
        self.assertEqual(self.s.minOperations([2, 4, 9, 3], -2), [12, 5, 6, 13])

    def test_single_element(self):
        self.assertEqual(self.s.minOperations([5], 0), [0])

    def test_k_equals_n_minus_1(self):
        self.assertEqual(self.s.minOperations([1, 2, 3, 4], 3), [9, 8, 7, 6])

    def test_k_equals_neg_n_minus_1(self):
        self.assertEqual(self.s.minOperations([1, 2, 3, 4], -3), [9, 8, 7, 6])

    def test_all_same_values(self):
        self.assertEqual(self.s.minOperations([3, 3, 3, 3], 2), [6, 6, 6, 6])

    def test_k_equals_1(self):
        self.assertEqual(self.s.minOperations([1, 2, 3], 1), [2, 3, 1])

    def test_k_equals_neg_1(self):
        self.assertEqual(self.s.minOperations([1, 2, 3], -1), [3, 1, 2])


if __name__ == "__main__":
    unittest.main()
