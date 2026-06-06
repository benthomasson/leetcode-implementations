"""Tests for find_pivot solution."""

import unittest

from solution import find_pivot


class TestFindPivot(unittest.TestCase):
    """Test cases for find_pivot function."""

    def test_example_1(self):
        """n=8 should return pivot 6."""
        self.assertEqual(find_pivot(8), 6)

    def test_example_2(self):
        """n=1 should return pivot 1."""
        self.assertEqual(find_pivot(1), 1)

    def test_example_3(self):
        """n=4 should return no pivot."""
        self.assertEqual(find_pivot(4), -1)

    def test_no_pivot_small(self):
        """n=2 and n=3 have no pivot."""
        self.assertEqual(find_pivot(2), -1)
        self.assertEqual(find_pivot(3), -1)

    def test_large_input(self):
        """n=1000 should return -1 (no pivot exists)."""
        self.assertEqual(find_pivot(1000), -1)

    def test_pivot_exists_values(self):
        """Verify known values where a pivot exists by brute force."""
        # Brute-force find all pivots for n in 1..1000
        pivots_found = {}
        for n in range(1, 1001):
            total = n * (n + 1) // 2
            for x in range(1, n + 1):
                left = x * (x + 1) // 2
                right = total - x * (x - 1) // 2
                if left == right:
                    pivots_found[n] = x
                    break

        # Verify find_pivot matches brute force for all n
        for n in range(1, 1001):
            expected = pivots_found.get(n, -1)
            self.assertEqual(find_pivot(n), expected, f"Failed for n={n}")

    def test_pivot_sum_property(self):
        """When a pivot exists, verify the sum property holds."""
        for n in range(1, 1001):
            x = find_pivot(n)
            if x != -1:
                left_sum = x * (x + 1) // 2
                right_sum = n * (n + 1) // 2 - x * (x - 1) // 2
                self.assertEqual(left_sum, right_sum,
                                 f"Sum property violated for n={n}, x={x}")


if __name__ == "__main__":
    unittest.main()
