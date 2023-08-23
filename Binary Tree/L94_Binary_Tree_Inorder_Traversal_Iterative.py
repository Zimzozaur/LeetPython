# https://leetcode.com/problems/binary-tree-inorder-traversal/
from collections import deque
from typing import Optional
from TreeNode import *


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """Traversal Tree in-order iteratively then return an array of values"""

        arr = []
        stack = deque([root])

        while stack:
            if stack[-1] is None:
                stack.pop()
                arr.append(stack[-1].val)
                stack.append(stack.pop().right)
            else:
                stack.append(stack[-1].left)

        return arr


