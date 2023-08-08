# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """Return length of an array where each number at most twice"""

        current = nums[0]
        streak = 0
        pointer_one = pointer_two = 0

        while pointer_two <= len(nums) - 1:

            if current == nums[pointer_two]:
                streak += 1
                pointer_two += 1
                continue

            if streak > 2:
                streak = 2

            for i in range(streak):
                # Change int to current to remove duplicates
                nums[pointer_one] = current
                pointer_one += 1

            streak = 0
            current = nums[pointer_two]

        # Here it is again to catch the last iteration
        if streak > 2:
            streak = 2

        for i in range(streak):
            # Change int to current to remove duplicates
            nums[pointer_one] = current
            pointer_one += 1

        return pointer_one


if __name__ == '__main__':
    sol = Solution()

    x = [1, 1, 1, 2]  # 3
    x1_5 = [1, 1, 2, 2]  # 4
    x2 = [1, 1, 2, 2, 3, 3, 4, 4]  # 8
    x3 = [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]  # 10

    for y in [x, x1_5, x2, x3]:
        print(sol.removeDuplicates(y))
