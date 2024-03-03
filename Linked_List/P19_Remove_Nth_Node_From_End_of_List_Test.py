import unittest
from ListNode import list_generator, compare_ll
from P19_Remove_Nth_Node_From_End_of_List import Solution


class TestLeetCode(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1_leetcode(self):
        list_test = [1, 2, 3, 4, 5]
        list_answer = [1, 2, 3, 5]
        test_list = list_generator(list_test)
        test_answer = list_generator(list_answer)
        res = self.sol.removeNthFromEnd(test_list, 2)
        self.assertTrue(compare_ll(test_answer, res))

    def test_2_leetcode(self):
        list_test = [1]
        list_answer = []
        test_list = list_generator(list_test)
        test_answer = list_generator(list_answer)
        res = self.sol.removeNthFromEnd(test_list, 1)
        self.assertTrue(compare_ll(test_answer, res))

    def test_3_leetcode(self):
        list_test = [1, 2]
        list_answer = [1]
        test_list = list_generator(list_test)
        test_answer = list_generator(list_answer)
        res = self.sol.removeNthFromEnd(test_list, 1)
        self.assertTrue(compare_ll(test_answer, res))

    def test_remove_last_node(self):
        list_test = [1, 2, 3]
        list_answer = [1, 2]
        test_list = list_generator(list_test)
        test_answer = list_generator(list_answer)
        res = self.sol.removeNthFromEnd(test_list, 1)
        self.assertTrue(compare_ll(test_answer, res))

    def test_remove_first_node(self):
        list_test = [1, 2, 3]
        list_answer = [2, 3]
        test_list = list_generator(list_test)
        test_answer = list_generator(list_answer)
        res = self.sol.removeNthFromEnd(test_list, 3)
        self.assertTrue(compare_ll(test_answer, res))

    def test_3_len_remove_middle(self):
        list_test = [1, 2, 3]
        list_answer = [1, 3]
        test_list = list_generator(list_test)
        test_answer = list_generator(list_answer)
        res = self.sol.removeNthFromEnd(test_list, 2)
        self.assertTrue(compare_ll(test_answer, res))




