import unittest
from solution import Solution


class TestIntersection(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(sorted(self.s.intersection([1, 2, 2, 1], [2, 2])), [2])

    def test_example2(self):
        self.assertEqual(sorted(self.s.intersection([4, 9, 5], [9, 4, 9, 8, 4])), [4, 9])

    def test_no_overlap(self):
        self.assertEqual(self.s.intersection([1, 2], [3, 4]), [])

    def test_complete_overlap(self):
        self.assertEqual(sorted(self.s.intersection([1, 2, 3], [1, 2, 3])), [1, 2, 3])

    def test_single_element_match(self):
        self.assertEqual(self.s.intersection([1], [1]), [1])

    def test_single_element_no_match(self):
        self.assertEqual(self.s.intersection([1], [2]), [])

    def test_all_duplicates(self):
        self.assertEqual(self.s.intersection([1, 1, 1], [1, 1]), [1])

    def test_large_input(self):
        nums1 = list(range(1000))
        nums2 = list(range(500, 1001))
        self.assertEqual(sorted(self.s.intersection(nums1, nums2)), list(range(500, 1000)))


if __name__ == "__main__":
    unittest.main()
