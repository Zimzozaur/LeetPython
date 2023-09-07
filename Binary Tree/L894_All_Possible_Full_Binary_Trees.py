# https://leetcode.com/problems/all-possible-full-binary-trees/
from TreeNode import *
from typing import Optional

class Solution:
    def allPossibleFBT(self, n: int):
        if n % 2 == 0:
            return None
        if n == 1:
            return [TreeNode(0)]

        trees = []

        def dfs(root, groot, leaves):
            leaves -= 2
            root.left = TreeNode(0)
            root.right = TreeNode(0)
            if leaves == 0:
                nonlocal trees
                trees.append(groot)
                return

            dfs(root.left, groot, leaves)
            root.left.left = None
            root.left.right = None
            dfs(root.right, groot, leaves)
            root.right.left = None
            root.right.right = None

        tree = TreeNode(0)
        dfs(tree, tree, n - 1)
        return trees

if __name__ == '__main__':
    sol = Solution()
    print(sol.allPossibleFBT(5))

