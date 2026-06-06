# Review: Check If All A's Appears Before All B's

## Solution
- **Approach**: Checks if substring "ba" exists; if "ba" is present, some 'a' follows some 'b', violating the condition.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Has Issues - **CRITICAL BUG**: Function name `firstDayBeenInAllRooms` is completely wrong for this problem. Should be something like `checkString` based on typical LeetCode naming.

## Tests
- **Coverage**: Good - covers all major cases including edge cases
- **Edge Cases**: Yes - single characters, only a's, only b's, "ba" pattern, and interleaved patterns

## Plan
- **Quality**: Good - correctly identifies the one-liner algorithm

## Overall
The solution algorithm is correct and elegant, and tests are comprehensive. However, there is a **critical function naming error** - `firstDayBeenInAllRooms` is the name of a completely different LeetCode problem (1997) involving array visits. The function should be named `checkString` or similar based on the actual problem statement.
