# Review: Number of Students Unable to Eat Lunch

## Solution
- **Approach**: Count student preferences (0s and 1s), then iterate through sandwich stack; if no students want the current sandwich, return remaining count, otherwise decrement the preference count.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers both examples, single student cases, all-same-preference scenarios, and blocked midway situation
- **Edge Cases**: Yes - single element arrays, uniform preferences with match/mismatch, and the alias function

## Plan
- **Quality**: Good - concise description of algorithm, correctly identifies O(n) time and O(1) space complexity, notes the function name discrepancy

## Overall
The solution is optimal and correct, using a counting approach to avoid simulating the queue. Tests are thorough with good edge case coverage. The function name `min_time_to_remove_balloons` appears to be from a different problem but is properly aliased.
