from collections import deque
from typing import Optional
from TreeNode import *


def tree_generate(arr: list) -> Optional[TreeNode]:
    """
    Generate Tree from a list of values. Example:

    input = [1, None, 2, 3, 4]
           1
         N   2
           3   4

    :param arr: list of values
    :return: Binary Tree or None
    """
    if arr[0] is None:
        return None

    queue = deque(arr)
    root = TreeNode(queue.popleft())
    nodes = deque([root])
    while queue:
        limit = len(nodes) * 2
        if limit > len(queue):
            limit = len(queue)
        new_nodes = deque([])
        left = False

        for i in range(limit):
            node = TreeNode(queue.popleft())
            if not left:
                if node.val is None:
                    left = True
                    continue
                nodes[0].left = node
                new_nodes.append(node)
                left = True
            else:
                if node.val is None:
                    nodes.popleft()
                    left = False
                    continue
                nodes[0].right = node
                new_nodes.append(node)
                nodes.popleft()
                left = False
        nodes = new_nodes

    return root


if __name__ == '__main__':
    """
                1
               2  3
             N  5 6  N
               7
    
    """
    x = [None]
    y = tree_generate(x)
    print()



