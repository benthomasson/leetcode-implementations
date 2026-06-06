import unittest
from solution import maxSizeSubsequenceSumQueries


class TestMaxSizeSubsequenceSumQueries(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(maxSizeSubsequenceSumQueries([4, 5, 2, 1], [3, 10, 21]), [2, 3, 4])

    def test_example2(self):
        self.assertEqual(maxSizeSubsequenceSumQueries([2, 3, 4, 5], [1]), [0])

    def test_query_smaller_than_all(self):
        self.assertEqual(maxSizeSubsequenceSumQueries([5, 10, 15], [2]), [0])

    def test_query_equals_total_sum(self):
        self.assertEqual(maxSizeSubsequenceSumQueries([1, 2, 3], [6]), [3])

    def test_single_element(self):
        self.assertEqual(maxSizeSubsequenceSumQueries([7], [7, 6, 10]), [1, 0, 1])

    def test_all_identical(self):
        self.assertEqual(maxSizeSubsequenceSumQueries([3, 3, 3, 3], [3, 6, 9, 12, 2]), [1, 2, 3, 4, 0])

    def test_large_values(self):
        nums = [1000000, 1000000]
        self.assertEqual(maxSizeSubsequenceSumQueries(nums, [999999, 1000000, 2000000]), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
