# https://leetcode.com/problems/design-browser-history/
class BrowserHistory:

    def __init__(self, homepage: str):
        """
        Inits - stack for back, forward, and current page
        :param homepage:
        """
        self.back_stack = []  # Stack of last visited pages.
        self.forward_stack = []  # Stack of last opened pages.
        self.current = homepage  # Current page

    def visit(self, url: str) -> None:
        """
        Opens page new page, clears forward and last current to back_stack
        :param url:
        :return:
        """
        self.forward_stack.clear()
        self.back_stack.append(self.current)
        self.current = url

    def back(self, steps: int) -> str:
        """
        Moves x pages back
        :param steps:
        :return:
        """

        # To not over shoot the stack
        # Checks how many pages a user can go back
        # if not enough, goes to first in stack
        if steps > len(self.back_stack):
            iteration = len(self.back_stack)
        else:
            iteration = steps

        for _ in range(0, iteration):
            if self.back_stack:
                # Adds current to forward_stack and goes back
                self.forward_stack.append(self.current)
                self.current = self.back_stack.pop()
            else:
                break

        return self.current

    def forward(self, steps: int) -> str:
        """
        Moves x pages forward
        :param steps:
        :return:
        """

        # To not over shoot the stack
        # Checks how many pages a user can go forward
        # if not enough, goes to first in stack
        if steps > len(self.forward_stack):
            iteration = len(self.forward_stack)
        else:
            iteration = steps

        for i in range(0, iteration):
            if self.forward_stack:
                # Adds current to back_stack and moves forward
                self.back_stack.append(self.current)
                self.current = self.forward_stack.pop()
            else:
                break
        return self.current


if __name__ == '__main__':
    sol = BrowserHistory("leetcode.com")
    sol.visit("google.com")
    sol.visit("facebook.com")
    sol.visit("youtube.com")
    sol.back(1)
    sol.back(1)
    sol.forward(1)
    sol.visit("linkedin.com")
    sol.forward(2)
    sol.back(2)
    sol.back(7)

