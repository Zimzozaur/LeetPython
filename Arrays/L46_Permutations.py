# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """Given an array of distinct integers, return all the possible permutations"""

        result = []
        permutation = []

        def recursion(nums):

            # Base Case
            if len(nums) < 1:
                result.append(permutation.copy())

            for i in range(len(nums)):
                permutation.append(nums[i])
                copy = nums.copy()
                copy.pop(i)
                recursion(copy)
                permutation.pop()

        recursion(nums)

        return result


if __name__ == '__main__':
    sol = Solution()
    x = [0, 1]
    print(sol.permute(x))
