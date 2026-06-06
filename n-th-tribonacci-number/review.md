# Review: N-th Tribonacci Number

## Solution
- **Approach**: Iterative solution with 3 rolling variables (a, b, c) tracking the last three Tribonacci numbers, updating them in each iteration.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes all base cases, provided examples, small sequence verification, and upper boundary test
- **Edge Cases**: Yes - covers n=0, n=1, n=2 base cases, maximum constraint n=37, and 32-bit integer verification

## Plan
- **Quality**: Good - correctly identifies iterative approach with O(n) time and O(1) space, appropriate level of detail for minimal effort requirement

## Overall
Clean, optimal solution with comprehensive test coverage. The implementation correctly handles all base cases and efficiently computes Tribonacci numbers using constant space. No issues found.
