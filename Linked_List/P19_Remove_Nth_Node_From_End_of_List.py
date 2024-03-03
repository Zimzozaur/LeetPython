# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=daily-question&envId=2024-03-03
from typing import Optional
from ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the list and return its head

        Loop over list and put nodes into HashMap
        Count which node to remove and perform it on node from HashMap
        """

        hash_map = {}

        i = 0
        pointer = head
        while pointer:
            hash_map[i] = pointer
            pointer = pointer.next
            i += 1

        if len(hash_map) == 1:
            head = None
        elif n == 1:
            hash_map[i - 2].next = None
        elif n == len(hash_map):
            head = head.next
        else:
            hash_map[i - n - 1].next = hash_map[i - n + 1]

        return head


