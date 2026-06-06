# Review: Moving Average from Data Stream

## Solution
- **Approach**: Uses a deque with fixed maxlen to maintain the sliding window and a running sum. When full, subtracts the outgoing element before adding the new one.
- **Time Complexity**: O(1)
- **Space Complexity**: O(size)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - tests basic functionality, edge cases (window size 1, negatives, unfilled window), and stress test with 10k calls
- **Edge Cases**: Yes - covers window size 1, negative values, zero, unfilled window, and many calls

## Plan
- **Quality**: Adequate - brief as requested (minimal effort), identifies key approach (deque + running sum) and complexity

## Overall
Solution is correct and efficient with O(1) time per operation. Tests provide good coverage of edge cases. Clean implementation with no bugs detected.
