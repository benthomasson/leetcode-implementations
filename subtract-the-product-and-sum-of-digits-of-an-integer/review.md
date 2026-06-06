# Review: Subtract the Product and Sum of Digits of an Integer

## Solution
- **Approach**: Extract digits using modulo and integer division, accumulate product (starting at 1) and sum (starting at 0), return product minus sum
- **Time Complexity**: O(log n) where n is the input (or O(d) where d is the number of digits)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes both examples, single digit, boundary case (n=1), zero-containing numbers, and large values
- **Edge Cases**: Yes - covers single digit (5), n=1, numbers with zero digits (10, 100000), max same digits (99999), and two-digit numbers

## Plan
- **Quality**: Good - correctly identifies the algorithm (digit extraction via modulo/division), analyzes complexity, and catches the function naming error from the requirements

## Overall
Solution is correct and efficient with O(log n) time and O(1) space. Test coverage is comprehensive, including important edge cases like zero-containing numbers where product becomes 0.
