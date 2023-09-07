# https://leetcode.com/problems/binary-search/submissions/
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Just a binary search
        If target exists, then return its index. Otherwise, return -1.
        :param nums:
        :param target:
        :return:

        Need 3 pointers
        1 - point to the begging
        2 - to the end
        3 - points to mid-pointer
        """

        pointer_1 = 0
        pointer_2 = len(nums) - 1
        pointer_3 = int((pointer_2 + pointer_1) / 2)

        if pointer_2 == 0:  # If len is 1
            return 0

        while pointer_1 <= pointer_2:  # Runs until the last digit is wrong

            if nums[pointer_3] == target:  # When found
                return pointer_3

            elif nums[pointer_3] < target:  # When to small move pointer_1 one above
                pointer_1 = pointer_3 + 1

            else:
                pointer_2 = pointer_3 - 1  # When to big move pointer_2 one below

            pointer_3 = int((pointer_2 + pointer_1) / 2)  # Recalculate pointer

        return -1


if __name__ == '__main__':
    sol = Solution()
    x = [0, 1]
    t = 1

    print(sol.search(x, t))
