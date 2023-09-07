# https://leetcode.com/problems/binary-tree-preorder-traversal/
from collections import deque
from typing import Optional
from TreeNode import *


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """Traversal Tree pre-order iteratively then return an array of values"""

        if not root:
            return []

        arr = []
        stack = deque([root])

        while stack:

            if not stack[-1]:
                stack.pop()
                continue

            node = stack.pop()
            stack.append(node.right)
            stack.append(node.left)
            arr.append(node.val)

        return arr


if __name__ == '__main__':
    sol = Solution()

    tree = TreeNode(3)
    tree.left = TreeNode(1)
    tree.right = TreeNode(2)

    print(sol.preorderTraversal(tree))
