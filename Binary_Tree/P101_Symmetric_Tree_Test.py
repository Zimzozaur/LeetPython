import unittest
from P101_Symmetric_Tree import Solution
from tree_generator import tree_generate


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        arr = [1, 2, 2, 3, 4, 4, 3]
        tree = tree_generate(arr)
        res = self.s.isSymmetric(tree)
        self.assertEqual(True, res)

    def test_2(self):
        arr = [1, 2, 2, None, 3, None, 3]
        tree = tree_generate(arr)
        res = self.s.isSymmetric(tree)
        self.assertEqual(False, res)

    def test_3(self):
        arr = [1, 2, 2, 3, 3, 2, 3, ]
        tree = tree_generate(arr)
        res = self.s.isSymmetric(tree)
        self.assertEqual(False, res)

    def test_4(self):
        arr = [1, 0]
        tree = tree_generate(arr)
        res = self.s.isSymmetric(tree)
        self.assertEqual(False, res)