# https://leetcode.com/problems/maximum-sum-circular-subarray/description/


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        max_sum = nums[0]
        min_sum = 0
        max_cur = 0
        min_cur = 0

        for num in nums:
            max_cur = max(num, max_cur + num)
            min_cur = min(num, min_cur + num)
            max_sum = max(max_sum, max_cur)
            min_sum = min(min_sum, min_cur)

        return max(total_sum - min_sum, max_sum) if max_sum > 0 else max_sum
