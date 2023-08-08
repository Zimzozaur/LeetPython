# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """Return length of an array after removing duplicates"""

        # Pointer_one is current int
        # Pointer_two is next int
        pointer_one, pointer_two = 0, 1

        while pointer_two <= len(nums) - 1:
            # When pointer_two is on a new number
            if nums[pointer_two] != nums[pointer_one]:
                pointer_one += 1
                nums[pointer_one] = nums[pointer_two]
            pointer_two += 1

        return pointer_one + 1  # Is a number of unique ints


if __name__ == '__main__':
    sol = Solution()

    x = [1,2,2,3,4,4,5,6,7,8,8,8,8,]

    print(sol.removeDuplicates(x))
