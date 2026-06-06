# Review: Maximum Average Subarray I

## Solution
- **Approach**: Sliding window—compute initial sum of first k elements, then slide by adding next element and removing leftmost element of previous window
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good—covers basic examples, single element, all negative, uniform values, k equals length, and max at different positions
- **Edge Cases**: Yes—single element (k=1), k equals array length, all negative numbers, all same values

## Plan
- **Quality**: Adequate—appropriate for MINIMAL effort level, correctly identifies sliding window as optimal approach

## Overall
Clean, correct implementation with efficient O(n) sliding window approach. Test coverage is comprehensive with good edge case handling. No bugs or improvements needed.
