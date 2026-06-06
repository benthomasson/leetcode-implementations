"""Baseball Game - LeetCode 682."""


def calPoints(operations: list[str]) -> int:
    """Calculate total score after applying all operations.

    Args:
        operations: List of operations - integers, "+", "D", or "C".

    Returns:
        Sum of all scores on the record.
    """
    stack: list[int] = []
    for op in operations:
        op = op.strip()
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    return sum(stack)
