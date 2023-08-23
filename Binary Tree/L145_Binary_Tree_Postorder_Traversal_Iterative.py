# https://leetcode.com/problems/binary-tree-inorder-traversal/
from collections import deque
from typing import Optional
from TreeNode import *


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """Traversal Tree post-order iteratively then return an array of values"""

        if not root:
            return []

        arr = []
        stack = deque([root])

        while stack:
            if not stack[-1].right and not stack[-1].left:
                arr.append(stack[-1].val)
                tree_node = stack.pop()
                if stack:
                    if stack[-1].left == tree_node:
                        stack[-1].left = None
                    else:
                        stack[-1].right = None
            elif stack[-1].left:
                stack.append(stack[-1].left)
            else:
                stack.append(stack[-1].right)

        return arr


if __name__ == '__main__':
    sol = Solution()

    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)

    print(sol.inorderTraversal(tree))

