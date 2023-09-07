# https://leetcode.com/problems/binary-tree-postorder-traversal/

from typing import Optional
from TreeNode import *


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        arr = []

        def traverse(root):
            if root:
                traverse(root.left)
                traverse(root.right)
                arr.append(root.val)

        traverse(root)

        return arr
