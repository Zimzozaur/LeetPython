# https://leetcode.com/problems/pascals-triangle-ii/description/
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        base = [1]
        for i in range(rowIndex):
            base = [0] + base + [0]
            for j in range(len(base) - 1):
                base[j - 1] = base[j - 1] + base[j]
            base.pop()
        return base


if __name__ == '__main__':
    sol = Solution()
    y = sol.getRow(3)
    print(y)

