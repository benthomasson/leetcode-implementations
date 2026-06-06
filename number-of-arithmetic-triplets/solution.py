"""Number of Arithmetic Triplets - LeetCode 2367."""


def count_arithmetic_triplets(nums: list[int], diff: int) -> int:
    """Count arithmetic triplets where consecutive elements differ by `diff`.

    Args:
        nums: Strictly increasing integer array.
        diff: Required difference between consecutive triplet elements.

    Returns:
        Number of unique arithmetic triplets.
    """
    seen = set()
    count = 0
    for x in nums:
        if x - diff in seen and x - 2 * diff in seen:
            count += 1
        seen.add(x)
    return count
