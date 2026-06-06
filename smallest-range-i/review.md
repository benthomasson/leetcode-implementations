# Review: Smallest Range I

## Solution
- **Approach**: Optimal greedy - shrink range by raising min by k and lowering max by k, clamped at 0.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Has Issues - Function named `middleNode` instead of `smallestRangeI` (wrong problem name)

## Tests
- **Coverage**: Good - covers single element, examples, k=0, all same values, exact/under 2k ranges, large values
- **Edge Cases**: Yes - single element, k=0, range boundaries, large values all tested

## Plan
- **Quality**: Good algorithm description, but specifies wrong function name (`middleNode` instead of `smallestRangeI`)

## Overall
Algorithm is correct and optimal, tests are comprehensive, but the function is misnamed `middleNode` (suggests linked list problem) instead of `smallestRangeI`. Fix function name in solution and tests.
