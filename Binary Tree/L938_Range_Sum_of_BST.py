# https://leetcode.com/problems/range-sum-of-bst/

from collections import deque
from typing import Optional
from TreeNode import *

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        in_range = 0
        queue = deque([root])
        while deque:
            for i in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                if low <= node.val <= high:
                    in_range += node.val
                queue.append(node.left)
                queue.append(node.right)
        return in_range
