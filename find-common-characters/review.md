# Review: Find Common Characters

## Solution
- **Approach**: Uses Counter intersection—initialize with first word's character counts, then iteratively intersect with each subsequent word's Counter using `&=`, finally expand to list via `elements()`.
- **Time Complexity**: O(n·m) where n is number of words, m is average word length
- **Space Complexity**: O(1) (bounded by 26 lowercase letters)
- **Correctness**: Correct

## Tests
- **Coverage**: Good—covers both examples, single word, no overlap, full overlap with duplicates, partial overlap, and single-character words
- **Edge Cases**: Yes—minimum input (single word), no common characters, all identical characters, and duplicate handling with partial overlap

## Plan
- **Quality**: Adequate—brief summary of Counter intersection approach with complexity analysis and test strategy, appropriate for minimal effort level

## Overall
Clean, efficient solution using Counter intersection. All tests pass and edge cases are well-covered. The approach correctly handles duplicates by maintaining minimum character counts across all words.
