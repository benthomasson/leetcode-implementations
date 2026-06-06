"""Longest Common Prefix - LeetCode Solution."""


def longest_common_prefix(strs: list[str]) -> str:
    """Find the longest common prefix string amongst an array of strings.

    Args:
        strs: List of strings to find common prefix for.

    Returns:
        The longest common prefix, or empty string if none exists.
    """
    if not strs:
        return ""

    for i, char in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0]
