"""Goal Parser Interpretation - LeetCode 1678."""


def num_ways(command: str) -> str:
    """Interpret a Goal Parser command string.

    Args:
        command: String consisting of "G", "()", and/or "(al)".

    Returns:
        The interpreted string with "()" replaced by "o" and "(al)" by "al".
    """
    return command.replace("()", "o").replace("(al)", "al")
