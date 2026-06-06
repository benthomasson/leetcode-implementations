import unittest
from solution import Solution


class TestTargetIndices(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.targetIndices([1, 2, 5, 2, 3], 2), [1, 2])

    def test_example2(self):
        self.assertEqual(self.s.targetIndices([1, 2, 5, 2, 3], 3), [3])

    def test_example3(self):
        self.assertEqual(self.s.targetIndices([1, 2, 5, 2, 3], 5), [4])

    def test_target_absent(self):
        self.assertEqual(self.s.targetIndices([1, 2, 3], 4), [])

    def test_all_equal_target(self):
        self.assertEqual(self.s.targetIndices([5, 5, 5], 5), [0, 1, 2])

    def test_single_match(self):
        self.assertEqual(self.s.targetIndices([7], 7), [0])

    def test_single_no_match(self):
        self.assertEqual(self.s.targetIndices([7], 3), [])

    def test_target_is_min(self):
        self.assertEqual(self.s.targetIndices([1, 3, 5], 1), [0])

    def test_target_is_max(self):
        self.assertEqual(self.s.targetIndices([1, 3, 5], 5), [2])


if __name__ == "__main__":
    unittest.main()
