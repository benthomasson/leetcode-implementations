# Review: The K Weakest Rows in a Matrix

## Solution
- **Approach**: Count soldiers per row using `sum()`, enumerate to pair with indices, sort by soldier count (stable sort handles tie-breaking by index), return first k indices.
- **Time Complexity**: O(m·n + m log m)
- **Space Complexity**: O(m)
- **Correctness**: Correct. Leverages stable sort for automatic tie-breaking by index.

## Tests
- **Coverage**: Good. All examples plus edge cases (all zeros, all ones, k=m, minimum size, explicit tie-breaking).
- **Edge Cases**: Yes. Covers uniform rows, boundary k values, and tie-breaking validation.

## Plan
- **Quality**: Good. Concise, identifies correct algorithm and complexity, lists test cases.

## Overall
Clean, correct solution with excellent test coverage. The implementation cleverly uses Python's stable sort to handle tie-breaking implicitly. No issues found.
