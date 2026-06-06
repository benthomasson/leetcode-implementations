# Review: Count Asterisks

## Solution
- **Approach**: Single pass through string with boolean toggle to track position relative to paired vertical bars, counting asterisks only when outside pairs.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - includes all examples plus edge cases
- **Edge Cases**: Yes - consecutive bars (empty pairs), no bars, all inside pairs, single character, no asterisks

## Plan
- **Quality**: Good - accurately describes toggle-based algorithm, appropriately brief for minimal effort level

## Overall
Clean, correct solution with comprehensive test coverage. The toggle approach efficiently handles paired bars in a single pass, and tests cover all relevant edge cases including empty pairs and boundary conditions.
