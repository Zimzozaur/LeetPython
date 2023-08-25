# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """Given an array of distinct integers, return all the possible permutations"""

        """My Solution"""
        # result = []
        # permutation = []
        #
        # def recursion(nums):
        #
        #     # Base Case
        #     if len(nums) < 1:
        #         result.append(permutation[:])
        #
        #     for i in range(len(nums)):
        #         permutation.append(nums[i])
        #         copy = nums[:]
        #         copy.pop(i)
        #         recursion(copy)
        #         permutation.pop()
        #
        # recursion(nums)
        #
        # return result

        res = []

        def backtrack(i):
            if i >= len(nums):
                res.append(nums[:])

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return res


if __name__ == '__main__':
    sol = Solution()
    x = [0,1,2]
    print(sol.permute(x))
