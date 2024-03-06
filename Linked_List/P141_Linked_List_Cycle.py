# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional
from ListNode import ListNode


# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         """
#         Fast pointer slow pointer
#
#         Cases: Is cycle or no
#         """
#         fast = head
#         slow = head
#
#         while fast:
#             fast = fast.next
#             if not fast:
#                 break
#             fast = fast.next
#             slow = slow.next
#             if slow == fast:
#                 return True
#         return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        HashSet Solution
        Time: O(n)
        Space: O(n)
        """
        node_set = set()
        pointer = head

        while pointer:
            if pointer not in node_set:
                node_set.add(pointer)
            else:
                return True
            pointer = pointer.next
        return False

