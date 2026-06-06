"""Sentence Similarity - LeetCode"""

import unittest


def areSentencesSimilar(
    sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]
) -> bool:
    """Check if two sentences are similar based on given word pairs.

    Args:
        sentence1: First sentence as list of words.
        sentence2: Second sentence as list of words.
        similarPairs: List of [word1, word2] pairs indicating similarity.

    Returns:
        True if sentences are similar, False otherwise.
    """
    if len(sentence1) != len(sentence2):
        return False

    similar_set = set()
    for x, y in similarPairs:
        similar_set.add((x, y))
        similar_set.add((y, x))

    return all(
        w1 == w2 or (w1, w2) in similar_set
        for w1, w2 in zip(sentence1, sentence2)
    )


class TestAreSentencesSimilar(unittest.TestCase):
    def test_basic_similar(self):
        self.assertTrue(
            areSentencesSimilar(
                ["great", "acting", "skills"],
                ["fine", "drama", "talent"],
                [["great", "fine"], ["drama", "acting"], ["skills", "talent"]],
            )
        )

    def test_identical_words_no_pairs(self):
        self.assertTrue(areSentencesSimilar(["great"], ["great"], []))

    def test_different_lengths(self):
        self.assertFalse(
            areSentencesSimilar(
                ["great"], ["doubleplus", "good"], [["great", "doubleplus"]]
            )
        )

    def test_empty_sentences(self):
        self.assertTrue(areSentencesSimilar([], [], []))

    def test_not_similar(self):
        self.assertFalse(areSentencesSimilar(["a"], ["b"], []))

    def test_reverse_pair_direction(self):
        self.assertTrue(
            areSentencesSimilar(["a"], ["b"], [["b", "a"]])
        )

    def test_no_transitivity(self):
        self.assertFalse(
            areSentencesSimilar(["a"], ["c"], [["a", "b"], ["b", "c"]])
        )

    def test_multiple_words_one_mismatch(self):
        self.assertFalse(
            areSentencesSimilar(
                ["a", "b", "c"],
                ["a", "b", "d"],
                [],
            )
        )


if __name__ == "__main__":
    unittest.main()
