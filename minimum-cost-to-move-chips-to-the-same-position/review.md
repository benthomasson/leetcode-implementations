# Review: Minimum Cost to Move Chips to the Same Position

## Solution
- **Approach**: Count chips at odd vs even positions; the minimum cost is the smaller count since moving by ±2 is free (preserves parity) and we only pay to move the minority group one step.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes all examples, boundary cases (single chip, all same parity), and balanced odd/even scenarios
- **Edge Cases**: Yes - covers single chip, all even, all odd, equal distribution, and large values

## Plan
- **Quality**: Good - brief as requested for MINIMAL effort, correctly identifies the parity insight as the key algorithmic observation

## Overall
Solid implementation of a greedy parity-based solution. All tests pass and edge cases are well-covered. Minor note: function name `sort_array` doesn't match the problem (acknowledged in plan).
