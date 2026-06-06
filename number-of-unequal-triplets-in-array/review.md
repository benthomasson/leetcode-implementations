# Review: Number of Unequal Triplets in Array

## Solution
- **Approach**: Uses Counter to group values, then for each distinct value v, counts triplets by multiplying (elements in preceding groups) × (count of v) × (elements in following groups).
- **Time Complexity**: O(n)
- **Space Complexity**: O(d) where d is number of distinct values
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes both examples, edge cases (all distinct, all same, two distinct values), and various mixed scenarios
- **Edge Cases**: Yes - covers all same values (0 triplets), two distinct values (0 triplets), minimum size, and different count distributions

## Plan
- **Quality**: Adequate - brief as requested for minimal effort, correctly identifies Counter + combinatorial approach and O(n) complexity

## Overall
Clean, efficient solution using combinatorics. The algorithm correctly computes the number of triplets from three distinct value groups regardless of Counter iteration order. Test suite is comprehensive.
