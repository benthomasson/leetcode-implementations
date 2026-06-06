# Review: Monotonic Array

## Solution
- **Approach**: Single pass with two boolean flags tracking whether array is non-decreasing or non-increasing; returns true if either flag remains true.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers all major scenarios including examples, edge cases, and boundary conditions
- **Edge Cases**: Yes - single element, two elements, all equal, strictly increasing/decreasing, peak/valley patterns

## Plan
- **Quality**: Adequate - brief as requested, identifies optimal approach and complexity, notes erroneous function name in task

## Overall
Clean, optimal solution with excellent test coverage. No bugs or improvements needed. Implementation correctly uses `isMonotonic` instead of the erroneous `maxDepth` name mentioned in the plan's task description.
