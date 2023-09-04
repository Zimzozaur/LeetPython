# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from collections import deque
from typing import Optional
from TreeNode import TreeNode
from tree_generator import tree_generate

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

if __name__ == '__main__':
    x = [2,1,3]
    y = tree_generate(x)
    sol = Solution()
    z = sol.kthSmallest(y, 10)
    print(z)
