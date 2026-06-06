def max_value(operations: list[str]) -> int:
    """Return final value of X after performing all increment/decrement operations.

    Args:
        operations: List of strings, each "++X", "X++", "--X", or "X--".

    Returns:
        Final integer value of X (starting from 0).
    """
    x = 0
    for op in operations:
        if op[1] == "+":
            x += 1
        else:
            x -= 1
    return x
