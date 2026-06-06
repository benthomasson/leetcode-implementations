# Review: Largest Number At Least Twice of Others

## Solution
- **Approach**: Single-pass O(n) scan tracking maximum value, second maximum, and index of maximum; returns index if max >= 2 * second_max.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: **Has Issues** - Function name is `minCostClimbingStairs` which is completely wrong (different LeetCode problem). Algorithm logic is correct.

## Tests
- **Coverage**: Good - covers both examples, edge cases with zeros, exactly-twice boundary, max at different positions, and dominant/non-dominant scenarios.
- **Edge Cases**: Yes - tests minimum size (2 elements), zeros, boundary conditions (exactly 2x), and various positions of maximum.

## Plan
- **Quality**: **Has Issues** - Plan incorrectly specifies function name as `minCostClimbingStairs` (wrong problem). Algorithm approach is sound.

## Overall
Critical bug: function name `minCostClimbingStairs` doesn't match the problem (should be something like `dominantIndex`). The algorithm itself is correct and optimal, and tests are comprehensive, but all tests also use the wrong function name. This appears to be a copy-paste error in the plan that propagated to the implementation.
