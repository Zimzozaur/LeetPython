# https://leetcode.com/problems/reverse-linked-list-ii/?envType=daily-question&envId=2023-09-07
from typing import Optional
from ListNode import ListNode, list_generator


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Corners:
        1. left is head - head to ostatni a pierwszy zostanie połączony z kolejnym po head
        2. right is tail -
            Jeżeli po przekręceniu list następny node to połącz ostatni nieprzekręcony z ostatnim nodem
        3. left is right - return head

        pointers:
        1. head
        2. first that will be last
        3. last that will be first
        4. last that will be connected to 2nd
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

        if left == 1:
            first_to_last.next = first_in_tail
            head = last_to_first
        else:
            first_to_last.next = first_in_tail
            tail_in_head.next = last_to_first

        return head


if __name__ == '__main__':
    sol = Solution()
    x = [99, 43, 89, 100, 24, 14, 71, 96, 34, 75, 68, 7, 64, 74, 83, 80, 15, 50, 66, 14, 76, 15, 61, 43, 14, 84, 40, 57, 42, 74, 33, 21, 22, 89, 13, 69, 71, 63, 4, 88, 70, 27, 51, 7, 100, 81, 56, 4, 100, 96, 81, 88, 60, 65, 95, 92, 20, 88, 46, 18, 85, 46, 82, 48, 80, 45, 92, 33, 55, 8, 72, 89, 97, 77, 25, 48, 87, 68, 34, 80, 73, 9, 93, 21, 93, 66, 61, 10, 48, 34, 46, 76, 53, 59, 8, 33, 25, 16, 17, 77]
    y = list_generator(x)
    sol.reverseBetween(y, 3, 5)
    print()


