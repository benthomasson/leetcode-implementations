"""Tests for Sentence Similarity solution."""

import sys
import unittest

sys.path.insert(0, "../implementer")
from solution import areSentencesSimilar


class TestAreSentencesSimilar(unittest.TestCase):
    # LeetCode examples
    def test_example1(self):
        self.assertTrue(
            areSentencesSimilar(
                ["great", "acting", "skills"],
                ["fine", "drama", "talent"],
                [["great", "fine"], ["drama", "acting"], ["skills", "talent"]],
            )
        )

    def test_example2(self):
        self.assertTrue(areSentencesSimilar(["great"], ["great"], []))

    def test_example3(self):
        self.assertFalse(
            areSentencesSimilar(
                ["great"], ["doubleplus", "good"], [["great", "doubleplus"]]
            )
        )

    # Edge cases
    def test_empty_sentences(self):
        self.assertTrue(areSentencesSimilar([], [], []))

    def test_no_transitivity(self):
        self.assertFalse(
            areSentencesSimilar(["a"], ["c"], [["a", "b"], ["b", "c"]])
        )

    def test_symmetric_lookup(self):
        self.assertTrue(areSentencesSimilar(["x"], ["y"], [["y", "x"]]))

    def test_self_similar_no_pair_needed(self):
        self.assertTrue(areSentencesSimilar(["hello", "world"], ["hello", "world"], []))

    def test_all_different_no_pairs(self):
        self.assertFalse(areSentencesSimilar(["a", "b"], ["c", "d"], []))

    def test_case_sensitive(self):
        self.assertFalse(areSentencesSimilar(["Hello"], ["hello"], []))


if __name__ == "__main__":
    unittest.main()
