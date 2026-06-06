# Review: Substrings of Size Three with Distinct Characters

## Solution
- **Approach**: Sliding window iterating through string, checking each consecutive triplet for distinctness using direct pairwise comparison
- **Time Complexity**: O(n) where n is string length
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers both examples, edge cases (strings shorter than 3, exact length 3), and various character patterns (all same, all distinct, alternating)
- **Edge Cases**: Yes - handles len < 3, len == 3, all same characters, all distinct, alternating patterns, repeated pairs

## Plan
- **Quality**: Good - identifies correct algorithm (sliding window), accurate complexity analysis, appropriate test coverage

## Overall
Clean, correct implementation with comprehensive test coverage. The solution efficiently identifies all substrings of length 3 with distinct characters using pairwise comparison. Minor note: function name `highest_island` doesn't semantically match the problem but follows specified requirements.
