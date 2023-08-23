# https://leetcode.com/problems/delete-node-in-a-bst/
from typing import Optional
from TreeNode import *


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """"Delete node from Binary Tree"""

        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right and not root.left:
                root = None
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                smallest = find_smallest(root.right)
                root.val = smallest
                root.right = self.deleteNode(root.right, smallest)

        return root

def find_smallest(root):

    while root and root.left:
        root = root.left

    return root.val