# Review: Find Subsequence of Length K With the Largest Sum

## Solution
- **Approach**: Pair elements with indices, select k largest by value, restore original order by sorting indices. Correctly maximizes sum while preserving subsequence property.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Correctness**: Correct, but function name `count_patterns_in_word` is wrong for this problem (copy-paste error from different problem)

## Tests
- **Coverage**: Good - includes all examples plus 7 edge cases (k=1, k=n, single element, duplicates, all negative, mixed signs)
- **Edge Cases**: Yes - covers single element, all identical, all negative, mixed values, boundary values of k

## Plan
- **Quality**: Good for minimal effort level - correctly identifies algorithm and complexity, notes function name error

## Overall
Solution is algorithmically correct and efficient. Tests are comprehensive with a clever validation helper that checks both subsequence validity and sum maximality. Only issue is the incorrect function name which should be changed from `count_patterns_in_word` to something appropriate like `maxSubsequence`.
