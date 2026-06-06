import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "implementer"))

from solution import Solution


class TestAverageSalary(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertAlmostEqual(
            self.sol.count_prefix_aligned([4000, 3000, 1000, 2000]), 2500.0, places=5
        )

    def test_example2(self):
        self.assertAlmostEqual(
            self.sol.count_prefix_aligned([1000, 2000, 3000]), 2000.0, places=5
        )

    def test_three_elements(self):
        self.assertAlmostEqual(
            self.sol.count_prefix_aligned([1000, 500000, 1000000]), 500000.0, places=5
        )

    def test_larger_array(self):
        self.assertAlmostEqual(
            self.sol.count_prefix_aligned([1000, 2000, 3000, 4000, 5000, 6000]),
            3500.0,
            places=5,
        )

    def test_boundary_min_max(self):
        self.assertAlmostEqual(
            self.sol.count_prefix_aligned([1000, 5000, 1000000]), 5000.0, places=5
        )

    def test_unsorted_input(self):
        self.assertAlmostEqual(
            self.sol.count_prefix_aligned([8000, 1000, 5000, 3000, 9000]),
            (8000 + 5000 + 3000) / 3,
            places=5,
        )

    def test_close_values(self):
        self.assertAlmostEqual(
            self.sol.count_prefix_aligned([1000, 1001, 1002]), 1001.0, places=5
        )

    def test_all_high_values(self):
        self.assertAlmostEqual(
            self.sol.count_prefix_aligned([999998, 999999, 1000000]),
            999999.0,
            places=5,
        )


if __name__ == "__main__":
    unittest.main()
