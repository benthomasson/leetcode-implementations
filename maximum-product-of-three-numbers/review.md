# Review: Maximum Product of Three Numbers

## Solution
- **Approach**: Sort array, then return max of (three largest) vs (two smallest × largest) to handle case where two large negatives produce larger product
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1) or O(n) depending on sort implementation
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers LeetCode examples, negative numbers, zeros, boundary values, and the key two-negatives case
- **Edge Cases**: Yes - all zeros, mixed with zero, all negatives, exactly 3 elements, boundary values (-1000, 1000), uniform values

## Plan
- **Quality**: Good - appropriately brief for minimal effort level, correctly identifies the key insight about negative numbers

## Overall
Solution correctly handles the negative number edge case by comparing both candidate products. Tests are comprehensive. Minor note: `test_input_not_mutated` has misleading name/comment—it verifies correctness but doesn't actually check if input was mutated (solution does mutate via sort).
