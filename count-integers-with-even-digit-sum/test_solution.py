"""Tests for count integers with even digit sum."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import max_tasks


class TestMaxTasks(unittest.TestCase):
    """Test max_tasks function."""

    def test_example1(self):
        """num=4 -> 2 (only 2 and 4 have even digit sums)."""
        self.assertEqual(max_tasks(4), 2)

    def test_example2(self):
        """num=30 -> 14."""
        self.assertEqual(max_tasks(30), 14)

    def test_edge_num_1(self):
        """num=1 -> 0 (digit sum of 1 is odd)."""
        self.assertEqual(max_tasks(1), 0)

    def test_edge_num_2(self):
        """num=2 -> 1 (only 2 has even digit sum)."""
        self.assertEqual(max_tasks(2), 1)

    def test_single_digit_all(self):
        """num=9 -> 4 (2,4,6,8)."""
        self.assertEqual(max_tasks(9), 4)

    def test_num_10(self):
        """num=10 -> 4 (2,4,6,8; 10 has digit sum 1, odd)."""
        self.assertEqual(max_tasks(10), 4)

    def test_num_11(self):
        """num=11 -> 5 (adds 11: 1+1=2, even)."""
        self.assertEqual(max_tasks(11), 5)

    def test_boundary_1000(self):
        """num=1000 -> 499 (1000 has digit sum 1, odd)."""
        self.assertEqual(max_tasks(1000), 499)

    def test_num_999(self):
        """num=999 -> 499 (9+9+9=27, odd)."""
        self.assertEqual(max_tasks(999), 499)

    def test_num_100(self):
        """num=100 -> 49."""
        self.assertEqual(max_tasks(100), 49)


if __name__ == "__main__":
    unittest.main()
