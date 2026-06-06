def mergeAlternately(word1: str, word2: str) -> str:
    """Merge two strings by adding letters in alternating order.

    Characters are interleaved starting with word1. If one string is longer
    than the other, the remaining characters are appended to the end.

    Args:
        word1: The first string to merge (starts first).
        word2: The second string to merge.

    Returns:
        The merged string with alternating characters.

    Examples:
        >>> mergeAlternately("abc", "pqr")
        'apbqcr'
        >>> mergeAlternately("ab", "pqrs")
        'apbqrs'
        >>> mergeAlternately("abcd", "pq")
        'apbqcd'
    """
    result = []
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
    return "".join(result)
