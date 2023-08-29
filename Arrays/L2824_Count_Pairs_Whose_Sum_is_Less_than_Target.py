import random
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        nums = sorted(nums)
        print(nums)

        while left < right:

            if nums[left] + nums[right] >= target:
                right -= 1
            else:
                num = 0
                for i in range(2, (right - left) + 1):
                    num += i
                return num
        return 0

if __name__ == '__main__':
    sol = Solution()
    x = [random.randint(-50,50) for num in range(50)]
    target = 3
    print(sol.countPairs(x, target))

