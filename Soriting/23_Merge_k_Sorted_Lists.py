# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import Optional, List
from Linked_List.ListNode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merge linked lists and sort them"""
        if len(lists) == 0:
            return None

        first_list = None
        first_index = None

        for num, linked_list in enumerate(lists):
            if linked_list:
                first_list = linked_list
                first_index = num
                break

        if not first_list:
            return None

        tail = first_list

        while tail.next:
            tail = tail.next

        for linked_list in lists[first_index + 1:]:
            if linked_list:
                tail.next = linked_list

            while tail.next:
                tail = tail.next

        temp = first_list
        new_arr = []

        while temp:
            new_arr.append(temp.val)
            temp = temp.next

        merge_sort(new_arr, 0, len(new_arr))

        head = ListNode(new_arr[0])
        temp = head

        for num in new_arr[1:]:
            temp.next = ListNode(num)
            temp = temp.next

        return head


def merge_sort(arr, start, end):
    """Divide an array into smaller arrays"""
    if end - start + 1 <= 1:
        return arr

    mid = (end + start) // 2

    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)

    merge(arr, start, mid, end)

    return arr


def merge(arr, start, mid, end):
    """Merge two arrays into one in ascending order"""

    left = arr[start: mid + 1]
    right = arr[mid + 1: end + 1]

    left_pointer = right_pointer = 0
    arr_pointer = start

    # Compare numbers
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            arr[arr_pointer] = left[left_pointer]
            left_pointer += 1
            arr_pointer += 1
        else:
            arr[arr_pointer] = right[right_pointer]
            right_pointer += 1
            arr_pointer += 1

    # Merge rest of left
    while left_pointer < len(left):
        arr[arr_pointer] = left[left_pointer]
        arr_pointer += 1
        left_pointer += 1

    # Merge rest of right
    while right_pointer < len(right):
        arr[arr_pointer] = right[right_pointer]
        arr_pointer += 1
        right_pointer += 1

    return arr


if __name__ == '__main__':

    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)

    ll2 = ListNode(4)
    ll2.next = ListNode(5)

    ll3 = ListNode(6)
    ll3.next = ListNode(7)

    sol = Solution()

    sol.mergeKLists([ll1, ll2, ll3])





