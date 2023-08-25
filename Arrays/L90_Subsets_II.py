# https://leetcode.com/problems/subsets/


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """Return all possible subsets (the power set)."""

        all_subs = set()
        empty = []

        def backtrack(index):
            if index == len(nums):
                copy = empty.copy()
                copy.sort()
                all_subs.add(tuple(copy))
                return

            empty.append(nums[index])
            backtrack(index + 1)
            empty.pop()
            backtrack(index + 1)

        backtrack(0)

        return list(all_subs)

        """Better Solution"""

        # def dfs(curr, nums):
        #
        #     result.append(curr[:])
        #
        #     if len(nums) == 0:
        #         return
        #
        #     for i in range(len(nums)):
        #         if i > 0 and nums[i] == nums[i - 1]:
        #             # we dont create duplicate initial branches.
        #             continue
        #         dfs(curr + [nums[i]], nums[i + 1:])
        #         # we are sending, nums[i+1:] for next loop
        #
        # result = []
        # dfs([], sorted(nums))
        # return result


if __name__ == '__main__':
    sol = Solution()
    x = [4, 1, 4]
    print(sol.subsetsWithDup(x))
