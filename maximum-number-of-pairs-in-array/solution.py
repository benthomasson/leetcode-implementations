from collections import Counter


def count_pairs_leftovers(nums: list[int]) -> list[int]:
    """Count pairs of equal numbers and leftover elements.

    Args:
        nums: List of integers where pairs of equal values are removed.

    Returns:
        List of [number_of_pairs, number_of_leftovers].
    """
    pairs = 0
    leftovers = 0
    for count in Counter(nums).values():
        pairs += count // 2
        leftovers += count % 2
    return [pairs, leftovers]
