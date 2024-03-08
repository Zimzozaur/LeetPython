import unittest
from P3005_Count_Elements_With_Maximum_Frequency import Solution


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_5_len_5_nums(self):
        arr = [1, 2, 3, 4, 5]
        res = self.s.maxFrequencyElements(arr)
        self.assertEqual(5, res)

    def test_6_len_2_nums_2_size(self):
        arr = [1, 2, 2, 1, 3, 4]
        res = self.s.maxFrequencyElements(arr)
        self.assertEqual(4, res)

    def test_5_len_1_num_3_size(self):
        arr = [1, 1, 1, 2, 3]
        res = self.s.maxFrequencyElements(arr)
        self.assertEqual(3, res)

    def test_1_len(self):
        arr = [15]
        res = self.s.maxFrequencyElements(arr)
        self.assertEqual(1, res)


