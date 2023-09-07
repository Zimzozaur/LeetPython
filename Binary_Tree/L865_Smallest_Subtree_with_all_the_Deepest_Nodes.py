# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
import copy
from typing import Tuple, Set, Any, List
from TreeNode import TreeNode
from collections import deque
from tree_generator import tree_generate

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """
        1. bfs - zapisz liscie do setu
        2. znajdz liść
        3. idź w górę aż znajdziesz node który usunie
        """
        def bfs(root) -> tuple[set[Any], list[Any]]:
            nodes = set()
            all_nodes = []
            queue = deque([root])
            while queue:
                nodes.clear()
                for i in range(len(queue)):
                    node = queue.popleft()
                    nodes.add(node)
                    if node.left or node.right:
                        all_nodes.append(node)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return nodes, all_nodes

        def dfs(root):
            if not root:
                return True
            if not dfs(root.left):
                return False
            nonlocal nodes
            if root in nodes:
                nodes.remove(root)
                if not nodes:
                    return False
            if not dfs(root.right):
                return False
            return True

        node_tuple = bfs(root)
        leaves = node_tuple[0]
        all_nodes = node_tuple[1]

        if len(leaves) == 1:
            return leaves.pop()

        for node in reversed(all_nodes):
            nodes = leaves.copy()
            if not dfs(node):
                return node


if __name__ == '__main__':
    sol = Solution()
    arr = [3,5,1,6,2,0,8,None,None,7,4,10]
    tree = tree_generate(arr)
    print(sol.subtreeWithAllDeepest(tree).val)
