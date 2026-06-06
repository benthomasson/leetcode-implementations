# Review: Lemonade Change

## Solution
- **Approach**: Greedy simulation tracking $5 and $10 bill counts; for $20 change, prefers one $10 + one $5 over three $5s to preserve flexibility.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes LeetCode examples, single-bill edge cases for all denominations, greedy strategy validation, boundary conditions, and stress test with 100k bills.
- **Edge Cases**: Yes - covers single $5/$10/$20 (including impossible cases), all $5s, just-enough/not-enough scenarios, and alternating patterns.

## Plan
- **Quality**: Adequate - Very brief as intended for MINIMAL effort level; identifies greedy approach as optimal but lacks detailed explanation of the algorithm.

## Overall
Correct greedy implementation with comprehensive test coverage including strategy validation (preferring $10+$5 over 3×$5). Plan is minimal but sufficient given the straightforward nature of the problem.
