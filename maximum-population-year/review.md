# Review: Maximum Population Year

## Solution
- **Approach**: Difference array (line sweep) technique that marks population changes at birth/death years, then sweeps through to find the earliest year with maximum running population.
- **Time Complexity**: O(n + k) where k=101 is constant, so effectively O(n)
- **Space Complexity**: O(1) constant space for fixed-size delta array
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes examples, single person, same ranges, adjacent ranges, overlaps, boundaries, and tie-breaking scenarios
- **Edge Cases**: Yes - covers boundary years (1950, 2050), adjacent non-overlapping ranges (validates death year exclusion), ties (validates earliest year selection), and full overlaps

## Plan
- **Quality**: Adequate - correctly identifies the difference array/line sweep approach as optimal for the constrained year range

## Overall
Clean, optimal implementation with comprehensive test coverage. The difference array approach efficiently handles the problem constraints, and tests properly validate death year exclusivity and tie-breaking rules.
