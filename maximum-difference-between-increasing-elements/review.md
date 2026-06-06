# Review: Maximum Difference Between Increasing Elements

## Solution
- **Approach**: Single pass tracking minimum value seen so far, computing max difference at each position (equivalent to max profit stock problem)
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Has Issues - **Function name is completely wrong**: `min_steps_to_equal_elements` should be `maximumDifference` or similar

## Tests
- **Coverage**: Good - covers all examples plus edge cases (two elements, all equal, large values, strictly increasing/decreasing, non-adjacent pairs)
- **Edge Cases**: Yes - two elements both directions, all equal, large values, strictly monotonic sequences, non-adjacent optimal pair

## Plan
- **Quality**: Adequate - Correctly identifies the stock profit analogy and algorithm, but specifies wrong function name in requirements

## Overall
Algorithm is correct and efficient, tests are comprehensive. **Critical bug**: Function name `min_steps_to_equal_elements` is from a different problem entirely - appears to be copy-paste error from plan template. Rename to `maximumDifference` or `max_difference_between_increasing_elements`.
