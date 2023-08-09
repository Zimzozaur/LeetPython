# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Each time you can either climb 1 or 2 steps.
        Return number of all possible ways to climb.
        """

        # Brute Force approach.
        # Base case
        # if n == 0:
        #     return 1
        # elif n < 0:
        #     return 0
        #
        # option1 = self.climbStairs(n - 1)
        # option2 = self.climbStairs(n - 2)
        #
        # return option1 + option2

        # Bottom-Up Approach

        if n == 1:
            return 1

        bottom_one = 1
        bottom_two = 2
        for i in range(n - 2):
            bottom_two = bottom_two + bottom_one
            bottom_one = bottom_two - bottom_one
        return bottom_two



if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(5))

