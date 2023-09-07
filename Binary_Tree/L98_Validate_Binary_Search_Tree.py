# https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional
from TreeNode import TreeNode
from tree_generator import binary_tree_generator


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last = None

        def dfs(root):
            if not root:
                return True

            if not dfs(root.left):
                return False

            nonlocal last
            if last is None or root.val > last:
                last = root.val
            else:
                return False

            if not dfs(root.right):
                return False

            return True

        return dfs(root)


if __name__ == '__main__':
    sol = Solution()
    arr = [i for i in range(1, 500)]
    print(arr)
    tree = binary_tree_generator(arr)
    tree.right.left.left.left = TreeNode(1)
    print(sol.isValidBST(tree))

