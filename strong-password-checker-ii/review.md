# Review: Strong Password Checker II

## Solution
- **Approach**: Single-pass validation checking 6 criteria (length ≥8, has lower/upper/digit/special, no adjacent duplicates).
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Has Issues - function name `merge_nodes_between_zeros` is completely wrong for this problem (should be `strongPasswordCheckerII` or similar).

## Tests
- **Coverage**: Good - tests all LeetCode examples plus edge cases (exactly 8 chars, too short, adjacent duplicates, missing special char, non-adjacent repeats).
- **Edge Cases**: Yes - covers length boundary, character requirements, and adjacent duplicate detection.

## Plan
- **Quality**: Has Issues - plan incorrectly specifies "Function name should be: merge_nodes_between_zeros" which appears to be a copy-paste error from a different problem (linked list problem).

## Overall
The algorithm is correct and efficiently validates all password criteria, but has a critical naming bug: `merge_nodes_between_zeros` is completely unrelated to password checking. The plan also propagates this error. Fix the function name to match the problem.
