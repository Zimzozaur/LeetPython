import unittest
from P2864_Maximum_Odd_Binary_Number import Solution


class LeetCodeTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_leetcode_1(self):
        s = '010'
        res = self.sol.maximumOddBinaryNumber(s)
        self.assertEqual('001', res)

    def test_leetcode_2(self):
        s = '0101'
        res = self.sol.maximumOddBinaryNumber(s)
        self.assertEqual('1001', res)

    def test_num_1(self):
        s = '000111'
        res = self.sol.maximumOddBinaryNumber(s)
        self.assertEqual('110001', res)













