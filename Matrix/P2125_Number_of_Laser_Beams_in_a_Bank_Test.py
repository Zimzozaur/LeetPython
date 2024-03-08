import unittest
from P2125_Number_of_Laser_Beams_in_a_Bank import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        arr = ["011001","000000","010100","001000"]
        res = self.s.numberOfBeams(arr)
        self.assertEqual(8, res)

    def test_2(self):
        arr =["000","111","000"]
        res = self.s.numberOfBeams(arr)
        self.assertEqual(0, res)

    def test_3(self):
        arr = ["1","0","0","1"]
        res = self.s.numberOfBeams(arr)
        self.assertEqual(1, res)

    def test_4(self):
        arr = ['0']
        res = self.s.numberOfBeams(arr)
        self.assertEqual(0, res)

    def test_5(self):
        arr = ['0', '0']
        res = self.s.numberOfBeams(arr)
        self.assertEqual(0, res)

    def test_6(self):
        arr = ['0', '0', '0', '0']
        res = self.s.numberOfBeams(arr)
        self.assertEqual(0, res)

