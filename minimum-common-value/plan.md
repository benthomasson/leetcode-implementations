# Plan (Iteration 1)

Task: Solve the LeetCode problem "minimum-common-value":

Given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, return _the **minimum integer common** to both arrays_. If there is no common integer amongst `nums1` and `nums2`, return `-1`.

Note that an integer is said to be **common** to `nums1` and `nums2` if both arrays have **at least one** occurrence of that integer.

**Example 1:**

**Input:** nums1 = \[1,2,3\], nums2 = \[2,4\]
**Output:** 2
**Explanation:** The smallest element common to both arrays is 2, so we return 2.

**Example 2:**

**Input:** nums1 = \[1,2,3,6\], nums2 = \[2,3,4,5\]
**Output:** 2
**Explanation:** There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

**Constraints:**

*   `1 <= nums1.length, nums2.length <= 105`
*   `1 <= nums1[i], nums2[j] <= 109`
*   Both `nums1` and `nums2` are sorted in **non-decreasing** order.

**Requirements:**
- Implement the solution with proper type hints
- Add comprehensive Google-style docstring
- Create thorough unit tests covering edge cases
- Optimize for time and space complexity
- Function name should be: min_common_number

IMPORTANT - EFFORT LEVEL: MINIMAL
Keep plan VERY brief (2-3 paragraphs max). Focus only on algorithm choice. Skip architectural discussions and detailed analysis.

Plan written to `PLAN.md`. The two-pointer approach is the clear optimal choice here — O(n+m) time, O(1) space, and trivial to implement given the sorted constraint.

[Committed changes to planner branch]