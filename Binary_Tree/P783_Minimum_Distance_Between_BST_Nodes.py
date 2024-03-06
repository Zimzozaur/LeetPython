# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
from TreeNode import TreeNode
from typing import Optional


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """Post order then loop over array and find smallest diff"""
        arr = []
        def helper(root):
            if root.left:
                helper(root.left)
            arr.append(root.val)
            if root.right:
                helper(root.right)

        helper(root)

        diff = abs(arr[0] - arr[1])
        before = arr[1]
        for num in arr[2:]:
            diff = min(diff, abs(before - num))
            before = num

        return diff


