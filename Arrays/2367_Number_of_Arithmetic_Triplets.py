# https://leetcode.com/problems/number-of-arithmetic-triplets/
class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        """
        You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
        A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
            i < j < k,
            nums[j] - nums[i] == diff, and
            nums[k] - nums[j] == diff.
            Return the number of unique arithmetic triplets.

        :param nums:
        :param diff:
        :return:
        """
        counter = 0
        look_up = set(nums)

        for num in nums:
            # Loops over the array
            if num + diff in look_up:  # Checks do 2nd number exists
                if num + diff * 2 in look_up:  # Checks do 3rd number exists
                    counter += 1

        return counter


if __name__ == '__main__':
    sol = Solution()
    x = [0, 1, 4, 6, 7, 10]
    d = 3
    print(sol.arithmeticTriplets(x, d))

