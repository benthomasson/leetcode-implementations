import unittest
from solution import Solution


class TestFindLengthOfLCIS(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.findLengthOfLCIS([1, 3, 5, 4, 7]), 3)

    def test_example2(self):
        self.assertEqual(self.s.findLengthOfLCIS([2, 2, 2, 2, 2]), 1)

    def test_single_element(self):
        self.assertEqual(self.s.findLengthOfLCIS([1]), 1)

    def test_two_increasing(self):
        self.assertEqual(self.s.findLengthOfLCIS([1, 2]), 2)

    def test_two_equal(self):
        self.assertEqual(self.s.findLengthOfLCIS([1, 1]), 1)

    def test_two_decreasing(self):
        self.assertEqual(self.s.findLengthOfLCIS([2, 1]), 1)

    def test_all_increasing(self):
        self.assertEqual(self.s.findLengthOfLCIS([1, 2, 3, 4, 5]), 5)

    def test_all_decreasing(self):
        self.assertEqual(self.s.findLengthOfLCIS([5, 4, 3, 2, 1]), 1)

    def test_increasing_at_end(self):
        self.assertEqual(self.s.findLengthOfLCIS([5, 4, 3, 2, 3, 4, 5]), 4)

    def test_negative_numbers(self):
        self.assertEqual(self.s.findLengthOfLCIS([-3, -2, -1, 0, -1]), 4)

    def test_alternating(self):
        self.assertEqual(self.s.findLengthOfLCIS([1, 2, 1, 2, 1, 2]), 2)


if __name__ == "__main__":
    unittest.main()
