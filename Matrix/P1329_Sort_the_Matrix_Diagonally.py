# https://leetcode.com/problems/sort-the-matrix-diagonally/description/


class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        r_limit = len(mat)
        c_limit = len(mat[0])

        # list[list[tuple]]
        arr = []
        for i in range(c_limit):
            cords = []
            c = i
            r = 0
            while r != r_limit and c != c_limit:
                cords.append((r, c))
                r += 1
                c += 1
            arr.append(cords)

        for i in range(1, r_limit):
            cords = []
            r = i
            c = 0
            while r != r_limit and c != c_limit:
                cords.append((r, c))
                r += 1
                c += 1
            arr.append(cords)

        for l in arr:
            val = []
            for tup in l:
                val.append(mat[tup[0]][tup[1]])
            val.sort()
            for v, tup in zip(val, l):
                mat[tup[0]][tup[1]] = v

        return mat