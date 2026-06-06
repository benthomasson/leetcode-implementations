from solution import Solution


def test_example1():
    nums = [1, 1, 2]
    k = Solution().removeDuplicates(nums)
    assert k == 2
    assert nums[:k] == [1, 2]


def test_example2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = Solution().removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]


def test_single_element():
    nums = [1]
    k = Solution().removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [1]


def test_no_duplicates():
    nums = [1, 2, 3, 4, 5]
    k = Solution().removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [1, 2, 3, 4, 5]


def test_all_duplicates():
    nums = [7, 7, 7, 7]
    k = Solution().removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [7]


def test_negative_numbers():
    nums = [-3, -1, -1, 0, 0, 2]
    k = Solution().removeDuplicates(nums)
    assert k == 4
    assert nums[:k] == [-3, -1, 0, 2]


def test_two_elements_same():
    nums = [1, 1]
    k = Solution().removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [1]


def test_two_elements_different():
    nums = [1, 2]
    k = Solution().removeDuplicates(nums)
    assert k == 2
    assert nums[:k] == [1, 2]
