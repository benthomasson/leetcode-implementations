import unittest
from solution import Solution


class TestSumOddLengthSubarrays(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.sumOddLengthSubarrays([1, 4, 2, 5, 3]), 58)

    def test_example2(self):
        self.assertEqual(self.s.sumOddLengthSubarrays([1, 2]), 3)

    def test_example3(self):
        self.assertEqual(self.s.sumOddLengthSubarrays([10, 11, 12]), 66)

    def test_single_element(self):
        self.assertEqual(self.s.sumOddLengthSubarrays([5]), 5)

    def test_all_same(self):
        self.assertEqual(self.s.sumOddLengthSubarrays([3, 3, 3]), 24)

    def test_max_constraints(self):
        arr = [1000] * 100
        # Each element contributes 1000 * ((i+1)*(100-i)+1)//2
        expected = sum(1000 * ((i + 1) * (100 - i) + 1) // 2 for i in range(100))
        self.assertEqual(self.s.sumOddLengthSubarrays(arr), expected)


if __name__ == "__main__":
    unittest.main()
