import unittest
import sys
sys.path.insert(0, "../implementer")

from solution import Solution


class TestPrefixesDivBy5(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # LeetCode examples
    def test_example1(self):
        self.assertEqual(self.s.prefixesDivBy5([0, 1, 1]), [True, False, False])

    def test_example2(self):
        self.assertEqual(self.s.prefixesDivBy5([1, 1, 1]), [False, False, False])

    # Edge cases
    def test_single_zero(self):
        self.assertEqual(self.s.prefixesDivBy5([0]), [True])

    def test_single_one(self):
        self.assertEqual(self.s.prefixesDivBy5([1]), [False])

    def test_all_zeros(self):
        self.assertEqual(self.s.prefixesDivBy5([0, 0, 0, 0]), [True, True, True, True])

    # Divisibility checks
    def test_five_binary_101(self):
        # 1->1, 10->2, 101->5
        self.assertEqual(self.s.prefixesDivBy5([1, 0, 1]), [False, False, True])

    def test_ten_binary_1010(self):
        # 1->1, 10->2, 101->5, 1010->10
        self.assertEqual(self.s.prefixesDivBy5([1, 0, 1, 0]), [False, False, True, True])

    def test_fifteen_binary_1111(self):
        # 1->1, 11->3, 111->7, 1111->15
        self.assertEqual(self.s.prefixesDivBy5([1, 1, 1, 1]), [False, False, False, True])

    def test_twentyfive_binary_11001(self):
        # 1->1, 11->3, 110->6, 1100->12, 11001->25
        self.assertEqual(self.s.prefixesDivBy5([1, 1, 0, 0, 1]), [False, False, False, False, True])

    def test_large_input(self):
        # Performance: 10^5 elements should complete quickly
        nums = [0] * 100000
        result = self.s.prefixesDivBy5(nums)
        self.assertEqual(len(result), 100000)
        self.assertTrue(all(result))  # all zeros -> all divisible by 5


if __name__ == "__main__":
    unittest.main()
