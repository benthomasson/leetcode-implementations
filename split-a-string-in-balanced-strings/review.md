# Review: Split a String in Balanced Strings

## Solution
- **Approach**: Greedy counter approach - increment for 'R', decrement for 'L', count splits when balance reaches zero.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct algorithm, but function name `find_special_integer` is wrong for this problem (should be `balanced_string_split` or similar)

## Tests
- **Coverage**: Good - includes all LeetCode examples plus edge cases (minimal, alternating, nested, longer strings)
- **Edge Cases**: Yes - minimal (RL/LR), max splits (alternating), deeply nested, mixed nesting, and longer strings (500 pairs)

## Plan
- **Quality**: Adequate - correctly identifies greedy counter approach, but contains wrong function name from copy-paste error

## Overall
Algorithm and tests are solid, but the function name `find_special_integer` is clearly wrong (likely copy-pasted from a different problem about finding special integers). Should be renamed to match the balanced strings problem.
