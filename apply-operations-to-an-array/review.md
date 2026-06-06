# Review: Apply Operations to an Array

## Solution
- **Approach**: Two-phase algorithm: iterate through array to apply pairwise doubling operations sequentially (if adjacent elements equal, double first and zero second), then use two-pointer technique to move all zeros to end.
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - 10 test cases covering problem examples, edge cases (minimum length, all zeros, no duplicates), and critical scenarios (sequential matters, chain doubling, zeros between values, input mutation check)
- **Edge Cases**: Yes - minimum length array, all zeros, consecutive triples, all same values, zeros between non-zeros

## Plan
- **Quality**: Good - concise description of two-phase O(n) approach with mention of edge case coverage, appropriate for minimal effort level

## Overall
Solution correctly implements the sequential operation requirement and efficiently moves zeros to end. Tests thoroughly cover edge cases including the tricky sequential behavior where [2,2,2]→[4,2,0]. Minor note: test file has hardcoded import path `"../implementer"` that assumes specific directory structure.
