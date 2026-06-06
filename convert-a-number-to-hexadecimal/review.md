# Review: Convert a Number to Hexadecimal

## Solution
- **Approach**: Bit manipulation - mask to 32-bit unsigned for two's complement, extract 4 bits per iteration, map to hex characters, reverse result.
- **Time Complexity**: O(1) - maximum 8 iterations
- **Space Complexity**: O(1) - result has at most 8 characters
- **Correctness**: Correct. Properly handles two's complement via `0xFFFFFFFF` mask.

## Tests
- **Coverage**: Good. Both test files provide comprehensive coverage with some duplication.
- **Edge Cases**: Yes. Covers zero, boundaries (single/multi hex digits, INT_MAX, INT_MIN), positive values, and negative values including -1 and -2.

## Plan
- **Quality**: Adequate. Brief as requested for minimal effort level, correctly identifies bit manipulation approach and O(1) complexity.

## Overall
Clean, correct implementation using standard bit manipulation technique. The 32-bit mask is essential for handling Python's arbitrary-precision integers correctly. Tests are thorough and cover all critical cases including two's complement edge cases.
