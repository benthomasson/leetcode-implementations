"""Count substrings with only one distinct letter."""


def count_letters(s: str) -> int:
    """Count substrings containing only one distinct letter.

    Groups consecutive identical characters and sums n*(n+1)/2 for each group.

    Args:
        s: Input string of lowercase English letters.

    Returns:
        Number of substrings with exactly one distinct letter.
    """
    result = 0
    i = 0
    while i < len(s):
        count = 1
        while i + count < len(s) and s[i + count] == s[i]:
            count += 1
        result += count * (count + 1) // 2
        i += count
    return result
