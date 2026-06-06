import unittest
from solution import findShortestSubArray


class TestFindShortestSubArray(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(findShortestSubArray([1, 2, 2, 3, 1]), 2)

    def test_example2(self):
        self.assertEqual(findShortestSubArray([1, 2, 2, 3, 1, 4, 2]), 6)

    def test_single_element(self):
        self.assertEqual(findShortestSubArray([5]), 1)

    def test_all_identical(self):
        self.assertEqual(findShortestSubArray([3, 3, 3]), 3)

    def test_all_unique(self):
        self.assertEqual(findShortestSubArray([1, 2, 3, 4]), 1)

    def test_tie_different_spans(self):
        # 1 appears twice (span 5), 2 appears twice (span 2) — answer is 2
        self.assertEqual(findShortestSubArray([1, 2, 2, 3, 1]), 2)

    def test_degree_at_edges(self):
        self.assertEqual(findShortestSubArray([1, 0, 0, 0, 1]), 3)

    def test_large_input(self):
        nums = list(range(50000))
        self.assertEqual(findShortestSubArray(nums), 1)


if __name__ == "__main__":
    unittest.main()
