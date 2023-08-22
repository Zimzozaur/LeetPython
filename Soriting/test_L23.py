import unittest
from ListNode import ListNode
from L23_Merge_k_Sorted_Lists import Solution


def ll_to_arr(linked_list):
    """Convert Linked List to array"""
    new_arr = []
    temp = linked_list
    while temp:
        new_arr.append(temp.val)
        temp = temp.next

    return new_arr


def merge_and_sort(arrs):
    """
    Merge nested arrays to one array
    Return a sorted array
    """

    new_arr = []

    for arr in arrs:
        for num in arr:
            new_arr.append(num)

    return sorted(new_arr)


def arr_to_ll(array_of_arrays):
    """Convert an array to Linked List"""

    arr_of_ll = []

    for arr in array_of_arrays:
        if arr is None:
            arr_of_ll.append(None)

        temp = ListNode()
        pointer = temp

        for num in arr:
            pointer.next = ListNode(num)
            pointer = pointer.next

        arr_of_ll.append(temp.next)

    return arr_of_ll


class TestL23(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

        self.test_arrays = [
            [
                [1]
            ],
            [
                [-1], [0], [1]
            ],
            [
                [-10, -9, -9, -3, -1, -1, 0],
                [-5],
                [4],
                [-8],
                [],
                [-9, -6, -5, -4, -2, 2, 3],
                [-3, -3, -2, -1, 0]
            ],
            [
                [-6, -3, -1, 1, 2, 2, 2],
                [-10, -8, -6, -2, 4],
                [-2],
                [-8, -4, -3, -3, -2, -1, 1, 2, 3],
                [-8, -6, -5, -4, -2, -2, 2, 4]
            ],
        ]

    def test_all_cases(self):
        """Test all cases from self.test_arrays"""

        for arr in self.test_arrays:
            merged_and_sorted = merge_and_sort(arr)
            input_ll = arr_to_ll(arr)
            output_ll = self.solution.mergeKLists(input_ll)
            converted_output = ll_to_arr(output_ll)
            self.assertEqual(merged_and_sorted, converted_output)
