# https://leetcode.com/problems/baseball-game/
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """
        The goal is to track of all the scores and returns of the operations performed on them.

        An integer x.
        Record a new score of x.

        '+'.
        Record a new score that is the sum of the previous two scores.

        'D'
        Record a new score that is the double of the previous score.

        'C'
        Invalidate the previous score, removing it from the record.
        :param operations:
        :return:
        """

        stack = []
        for operation in operations:
            if operation == '+':
                stack.append(stack[-1] + stack[-2])
            elif operation == 'D':
                stack.append(2 * stack[-1])
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))

        return sum(stack)


if __name__ == '__main__':
    sol = Solution()
    print(sol.calPoints(["5", "2", "C", "D", "+"]))
