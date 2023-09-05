# https://leetcode.com/problems/copy-list-with-random-pointer/

from RNode import Node


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        We need to preformt 3 operation
        1. put duplicates after original nodes
        2. connect random pointers
        3. unchain
        """
        if not head:
            return None

        temp = head
        while temp:
            newNode = Node(temp.val, temp.next)
            temp.next = newNode
            temp = newNode.next

        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        newHead = head.next
        temp = head
        newNode = head.next
        while temp:
            tempNext = newNode.next
            temp.next = tempNext
            temp = tempNext

            # If temp is None, newNode already points to None.
            if temp:
                newNodeNext = temp.next
                newNode.next = newNodeNext
                newNode = newNodeNext

        return newHead


if __name__ == '__main__':
    sol = Solution()
    ll = Node(1)
    ll.next = Node(2)
    ll.next.random = ll

    x = sol.copyRandomList(ll)
    print()