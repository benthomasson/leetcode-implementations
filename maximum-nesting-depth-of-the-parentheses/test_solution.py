import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))

from solution import Solution
import unittest


class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.maxDepth("(1+(2*3)+((8)/4))+1"), 3)

    def test_example2(self):
        self.assertEqual(self.sol.maxDepth("(1)+((2))+(((3)))"), 3)

    def test_single_char(self):
        self.assertEqual(self.sol.maxDepth("1"), 0)

    def test_no_parens(self):
        self.assertEqual(self.sol.maxDepth("1+2+3"), 0)

    def test_single_pair(self):
        self.assertEqual(self.sol.maxDepth("(1)"), 1)

    def test_deeply_nested(self):
        self.assertEqual(self.sol.maxDepth("((((1))))"), 4)

    def test_sequential_groups(self):
        self.assertEqual(self.sol.maxDepth("(1)+(2)+(3)"), 1)

    def test_mixed_depths(self):
        self.assertEqual(self.sol.maxDepth("(1)+((2+3))"), 2)


if __name__ == "__main__":
    unittest.main()
