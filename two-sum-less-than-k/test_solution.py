import unittest
from solution import max_sum_under_k


class TestMaxSumUnderK(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(max_sum_under_k([34, 23, 1, 24, 75, 33, 54, 8], 60), 58)

    def test_example2(self):
        self.assertEqual(max_sum_under_k([10, 20, 30], 15), -1)

    def test_single_element(self):
        self.assertEqual(max_sum_under_k([5], 10), -1)

    def test_all_pairs_at_or_above_k(self):
        self.assertEqual(max_sum_under_k([50, 50], 100), -1)
        self.assertEqual(max_sum_under_k([50, 51], 100), -1)

    def test_boundary_k_minus_one(self):
        self.assertEqual(max_sum_under_k([1, 2], 4), 3)
        self.assertEqual(max_sum_under_k([1, 3], 4), -1)

    def test_duplicates(self):
        self.assertEqual(max_sum_under_k([5, 5, 5], 11), 10)

    def test_two_elements_valid(self):
        self.assertEqual(max_sum_under_k([1, 2], 10), 3)

    def test_large_values(self):
        self.assertEqual(max_sum_under_k([1000, 1000], 2000), -1)
        self.assertEqual(max_sum_under_k([999, 1000], 2000), 1999)

    def test_min_values(self):
        self.assertEqual(max_sum_under_k([1, 1], 3), 2)
        self.assertEqual(max_sum_under_k([1, 1], 2), -1)


if __name__ == "__main__":
    unittest.main()
