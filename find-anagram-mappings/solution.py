from collections import defaultdict, deque


def anagramMappings(nums1: list[int], nums2: list[int]) -> list[int]:
    """Return index mapping from nums1 to nums2 where mapping[i] = j means nums1[i] == nums2[j].

    Args:
        nums1: Source integer array.
        nums2: Anagram of nums1.

    Returns:
        List of indices mapping each element in nums1 to its position in nums2.
    """
    index_map: dict[int, deque[int]] = defaultdict(deque)
    for i, val in enumerate(nums2):
        index_map[val].append(i)
    return [index_map[val].pop() for val in nums1]
