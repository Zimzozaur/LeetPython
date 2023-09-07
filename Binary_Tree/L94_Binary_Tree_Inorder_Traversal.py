# https://leetcode.com/problems/binary-tree-inorder-traversal/
from typing import Optional
from TreeNode import *


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """Traversal Tree in-order then return array of values"""

        arr = []

        def traverse(root):
            if root:
                traverse(root.left)
                arr.append(root.val)
                traverse(root.right)

        traverse(root)

        return arr


