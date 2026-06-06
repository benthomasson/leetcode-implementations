# Review: Count Elements With Strictly Smaller and Greater Elements

## Solution
- **Approach**: Find min and max values in the array, then count all elements strictly between them (since any element with both a smaller and greater element must fall between min and max).
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct algorithm, but **function name is wrong** (`min_moves` should be something like `count_elements`)

## Tests
- **Coverage**: Good - covers examples, edge cases (single element, two elements, all same values, duplicates at boundaries), negative numbers, multiple middle elements, and constraint boundaries
- **Edge Cases**: Yes - single element, two elements, all same, duplicates, negatives, large ranges all covered

## Plan
- **Quality**: Good - brief and appropriate for minimal effort level, correctly identifies algorithm and complexity

## Overall
Solution logic is correct and efficient, tests are comprehensive, but the function name `min_moves` is incorrect for this problem (appears to be copy-paste error). Should be renamed to match the problem (e.g., `count_elements`).
