# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        """Return a list of all unique combinations of nums where the chosen numbers sum to target"""

        all_combs = []
        combination = []

        def backtrack(nums, index, total):

            if total == target:
                all_combs.append(combination[:])
                return
            elif total > target or index >= len(nums):
                return

            backtrack(nums, index + 1, total)
            combination.append(nums[index])

            backtrack(nums, index, total + nums[index])
            combination.pop()

        backtrack(nums, 0, 0)

        return all_combs


if __name__ == '__main__':
    sol = Solution()
    x = [2,3,5]
    target = 8
    print(sol.combinationSum(x, target))
