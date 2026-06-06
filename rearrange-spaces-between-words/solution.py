"""LeetCode: Rearrange Spaces Between Words."""


def reorderSpaces(text: str) -> str:
    """Rearrange spaces evenly between words, extras at end.

    Args:
        text: String of words separated by spaces.

    Returns:
        String with spaces evenly distributed between words.
    """
    total_spaces = text.count(' ')
    words = text.split()

    if len(words) == 1:
        return words[0] + ' ' * total_spaces

    between, extra = divmod(total_spaces, len(words) - 1)
    return (' ' * between).join(words) + ' ' * extra
