# https://leetcode.com/problems/minimize-string-length/description/

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        """
        Returns number of unique characters in a string.
        An easy solution is to - return(len(set(s)))
        This solution keeps the order of characters.
        :param s:
        :return:
        """

        stack = []
        HashSet = set()

        for char in s:
            if char not in HashSet:
                stack.append(char)
                HashSet.add(char)

        return len(stack)




if __name__ == '__main__':
    sol = Solution()
    print(sol.minimizedStringLength("dddaaa"))

