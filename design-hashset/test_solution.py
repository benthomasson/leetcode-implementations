"""Tests for MyHashSet implementation."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import MyHashSet


class TestMyHashSet(unittest.TestCase):

    def test_leetcode_example(self):
        """Exact sequence from the problem statement."""
        s = MyHashSet()
        s.add(1)
        s.add(2)
        self.assertTrue(s.contains(1))
        self.assertFalse(s.contains(3))
        s.add(2)
        self.assertTrue(s.contains(2))
        s.remove(2)
        self.assertFalse(s.contains(2))

    def test_empty_set(self):
        """Contains and remove on empty set."""
        s = MyHashSet()
        self.assertFalse(s.contains(0))
        s.remove(0)  # no-op, should not raise

    def test_boundary_min(self):
        """Key = 0 (minimum constraint)."""
        s = MyHashSet()
        s.add(0)
        self.assertTrue(s.contains(0))
        s.remove(0)
        self.assertFalse(s.contains(0))

    def test_boundary_max(self):
        """Key = 10^6 (maximum constraint)."""
        s = MyHashSet()
        s.add(1_000_000)
        self.assertTrue(s.contains(1_000_000))
        s.remove(1_000_000)
        self.assertFalse(s.contains(1_000_000))

    def test_duplicate_add(self):
        """Adding same key twice should not create duplicates."""
        s = MyHashSet()
        s.add(42)
        s.add(42)
        s.remove(42)
        self.assertFalse(s.contains(42))

    def test_collision_handling(self):
        """Keys 0 and 769 collide (both hash to bucket 0)."""
        s = MyHashSet()
        s.add(0)
        s.add(769)
        self.assertTrue(s.contains(0))
        self.assertTrue(s.contains(769))
        s.remove(0)
        self.assertFalse(s.contains(0))
        self.assertTrue(s.contains(769))

    def test_add_remove_readd(self):
        """Re-adding a removed key should work."""
        s = MyHashSet()
        s.add(10)
        s.remove(10)
        self.assertFalse(s.contains(10))
        s.add(10)
        self.assertTrue(s.contains(10))

    def test_multiple_keys(self):
        """Add several keys, verify all present, remove some."""
        s = MyHashSet()
        for k in range(10):
            s.add(k)
        for k in range(10):
            self.assertTrue(s.contains(k))
        s.remove(5)
        self.assertFalse(s.contains(5))
        self.assertTrue(s.contains(4))
        self.assertTrue(s.contains(6))


if __name__ == "__main__":
    unittest.main()
