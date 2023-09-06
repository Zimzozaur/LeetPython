# https://leetcode.com/problems/split-linked-list-in-parts/?envType=daily-question&envId=2023-09-06
from ListNode import ListNode
from typing import Optional


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        def disjoint(ll, chunks, size, additional=0):
            result = []
            temp = ll
            for i in range(chunks):
                if additional > 0:
                    nodes = size + 1
                    additional -= 1
                else:
                    nodes = size
                for j in range(nodes - 1):
                    temp = temp.next

                after = temp.next
                temp.next = None
                result.append(ll)
                temp = ll = after
            return result

        list_len = 0
        temp = head
        while temp:
            list_len += 1
            temp = temp.next

        rest = list_len % k
        size = int((list_len - rest) / k)

        if list_len < k:
            size = 1
            arr = disjoint(head, list_len, size)
            for i in range(k - list_len):
                arr.append(None)
            return arr

        return disjoint(head, k, size, rest)


if __name__ == '__main__':
    sol = Solution()

    nod = ListNode(1)
    nod.next = ListNode(2)
    nod.next = ListNode(3)

    # node3 = ListNode(8)
    # node3.next = ListNode(9)
    # node3.next.next = ListNode(10)
    # node2 = ListNode(4)
    # node2.next = ListNode(5)
    # node2.next.next = ListNode(6)
    # node2.next.next.next = ListNode(7)
    # node2.next.next.next.next = node3
    # node1 = ListNode(1)
    # node1.next = ListNode(2)
    # node1.next.next = ListNode(3)
    # node1.next.next.next = node2

    y = sol.splitListToParts(nod, 3)
    print()



