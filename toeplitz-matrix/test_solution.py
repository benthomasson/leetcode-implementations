import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementer'))
from solution import Solution

import unittest

class TestToeplitzMatrix(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1_toeplitz(self):
        assert self.s.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]) is True

    def test_example2_not_toeplitz(self):
        assert self.s.isToeplitzMatrix([[1,2],[2,2]]) is False

    def test_single_element(self):
        assert self.s.isToeplitzMatrix([[5]]) is True

    def test_single_row(self):
        assert self.s.isToeplitzMatrix([[1,2,3,4]]) is True

    def test_single_column(self):
        assert self.s.isToeplitzMatrix([[1],[2],[3]]) is True

    def test_all_same(self):
        assert self.s.isToeplitzMatrix([[7,7],[7,7],[7,7]]) is True

    def test_mismatch_last_position(self):
        assert self.s.isToeplitzMatrix([[1,2],[3,2]]) is False

    def test_2x2_toeplitz(self):
        assert self.s.isToeplitzMatrix([[1,2],[3,1]]) is True

if __name__ == '__main__':
    unittest.main()
