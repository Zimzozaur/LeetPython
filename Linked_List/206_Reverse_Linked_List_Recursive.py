# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional
from ListNode import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Revers list Recursively"""

        # Base case
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head

    def reverseListRecursive(self, head):
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                next = cur.next
                cur.next = prev
                return reverse(next, cur)

        return reverse(head, None)

    def reverseListYT(self, node, prev=None):
        if node == None:
            return prev
        else:
            next = node.next
            node.next = prev
            return self.reverseList(next, prev=node)

    def reverseListLong(self, head: ListNode) -> ListNode:
        # Recursive answer
        # Base case: If the list is empty or has only one node, it's already reversed.
        if not head or not head.next:
            return head

        # Recursive call to reverse the remaining part of the linked list.
        # Break it down to sub problems to keep reversing.
        # reversed_head will be the head of the reversed linked list for the rest of the nodes.
        reversed_head = self.reverseListLong(head.next)

        # At this point, head.next points to the next node in the original list,
        # which will be the last node in the reversed linked list.
        # We need to make the next node point to the current head node, effectively reversing the link.
        print(head.next.next)
        head.next.next = head
        print(head.next.next.val)

        # Set the current head's next pointer to None, as it will be the last node in the reversed linked list.
        head.next = None

        # Return the new head of the reversed linked list (reversed_head).
        return reversed_head


if __name__ == '__main__':
    sol = Solution()
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    me = sol.reverseListLong(node1)
    print("me")
