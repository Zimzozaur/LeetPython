#https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from TreeNode import *


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Given the root of a binary tree, inverts the tree, and return its root.
        :param root:
        :return:

        Return when children are null.
        """

        if root is None:
            return

        # Swap the children
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)  # Go deeper to the next level.
        self.invertTree(root.right)
        return root


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    sol.invertTree(root)
    print(root.left.val, root.right.val)