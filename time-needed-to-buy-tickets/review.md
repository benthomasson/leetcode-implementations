# Review: Time Needed to Buy Tickets

## Solution
- **Approach**: Mathematical formula counting contributions - people at/before position k contribute min(tickets[i], tickets[k]), people after k contribute min(tickets[i], tickets[k]-1)
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Correctness**: Correct

## Tests
- **Coverage**: Good - covers LeetCode examples, single person, k at various positions, different ticket distributions, and minimal cases
- **Edge Cases**: Yes - includes single person, k at boundaries (first/last), uniform tickets, and k with smallest value

## Plan
- **Quality**: Good - identifies the key mathematical insight to avoid simulation, appropriate brevity for minimal effort level

## Overall
Optimal solution using formula instead of simulation. All tests pass and cover edge cases thoroughly. No bugs or improvements needed.
