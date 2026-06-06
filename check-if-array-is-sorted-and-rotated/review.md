# Review: Check if Array is Sorted and Rotated

## Solution
- **Approach**: Count circular breaks where nums[i] > nums[(i+1) % n]; array is sorted-rotated if breaks ≤ 1
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes LeetCode examples, single element, duplicates, multiple breaks, edge cases
- **Edge Cases**: Yes - single element, all equal, two elements, duplicates at break point, descending order

## Plan
- **Quality**: Adequate - describes algorithm correctly but has wrong function name in requirements (says `check_arithmetic_subarrays` instead of `check`)

## Overall
Solution correctly identifies sorted-rotated arrays by counting break points in O(n) time. Tests are comprehensive. Plan has incorrect function name requirement that doesn't match implementation.
