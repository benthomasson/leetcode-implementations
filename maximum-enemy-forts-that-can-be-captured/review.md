# Review: Maximum Enemy Forts That Can Be Captured

## Solution
- **Approach**: Linear scan tracking the last non-zero position; when finding a different non-zero value, calculate captured forts as the distance minus one.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers both examples, single elements, all zeros, adjacent opposites, missing fort types, and both movement directions
- **Edge Cases**: Yes - single element, all zeros, adjacent opposite forts, no enemy forts between allies, and bidirectional movement

## Plan
- **Quality**: Adequate - brief but accurately describes the O(n) linear scan approach

## Overall
Clean, efficient solution with excellent test coverage. The algorithm correctly identifies valid moves between opposite fort types and counts enemy forts in between.
