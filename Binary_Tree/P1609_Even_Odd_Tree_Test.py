# https://leetcode.com/problems/even-odd-tree/?envType=daily-question&envId=2024-02-29
import unittest
from tree_generator import tree_generate
from P1609_Even_Odd_Tree import *
from collections import deque


class BasicTest(unittest.TestCase):

    def test_class_exist(self):
        sol = Solution()
        assert isinstance(sol, Solution), 'Class is not exported'

    def test_is_even_on_odd(self):
        n = 1
        res = is_even(n)
        self.assertEqual(False, res)

    def test_is_even_on_even(self):
        n = 2
        res = is_even(n)
        self.assertEqual(True, res)

    def test_is_odd_on_even(self):
        n = 2
        res = is_odd(n)
        self.assertEqual(False, res)

    def test_is_odd_on_odd(self):
        n = 1
        res = is_odd(n)
        self.assertEqual(True, res)

    def test_is_ascending_asc(self):
        deck = deque([TreeNode(1), TreeNode(2), TreeNode(3)])
        res = is_ascending(deck)
        self.assertEqual(True, res)

    def test_is_ascending_equal(self):
        deck = deque([TreeNode(1), TreeNode(2), TreeNode(2)])
        res = is_ascending(deck)
        self.assertEqual(False, res)

    def test_is_ascending_desc(self):
        deck = deque([TreeNode(3), TreeNode(2), TreeNode(1)])
        res = is_ascending(deck)
        self.assertEqual(False, res)

    def test_is_descending_desc(self):
        deck = deque([TreeNode(3), TreeNode(2), TreeNode(1)])
        res = is_descending(deck)
        self.assertEqual(True, res)

    def test_is_descending_equal(self):
        deck = deque([TreeNode(3), TreeNode(2), TreeNode(2)])
        res = is_descending(deck)
        self.assertEqual(False, res)

    def test_is_descending_asc(self):
        deck = deque([TreeNode(1), TreeNode(2), TreeNode(3)])
        res = is_descending(deck)
        self.assertEqual(False, res)


class TestHelperFunction(unittest.TestCase):
    """
    Test Generator
    asc_desc = ['ascending', 'descending']
    odd_even = ['odd', 'even']
    is_asc_desc = ['is_ascending', 'is_descending']
    is_odd_even = ['is_odd', 'is_even']

    d = {
        '00': (1, 3, 5),
        '01': (2, 4, 6),
        '10': (5, 3, 1),
        '11': (6, 4, 2)
    }

    for one in range(2):
        for two in range(2):
            for three in range(2):
                for four in range(2):
                    n1, n2, n3 = d[str(three) + str(four)]
                    print(
                    f'''
                    def test_{asc_desc[one]}_{odd_even[two]}_input_{asc_desc[three]}_{odd_even[four]}(self):
                        deck = deque([TreeNode({n1}), TreeNode({n2}), TreeNode({n3})])
                        res = helper({is_asc_desc[one]}, {is_odd_even[two]}, deck)
                        self.assertEqual({True if one == three and two == four else False}, res)
                    ''')
        """

    def test_ascending_odd_input_ascending_odd(self):
        deck = deque([TreeNode(1), TreeNode(3), TreeNode(5)])
        res = helper(is_ascending, is_odd, deck)
        self.assertEqual(True, res)

    def test_ascending_odd_input_ascending_even(self):
        deck = deque([TreeNode(2), TreeNode(4), TreeNode(6)])
        res = helper(is_ascending, is_odd, deck)
        self.assertEqual(False, res)

    def test_ascending_odd_input_descending_odd(self):
        deck = deque([TreeNode(5), TreeNode(3), TreeNode(1)])
        res = helper(is_ascending, is_odd, deck)
        self.assertEqual(False, res)

    def test_ascending_odd_input_descending_even(self):
        deck = deque([TreeNode(6), TreeNode(4), TreeNode(2)])
        res = helper(is_ascending, is_odd, deck)
        self.assertEqual(False, res)

    def test_ascending_even_input_ascending_odd(self):
        deck = deque([TreeNode(1), TreeNode(3), TreeNode(5)])
        res = helper(is_ascending, is_even, deck)
        self.assertEqual(False, res)

    def test_ascending_even_input_ascending_even(self):
        deck = deque([TreeNode(2), TreeNode(4), TreeNode(6)])
        res = helper(is_ascending, is_even, deck)
        self.assertEqual(True, res)

    def test_ascending_even_input_descending_odd(self):
        deck = deque([TreeNode(5), TreeNode(3), TreeNode(1)])
        res = helper(is_ascending, is_even, deck)
        self.assertEqual(False, res)

    def test_ascending_even_input_descending_even(self):
        deck = deque([TreeNode(6), TreeNode(4), TreeNode(2)])
        res = helper(is_ascending, is_even, deck)
        self.assertEqual(False, res)

    def test_descending_odd_input_ascending_odd(self):
        deck = deque([TreeNode(1), TreeNode(3), TreeNode(5)])
        res = helper(is_descending, is_odd, deck)
        self.assertEqual(False, res)

    def test_descending_odd_input_ascending_even(self):
        deck = deque([TreeNode(2), TreeNode(4), TreeNode(6)])
        res = helper(is_descending, is_odd, deck)
        self.assertEqual(False, res)

    def test_descending_odd_input_descending_odd(self):
        deck = deque([TreeNode(5), TreeNode(3), TreeNode(1)])
        res = helper(is_descending, is_odd, deck)
        self.assertEqual(True, res)

    def test_descending_odd_input_descending_even(self):
        deck = deque([TreeNode(6), TreeNode(4), TreeNode(2)])
        res = helper(is_descending, is_odd, deck)
        self.assertEqual(False, res)

    def test_descending_even_input_ascending_odd(self):
        deck = deque([TreeNode(1), TreeNode(3), TreeNode(5)])
        res = helper(is_descending, is_even, deck)
        self.assertEqual(False, res)

    def test_descending_even_input_ascending_even(self):
        deck = deque([TreeNode(2), TreeNode(4), TreeNode(6)])
        res = helper(is_descending, is_even, deck)
        self.assertEqual(False, res)

    def test_descending_even_input_descending_odd(self):
        deck = deque([TreeNode(5), TreeNode(3), TreeNode(1)])
        res = helper(is_descending, is_even, deck)
        self.assertEqual(False, res)

    def test_descending_even_input_descending_even(self):
        deck = deque([TreeNode(6), TreeNode(4), TreeNode(2)])
        res = helper(is_descending, is_even, deck)
        self.assertEqual(True, res)


class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one_node_tree_odd(self):
        tree = TreeNode(1)
        res = self.sol.isEvenOddTree(tree)
        self.assertEqual(True, res)

    def test_one_node_tree_even(self):
        tree = TreeNode(2)
        res = self.sol.isEvenOddTree(tree)
        self.assertEqual(False, res)

    def test_leetcode_1(self):
        tree_arr = [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2]
        tree = tree_generate(tree_arr)
        res = self.sol.isEvenOddTree(tree)
        self.assertEqual(True, res)

    def test_leetcode_2(self):
        tree_arr = [5, 4, 2, 3, 3, 7]
        tree = tree_generate(tree_arr)
        res = self.sol.isEvenOddTree(tree)
        self.assertEqual(False, res)

    def test_leetcode_3(self):
        tree_arr = [5, 9, 1, 3, 5, 7]
        tree = tree_generate(tree_arr)
        res = self.sol.isEvenOddTree(tree)
        self.assertEqual(False, res)

    def test_my_1(self):
        tree_arr = [5, 6, 4, 1]
        tree = tree_generate(tree_arr)
        res = self.sol.isEvenOddTree(tree)
        self.assertEqual(True, res)
