import unittest
from solution import Solution


class TestRelativeSortArray(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(
            self.s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]),
            [2,2,2,1,4,3,3,9,6,7,19],
        )

    def test_example2(self):
        self.assertEqual(
            self.s.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]),
            [22,28,8,6,17,44],
        )

    def test_all_in_arr2(self):
        self.assertEqual(self.s.relativeSortArray([3,1,2], [2,3,1]), [2,3,1])

    def test_no_overlap_beyond_arr2(self):
        self.assertEqual(self.s.relativeSortArray([5,3,1], [1]), [1,3,5])

    def test_single_element(self):
        self.assertEqual(self.s.relativeSortArray([1], [1]), [1])

    def test_duplicates(self):
        self.assertEqual(
            self.s.relativeSortArray([2,2,2,1,1], [1,2]),
            [1,1,2,2,2],
        )

    def test_boundary_values(self):
        self.assertEqual(
            self.s.relativeSortArray([1000,0,500,0], [0,1000]),
            [0,0,1000,500],
        )


if __name__ == "__main__":
    unittest.main()
