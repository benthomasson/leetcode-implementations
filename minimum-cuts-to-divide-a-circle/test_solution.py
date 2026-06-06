import unittest
from solution import min_cuts


class TestMinCuts(unittest.TestCase):
    def test_example_1_four_slices(self):
        """Test LeetCode Example 1: 4 slices requires 2 cuts."""
        self.assertEqual(min_cuts(4), 2)

    def test_example_2_three_slices(self):
        """Test LeetCode Example 2: 3 slices requires 3 cuts."""
        self.assertEqual(min_cuts(3), 3)

    def test_edge_case_one_slice(self):
        """Test minimum input: 1 slice requires 0 cuts."""
        self.assertEqual(min_cuts(1), 0)

    def test_edge_case_two_slices(self):
        """Test smallest even number: 2 slices requires 1 cut."""
        self.assertEqual(min_cuts(2), 1)

    def test_even_numbers_small(self):
        """Test small even numbers follow n/2 pattern."""
        self.assertEqual(min_cuts(6), 3)
        self.assertEqual(min_cuts(8), 4)
        self.assertEqual(min_cuts(10), 5)

    def test_even_numbers_large(self):
        """Test larger even numbers follow n/2 pattern."""
        self.assertEqual(min_cuts(50), 25)
        self.assertEqual(min_cuts(98), 49)

    def test_odd_numbers_small(self):
        """Test small odd numbers require n cuts."""
        self.assertEqual(min_cuts(5), 5)
        self.assertEqual(min_cuts(7), 7)
        self.assertEqual(min_cuts(9), 9)

    def test_odd_numbers_large(self):
        """Test larger odd numbers require n cuts."""
        self.assertEqual(min_cuts(51), 51)
        self.assertEqual(min_cuts(97), 97)

    def test_boundary_max_even(self):
        """Test maximum constraint value (even): 100 slices."""
        self.assertEqual(min_cuts(100), 50)

    def test_boundary_max_odd(self):
        """Test maximum constraint value (odd): 99 slices."""
        self.assertEqual(min_cuts(99), 99)


if __name__ == "__main__":
    unittest.main()
