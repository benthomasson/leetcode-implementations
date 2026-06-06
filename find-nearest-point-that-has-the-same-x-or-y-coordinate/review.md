# Review: Find Nearest Point That Has the Same X or Y Coordinate

## Solution
- **Approach**: Linear scan through points, filtering for valid points (sharing x or y coordinate), calculating Manhattan distance for each, tracking the minimum distance and its index.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers all example cases, boundary values, ties, and various valid/invalid point scenarios
- **Edge Cases**: Yes - same location, no valid points, tie-breaking by index, all valid points, boundary values (10^4)

## Plan
- **Quality**: Adequate - brief as requested, correctly identifies O(n) time and O(1) space, describes the algorithm

## Overall
Clean, correct implementation with comprehensive test coverage. The solution efficiently handles all edge cases including tie-breaking by smallest index and returns -1 when no valid points exist.
