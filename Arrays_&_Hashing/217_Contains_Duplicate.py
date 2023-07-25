class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Check is  the duplicate in the list
        :param nums:
        :return:
        """
        set_num = {}
        for num in nums:
            # Adds number to dict with value 1 or add + 1 when already in dict
            set_num[num] = set_num.get(num, 0) + 1
            if set_num[num] == 2:
                return True
        return False
