# Review: Count Number of Pairs With Absolute Difference K

## Solution
- **Approach**: Uses frequency counter to count pairs; for each value v, multiplies count[v] by count[v+k].
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Correctness**: Has Issues - function name `chalk_replacer` doesn't match the problem (should be something like `count_pairs`)

## Tests
- **Coverage**: Good - covers examples, edge cases, and various scenarios
- **Edge Cases**: Yes - single element, no pairs, identical elements, large k, boundary values

## Plan
- **Quality**: No plan provided

## Overall
Algorithm is correct and efficient, but the function is misnamed as `chalk_replacer` instead of something appropriate for counting pairs. Tests are comprehensive and well-structured.
