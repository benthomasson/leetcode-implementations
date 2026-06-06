# Plan (Iteration 1)

Task: Solve the LeetCode problem "decompress-run-length-encoded-list":

We are given a list `nums` of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements `[freq, val] = [nums[2*i], nums[2*i+1]]` (with `i >= 0`). For each such pair, there are `freq` elements with value `val` concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

**Example 1:**

**Input:** nums = \[1,2,3,4\]
**Output:** \[2,4,4,4\]
**Explanation:** The first pair \[1,2\] means we have freq = 1 and val = 2 so we generate the array \[2\].
The second pair \[3,4\] means we have freq = 3 and val = 4 so we generate \[4,4,4\].
At the end the concatenation \[2\] + \[4,4,4\] is \[2,4,4,4\].

**Example 2:**

**Input:** nums = \[1,1,2,3\]
**Output:** \[1,3,3\]

**Constraints:**

*   `2 <= nums.length <= 100`
*   `nums.length % 2 == 0`
*   `1 <= nums[i] <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: add_rooms

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. Summary: step through pairs with `range(0, len(nums), 2)`, extend result with `[val] * freq`. Two files to create — `solution.py` and `tests/test_solution.py`. High confidence, straightforward problem.

[Committed changes to planner branch]