# Review: Available Captures for Rook

## Solution
- **Approach**: Scan board to find rook position, then ray-cast in 4 cardinal directions until hitting edge, bishop (blocked), or pawn (captured).
- **Time Complexity**: O(1) - fixed 8×8 board
- **Space Complexity**: O(1) - constant variables only
- **Correctness**: Correct algorithm, but **critical naming issue** - function name `regionsBySlashes` belongs to a completely different LeetCode problem

## Tests
- **Coverage**: Good - tests all 3 examples plus 6 additional edge cases (corner positions, blocking scenarios, adjacent pawns, empty board)
- **Edge Cases**: Yes - covers rook in corners, center, bishops blocking pawns, pawns at various distances, and empty board

## Plan
- **Quality**: Adequate - correctly identifies the algorithm and notes the function name mismatch, but proceeds with the wrong name anyway rather than correcting it

## Overall
The solution correctly implements the rook capture logic with optimal complexity, and tests are thorough. However, the function is named `regionsBySlashes` which is for LeetCode problem #959 (Regions Cut By Slashes), not this problem. This should be renamed to something appropriate like `numRookCaptures` or `availableCapturesForRook`.
