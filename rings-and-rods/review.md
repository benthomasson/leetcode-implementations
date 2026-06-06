# Review: Rings and Rods

## Solution
- **Approach**: Uses defaultdict with sets to track colors per rod, then counts rods with exactly 3 colors
- **Time Complexity**: O(n) where n is the length of the rings string
- **Space Complexity**: O(1) - at most 10 rods with 3 colors each
- **Correctness**: Has Issues - function name is `findFarmland` but should match the problem (likely `countPoints` per LeetCode)

## Tests
- **Coverage**: Good - includes LeetCode examples, edge cases (empty string, all rods, duplicates, max input)
- **Edge Cases**: Yes - covers single rod, no qualifying rods, multiple qualifying rods, duplicate colors, empty input

## Plan
- **Quality**: Adequate - correct algorithm identified (parse-and-count with sets), but wrong function name specified

## Overall
Solution logic is correct and efficient, but the function name `findFarmland` doesn't match the "Rings and Rods" problem (appears to be a copy-paste error from a different problem). Tests are comprehensive and well-structured. Rename function to match LeetCode's expected signature.
