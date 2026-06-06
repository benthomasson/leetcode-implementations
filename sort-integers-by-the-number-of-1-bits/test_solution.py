import unittest
from solution import Solution, min_moves_to_palindrome


class TestSortByBits(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.sortByBits([0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])

    def test_example2(self):
        self.assertEqual(self.s.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]),
                         [1,2,4,8,16,32,64,128,256,512,1024])

    def test_single_element(self):
        self.assertEqual(self.s.sortByBits([5]), [5])

    def test_all_zeros(self):
        self.assertEqual(self.s.sortByBits([0,0,0]), [0,0,0])

    def test_same_bit_count(self):
        self.assertEqual(self.s.sortByBits([3,6,5]), [3,5,6])

    def test_max_value(self):
        self.assertEqual(self.s.sortByBits([10000, 0]), [0, 10000])

    def test_alias(self):
        self.assertEqual(min_moves_to_palindrome([0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])


if __name__ == '__main__':
    unittest.main()
