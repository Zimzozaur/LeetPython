# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            elif len(res) < 3:
                res[num] = 1
            if len(res) == 3:
                del_them = []
                for key in res:
                    res[key] -= 1
                    if res[key] == 0:
                        del_them.append(key)
                for them in del_them:
                    del res[them]

        for key in res:
            res[key] = 0

        for num in nums:
            if num in res:
                res[num] += 1

        return [key for key, val in res.items() if val > len(nums) // 3]

