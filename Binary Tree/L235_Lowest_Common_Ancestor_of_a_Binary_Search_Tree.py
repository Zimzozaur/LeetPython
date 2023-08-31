# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
from TreeNode import *
from tree_generator import *


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, node, path=None):
            if path is None:
                path = deque([])
            path.append(root)
            if root == node:
                return path
            if root.val > node.val:
                path = dfs(root.left, node, path)
            else:
                path = dfs(root.right, node, path)
            return path

        p_path = dfs(root, p)
        q_path = dfs(root, q)

        result = None
        while len(p_path) > 0 and len(q_path) > 0:
            if p_path[0] == q_path[0]:
                result = p_path.popleft()
                q_path.popleft()
            else:
                break
        return result


if __name__ == '__main__':
    sol = Solution()
    x = [6,2,8,0,4,7,9,None,None,3,5]
    """
            6
          2         8
        0   4      7  9
           3  5
    
    """
    y = tree_generate(x)
    p = y    # 0
    q = y.left.right.left  # 3
    print(sol.lowestCommonAncestor(y, p, q).val)
