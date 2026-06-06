# Review: Find Words That Can Be Formed by Characters

## Solution
- **Approach**: Counter-based frequency comparison; for each word, check if all character counts are available in chars using Counter subtraction
- **Time Complexity**: O(n·m) where n is number of words, m is average word/chars length
- **Space Complexity**: O(1) for fixed 26-letter alphabet, or O(k) for character set size
- **Correctness**: Has Issues - **CRITICAL BUG**: Function name is `num_tile_possibilities` (a different LeetCode problem #1079) instead of `countCharacters` or similar for this problem (#1160). Algorithm logic is correct.

## Tests
- **Coverage**: Good - covers both examples, empty list, no matches, all matches, character frequency (not just presence), single character, and duplicate words
- **Edge Cases**: Yes - empty words, no good words, duplicate character requirements, single character, duplicate words in list

## Plan
- **Quality**: Has Issues - Plan describes correct approach but specifies wrong function name (`num_tile_possibilities` instead of `countCharacters`)

## Overall
Algorithm and test logic are correct, but function name is completely wrong (belongs to different LeetCode problem). Must rename from `num_tile_possibilities` to `countCharacters` to match problem #1160.
