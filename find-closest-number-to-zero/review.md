# Review: Find Closest Number to Zero

## Solution
- **Approach**: Single-pass scan tracking the closest number to zero, updating when a closer number is found or when tied distances favor the larger value.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes examples, single element, zero present, all negative, tie-breaking, identical elements, and boundary values
- **Edge Cases**: Yes - zero in array, single element, tie-breaking (positive/negative pairs), all negative, all same, and constraint boundaries

## Plan
- **Quality**: Adequate - correctly identifies single-pass O(n) approach with tie-breaking logic, though brief

## Overall
The solution is correct and optimal with comprehensive test coverage. Minor issue: function name `robot_instructions` is misleading for a problem about finding closest number to zero (likely copy-paste error from plan template).
