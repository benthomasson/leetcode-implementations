def count_vowel_substrings(word: str) -> int:
    """Count substrings that contain only vowels and include all five vowels.

    Args:
        word: Input string of lowercase English letters.

    Returns:
        Number of vowel substrings containing all five vowels.
    """
    vowels = set("aeiou")
    count = 0
    n = len(word)
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if word[j] not in vowels:
                break
            seen.add(word[j])
            if len(seen) == 5:
                count += 1
    return count
