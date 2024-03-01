# https://leetcode.com/problems/even-odd-tree/?envType=daily-question&envId=2024-02-29
from TreeNode import TreeNode
from collections import deque


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        """
        For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).

        For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
        """
        curr = deque([root])
        odd = True
        while curr:
            prev = None
            for _ in range(len(curr)):
                node = curr.popleft()
                if prev and not (prev.val < node.val if odd else prev.val > node.val):
                    return False
                if not node.val % 2 == (1 if odd else 0):
                    return False
                prev = node
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            odd = not odd
        return True
