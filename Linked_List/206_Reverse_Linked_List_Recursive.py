# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional
from Soriting.ListNode import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        tail = head
        if head.next:
            tail = self.reverseList(head.next)
            head.next.next = head
            head.next = None

        return tail


if __name__ == '__main__':
    sol = Solution()
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    me = sol.reverseList(node1)
    print("me")
