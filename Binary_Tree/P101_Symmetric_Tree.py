# https://leetcode.com/problems/symmetric-tree/
from TreeNode import TreeNode
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """BFS + Two lists for left and right side"""
        left = []
        right = []
        if root.left:
            left.append(root.left)
        if root.right:
            right.append(root.right)

        while True:
            for node_l, node_r in zip(left, right[::-1]):
                if not node_l and not node_r:
                    continue
                elif node_l and not node_r or not node_l and node_r:
                    return False
                elif node_l.val != node_r.val:
                    return False

            new_l = []
            for node in left:
                if node:
                    new_l.append(node.left)
                    new_l.append(node.right)

            new_r = []
            for node in right:
                if node:
                    new_r.append(node.left)
                    new_r.append(node.right)

            left = new_l
            right = new_r

            if len(left) != len(right):
                return False

            if len(left) == 0 and len(right) == 0:
                return True