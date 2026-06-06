# Review: Find All K-Distant Indices in an Array

## Solution
- **Approach**: Find all positions j where nums[j] == key, then for each, add all indices within distance k (range [j-k, j+k]) to a set, return sorted.
- **Time Complexity**: O(n + m×k) where m is the number of keys found; worst case O(n²) when all elements are keys
- **Space Complexity**: O(n)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes examples, single element, boundary positions, overlapping/non-overlapping ranges, and k larger than array
- **Edge Cases**: Yes - single element, key at start/end, non-overlapping ranges, k covering entire array, overlapping ranges

## Plan
- **Quality**: Good - brief as requested for minimal effort, identifies O(n) approach (though more accurately O(n + m×k)), notes the function name template bug

## Overall
Solution is correct and efficient with comprehensive test coverage. The plan correctly identifies the approach and acknowledges the function name discrepancy between requirements and implementation.
