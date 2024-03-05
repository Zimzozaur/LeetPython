# https://leetcode.com/problems/range-sum-query-immutable/description/


class NumArray:

    def __init__(self, nums: list[int]):
        val = 0
        self.arr = [val := val + num for num in nums]

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right] if left == 0 else self.arr[right] - self.arr[left - 1]

