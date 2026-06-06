"""Goat Latin sentence converter."""

import unittest


def to_goat_latin(sentence: str) -> str:
    """Convert a sentence to Goat Latin.

    Args:
        sentence: Space-separated words of English letters.

    Returns:
        The sentence converted to Goat Latin.
    """
    vowels = set("aeiouAEIOU")
    result = []
    for i, word in enumerate(sentence.split(), 1):
        if word[0] in vowels:
            result.append(word + "ma" + "a" * i)
        else:
            result.append(word[1:] + word[0] + "ma" + "a" * i)
    return " ".join(result)


class TestToGoatLatin(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(
            to_goat_latin("I speak Goat Latin"),
            "Imaa peaksmaaa oatGmaaaa atinLmaaaaa",
        )

    def test_example2(self):
        self.assertEqual(
            to_goat_latin("The quick brown fox jumped over the lazy dog"),
            "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
        )

    def test_single_vowel_word(self):
        self.assertEqual(to_goat_latin("apple"), "applemaa")

    def test_single_consonant_word(self):
        self.assertEqual(to_goat_latin("goat"), "oatgmaa")

    def test_single_letter_vowel(self):
        self.assertEqual(to_goat_latin("I"), "Imaa")

    def test_single_letter_consonant(self):
        self.assertEqual(to_goat_latin("b"), "bmaa")

    def test_uppercase_vowel_start(self):
        self.assertEqual(to_goat_latin("Each"), "Eachmaa")

    def test_all_vowel_starts(self):
        self.assertEqual(
            to_goat_latin("a e i o u"),
            "amaa emaaa imaaaa omaaaaa umaaaaaa",
        )


if __name__ == "__main__":
    unittest.main()
