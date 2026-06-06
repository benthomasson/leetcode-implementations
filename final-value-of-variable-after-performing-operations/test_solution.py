import unittest
from solution import max_value


class TestMaxValue(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(max_value(["--X", "X++", "X++"]), 1)

    def test_example_2(self):
        self.assertEqual(max_value(["++X", "++X", "X++"]), 3)

    def test_example_3(self):
        self.assertEqual(max_value(["X++", "++X", "--X", "X--"]), 0)

    def test_all_increment(self):
        self.assertEqual(max_value(["++X", "X++", "++X"]), 3)

    def test_all_decrement(self):
        self.assertEqual(max_value(["--X", "X--", "--X"]), -3)

    def test_single_increment(self):
        self.assertEqual(max_value(["X++"]), 1)

    def test_single_decrement(self):
        self.assertEqual(max_value(["--X"]), -1)


if __name__ == "__main__":
    unittest.main()
