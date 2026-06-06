# Review: Distribute Candies

## Solution
- **Approach**: Return the minimum of n/2 (allowed candies) and the number of unique candy types, using a set to count unique types.
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers all examples, minimum length, negative/mixed types, and extremes (all same, all unique, large inputs)
- **Edge Cases**: Yes - minimum length (n=2), single type repeated, all unique types, negative values, and large arrays

## Plan
- **Quality**: Adequate - brief but identifies correct algorithm and complexity for minimal effort level

## Overall
Clean, correct one-line solution with comprehensive test coverage. The algorithm correctly handles the constraint that Alice can eat at most n/2 candies and wants to maximize variety.
