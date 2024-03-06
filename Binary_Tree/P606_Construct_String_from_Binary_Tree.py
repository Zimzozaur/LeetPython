# https://leetcode.com/problems/construct-string-from-binary-tree/description/
from TreeNode import TreeNode
from typing import Optional


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(node):
            if not node.left and not node.right:
                return f'{node.val}'
            elif not node.left:
                return f'{node.val}()({helper(node.right)})'
            elif not node.right:
                return f'{node.val}({helper(node.left)})'
            else:
                return f'{node.val}({helper(node.left)})({helper(node.right)})'

        return helper(root)