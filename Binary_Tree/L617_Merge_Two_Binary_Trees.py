# https://leetcode.com/problems/merge-two-binary-trees/
from typing import Optional
from TreeNode import *


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        The merge rule is that if two nodes overlap,
        then sum node values up as the new value of the merged node.
        Otherwise, the NOT null node will be used as the node of the new tree.
        """
        if not root1:
            return root2
        if not root2:
            return root1

        def merge_tree(root1, root2):
            # Base case
            if not root1 and not root2:
                return
            if not root2:
                return root1
            if not root1:
                root1 = TreeNode(root2.val)
                root1.left = merge_tree(root1.left, root2.left)
                root1.right = merge_tree(root1.right, root2.right)
                return root1

            root1.val = root1.val + root2.val
            root1.left = merge_tree(root1.left, root2.left)
            root1.right = merge_tree(root1.right, root2.right)

            return root1

        return merge_tree(root1, root2)


if __name__ == '__main__':
    sol = Solution()

    tree1 = TreeNode(1)
    # tree1.left = TreeNode(2)
    # tree1.left.left = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.right = TreeNode(2)
    tree2.right.right = TreeNode(3)


    sol.mergeTrees(tree1, tree2)
    print()


    # tree1 = TreeNode(1)
    # tree2 = TreeNode(2)
    #
    # tree1.left = TreeNode(3)
    # tree2.left = TreeNode(1)
    #
    # tree1.right = TreeNode(2)
    # tree2.right = TreeNode(3)
    #
    # tree1.left.left = TreeNode(5)
    # tree2.left.right = TreeNode(4)
    #
    # tree2.right.right = TreeNode(7)