# Review: Sum of Unique Elements

## Solution
- **Approach**: Uses Counter to count element frequencies, then sums values appearing exactly once.
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Correctness**: Has Issues - Function name `bestTeamScore` is incorrect for this problem (likely copy-paste error). Logic is correct.

## Tests
- **Coverage**: Good - covers examples, single element, all duplicates, boundary values, and mixed cases
- **Edge Cases**: Yes - single element, all duplicates, boundary values (1, 100), and mixed unique/duplicate elements

## Plan
- **Quality**: Adequate - Algorithm choice is correct and brief, but specifies wrong function name (`bestTeamScore` instead of something like `sumOfUnique`)

## Overall
The algorithm and tests are solid, but there's a critical naming bug: the function is called `bestTeamScore` when it should match the problem (sum-of-unique-elements). This appears to be a copy-paste error from a different LeetCode problem.
