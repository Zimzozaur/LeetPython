# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.
        :param nums:
        :return:

        Two Pointers + sort:
            Speed: 0(n^2)
            One pointer loops from 0 to len - 3
            Pointer two start at one + 1
            Pointer three start at the end
        """
        return_me = set()  # Removes duplicates
        array_len = len(nums)

        quick_sort(nums, 0, array_len - 1)

        for i in range(0, array_len - 2):  # Move "pointerZero"
            pointerOne = i + 1
            pointerTwo = array_len - 1

            while pointerOne < pointerTwo:  # Runs two pointers
                numOne = nums[pointerOne]
                numTwo = nums[pointerTwo]

                if nums[i] + numOne + numTwo == 0:  # If meets the condition, add and move
                    return_me.add((nums[i], numOne, numTwo))
                    pointerOne += 1
                elif nums[i] + numOne + numTwo < 0:  # if too small push pointerOne
                    pointerOne += 1
                else:
                    pointerTwo -= 1  # Push pointer two

        return [list(element) for element in return_me]


def quick_sort(arr, left, right):
    if left >= right:
        return

    pivot = partition(arr, left, right)

    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)


def partition(arr, left, right):
    i = left - 1
    pivot = arr[right]

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


if __name__ == '__main__':
    sol = Solution()
    arr = [0, 0, 0]
    print(sol.threeSum(arr))
