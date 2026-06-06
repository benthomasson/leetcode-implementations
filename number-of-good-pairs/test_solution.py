import unittest
from solution import Solution


class TestNumIdenticalPairs(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.numIdenticalPairs([1, 2, 3, 1, 1, 3]), 4)

    def test_example2(self):
        self.assertEqual(self.s.numIdenticalPairs([1, 1, 1, 1]), 6)

    def test_example3(self):
        self.assertEqual(self.s.numIdenticalPairs([1, 2, 3]), 0)

    def test_single_element(self):
        self.assertEqual(self.s.numIdenticalPairs([1]), 0)

    def test_two_same(self):
        self.assertEqual(self.s.numIdenticalPairs([5, 5]), 1)

    def test_two_different(self):
        self.assertEqual(self.s.numIdenticalPairs([1, 2]), 0)

    def test_large_all_same(self):
        # 100 identical elements -> C(100,2) = 4950
        self.assertEqual(self.s.numIdenticalPairs([1] * 100), 4950)


if __name__ == "__main__":
    unittest.main()
