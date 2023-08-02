# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
import random


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        """
        Check how many times you can increase every number, without making it greater.
        Then the greatest in row and column of the target number
        Returns number of operations
        :param grid:
        :return:
        """

        rows = len(grid)
        columns = len(grid[0])
        maxIncrease = 0  # Store number of operations needed to increase the number.

        for row in range(rows):
            # Loop over rows
            for column in range(columns):
                # Loops over columns
                building = grid[row][column]
                maxVal1 = 0
                maxVal2 = 0
                for num in grid[row]:
                    # Looks for bigger value in a row
                    if num > maxVal1:
                        maxVal1 = num

                for num in range(columns):
                    # Looks for bigger number in a column
                    if grid[num][column] > maxVal2:
                        maxVal2 = grid[num][column]

                if maxVal2 < maxVal1:
                    # Finds smaller maxVal
                    maxIncrease += maxVal2 - building
                else:
                    maxIncrease += maxVal1 - building

        return maxIncrease


if __name__ == '__main__':
    sol = Solution()
    for _ in range(1000):
        table = []
        for i in range(10):
            table.append([])
            for j in range(10):
                table[i].append(random.randint(0, 100))
        print(sol.maxIncreaseKeepingSkyline(table))

"""

From north and south it is the same
And from west and east it is the same




[59, 88, 44], 
[3, 18, 38], 
[21, 26, 51]]

[59, 88, 51], 
[38, 38, 38], 
[51, 51, 51]]

7 35 20 30 25 

"""