# Review: Majority Element

## Solution
- **Approach**: Boyer-Moore Voting Algorithm that maintains a candidate and count, canceling out non-matching elements
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good — includes single element, all same, negative numbers, majority at different positions
- **Edge Cases**: Yes — covers minimum size (n=1), negative values, and majority appearing at start/end/throughout

## Plan
- **Quality**: Adequate — brief but identifies optimal algorithm and complexity (appropriate for minimal effort level)

## Overall
Clean implementation of the optimal Boyer-Moore algorithm with comprehensive test coverage. No bugs or issues detected. Solution meets the follow-up challenge of O(n) time and O(1) space.
