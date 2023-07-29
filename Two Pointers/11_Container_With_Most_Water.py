# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Counts maximum capacity of a container
        Capacity is counted like this:
        You need two numbers, and from two numbers you pick smaller
        then count the distance between them and multiply by smaller number
        Voilà!
        :param height:
        :return:

        The bottleneck is the size of smaller height
        Greedy algorithm that looks for increasing smaller height is the key.
        """
        pointerOne = 0
        pointerTwo = len(height) - 1

        biggest = 0

        while pointerOne < pointerTwo:
            one_is_smaller = False
            if height[pointerOne] < height[pointerTwo]:  # Finds smaller height
                smaller = height[pointerOne]
                one_is_smaller = True  # Flag to find smaller
            else:
                smaller = height[pointerTwo]

            distance = pointerTwo - pointerOne  # Counts distance between heights

            capacity = smaller * distance  # Counts capacity

            if biggest < capacity:  # Check is bigger capacity
                biggest = capacity

            if one_is_smaller:
                pointerOne += 1
                continue

            pointerTwo -= 1

        return biggest


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1,3,2,5,25,24,5]))
