class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        Performs Reverse Polish Notation
        :param tokens:
        :return: Number from int stack

        Add numbers to stack when encounter + - * /
        Perform operation on first 2 ints from stack
        Than put result back to stack
        """
        stack = []  # holds numbers

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                # Take ints from stack and perform operation on it then put into stack
                num1 = stack.pop()
                num2 = stack.pop()
                match token:
                    # Chooses operation
                    case '+':
                        stack.append(num2 + num1)
                    case '-':
                        stack.append(num2 - num1)
                    case '*':
                        stack.append(num2 * num1)
                    case '/':
                        stack.append(int(num2 / num1))
            else:
                # Adds int to stack
                stack.append(int(token))

        return stack.pop()
