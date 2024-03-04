import unittest
from P605_Can_Place_Flowers import Solution


class LeetCode(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        arr = [1, 0, 0, 0, 1]
        res = self.s.canPlaceFlowers(arr, 1)
        self.assertEqual(True, res)

    def test_2(self):
        arr = [1, 0, 0, 0, 1]
        res = self.s.canPlaceFlowers(arr, 2)
        self.assertEqual(False, res)

    def test_1_len_1_seed(self):
        arr = [0]
        res = self.s.canPlaceFlowers(arr, 1)
        self.assertEqual(True, res)

    def test_2_len_1_seed(self):
        arr = [0, 0]
        res = self.s.canPlaceFlowers(arr, 1)
        self.assertEqual(True, res)

    def test_2_len_2_seed(self):
        arr = [0, 0]
        res = self.s.canPlaceFlowers(arr, 2)
        self.assertEqual(False, res)

    def test_3_len_1_seed_1_plant_true(self):
        arr = [1, 0, 0]
        res = self.s.canPlaceFlowers(arr, 1)
        self.assertEqual(True, res)

    def test_3_len_1_seed_1_plant_false(self):
        arr = [0, 1, 0]
        res = self.s.canPlaceFlowers(arr, 1)
        self.assertEqual(False, res)

    def test_1_len_0_seed_1_plant(self):
        arr = [1]
        res = self.s.canPlaceFlowers(arr, 0)
        self.assertEqual(True, res)

    def test_5_len_1_seed_1_plan(self):
        arr = [0, 0, 1, 0, 0]
        res = self.s.canPlaceFlowers(arr, 1)
        self.assertEqual(True, res)

