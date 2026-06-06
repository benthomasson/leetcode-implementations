import unittest
from solution import Solution


class TestLargestSubarray(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.largestSubarray([1, 4, 5, 2, 3], 3), [5, 2, 3])

    def test_example2(self):
        self.assertEqual(self.s.largestSubarray([1, 4, 5, 2, 3], 4), [4, 5, 2, 3])

    def test_example3(self):
        self.assertEqual(self.s.largestSubarray([1, 4, 5, 2, 3], 1), [5])

    def test_k_equals_n(self):
        self.assertEqual(self.s.largestSubarray([3, 1, 2], 3), [3, 1, 2])

    def test_single_element(self):
        self.assertEqual(self.s.largestSubarray([42], 1), [42])

    def test_sorted_ascending(self):
        self.assertEqual(self.s.largestSubarray([1, 2, 3, 4, 5], 2), [4, 5])

    def test_sorted_descending(self):
        self.assertEqual(self.s.largestSubarray([5, 4, 3, 2, 1], 2), [5, 4])

    def test_max_at_last_valid_position(self):
        self.assertEqual(self.s.largestSubarray([1, 2, 5, 3, 4], 3), [5, 3, 4])

    def test_large_input(self):
        nums = list(range(1, 100001))
        result = self.s.largestSubarray(nums, 10)
        self.assertEqual(result, list(range(99991, 100001)))


if __name__ == "__main__":
    unittest.main()
