"""Solution for LeetCode: Find Resultant Array After Removing Anagrams."""


def anagramOperations(words: list[str]) -> list[str]:
    """Remove consecutive anagrams from words, keeping the first occurrence.

    Args:
        words: List of lowercase English letter strings.

    Returns:
        List with consecutive anagrams removed.
    """
    result = [words[0]]
    for word in words[1:]:
        if sorted(word) != sorted(result[-1]):
            result.append(word)
    return result
