from typing import List


def inorder(s: str, shift: List[List[int]]) -> str:
    """Perform string shifts and return the final string.

    Args:
        s: Input string of lowercase English letters.
        shift: List of [direction, amount] pairs. 0=left, 1=right.

    Returns:
        The string after all shift operations.
    """
    net = 0
    for direction, amount in shift:
        if direction == 1:
            net += amount
        else:
            net -= amount

    net %= len(s)

    if net == 0:
        return s
    return s[-net:] + s[:-net]
