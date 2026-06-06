# Review: Count Negative Numbers in a Sorted Matrix

## Solution
- **Approach**: Staircase traversal from top-right corner; moves left when negative (counting remaining rows), down otherwise.
- **Time Complexity**: O(m + n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes both examples, edge cases (all negative/positive, single element, single row/column), and boundary conditions (zeros)
- **Edge Cases**: Yes - single element, single row/column, all negative/positive, zeros at boundary

## Plan
- **Quality**: Good - concise per MINIMAL effort level, correctly identifies optimal O(m+n) algorithm

## Overall
Solution is algorithmically correct and efficient with comprehensive test coverage. Function name `balanced_string` is mismatched with the problem (likely a template error; should be `countNegatives` or similar).
