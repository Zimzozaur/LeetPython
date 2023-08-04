# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        """
        Creates an array of operations to perform on stack to build
        An array similar to target while using a stream of the integers in the range [1, n].
        :param target:
        :param n:
        :return:

        Create a set of targets to quickly look up values
        Loop over stream add value if not in set pop when hit the biggest return
        """

        Hash_Set = set(target)
        biggest = target[-1]  # N is not needed, biggest it the edge
        return_stack = []

        for i in range(1, biggest + 1):
            return_stack.append("Push")  # Always adds
            if i not in Hash_Set:
                # Pops when not in set
                return_stack.append("Pop")

        return return_stack
