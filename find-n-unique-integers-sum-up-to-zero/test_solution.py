import unittest
from solution import Solution


class TestSumZero(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def _validate(self, n):
        result = self.sol.sumZero(n)
        self.assertEqual(len(result), n)
        self.assertEqual(len(set(result)), n, "Elements must be unique")
        self.assertEqual(sum(result), 0, "Elements must sum to zero")

    def test_n1(self):
        self._validate(1)

    def test_n2(self):
        self._validate(2)

    def test_n3(self):
        self._validate(3)

    def test_n5(self):
        self._validate(5)

    def test_n1000(self):
        self._validate(1000)


if __name__ == "__main__":
    unittest.main()
