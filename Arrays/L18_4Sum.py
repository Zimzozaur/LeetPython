# https://leetcode.com/problems/4sum/description/


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        cut ints above 4 occurrences
        check what is the smallest value in to start with to compare from hash map

        """
        vals = {}
        ints = []
        for num in nums:
            if num in vals and vals.get(num) < 4:
                vals[num] = vals.get(num) + 1
                ints.append(num)
            elif num not in vals:
                vals[num] = 1
                ints.append(num)
        ints = sorted(ints)
        result = []

        for i in range(len(ints)):
            for j in range(i + 1, len(ints) - 2):
                left = j + 1
                right = len(ints) - 1
                while left < right:
                    if ints[i] + ints[j] + ints[left] + ints[right] > target:
                        right -= 1
                    elif ints[i] + ints[j] + ints[left] + ints[right] < target:
                        left += 1
                    else:
                        result.append([ints[i], ints[j], ints[left], ints[right]])
                        break

        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [-2, -1, 0, 0, 1, 2]
    target = 0
    z = sol.fourSum(nums, target)
    print(z)

