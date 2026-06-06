from collections import Counter


def most_frequent_number_following_key_in_an_array(nums: list[int], key: int) -> int:
    """Find the most frequent number immediately following key in nums.

    Args:
        nums: 0-indexed integer array.
        key: Integer present in nums to search for.

    Returns:
        The target with the maximum count of occurrences following key.
    """
    counts: Counter[int] = Counter()
    for i in range(len(nums) - 1):
        if nums[i] == key:
            counts[nums[i + 1]] += 1
    return counts.most_common(1)[0][0]
