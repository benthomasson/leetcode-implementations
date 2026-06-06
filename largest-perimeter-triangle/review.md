# Review: Largest Perimeter Triangle

## Solution
- **Approach**: Sort descending, iterate through triplets checking triangle inequality (a < b + c), return first valid perimeter.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1)
- **Correctness**: Has Issues - function named `min_area_rect` but solves largest perimeter triangle problem

## Tests
- **Coverage**: Good - tests basic valid, no valid triangle, all equal, degenerate case, large values, later triplet
- **Edge Cases**: Yes - covers degenerate triangle (a + b == c), no valid triangle, and later valid triplet after invalid ones

## Plan
- **Quality**: Missing - No plan provided

## Overall
Algorithm is correct and efficiently finds largest triangle perimeter using greedy approach with sorted array. Critical bug: function name `min_area_rect` is completely wrong for this problem (should be `largest_perimeter` or similar).
