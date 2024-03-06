# https://leetcode.com/problems/maximum-subarray/description/

# Greedy Time O(n)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for num in nums:
            # is num bigger or current subarray + num
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum

# Greedy divide and conquer


