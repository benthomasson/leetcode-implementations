"""Distribute Candies to People."""


def distribute_candies(candies: int, num_people: int) -> list[int]:
    """Distribute candies to people in increasing order, wrapping around.

    Args:
        candies: Total number of candies to distribute.
        num_people: Number of people in the row.

    Returns:
        List of candies each person receives.
    """
    result = [0] * num_people
    give = 1
    while candies > 0:
        result[(give - 1) % num_people] += min(give, candies)
        candies -= give
        give += 1
    return result
