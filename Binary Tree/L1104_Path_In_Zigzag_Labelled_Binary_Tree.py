from math import log
from collections import deque


class Solution:
    def pathInZigZagTree(self, label):
        level = int(log(label, 2))
        solution = deque()
        for l in range(level, -1, -1):
            solution.appendleft(label)
            label = (3*(2**l) - 1 - label) // 2
        return list(solution)


if __name__ == '__main__':
    sol = Solution()
    print(sol.pathInZigZagTree(13))

