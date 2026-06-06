# Review: Final Prices With a Special Discount in a Shop

## Solution
- **Approach**: Monotonic increasing stack to find the next smaller or equal price for each item, processing in O(n) time.
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes all examples, single element, equal prices, increasing/decreasing sequences, and constraint test with n=500
- **Edge Cases**: Yes - covers n=1, n=500, discount to zero, no discounts available, all equal prices

## Plan
- **Quality**: Adequate - correctly identifies algorithm and complexity, but contains copy-paste errors (BST references and maxSumBST function name are unrelated to this problem)

## Overall
Solution is correct and optimal using monotonic stack. Tests are comprehensive with excellent edge case coverage. Plan has copy-paste contamination from a different problem but implementation correctly solves the discount problem.
