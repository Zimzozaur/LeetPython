# https://leetcode.com/problems/merge-k-sorted-lists/

import math
from typing import Optional, List
from Soriting.ListNode import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merge linked lists and sort them"""
        if not lists and len(lists) < 1:
            return None
        elif len(lists) == 1:
            return lists[0]

        if len(lists) % 2 == 0:
            lists[0] = self.merge_lists(lists[0], lists[-1])
            number_of_iterations = len(lists) - 1
        else:
            number_of_iterations = len(lists)

        while number_of_iterations > 1:
            put_to_place = 0
            for i in range(0, number_of_iterations, 2):
                list_one = lists[i]
                list_two = lists[i + 1] if i + 1 < number_of_iterations else None
                lists[put_to_place] = self.merge_lists(list_one, list_two)
                put_to_place += 1

            number_of_iterations = int(math.ceil(number_of_iterations / 2))

        return lists[0]

    def merge_lists(self, list_one, list_two):
        """Merge two linked lists"""

        dummy = ListNode()
        tail = dummy

        while list_one and list_two:
            if list_one.val < list_two.val:
                tail.next = list_one
                list_one = list_one.next
            else:
                tail.next = list_two
                list_two = list_two.next

            tail = tail.next

        if list_one:
            tail.next = list_one
        if list_two:
            tail.next = list_two

        return dummy.next


if __name__ == '__main__':

    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)

    ll2 = ListNode(4)
    ll2.next = ListNode(5)

    ll3 = ListNode(6)
    ll3.next = ListNode(7)

    sol = Solution()

    sol.mergeKLists([ll1, ll2, ll3])

