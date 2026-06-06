# Review: Flipping an Image

## Solution
- **Approach**: Two-pointer technique that simultaneously flips each row horizontally and inverts values using XOR in a single pass.
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good, tests both provided examples plus edge cases
- **Edge Cases**: Yes, covers 1x1 matrices, uniform values (all 0s/1s), and odd dimensions (important for middle element handling)

## Plan
- **Quality**: Adequate, brief plan correctly identifies the algorithm and notes the function name discrepancy in requirements

## Overall
Solid implementation with optimal in-place solution. Tests are comprehensive and the plan correctly catches that requirements mention wrong function name (`pruneTree` instead of `flipAndInvertImage`).
