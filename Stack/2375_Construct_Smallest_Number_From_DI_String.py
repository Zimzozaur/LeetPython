# https://leetcode.com/problems/construct-smallest-number-from-di-string/
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """

        A 0-indexed string num of length n + 1 is created using the following conditions:
        num consists of the digits '1' to '9', where each digit is used at most once.
        If pattern[i] == 'I', then num[i] < num[i + 1].
        If pattern[i] == 'D', then num[i] > num[i + 1].
        Return the lexicographically smallest possible string num that meets the condition

          I I I D I D D D
        1 2 3 5 4 9 8 7 6

        1 2 3 5 4 9 8 7 6

          I I I D I I I D
        1 2 3 5 4 7 8 9 6





        :param pattern:
        :return:
        """

        stack = [1]
        stack = []
        for char in pattern:
            stack.append(char)

            if char == 'I':
                stack.append(max(stack) + 1)
            else:
                max_val = max(stack)
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] < max_val + 1:
                        stack.insert(i, max_val + 1)
                        break
                        

        return "".join([str(num) for num in stack])


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestNumber("IIIDIDDD"))
