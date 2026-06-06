# Review: Maximize Sum of Array After K Negations

## Solution
- **Approach**: Greedy algorithm that sorts the array, negates negative numbers from smallest to largest while k > 0, then if remaining k is odd, effectively negates the smallest absolute value element by subtracting 2*min(nums) from the total.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good — tests all provided examples plus edge cases (all positive with odd/even k, all negative, contains zero, single element scenarios)
- **Edge Cases**: Yes — covers single element, all positive, all negative, zero in array, and both odd/even remaining k values

## Plan
- **Quality**: Good — concise as requested for MINIMAL effort level, correctly identifies greedy approach and O(n log n) complexity, notes the function name inconsistency (`is_univalued` doesn't match this problem)

## Overall
Correct implementation with comprehensive test coverage. The plan correctly notes that `is_univalued` is the wrong function name for this problem; solution properly uses `largest_sum_after_k_negations` with an alias for compatibility.
