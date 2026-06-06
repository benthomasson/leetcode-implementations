# Review: Pass the Pillow

## Solution
- **Approach**: Uses modular arithmetic to determine direction (even/odd passes) and position based on remainder, avoiding simulation
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers both examples, edge cases, boundary conditions, and multiple cycle scenarios
- **Edge Cases**: Yes - time=0, pillow at end position, full round trip, n=2 bouncing, max constraints, multiple complete cycles

## Plan
- **Quality**: Adequate - correctly identifies O(1) formula approach and avoids simulation loop as required

## Overall
The solution correctly implements an O(1) formula using modular arithmetic to determine position without simulating each pass. Tests are comprehensive and all edge cases are properly covered. No bugs or issues found.
