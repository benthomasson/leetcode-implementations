def maxAliveYear(logs: list[list[int]]) -> int:
    """Return the earliest year with the maximum population.

    Args:
        logs: List of [birth, death] year pairs. Person is alive in [birth, death-1].

    Returns:
        Earliest year with the highest population count.
    """
    delta = [0] * 101  # years 1950..2050

    for birth, death in logs:
        delta[birth - 1950] += 1
        delta[death - 1950] -= 1

    max_pop = 0
    best_year = 1950
    running = 0
    for i in range(101):
        running += delta[i]
        if running > max_pop:
            max_pop = running
            best_year = 1950 + i

    return best_year
