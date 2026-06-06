# Review: Two Furthest Houses With Different Colors

## Solution
- **Approach**: Optimal greedy approach checking maximum distance from both endpoints - finds furthest house with different color than first house, then furthest house with different color than last house, returns maximum.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Has Issues - **CRITICAL BUG**: Wrong function name `maxCompatibilitySum` (should be something like `maxDistance`). Algorithm logic is correct.

## Tests
- **Coverage**: Good - covers all problem examples, edge cases (minimum size, different/same endpoints, max length, all different), and various patterns
- **Edge Cases**: Yes - minimum size (2), maximum size (100), same endpoints with different middle, all different colors, different endpoints

## Plan
- **Quality**: Adequate - correctly identifies key insight that optimal answer involves first or last house, enabling O(n) solution with two scans

## Overall
Algorithm is correct and efficient, tests are comprehensive, but has a critical bug: function name is completely wrong for this problem (maxCompatibilitySum vs. a distance-related name). This appears to be copy-paste from a different LeetCode problem about student compatibility.
