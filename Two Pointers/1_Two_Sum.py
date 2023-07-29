# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to the target.
        :param nums:
        :param target:
        :return:

        Create HashMap
        Loop over the array
        Take element and subtract it from the target
            if result is in hashmap, return the indexes of them
            else add element to hashmap key is value value is index of element
        """
        hash_map = {}

        for i in range(len(nums)):
            if target - nums[i] in hash_map:  # Checks is element in HashMap
                return [hash_map.get(target - nums[i]), i]  # Returns indexes
            else:
                hash_map[nums[i]] = i  # Adds num to HashMap


if __name__ == '__main__':

    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))