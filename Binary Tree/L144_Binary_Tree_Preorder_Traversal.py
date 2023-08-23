# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

from typing import Optional
from TreeNode import *


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        arr = []

        def traverse(root):
            if root:
                arr.append(root.val)
                traverse(root.left)
                traverse(root.right)

        traverse(root)

        return arr
