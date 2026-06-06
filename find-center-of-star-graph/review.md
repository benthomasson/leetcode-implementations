# Review: Find Center of Star Graph

## Solution
- **Approach**: Find common node between first two edges by checking if edges[0][0] appears in edges[1], otherwise return edges[0][1]
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)
- **Correctness**: Has Issues - Wrong function name `maximum_wealth` (should be `findCenter` or similar)

## Tests
- **Coverage**: Good - includes problem examples, minimal graph, various center positions, large labels, and many edges
- **Edge Cases**: Yes - covers minimal 3-node graph, center at different positions, large node labels, and large number of edges

## Plan
- **Quality**: Good - correctly identifies O(1) algorithm by checking first two edges

## Overall
The algorithm is correct and efficient, but there's a critical bug: the function is named `maximum_wealth` instead of matching the problem (e.g., `findCenter`). All tests call the wrong function name. The logic correctly finds the common node between the first two edges in O(1) time.
