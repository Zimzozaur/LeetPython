# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
from collections import deque
from typing import Optional
from TreeNode import *


class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:
        """
        Array preorder traversal of a BST,
        construct the tree and return its root
        """
        tree = TreeNode(preorder[0])
        mono_stack = deque([tree])

        for num in preorder[1:]:
            if mono_stack[-1].val > num:
                node = TreeNode(num)
                mono_stack[-1].left = node
                mono_stack.append(node)
                continue
            last = mono_stack[-1]
            while len(mono_stack) > 0 and mono_stack[-1].val < num:
                last = mono_stack.pop()
            last.right = TreeNode(num)
            mono_stack.append(last.right)



        return tree

if __name__ == '__main__':
    sol = Solution()
    x = [8,5,1,6,7,10,12]
    y = sol.bstFromPreorder(x)
    print()

