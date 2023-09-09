# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        maxSoFar, arr[-1] = arr[-1], -1
        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = maxSoFar
            maxSoFar = max(temp, maxSoFar)
        return arr


if __name__ == '__main__':
    sol = Solution()
    x = [17, 18, 5, 4, 6, 1]
    z = sol.replaceElements(x)
    print(z)
