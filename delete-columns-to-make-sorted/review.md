# Review: Delete Columns to Make Sorted

## Solution
- **Approach**: Iterate through each column and check if characters are sorted lexicographically row-by-row; count columns where any character is less than the previous row's character.
- **Time Complexity**: O(n*m) where n is number of strings, m is string length
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes all problem examples, single string, all same characters, single column (sorted/unsorted), and all sorted columns
- **Edge Cases**: Yes - covers single string, single column, equal characters, and boundary conditions

## Plan
- **Quality**: Good - correctly identifies the algorithm and complexity; notes function name discrepancy between requirements (minDifference) and actual LeetCode problem (minDeletionSize)

## Overall
Clean, correct implementation that efficiently solves the problem. Solution uses the correct LeetCode function name (minDeletionSize) despite plan mentioning minDifference. No bugs or improvements needed.
