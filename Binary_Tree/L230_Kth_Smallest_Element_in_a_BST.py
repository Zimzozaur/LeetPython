# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional
from TreeNode import TreeNode
from tree_generator import tree_generate

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = 0

        def dfs(root, k):
            if k == 1:
                return k
            if not root:
                return k

            k = dfs(root.left, k)
            k -= 1
            if k == 1:
                nonlocal num
                num = root.val
            k = dfs(root.right, k)

            return k
        dfs(root, k)
        return num


if __name__ == '__main__':
    x = [2,1,3]
    y = tree_generate(x)
    sol = Solution()
    z = sol.kthSmallest(y,3)
    print(z)

