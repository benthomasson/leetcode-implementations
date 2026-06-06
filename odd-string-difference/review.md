# Review: Odd String Difference

## Solution
- **Approach**: Compute difference arrays for all words, count frequencies using Counter, return the word with unique (count=1) difference array.
- **Time Complexity**: O(n * m) where n is number of words, m is word length
- **Space Complexity**: O(n * m) to store difference arrays and counter
- **Correctness**: Correct

## Tests
- **Coverage**: Good - tests both examples, odd string at different positions, min/max constraints, edge cases
- **Edge Cases**: Yes - minimum length strings (2 chars), minimum words (3), all same except one, longer strings (5 chars), many words (100)

## Plan
- **Quality**: Adequate - brief as intended for minimal effort level, correctly identifies hash-and-count approach

## Overall
Clean, correct solution with excellent test coverage. The Counter-based approach efficiently identifies the unique difference array, and tests thoroughly validate edge cases and constraints.
