# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
import random
from typing import Optional
from TreeNode import TreeNode
from tree_generator import tree_generate


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, queue=None):
            if queue is None:
                queue = []
            if not root:
                return
            queue.append(root.val)
            if not root.left and not root.right:
                nonlocal result
                power = 0
                for num in queue[::-1]:
                    result += num * 2 ** power
                    power += 1

            dfs(root.left, queue)
            dfs(root.right, queue)
            queue.pop()
            return queue

        result = 0
        dfs(root)
        return result


if __name__ == '__main__':
    sol = Solution()
    x = [1,0,1,0,1,0,1]
    y = tree_generate(x)
    print(sol.sumRootToLeaf(y))
    print([random.randint(0,1) for num in range(1000)])
