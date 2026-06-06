import unittest
from solution import Solution


class TestBuildArray(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.buildArray([0, 2, 1, 5, 3, 4]), [0, 1, 2, 4, 5, 3])

    def test_example2(self):
        self.assertEqual(self.s.buildArray([5, 0, 1, 2, 3, 4]), [4, 5, 0, 1, 2, 3])

    def test_single_element(self):
        self.assertEqual(self.s.buildArray([0]), [0])

    def test_identity(self):
        self.assertEqual(self.s.buildArray([0, 1, 2, 3]), [0, 1, 2, 3])

    def test_reverse(self):
        self.assertEqual(self.s.buildArray([3, 2, 1, 0]), [0, 1, 2, 3])

    def test_large(self):
        n = 1000
        nums = list(range(1, n)) + [0]  # cyclic shift
        result = self.s.buildArray(nums[:])
        expected = [nums[nums[i]] for i in range(n)]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
