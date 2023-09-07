# https://leetcode.com/problems/reverse-linked-list-ii/?envType=daily-question&envId=2023-09-07
from typing import Optional
from ListNode import ListNode, list_generator


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        left and right where left <= right,
        reverse the nodes of the list from position left to position right
        return the reversed list.
        """

        if left == right:
            return head

        pre = None
        temp = head
        for i in range(1, right + 1):
            if i == left - 1:
                tail_in_head = temp
            if i == left:
                first_to_last = temp
            if i == right:
                last_to_first = temp
                first_in_tail = temp.next

            if left <= i <= right:
                reverse = temp
                temp = temp.next
                reverse.next = pre
                pre = reverse
            else:
                temp = temp.next

        first_to_last.next = first_in_tail
        if left == 1:
            head = last_to_first
        else:
            tail_in_head.next = last_to_first

        return head


if __name__ == '__main__':
    sol = Solution()
    x = [99, 43, 89, 100, 24, 14, 71, 96, 34, 75, 68, 7, 64, 74, 83, 80, 15, 50, 66, 14, 76, 15, 61, 43, 14, 84, 40, 57, 42, 74, 33, 21, 22, 89, 13, 69, 71, 63, 4, 88, 70, 27, 51, 7, 100, 81, 56, 4, 100, 96, 81, 88, 60, 65, 95, 92, 20, 88, 46, 18, 85, 46, 82, 48, 80, 45, 92, 33, 55, 8, 72, 89, 97, 77, 25, 48, 87, 68, 34, 80, 73, 9, 93, 21, 93, 66, 61, 10, 48, 34, 46, 76, 53, 59, 8, 33, 25, 16, 17, 77]
    y = list_generator(x)
    sol.reverseBetween(y, 3, 5)
    print()


