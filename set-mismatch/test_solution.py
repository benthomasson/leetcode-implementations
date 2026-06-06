import unittest
from solution import Solution


class TestFindErrorNums(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.findErrorNums([1, 2, 2, 4]), [2, 3])

    def test_example2(self):
        self.assertEqual(self.s.findErrorNums([1, 1]), [1, 2])

    def test_duplicate_first(self):
        self.assertEqual(self.s.findErrorNums([1, 1, 3]), [1, 2])

    def test_duplicate_last(self):
        self.assertEqual(self.s.findErrorNums([1, 2, 3, 3]), [3, 4])

    def test_missing_first(self):
        self.assertEqual(self.s.findErrorNums([2, 2]), [2, 1])

    def test_missing_last(self):
        self.assertEqual(self.s.findErrorNums([1, 1]), [1, 2])

    def test_larger(self):
        self.assertEqual(self.s.findErrorNums([1, 3, 3, 4, 5]), [3, 2])

    def test_unsorted(self):
        self.assertEqual(self.s.findErrorNums([3, 2, 2, 1]), [2, 4])


if __name__ == "__main__":
    unittest.main()
