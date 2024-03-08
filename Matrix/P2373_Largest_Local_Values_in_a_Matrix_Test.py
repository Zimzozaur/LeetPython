import unittest
from P2373_Largest_Local_Values_in_a_Matrix import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        m = [[9, 9, 8, 1],
             [5, 6, 2, 6],
             [8, 2, 6, 4],
             [6, 2, 2, 2]]
        res = self.s.largestLocal(m)
        ans = [[9, 9],
               [8, 6]]
        self.assertEqual(ans, res)

    def test_2(self):
        m = [[1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [1, 1, 2, 1, 1],
             [1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1]]
        res = self.s.largestLocal(m)
        ans = [[2, 2, 2],
               [2, 2, 2],
               [2, 2, 2]]
        self.assertEqual(ans, res)

    def test_3x3(self):
        m = [[1, 1, 1],
             [1, 9, 1],
             [1, 1, 1]]
        res = self.s.largestLocal(m)
        ans = [[9]]
        self.assertEqual(ans, res)

    def test_4x4(self):
        m = [[8, 1, 1, 7],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [6, 1, 1, 5]]
        res = self.s.largestLocal(m)
        ans = [[8, 7],
               [6, 5]]
        self.assertEqual(ans, res)