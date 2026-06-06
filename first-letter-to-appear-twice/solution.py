def first_letter_to_appear_twice(s: str) -> str:
    """Return the first letter that appears twice in s.

    Args:
        s: A string of lowercase English letters with at least one repeated letter.

    Returns:
        The first letter whose second occurrence comes earliest.
    """
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)
