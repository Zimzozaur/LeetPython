# https://leetcode.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
from typing import Optional
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Counts maximum depth of a tree
        :param depth:
        :param root:
        :return:
        """

        # if not root:
        #     return 0
        #
        # # Goes one level deeper and adds +1
        # depth_left = self.maxDepth(root.left)
        # depth_right = self.maxDepth(root.right)
        #
        # return 1 + max(depth_left, depth_right)  # Picks greater depth

        # # Breath First Search
        #
        # if not root:
        #     return 0
        #
        # level = 0
        # deck = deque([root])
        # while deck:
        #
        #     for i in range(len(deck)):
        #         root = deck.popleft()
        #         if root.left:
        #             deck.append(root.left)
        #         if root.right:
        #             deck.append(root.right)
        #
        #     level += 1
        # return level

        # Iterative Depth first search

        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([root.left, depth + 1])
                stack.append([root.right, depth + 1])

        return res