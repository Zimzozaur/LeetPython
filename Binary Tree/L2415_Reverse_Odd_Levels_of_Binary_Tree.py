# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from TreeNode import *
from typing import Optional
from tree_generator import tree_generate


class Solution:
    def reverseOddLevels(self, root: TreeNode) -> Optional[TreeNode]:
        def reverse(a, b, is_odd=False):
            if a is None or b is None:
                return
            if is_odd:
                a.val, b.val = b.val, a.val
            reverse(a.left, b.right, not is_odd)
            reverse(a.right, b.left, not is_odd)

        reverse(root.left, root.right, is_odd=True)
        return root


if __name__ == '__main__':

    result = 0
    for i in range(0, ):
        x = 1 * 2 ** i
        result += x
    arr = [i + 1 for i in range(result)]
    print(arr)
    root = tree_generate(arr)
    sol = Solution()
    sol.reverseOddLevels(root)
    print()
