class Solution:
    def isValid(self, s: str) -> bool:
        """
        Check is every parenthesis correctly closed
        *Example*

        When encounter open parenthesis add the same type close to stack
        When encounter close check is first in stack the same
            yes - pop and loop
            no - return false

        Input: s = "()[]{}"
        Output: true

        Input: s = "(]"
        Output: false

        :param s:
        :return: bool
        """

        stack = []

        for char in s:
            # Loop over every char
            if char == '(':
                # Adds char if encountered
                stack.append(chr(ord('(') + 1))
            elif char in ['[']:
                stack.append(chr(ord('[') + 2))
            elif char in ['{']:
                stack.append(chr(ord('{') + 2))

            elif len(stack) == 0:
                # If did not add check is list empty
                return False

            elif char == ')':
                # Removes char
                if stack[-1] == ')':
                    stack.pop()
                else:
                    return False
            elif char == ']':
                if stack[-1] == ']':
                    stack.pop()
                else:
                    return False
            else:
                if stack[-1] == '}':
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            # Check is list empty
            return True
        return False


if __name__ == '__main__':

    test = "}"

    sol = Solution()
    print(sol.isValid(test))

