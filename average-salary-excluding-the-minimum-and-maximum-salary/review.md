# Review: Average Salary Excluding the Minimum and Maximum Salary

## Solution
- **Approach**: Single-pass computation of sum, min, and max, then calculate `(sum - min - max) / (n - 2)`.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Has Issues - **CRITICAL BUG**: Function name is `count_prefix_aligned` instead of the correct problem-specific name. Algorithm implementation is correct.

## Tests
- **Coverage**: Good - includes both examples, minimum case (3 elements), larger arrays, boundary values, unsorted input, and edge cases with close/high values.
- **Edge Cases**: Yes - covers minimum length array, extreme values, unsorted input, and close values.

## Plan
- **Quality**: Adequate - correctly identifies O(n) single-pass approach, but contains the same function naming error as the solution.

## Overall
The algorithm is correct and efficient, but has a critical bug: the function is named `count_prefix_aligned` (appears to be from a different problem) instead of the appropriate name for this problem. All tests call the wrong function name. Rename the function to fix.
