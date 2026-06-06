"""Valid Parentheses - LeetCode Problem."""


def is_valid(s: str) -> bool:
    """Determine if a string of brackets is valid.

    Args:
        s: String containing only '(', ')', '{', '}', '[', ']'.

    Returns:
        True if all brackets are properly matched and nested.
    """
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in match:
            if not stack or stack.pop() != match[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
