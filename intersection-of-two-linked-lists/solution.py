from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """Find the node where two linked lists intersect.

        Args:
            headA: Head of the first linked list.
            headB: Head of the second linked list.

        Returns:
            The intersecting node, or None if no intersection.
        """
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
