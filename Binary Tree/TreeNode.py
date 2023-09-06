from collections import deque
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def display(self):
        arr = []
        layer = deque([self])
        while layer:
            for i in range(len(layer)):
                node = layer.popleft()
                arr.append(node.val)
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
        print(arr)
