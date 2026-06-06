"""Assign Cookies - LeetCode 455."""


def find_content_children(g: list[int], s: list[int]) -> int:
    """Maximize the number of content children by assigning cookies greedily.

    Args:
        g: Greed factors of children.
        s: Sizes of cookies.

    Returns:
        Maximum number of content children.
    """
    g.sort()
    s.sort()
    child = 0
    cookie = 0
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1
    return child
