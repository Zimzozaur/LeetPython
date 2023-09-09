# https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        st = strs[0]
        for s in strs:
            while not s.startswith(st):
                st = st[:-1]
        return st


if __name__ == '__main__':
    sol = Solution()
    strs = ["dog","racecar","car"]
    print(sol.longestCommonPrefix(strs))

