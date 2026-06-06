# Review: Determine if String Halves Are Alike

## Solution
- **Approach**: Split string at midpoint, count vowels in each half using set lookup, compare counts.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Has Issues - Function name `numSpecial` is incorrect for this problem (should be `halvesAreAlike` or similar).

## Tests
- **Coverage**: Good - covers examples, edge cases (all vowels, no vowels, min/max length, mixed case).
- **Edge Cases**: Yes - min length, all vowels, no vowels, mixed case, long strings.

## Plan
- **Quality**: Adequate - Algorithm correct but acknowledges wrong function name without addressing it.

## Overall
Algorithm implementation is correct and efficient, but **critical bug**: function name `numSpecial` is completely wrong for a problem about string halves being alike. Tests are comprehensive and would pass with the current implementation, but the function should be renamed to match the problem semantics.
