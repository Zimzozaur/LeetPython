# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
from TreeNode import *


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        arr = []

        def dfs(root):
            nonlocal arr
            if not root:
                return

            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        def change(root):
            nonlocal arr_sum
            if not root:
                return

            change(root.left)
            temp = root.val
            root.val = arr_sum
            arr_sum -= temp
            change(root.right)

        dfs(root)
        arr_sum = sum(arr)
        change(root)
        return root


if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(2)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    sol.bstToGst(tree)

    print()
