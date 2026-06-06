import unittest
from solution import Solution


class TestPivotIndex(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.pivotIndex([1, 7, 3, 6, 5, 6]), 3)

    def test_example2(self):
        self.assertEqual(self.s.pivotIndex([1, 2, 3]), -1)

    def test_example3(self):
        self.assertEqual(self.s.pivotIndex([2, 1, -1]), 0)

    def test_single_element(self):
        self.assertEqual(self.s.pivotIndex([1]), 0)

    def test_pivot_at_end(self):
        self.assertEqual(self.s.pivotIndex([-1, 1, 0]), 2)

    def test_all_zeros(self):
        self.assertEqual(self.s.pivotIndex([0, 0, 0]), 0)

    def test_negatives(self):
        self.assertEqual(self.s.pivotIndex([-1, -1, -1, -1, 0, 1]), 1)

    def test_no_pivot(self):
        self.assertEqual(self.s.pivotIndex([1, 2, 3, 4, 5]), -1)


if __name__ == "__main__":
    unittest.main()
