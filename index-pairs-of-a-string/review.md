# Review: Index Pairs of a String

## Solution
- **Approach**: Brute-force substring matching — for each word, scan all positions in text to find matches, collect [i, j] pairs, then sort.
- **Time Complexity**: O(n * m * k) where n = text length, m = number of words, k = average word length
- **Space Complexity**: O(r) where r = number of result pairs
- **Correctness**: Correct. End index properly calculated as `i + wlen - 1`. Wrapper function handles mismatched function name requirement.

## Tests
- **Coverage**: Good. Tests include both examples, no matches, single character, full string match, word longer than text, multiple occurrences of same word, and wrapper function.
- **Edge Cases**: Yes. Covers single character match, no match, full string match, word longer than text, multiple occurrences, and overlapping matches (from example 2).

## Plan
- **Quality**: Adequate. Brief as requested for minimal effort level. Clearly states algorithm choice, complexity analysis, and acknowledges the function name mismatch from a different problem.

## Overall
Solution is correct and efficient for the given constraints. Tests are comprehensive with good edge case coverage. The plan appropriately notes the function name discrepancy (`has_all_codes_in_range` vs `indexPairs`) and handles it with a wrapper.
