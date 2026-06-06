import unittest
from solution import repeated_n_times


class TestRepeatedNTimes(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(repeated_n_times([1, 2, 3, 3]), 3)

    def test_example2(self):
        self.assertEqual(repeated_n_times([2, 1, 2, 5, 3, 2]), 2)

    def test_example3(self):
        self.assertEqual(repeated_n_times([5, 1, 5, 2, 5, 3, 5, 4]), 5)

    def test_min_array(self):
        self.assertEqual(repeated_n_times([1, 1]), 1)

    def test_boundary_values(self):
        self.assertEqual(repeated_n_times([0, 10000, 0]), 0)

    def test_repeated_at_end(self):
        self.assertEqual(repeated_n_times([1, 2, 3, 4, 5, 5]), 5)


if __name__ == "__main__":
    unittest.main()
