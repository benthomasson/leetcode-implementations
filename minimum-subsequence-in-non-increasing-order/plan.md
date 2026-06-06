# Plan (Iteration 1)

Task: Solve the LeetCode problem "minimum-subsequence-in-non-increasing-order":

Given the array `nums`, obtain a subsequence of the array whose sum of elements is **strictly greater** than the sum of the non included elements in such subsequence.

If there are multiple solutions, return the subsequence with **minimum size** and if there still exist multiple solutions, return the subsequence with the **maximum total sum** of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.

Note that the solution with the given constraints is guaranteed to be **unique**. Also return the answer sorted in **non-increasing** order.

**Example 1:**

**Input:** nums = \[4,3,10,9,8\]
**Output:** \[10,9\] 
**Explanation:** The subsequences \[10,9\] and \[10,8\] are minimal such that the sum of their elements is strictly greater than the sum of elements not included. However, the subsequence \[10,9\] has the maximum total sum of its elements. 

**Example 2:**

**Input:** nums = \[4,4,7,6,7\]
**Output:** \[7,7,6\] 
**Explanation:** The subsequence \[7,7\] has the sum of its elements equal to 14 which is not strictly greater than the sum of elements not included (14 = 4 + 4 + 6). Therefore, the subsequence \[7,6,7\] is the minimal satisfying the conditions. Note the subsequence has to be returned in non-decreasing order.  

**Constraints:**

*   `1 <= nums.length <= 500`
*   `1 <= nums[i] <= 100`

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: min_changes_to_divide_string

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `planner/PLAN.md`. The approach is a simple greedy algorithm — sort descending, take elements until the subsequence sum exceeds the remainder.

[Committed changes to planner branch]