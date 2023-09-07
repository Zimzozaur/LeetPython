# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from TreeNode import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Find the minimum depth of a binary tree

        The minimum depth is the number of nodes along the shortest path
        from the root node down to the nearest leaf node.
        """
        # If a tree is empty
        if root is None:
            return 0

        # Base case
        if root.left is None and root.right is None:
            return 1

        # Go level deeper and add 1 to return
        else:
            left_exists = root.left is not None
            right_exists = root.right is not None

            if left_exists and right_exists:
                # Chose smaller depth of 2 branches
                return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)
            elif left_exists:
                return self.minDepth(root.left) + 1
            else:
                return self.minDepth(root.right) + 1


if __name__ == '__main__':
    sol = Solution()
    groot = TreeNode(1)
    groot.left = TreeNode(2)
    # groot.right = TreeNode(3)
    # groot.left.left = TreeNode(4)
    # groot.left.right = TreeNode(5)

    print(sol.minDepth(groot))

