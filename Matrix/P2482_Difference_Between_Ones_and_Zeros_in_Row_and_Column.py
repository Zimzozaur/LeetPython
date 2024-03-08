# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/
from collections import Counter


class Solution:
    # List comprehension solution
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])

        # Compute counters for rows and columns
        row_counters = [Counter(row) for row in grid]
        col_counters = [Counter(grid[k][j] for k in range(rows)) for j in range(cols)]

        # Compute the difference between ones and zeros for each cell
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = row_counters[i][1] + col_counters[j][1] - row_counters[i][0] - col_counters[j][0]

        return grid

    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        onesRow = []
        onesCol = []
        zerosRow = []
        zerosCol = []

        for row in grid:
            c = Counter(row)
            onesRow.append(c[1])
            zerosRow.append(c[0])

        for i in range(len(grid[0])):
            nums = []
            for j in range(len(grid)):
                nums.append(grid[j][i])
            c = Counter(nums)
            onesCol.append(c[1])
            zerosCol.append(c[0])
            del nums

        for i in range(len(grid)):  # Row
            for j in range(len(grid[0])): # Column
                grid[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]

        return grid

