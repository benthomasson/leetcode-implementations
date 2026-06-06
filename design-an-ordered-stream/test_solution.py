"""Tests for OrderedStream."""

import unittest
from solution import OrderedStream


class TestOrderedStream(unittest.TestCase):

    def test_example(self):
        """Test the provided example from the problem."""
        os = OrderedStream(5)
        self.assertEqual(os.insert(3, "ccccc"), [])
        self.assertEqual(os.insert(1, "aaaaa"), ["aaaaa"])
        self.assertEqual(os.insert(2, "bbbbb"), ["bbbbb", "ccccc"])
        self.assertEqual(os.insert(5, "eeeee"), [])
        self.assertEqual(os.insert(4, "ddddd"), ["ddddd", "eeeee"])

    def test_sequential_insert(self):
        """Insert in order 1, 2, 3 — each returns its own value."""
        os = OrderedStream(3)
        self.assertEqual(os.insert(1, "aaaaa"), ["aaaaa"])
        self.assertEqual(os.insert(2, "bbbbb"), ["bbbbb"])
        self.assertEqual(os.insert(3, "ccccc"), ["ccccc"])

    def test_reverse_insert(self):
        """Insert in reverse — only the last insert returns everything."""
        os = OrderedStream(3)
        self.assertEqual(os.insert(3, "ccccc"), [])
        self.assertEqual(os.insert(2, "bbbbb"), [])
        self.assertEqual(os.insert(1, "aaaaa"), ["aaaaa", "bbbbb", "ccccc"])

    def test_single_element(self):
        """n=1 boundary case."""
        os = OrderedStream(1)
        self.assertEqual(os.insert(1, "abcde"), ["abcde"])

    def test_two_elements_gap_then_fill(self):
        """Insert id 2 first (gap), then id 1 fills and flushes both."""
        os = OrderedStream(2)
        self.assertEqual(os.insert(2, "bbbbb"), [])
        self.assertEqual(os.insert(1, "aaaaa"), ["aaaaa", "bbbbb"])

    def test_middle_gap(self):
        """Insert 1, skip 2, insert 3, then fill 2 to flush 2 and 3."""
        os = OrderedStream(4)
        self.assertEqual(os.insert(1, "aaaaa"), ["aaaaa"])
        self.assertEqual(os.insert(3, "ccccc"), [])
        self.assertEqual(os.insert(4, "ddddd"), [])
        self.assertEqual(os.insert(2, "bbbbb"), ["bbbbb", "ccccc", "ddddd"])

    def test_concatenation_equals_sorted(self):
        """All chunks concatenated should equal the sorted value list."""
        os = OrderedStream(5)
        all_chunks = []
        all_chunks.extend(os.insert(3, "ccccc"))
        all_chunks.extend(os.insert(1, "aaaaa"))
        all_chunks.extend(os.insert(2, "bbbbb"))
        all_chunks.extend(os.insert(5, "eeeee"))
        all_chunks.extend(os.insert(4, "ddddd"))
        self.assertEqual(all_chunks, ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"])

    def test_last_element_inserted_first(self):
        """Insert only the last element — returns empty until rest filled."""
        os = OrderedStream(3)
        self.assertEqual(os.insert(3, "ccccc"), [])
        self.assertEqual(os.insert(1, "aaaaa"), ["aaaaa"])
        self.assertEqual(os.insert(2, "bbbbb"), ["bbbbb", "ccccc"])


if __name__ == "__main__":
    unittest.main()
