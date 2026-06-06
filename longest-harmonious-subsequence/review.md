# Review: Longest Harmonious Subsequence

## Solution
- **Approach**: Uses Counter to count frequencies, then iterates over keys checking if k+1 exists, tracking maximum sum of count[k] + count[k+1]
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers examples, single element, consecutive/non-consecutive pairs, negatives, large values, and many duplicates
- **Edge Cases**: Yes - single element, all same values, negatives, boundary values (10^9), duplicates

## Plan
- **Quality**: Adequate - brief as requested for minimal effort level, correctly identifies Counter approach and O(n) complexity

## Overall
Solution is correct and optimal. Tests provide comprehensive coverage including important edge cases. No bugs or improvements needed.
