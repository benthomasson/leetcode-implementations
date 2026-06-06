# Review: Number of Recent Calls

## Solution
- **Approach**: Deque-based sliding window that appends new timestamps and evicts entries older than t-3000, returning the count of remaining elements.
- **Time Complexity**: O(1) amortized per ping
- **Space Complexity**: O(W) where W is max requests in 3000ms window
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers basic functionality, boundary conditions (inclusive/exclusive), large gaps, large values, and instance independence
- **Edge Cases**: Yes - boundary at exactly t-3000 (inclusive), t-3001 (exclusive), single ping, large t values near 10^9, and eviction scenarios

## Plan
- **Quality**: Adequate - brief algorithm description with complexity analysis as appropriate for MINIMAL effort level

## Overall
Clean, correct implementation using deque for efficient sliding window maintenance. Comprehensive test suite with no bugs detected. Properly handles all boundary conditions and edge cases.
