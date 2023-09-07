# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
from typing import Optional
from TreeNode import TreeNode
from tree_generator import tree_generate

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def reverse(root):
            if not root:
                return
            root.left = reverse(root.left)
            root.right = reverse(root.right)
            root.left, root.right = root.right, root.left
            return root

        def max_right(root):
           if not root.right:
               return root
           return max_right(root.right)

        def connect_next(root):
            if not root:
                return None
            root.right = connect_next(root.right)
            if root.left:
                nonlocal pointer
                pointer.right = root.left
                pointer = max_right(root)
                root.left = None
                connect_next(root.right)

            return root

        if not root:
            return None
        reverse(root)
        pointer = max_right(root)
        connect_next(root)


if __name__ == '__main__':
    sol = Solution()
    arr = [1,2,3,4,5,6,7]
    tree = tree_generate(arr)
    tree.display()
    y = sol.flatten(tree)
    tree.display()


