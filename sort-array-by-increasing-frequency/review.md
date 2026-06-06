# Review: Sort Array by Increasing Frequency

## Solution
- **Approach**: Uses Counter to compute frequencies, then sorts array by (frequency, -value) key to achieve increasing frequency order with decreasing value tie-breaking.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes all examples, single element, all same values, all unique values, negative tie-breaking, boundary values, and mixed frequencies
- **Edge Cases**: Yes - covers single element, all same, all unique, negative numbers, boundary values (-100, 100), and tie-breaking scenarios

## Plan
- **Quality**: Good - brief but clearly describes the Counter + sort approach with appropriate key function

## Overall
Solution is correct and efficient with comprehensive test coverage. The function name `num_sub` is unusual for a frequency-sorting problem but matches the stated requirements.
