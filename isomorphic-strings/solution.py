"""Isomorphic Strings - LeetCode solution."""


def is_isomorphic(s: str, t: str) -> bool:
    """Determine if two strings are isomorphic.

    Args:
        s: Source string.
        t: Target string (same length as s).

    Returns:
        True if s and t are isomorphic, False otherwise.
    """
    s_to_t: dict[str, str] = {}
    t_to_s: dict[str, str] = {}

    for c_s, c_t in zip(s, t):
        if c_s in s_to_t:
            if s_to_t[c_s] != c_t:
                return False
        elif c_t in t_to_s:
            return False
        else:
            s_to_t[c_s] = c_t
            t_to_s[c_t] = c_s

    return True
