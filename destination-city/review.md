# Review: Destination City

## Solution
- **Approach**: Creates a set of all source cities, then returns the first destination city not in that set.
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Correctness**: Has Issues - method name is `watched_videos_by_friends` instead of the correct name for this problem (should be `destCity` or similar). Implementation logic is correct.

## Tests
- **Coverage**: Good - tests linear chains, unordered paths, single paths, longer chains, and reversed order
- **Edge Cases**: Yes - empty paths (raises ValueError), single path, cities with spaces, mixed case

## Plan
- **Quality**: No plan provided

## Overall
The algorithm is correct and efficient, but the method is catastrophically misnamed as `watched_videos_by_friends` (a different LeetCode problem). All tests call this wrong method name. Rename the method to match the Destination City problem.
