# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

from typing import Optional
from TreeNode import *
from tree_generator import binary_tree_generator


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        arr = []

        def traverse(root):
            if root:
                arr.append(root.val)
                traverse(root.left)
                traverse(root.right)

        traverse(root)

        return arr


if __name__ == '__main__':
    sol = Solution()
    x = [i for i in range(1, 500)]
    tree = binary_tree_generator(x)
    print(sol.postorderTraversal(tree))