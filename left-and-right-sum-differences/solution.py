"""Left and Right Sum Differences."""


def get_answer(nums: list[int]) -> list[int]:
    """Return array of absolute differences between left and right sums.

    Args:
        nums: 0-indexed integer array.

    Returns:
        Array where answer[i] = |leftSum[i] - rightSum[i]|.
    """
    total = sum(nums)
    left = 0
    answer = []
    for x in nums:
        right = total - left - x
        answer.append(abs(left - right))
        left += x
    return answer
