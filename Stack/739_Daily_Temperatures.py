# https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
        I: [73,74,75,71,69,72,76,73]
        O: [1, 1, 4, 2, 1, 1, 0, 0]
        :param temperatures:
        :return:

        Build stack that is monotonically decreasing
        Stack holds arrays that holds temps and indexes

        if the temperature is not smaller than the previous temp,
        pop last and put new temp in the stack
        """

        stack = [[0]]

        for i in range(len(temperatures) - 1, -1, -1):
            # Loop from last to 1st
            while stack:
                if temperatures[i] >= stack[-1][0]:
                    # pops when not greater to keep the stack decreasing
                    stack.pop()
                else:
                    # when is smaller
                    break
            if stack:
                # if not empty
                stack.append([temperatures[i], i])
                temperatures[i] = stack[-2][1] - i  # -2 because -1 is already temp[i]
            else:
                # if empty
                stack.append([temperatures[i], i])
                temperatures[i] = 0

        return temperatures


if __name__ == '__main__':
    sol = Solution()
    temps = [2,3, 1,1,1,2]

    print(sol.dailyTemperatures(temps))
