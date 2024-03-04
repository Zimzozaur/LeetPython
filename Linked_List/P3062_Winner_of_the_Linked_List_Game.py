# https://leetcode.com/problems/winner-of-the-linked-list-game/description/?envType=weekly-question&envId=2024-03-01

from ListNode import ListNode
from typing import Optional


class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        d = {'Even': 0, 'Odd': 0}

        pointer = head
        while pointer:
            if pointer.val > pointer.next.val:
                d['Even'] = d.get('Even') + 1
            else:
                d['Odd'] = d.get('Odd') + 1

            pointer = pointer.next.next

        if d.get('Even') == d.get('Odd'):
            return 'Tie'
        elif d.get('Even') > d.get('Odd'):
            return 'Even'
        else:
            return 'Odd'

