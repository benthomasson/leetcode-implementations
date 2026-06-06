"""Design HashSet using bucket array with separate chaining."""

import unittest


class MyHashSet:
    """HashSet implementation using a fixed-size bucket array with separate chaining."""

    def __init__(self):
        self._num_buckets = 769
        self._buckets: list[list[int]] = [[] for _ in range(self._num_buckets)]

    def _hash(self, key: int) -> int:
        return key % self._num_buckets

    def add(self, key: int) -> None:
        """Add key to the set."""
        bucket = self._buckets[self._hash(key)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        """Remove key from the set. No-op if absent."""
        bucket = self._buckets[self._hash(key)]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        """Return True if key is in the set."""
        return key in self._buckets[self._hash(key)]


class TestMyHashSet(unittest.TestCase):

    def test_example(self):
        s = MyHashSet()
        s.add(1)
        s.add(2)
        self.assertTrue(s.contains(1))
        self.assertFalse(s.contains(3))
        s.add(2)
        self.assertTrue(s.contains(2))
        s.remove(2)
        self.assertFalse(s.contains(2))

    def test_duplicate_add(self):
        s = MyHashSet()
        s.add(5)
        s.add(5)
        s.remove(5)
        self.assertFalse(s.contains(5))

    def test_remove_nonexistent(self):
        s = MyHashSet()
        s.remove(99)  # should not raise

    def test_boundary_values(self):
        s = MyHashSet()
        s.add(0)
        s.add(10**6)
        self.assertTrue(s.contains(0))
        self.assertTrue(s.contains(10**6))
        s.remove(0)
        self.assertFalse(s.contains(0))

    def test_collision(self):
        s = MyHashSet()
        # 0 and 769 hash to the same bucket
        s.add(0)
        s.add(769)
        self.assertTrue(s.contains(0))
        self.assertTrue(s.contains(769))
        s.remove(0)
        self.assertFalse(s.contains(0))
        self.assertTrue(s.contains(769))

    def test_empty_contains(self):
        s = MyHashSet()
        self.assertFalse(s.contains(1))


if __name__ == "__main__":
    unittest.main()
