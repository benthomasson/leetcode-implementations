# Review: Sort Even and Odd Indices Independently

## Solution
- **Approach**: Extract elements at even/odd indices separately, sort evens ascending and odds descending, then interleave back into result array.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Correctness**: Correct, but function name `maxValue` is misleading (doesn't describe sorting operation)

## Tests
- **Coverage**: Good - includes provided examples, single element, all same values, odd/even lengths, boundary values
- **Edge Cases**: Yes - single element, all identical values, min/max constraint values (1, 100)

## Plan
- **Quality**: Adequate - brief description matches MINIMAL effort level, accurately describes algorithm

## Overall
Solution is correct and efficient with comprehensive test coverage. The only issue is the misleading function name `maxValue` which should reflect the sorting operation instead.
