"""Solution for LeetCode problem: Jewels and Stones."""


def num_jewels_in_stones(jewels: str, stones: str) -> int:
    """Count how many stones are also jewels.

    Args:
        jewels: String of unique characters representing jewel types.
        stones: String of characters representing stones you have.

    Returns:
        Number of stones that are jewels.
    """
    jewel_set = set(jewels)
    return sum(s in jewel_set for s in stones)
