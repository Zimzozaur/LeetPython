import unittest
from P2482_Difference_Between_Ones_and_Zeros_in_Row_and_Column import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        matrix = [[0, 1, 1],
                  [1, 0, 1],
                  [0, 0, 1]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[0, 0, 4],
               [0, 0, 4],
               [-2, -2, 2]]
        self.assertEqual(ans, res)

    def test_2(self):
        matrix = [[1, 1, 1],
                  [1, 1, 1]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[5, 5, 5],
               [5, 5, 5]]
        self.assertEqual(ans, res)

    def test_2_row_2_col_1_only(self):
        matrix = [[1, 1],
                  [1, 1]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[4, 4],
               [4, 4]]
        self.assertEqual(ans, res)

    def test_2_row_2_col_0_only(self):
        matrix = [[0, 0],
                  [0, 0]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[-4, -4],
               [-4, -4]]
        self.assertEqual(ans, res)

    def test_2_row_2_col_1_0_0_1(self):
        matrix = [[1, 0],
                  [0, 1]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[0, 0],
               [0, 0]]
        self.assertEqual(ans, res)

    def test_2_row_2_col_0_1_1_0(self):
        matrix = [[0, 1],
                  [1, 0]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[0, 0],
               [0, 0]]
        self.assertEqual(ans, res)

    def test_2_row_2_col_0_1_0_1(self):
        matrix = [[0, 1],
                  [0, 1]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[-2, 2],
               [-2, 2]]
        self.assertEqual(ans, res)

    def test_2_row_2_col_1_0_1_0(self):
        matrix = [[1, 0],
                  [1, 0]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[2, -2],
               [2, -2]]
        self.assertEqual(ans, res)

    def test_2_row_2_col_1_1_1_0(self):
        matrix = [[1, 1],
                  [1, 0]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[4, 2],
               [2, 0]]
        self.assertEqual(ans, res)

    def test_1_row_1_col_0(self):
        matrix = [[0]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[-2]]
        self.assertEqual(ans, res)

    def test_1_row_1_col_1(self):
        matrix = [[1]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[2]]
        self.assertEqual(ans, res)

    def test_1_row_2_col_1_1(self):
        matrix = [[1, 1]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[3, 3]]
        self.assertEqual(ans, res)

    def test_1_row_2_col_0_0(self):
        matrix = [[0, 0]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[-3, -3]]
        self.assertEqual(ans, res)

    def test_1_row_2_col_1_0(self):
        matrix = [[1, 0]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[1, -1]]
        self.assertEqual(ans, res)

    def test_2_row_1_col_1_0(self):
        matrix = [[1], [0]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[1], [-1]]
        self.assertEqual(ans, res)

    def test_2_row_1_col_1_1(self):
        matrix = [[1], [1]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[3], [3]]
        self.assertEqual(ans, res)

    def test_2_row_1_col_0_0(self):
        matrix = [[0], [0]]
        res = self.s.onesMinusZeros(matrix)
        ans = [[-3], [-3]]
        self.assertEqual(ans, res)
