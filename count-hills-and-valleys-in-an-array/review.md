# Review: Count Hills and Valleys in an Array

## Solution
- **Approach**: Removes consecutive duplicates, then counts local maxima (hills) and local minima (valleys) in one pass through the deduplicated array.
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers both examples, edge cases (all same, monotonic, plateaus, minimum length, alternating)
- **Edge Cases**: Yes - all same values, monotonic sequences, plateau hills/valleys, minimum length arrays, alternating patterns
- **Issue**: In solution.py line 39, `test_alternating` expects 4 but should expect 3 for input [1,3,1,3,1]

## Plan
- **Quality**: Adequate - correctly identifies deduplication and one-pass counting approach, but contains wrong function name (says `sorted_target_indices` instead of `count_hills_and_valleys`)

## Overall
The solution algorithm is correct and efficient. One test expectation bug in solution.py (test_alternating should expect 3, not 4). The plan has a copy-paste error with the wrong function name requirement.
