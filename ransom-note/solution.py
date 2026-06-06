from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    """Return True if ransomNote can be constructed from magazine letters.

    Args:
        ransom_note: The string to construct.
        magazine: The string providing available letters.

    Returns:
        True if ransom_note can be built using magazine's letters (each used once).
    """
    return not (Counter(ransom_note) - Counter(magazine))
