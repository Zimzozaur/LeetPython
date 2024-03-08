# https://leetcode.com/problems/largest-local-values-in-a-matrix/description/


class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        res = []
        for i in range(len(grid) - 2):
            ans = []
            for j in range(len(grid) - 2):
                ans.append(max(*grid[i][j:j+3], *grid[i+1][j:j+3], *grid[i+2][j:j+3]))
            res.append(ans)

        return res

