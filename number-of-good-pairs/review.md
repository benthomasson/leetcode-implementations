# Review: Number of Good Pairs

## Solution
- **Approach**: Single-pass hash map that counts previous occurrences of each number, adding the count to the result before incrementing (each previous occurrence forms a good pair with the current index).
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes all examples, single element, pairs, no pairs, and maximum constraint boundary
- **Edge Cases**: Yes - minimum size (1 element), all identical elements, all different elements, and maximum size (100 elements)

## Plan
- **Quality**: Adequate - briefly describes the hash map counting approach, appropriate for minimal effort level

## Overall
Optimal solution with correct implementation and comprehensive test coverage. The algorithm efficiently counts good pairs in a single pass, and tests validate correctness across edge cases and constraint boundaries.
