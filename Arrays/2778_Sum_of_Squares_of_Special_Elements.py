# https://leetcode.com/problems/sum-of-squares-of-special-elements/description/
class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        """
        You are given a 1-indexed integer array nums of length n.
        An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
        Return the sum of the squares of all special elements of nums.

        :param nums:
        :return:
        """

        sum_result = 0
        divider = len(nums)

        for i in range(1, divider + 1):
            if divider % i == 0:
                # If length is divisible by index
                sum_result += nums[i - 1] * nums[i - 1]

        return sum_result


if __name__ == '__main__':
    sol = Solution()
    print(sol.sumOfSquares([1,2,3,4]))
