from solution import anagramMappings


def test_example1():
    nums1 = [12, 28, 46, 32, 50]
    nums2 = [50, 12, 32, 46, 28]
    result = anagramMappings(nums1, nums2)
    assert [nums2[j] for j in result] == nums1


def test_example2():
    assert anagramMappings([84, 46], [84, 46]) == [0, 1]


def test_single_element():
    assert anagramMappings([5], [5]) == [0]


def test_all_duplicates():
    nums1 = [3, 3, 3]
    nums2 = [3, 3, 3]
    result = anagramMappings(nums1, nums2)
    assert sorted(result) == [0, 1, 2]
    assert all(nums2[j] == nums1[i] for i, j in enumerate(result))


def test_duplicates_mixed():
    nums1 = [1, 2, 1, 2]
    nums2 = [2, 1, 2, 1]
    result = anagramMappings(nums1, nums2)
    assert all(nums2[j] == nums1[i] for i, j in enumerate(result))
    assert sorted(result) == [0, 1, 2, 3]
