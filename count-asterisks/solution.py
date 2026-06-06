def count_stars_except_between_pair(s: str) -> int:
    """Count asterisks in s, excluding those between paired vertical bars.

    Args:
        s: String of lowercase letters, '|', and '*' with even number of '|'.

    Returns:
        Number of '*' outside paired '|' segments.
    """
    count = 0
    inside = False
    for ch in s:
        if ch == '|':
            inside = not inside
        elif ch == '*' and not inside:
            count += 1
    return count
