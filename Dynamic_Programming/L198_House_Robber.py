# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2




if __name__ == '__main__':
    sol = Solution()
    x = [1,1,1,1,2]
    y = sol.rob(x)
    print(y)
