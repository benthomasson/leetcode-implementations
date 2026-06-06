# Review: Minimum Difference Between Highest and Lowest of K Scores

## Solution
- **Approach**: Sort the array, then use a sliding window of size k to find the minimum difference between the last and first element in each window.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1) to O(n) depending on sorting implementation
- **Correctness**: Correct, though function name `max_distance` is misleading for a problem asking for minimum difference

## Tests
- **Coverage**: Good - comprehensive test suite covering multiple scenarios
- **Edge Cases**: Yes - covers k=1, k=length, all identical elements, duplicates, sorted/unsorted inputs, constraint boundaries, and input mutation

## Plan
- **Quality**: Adequate - brief plan appropriate for minimal effort level, correctly identifies sort + sliding window approach with O(n log n) complexity

## Overall
Solution is algorithmically correct and efficiently implemented. Tests are thorough with good edge case coverage. Minor note: solution mutates input array (sorted in-place), which is tested but worth being aware of.
