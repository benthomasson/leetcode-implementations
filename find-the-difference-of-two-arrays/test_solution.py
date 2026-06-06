import unittest
from solution import Solution


class TestFindDifference(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        result = self.s.findDifference([1, 2, 3], [2, 4, 6])
        self.assertCountEqual(result[0], [1, 3])
        self.assertCountEqual(result[1], [4, 6])

    def test_example2(self):
        result = self.s.findDifference([1, 2, 3, 3], [1, 1, 2, 2])
        self.assertCountEqual(result[0], [3])
        self.assertCountEqual(result[1], [])

    def test_no_overlap(self):
        result = self.s.findDifference([1, 2], [3, 4])
        self.assertCountEqual(result[0], [1, 2])
        self.assertCountEqual(result[1], [3, 4])

    def test_complete_overlap(self):
        result = self.s.findDifference([1, 2, 3], [1, 2, 3])
        self.assertCountEqual(result[0], [])
        self.assertCountEqual(result[1], [])

    def test_single_elements(self):
        result = self.s.findDifference([1], [1])
        self.assertCountEqual(result[0], [])
        self.assertCountEqual(result[1], [])

    def test_negative_numbers(self):
        result = self.s.findDifference([-1, -2, 3], [-2, 4])
        self.assertCountEqual(result[0], [-1, 3])
        self.assertCountEqual(result[1], [4])

    def test_all_duplicates(self):
        result = self.s.findDifference([5, 5, 5], [5, 5])
        self.assertCountEqual(result[0], [])
        self.assertCountEqual(result[1], [])


if __name__ == "__main__":
    unittest.main()
