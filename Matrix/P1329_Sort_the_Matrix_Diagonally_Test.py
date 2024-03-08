import unittest
from P1329_Sort_the_Matrix_Diagonally import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        m = [[3, 3, 1, 1],
             [2, 2, 1, 2],
             [1, 1, 1, 2]]
        res = self.s.diagonalSort(m)
        ans = [[1, 1, 1, 1],
               [1, 2, 2, 2],
               [1, 2, 3, 3]]
        self.assertEqual(ans, res)

    def test_2(self):
        m = [[11, 25, 66, 1, 69, 7],
             [23, 55, 17, 45, 15, 52],
             [75, 31, 36, 44, 58, 8],
             [22, 27, 33, 25, 68, 4],
             [84, 28, 14, 11, 5, 50]]
        res = self.s.diagonalSort(m)
        ans = [[5, 17, 4, 1, 52, 7],
               [11, 11, 25, 45, 8, 69],
               [14, 23, 25, 44, 58, 15],
               [22, 27, 31, 36, 50, 66],
               [84, 28, 75, 33, 55, 68]]
        self.assertEqual(ans, res)

    def test_1_row_1_col(self):
        m = [[1]]
        res = self.s.diagonalSort(m)
        self.assertEqual(m, res)

    def test_3_rows_1_col(self):
        m = [[1], [2], [3]]
        res = self.s.diagonalSort(m)
        self.assertEqual(m, res)

    def test_3_rows_3_col(self):
        m = [[3, 3, 3],
             [3, 2, 2],
             [3, 2, 1]]
        res = self.s.diagonalSort(m)
        ans = [[1, 2, 3],
               [2, 2, 3],
               [3, 3, 3]]
        self.assertEqual(ans, res)
