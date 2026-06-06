"""Sort the People - LeetCode problem solution."""


def sort_names_by_height(names: list[str], heights: list[int]) -> list[str]:
    """Sort names in descending order by corresponding heights.

    Args:
        names: List of people's names.
        heights: List of distinct positive integers representing heights.

    Returns:
        Names sorted by height in descending order.
    """
    return [name for _, name in sorted(zip(heights, names), reverse=True)]
