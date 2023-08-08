# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from TreeNode import *


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Check is tree a height-balanced tree"""

        # Base case
        if not root:
            return True

        # Check length for both branches
        left = count_max_depth(root.left)
        right = count_max_depth(root.right)

        # When not balanced
        if abs(left - right) > 1:
            return False

        # When balanced go level deeper
        left_bool = self.isBalanced(root.left)
        right_bool = self.isBalanced(root.right)
        if left_bool and right_bool:
            return True
        return False


def count_max_depth(root: Optional[TreeNode]):
    """Count maximum depth of a binary tree"""

    # Base case
    if not root:
        return 0

    # Go level deeper
    depth_left = count_max_depth(root.left)
    depth_right = count_max_depth(root.right)

    return 1 + max(depth_left, depth_right)  # Pick greater depth


if __name__ == '__main__':
    sol = Solution()
    groot = TreeNode(1)
    groot.left = TreeNode(2)
    groot.right = TreeNode(3)
    groot.right.left = TreeNode(4)
    groot.right.right = TreeNode(5)
    print(sol.isBalanced(groot))
