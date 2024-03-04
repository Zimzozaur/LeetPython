import unittest
from P948_Bag_of_Tokens import Solution


class LeetCode(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1_leetcode(self):
        tokens = [100]
        power = 50
        res = self.sol.bagOfTokensScore(tokens, power)
        self.assertEqual(0, res)

    def test_2_leetcode(self):
        tokens = [200, 100]
        power = 150
        res = self.sol.bagOfTokensScore(tokens, power)
        self.assertEqual(1, res)

    def test_3_leetcode(self):
        tokens = [100, 200, 300, 400]
        power = 200
        res = self.sol.bagOfTokensScore(tokens, power)
        self.assertEqual(2, res)

    def test_buy_all(self):
        token = [100, 200, 300, 400]
        power = 1000
        res = self.sol.bagOfTokensScore(token, power)
        self.assertEqual(4, res)

    def test_buy_nothing(self):
        token = [100, 200, 400, 800]
        power = 0
        res = self.sol.bagOfTokensScore(token, power)
        self.assertEqual(0, res)

