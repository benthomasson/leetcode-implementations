# Review: Sum of All Odd Length Subarrays

## Solution
- **Approach**: O(n) contribution counting—for each element at index i, calculates how many odd-length subarrays contain it using formula `((i+1) * (n-i) + 1) // 2`, then multiplies by element value and sums.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good—all 3 examples covered plus edge cases (single element, uniform array, max constraints)
- **Edge Cases**: Yes—single element, all same values, and maximum constraint boundary (100 elements of value 1000)

## Plan
- **Quality**: Good—brief as requested for MINIMAL effort level, correctly identifies optimal O(n) contribution-counting approach with the mathematical formula

## Overall
Optimal solution with correct mathematical formula. Clean implementation with comprehensive test coverage including boundary cases. No issues found.
