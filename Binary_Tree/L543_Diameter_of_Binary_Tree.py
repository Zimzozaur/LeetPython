from collections import deque
from typing import Optional
from TreeNode import *


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Return max length between nodes
        The length of a path between two nodes is
        represented by the number of edges between them

        Recursively go to the bottom
        add depth by one and sum of both branches
        check is bigger then the biggest
        chose bigger and go up
        """
        max_diameter = 0
        def count_diameter(root):
            nonlocal max_diameter
            if not root:
                return -1

            left = count_diameter(root.left)
            right = count_diameter(root.right)
            max_diameter = max(max_diameter, left + right + 2)

            return max(left, right) + 1

        count_diameter(root)
        return max_diameter

if __name__ == '__main__':
     sol = Solution()
     groot = TreeNode(2)
     groot.left = TreeNode(1)
     groot.right = TreeNode(3)
     groot.left.left = TreeNode(4)
     groot.left.right = TreeNode(5)

     print(sol.diameterOfBinaryTree(groot))
