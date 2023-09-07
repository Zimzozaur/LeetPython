# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Find all unique combinations in candidates where the candidate numbers sum to target.
        Solution set do not contain duplicate combinations.

        Problem: Remove duplicates

        """

        all_subs = set()
        empty = []

        def backtrack(index):

            if sum(empty) == target:
                copy = empty.copy()
                copy.sort()
                all_subs.add(tuple(copy))
                return
            if sum(empty) > target or index >= len(nums):
                return


            empty.append(nums[index])
            backtrack(index + 1)
            empty.pop()
            backtrack(index + 1)

        backtrack(0)

        return list(all_subs)

if __name__ == '__main__':
    sol = Solution()
    x = [1,2,2,2,5]
    target = 5
    print(sol.combinationSum2(x, target))