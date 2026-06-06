import unittest
from solution import Solution


class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one_step(self):
        self.assertEqual(self.s.climbStairs(1), 1)

    def test_two_steps(self):
        self.assertEqual(self.s.climbStairs(2), 2)

    def test_three_steps(self):
        self.assertEqual(self.s.climbStairs(3), 3)

    def test_ten_steps(self):
        self.assertEqual(self.s.climbStairs(10), 89)

    def test_max_constraint(self):
        self.assertEqual(self.s.climbStairs(45), 1134903170)


if __name__ == "__main__":
    unittest.main()
