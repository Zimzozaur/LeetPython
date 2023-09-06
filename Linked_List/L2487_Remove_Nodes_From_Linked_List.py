# https://leetcode.com/problems/remove-nodes-from-linked-list/description/
from ListNode import ListNode
from typing import Optional

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(temp):
            pre = None
            while temp:
                after = temp.next
                temp.next = pre
                pre = temp
                temp = after
            return pre

        head = reverse(head)
        last = 0
        temp = head
        pre = head
        while temp:
            if temp.val > last:
                last = temp.val
                pre = temp
            else:
                pre.next = temp.next
            temp = temp.next

        return reverse(head)


if __name__ == '__main__':
    sol = Solution()
    node = ListNode(4)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(8)
    node.next.next.next.next = ListNode(3)

    y = sol.removeNodes(node)
    print()
