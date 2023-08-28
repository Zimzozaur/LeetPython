from typing import Optional
from TreeNode import *


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Return max length between nodes
        The length of a path between two nodes is
        represented by the number of edges between them

        Check max level of depth for every node in a

        Chce rekurencyjnie dla kazegej kilki sprawdzic jak daleko mozna pojsc
        return odległosć w prawo i lewo i zwrócić maksymalną różniece
        """

        result = 0

        def max_depth(root, depth):

            nonlocal result

            # Base Case
            if not root.left and not root.right:
                return depth

            left_depth = None
            right_depth = None

            if root.left:
                left_depth = max_depth(root.left, depth + 1)
            if root.right:
                right_depth = max_depth(root.right, depth + 1)

            if isinstance(left_depth, int) and isinstance(right_depth, int):
                curr = sum((left_depth, right_depth))
                if curr > result:
                    result = curr
                return max(left_depth, right_depth)
            elif isinstance(left_depth, int):
                if left_depth > result:
                    result = left_depth
                return left_depth
            elif isinstance(right_depth, int):
                if right_depth > result:
                    result = right_depth
                return right_depth

        max_depth(root, 0)

        return result


if __name__ == '__main__':
     sol = Solution()

     groot = TreeNode(2)
     groot.left = TreeNode(1)
     groot.right = TreeNode(3)
     groot.left.left = TreeNode(4)
     groot.left.right = TreeNode(5)

     print(sol.diameterOfBinaryTree(groot))
