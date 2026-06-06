import unittest
from solution import Solution


class TestIsThreeDivisors(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertFalse(self.sol.isThreeDivisors(2))
        self.assertTrue(self.sol.isThreeDivisors(4))

    def test_one(self):
        self.assertFalse(self.sol.isThreeDivisors(1))

    def test_prime_squares(self):
        # 2²=4, 3²=9, 5²=25, 7²=49
        for n in [4, 9, 25, 49]:
            self.assertTrue(self.sol.isThreeDivisors(n), f"n={n}")

    def test_non_prime_squares(self):
        # 4²=16 (4 not prime), 6²=36, 10²=100
        for n in [16, 36, 100]:
            self.assertFalse(self.sol.isThreeDivisors(n), f"n={n}")

    def test_non_squares(self):
        for n in [2, 3, 5, 6, 7, 8, 10, 12, 15]:
            self.assertFalse(self.sol.isThreeDivisors(n), f"n={n}")

    def test_upper_bound(self):
        # 97²=9409 (97 is prime) -> True
        self.assertTrue(self.sol.isThreeDivisors(9409))
        # 100²=10000 (100 not prime) -> False
        self.assertFalse(self.sol.isThreeDivisors(10000))


if __name__ == "__main__":
    unittest.main()
