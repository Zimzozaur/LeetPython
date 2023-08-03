# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Counts maximum depth of a tree
        :param depth:
        :param root:
        :return:
        """

        if not root:
            return 0

        # Goes one level deeper and adds +1
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)

        return 1 + max(depth_left, depth_right)  # Picks greater depth


