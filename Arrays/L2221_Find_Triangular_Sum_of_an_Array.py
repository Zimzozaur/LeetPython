# https://leetcode.com/problems/find-triangular-sum-of-an-array/

class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        # I do not understand it XD
        n = len(nums)
        result = 0
        i = 0
        mul = 1
        while i < n // 2:
            result += nums[i] * mul
            result += nums[n - i - 1] * mul
            mul *= (n - 1 - i)
            mul //= (i + 1)
            i += 1
        if n % 2 == 1:
            result += nums[i] * mul
        return result % 10


if __name__ == '__main__':
    sol = Solution()
    x = [1, 2, 3, 4, 5]
    sol.triangularSum(x)
