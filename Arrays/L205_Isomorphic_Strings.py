# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first = {}
        second = {}
        num = 0
        for i in range(len(s)):
            if s[i] not in first and t[i] not in second:
                first[s[i]] = num
                second[t[i]] = num
                num += 1
            elif first.get(s[i]) != second.get(t[i]):
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    s = "eszr"
    t = "asta"
    res = sol.isIsomorphic(s, t)
    print(res)