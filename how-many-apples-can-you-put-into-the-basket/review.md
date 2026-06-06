# Review: How Many Apples Can You Put into the Basket

## Solution
- **Approach**: Sort weights ascending, greedily accumulate lightest apples until total exceeds 5000 capacity, return count before overflow.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1) auxiliary, O(n) for sorting
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers both examples, single element, exact capacity, overflow, all-fit, none-fit, and max constraint scenarios
- **Edge Cases**: Yes - handles single apple (fits/exceeds), exact capacity match, all items too heavy, minimum input, and boundary weights

## Plan
- **Quality**: Adequate - correctly identifies greedy algorithm with sorting, notes function name discrepancy in requirements, appropriately brief for MINIMAL effort level

## Overall
Solution correctly implements greedy approach with optimal algorithm choice. Comprehensive test coverage includes all critical edge cases. Plan appropriately concise while capturing the core strategy.
