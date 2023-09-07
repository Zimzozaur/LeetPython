# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional
from ListNode import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Check the length
        Splint in two parts
        revers second part
        run both and check are vals the same
        """

        list_len = 0
        temp = head
        while temp:
            list_len += 1
            temp = temp.next

        if list_len == 1:
            return True

        mid = list_len // 2 - 1
        before = head
        for i in range(mid):
            before = before.next

        if list_len % 2 == 0:
            head2 = before.next
        else:
            pivot = before.next
            head2 = pivot.next
            print(pivot.val)
            pivot.next = None
        before.next = None

        pre = None
        while head2:
            after = head2.next
            head2.next = pre
            pre = head2
            head2 = after
        head2 = pre

        while head2 and head:
            if head2.val != head.val:
                return False
            head = head.next
            head2 = head2.next
        return True


if __name__ == '__main__':
    sol = Solution()
    node = ListNode(1)
    # node.next = ListNode(1)
    # node.next.next = ListNode(3)
    # node.next.next = ListNode(4)

    print(sol.isPalindrome(node))
