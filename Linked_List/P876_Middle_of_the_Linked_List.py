# https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=daily-question&envId=2024-03-07
from ListNode import ListNode
from typing import Optional




class Solution:
    # Two pointer solution
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Edge cases:
            - One node
            - Even
            - Odd
        """
        slow_pointer = head
        fast_pointer = head

        # Move fast pointer twice as fast as slow pointer
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        # At this point, slow pointer is at the middle node
        return slow_pointer

    # Array solution
    def middleNodeArr(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Edge cases:
            - One node
            - Even
            - Odd
        """
        if not head.next:
            return head

        nodes = []
        pointer = head

        while pointer:
            nodes.append(pointer)
            pointer = pointer.next

        return nodes[len(nodes) // 2]

