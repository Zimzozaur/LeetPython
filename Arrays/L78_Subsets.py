# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """Return all possible subsets (the power set)."""

        all_subs = []
        empty = []

        def backtrack(index):
            if index == len(nums):
                all_subs.append(empty.copy())
                return

            empty.append(nums[index])
            backtrack(index + 1)
            empty.pop()
            backtrack(index + 1)

        backtrack(0)

        return all_subs


if __name__ == '__main__':
    sol = Solution()
    x = [1, 2, 3,]
    print(sol.subsets(x))
