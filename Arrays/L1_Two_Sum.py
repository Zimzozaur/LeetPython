# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: list[int], tar: int) -> list[int]:
        hs = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            second = hs.get(tar - num)
            if tar - num in hs and i != second:
                return [min(i, second), max(i, second)]


if __name__ == '__main__':
    sol = Solution()
    x = [3,3]
    tar = 6
    res = sol.twoSum(x, tar)
    print(res)
