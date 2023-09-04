# https://leetcode.com/problems/create-binary-tree-from-descriptions/
from TreeNode import TreeNode
from typing import Optional


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        def connect(root1, root2):
            nonlocal side
            if side == 1:
                root1.left = root2
            else:
                root1.right = root2

        root = TreeNode(descriptions[0][0])
        newNode = TreeNode(descriptions[0][1])
        side = descriptions[0][2]
        connect(root, newNode)

        roots = {root.val: root}  # Only for root nodes
        conn = {newNode.val: newNode}  # For non-root nodes
        for desc in descriptions[1:]:
            val1 = desc[0]
            val2 = desc[1]
            side = desc[2]  # nonlocal in connect func
            if val1 in roots and val2 in roots:
                connect(roots.get(val1), roots.get(val2))
                check = roots.pop(val2)
                if check.left or check.right:
                    conn[check.val] = check
            elif val1 in roots and val2 not in roots and val2 not in conn:
                newNode = TreeNode(val2)
                connect(roots.get(val1), newNode)
                conn[newNode.val] = newNode
            elif val1 in conn and val2 not in roots and val2 not in conn:
                node = conn.get(val1)
                newNode = TreeNode(val2)
                connect(node, newNode)
                conn[newNode.val] = newNode
                if node.left and node.right:
                    conn.pop(node.val)
            elif val1 in conn and val2 in roots:
                node = roots.get(val2)
                connect(conn.get(val1), roots.get(val2))
                roots.pop(val2)
                if not node.left or not node.right:
                    conn[val2] = node
            elif val1 not in conn and val1 not in roots and val2 in roots:
                newNode = TreeNode(val1)
                node = roots.get(val2)
                connect(newNode, node)
                roots[newNode.val] = newNode
                roots.pop(node.val)
                if not node.left or not node.right:
                    conn[node.val] = node
            else:
                newRoot = TreeNode(val1)
                newNode = TreeNode(val2)
                connect(newRoot, newNode)
                roots[newRoot.val] = newRoot
                conn[newNode.val] = newNode

        return list(roots.values())[0]

if __name__ == '__main__':
    sol = Solution()
    x = [[80,1,1],[90,2,1],[2,80,1]]
    y = sol.createBinaryTree(x)
    print()
