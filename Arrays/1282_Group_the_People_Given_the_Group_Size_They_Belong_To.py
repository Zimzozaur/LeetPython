# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        nums = {}
        for index, value in enumerate(groupSizes):
            if value in nums:
                if len(nums.get(value)[-1]) < value:
                    nums.get(value)[-1].append(index)
                else:
                    nums.get(value).append([value])
            else:
                nums[value] = [[index]]

        result = []
        for num in nums.values():
            for kind in num:
                result.append(kind)

        return result



if __name__ == '__main__':
    sol = Solution()
    x = [3,3,3,3,3,1,3]
    print(sol.groupThePeople(x))
