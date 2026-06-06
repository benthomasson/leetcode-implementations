def find_relative_ranks(score: list[int]) -> list[str]:
    """Assign ranks to athletes based on their scores.

    Args:
        score: List of unique integer scores for each athlete.

    Returns:
        List of rank strings for each athlete's original position.
    """
    n = len(score)
    ranked = sorted(range(n), key=lambda i: score[i], reverse=True)
    result = [""] * n
    for place, idx in enumerate(ranked):
        if place == 0:
            result[idx] = "Gold Medal"
        elif place == 1:
            result[idx] = "Silver Medal"
        elif place == 2:
            result[idx] = "Bronze Medal"
        else:
            result[idx] = str(place + 1)
    return result
